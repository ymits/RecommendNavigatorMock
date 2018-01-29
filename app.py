# -*- coding: utf-8 -*-
from bottle import route, get, post, delete, run, static_file, template, request, HTTPResponse
import json
import repositories.recommendRule as recommendRule
import repositories.groupingRule as groupingRule
import repositories.group as group
import repositories.groupScore as groupScore

@get('/static/<file_path:path>')
def static(file_path):
    return static_file(file_path, root='./client/dist/static')

@get('/app')
def app():
    return static_file('index.html', root='./client/dist')

@get('/bot')
def bot():
    return template('''
    <!DOCTYPE html>
<html>
  <head>
    <title>ファイナンシャル・アドバイザーデモ</title>
    <link rel='stylesheet' href='/stylesheets/style.css' />
  </head>
  <body>
    <h1>ファイナンシャル・アドバイザーデモ</h1>
<div style="overflow:hidden;">
<iframe
    width="350"
    height="500"
    style="margin-top:-80px;"
    src="https://console.dialogflow.com/api-client/demo/embedded/93173144-ecfd-42ac-a300-3afb166cbaca">
</iframe>
</div>
  </body>
</html>
    ''')

def resJSON(body, dataFieldFlg = True):
    print('Response body: ' +  json.dumps(body))
    if dataFieldFlg:
        body={'data': body}
    res = HTTPResponse(status=200, body=body)
    res.set_header('Content-Type', 'application/json')
    return res

def resError(err):
    print(err)
    res = HTTPResponse(status=400, body={'message': "{0}".format(err)})
    res.set_header('Content-Type', 'application/json')
    return res

@get('/api/recommendRule')
def findRecommendRule():
    rules = recommendRule.findAll()
    return resJSON(rules)

@get('/api/recommendRule/<id>')
def findRecommendRule(id):
    rule = recommendRule.findOne(id)
    return resJSON(rule)

@post('/api/recommendRule')
def saveRecommendRule():
    print('Request body: ' +  json.dumps(request.json))
    recommendRule.save(request.json)
    return resJSON({})

@get('/api/groupingRule')
def findGroupingRule():
    rules = groupingRule.findAll()
    return resJSON(rules)

@get('/api/groupingRule/<id>')
def findGroupingRule(id):
    rule = groupingRule.findOne(id)
    return resJSON(rule)

@post('/api/groupingRule')
def saveGroupingRule():
    print('Request body: ' +  json.dumps(request.json))
    groupingRule.save(request.json)
    return resJSON({})

@post('/api/groupingRule/trial')
def trialGrouping():
    print('Request body: ' +  json.dumps(request.json))
    try:
        groups = groupingRule.trialGrouping(request.json)
        return resJSON(groups)
    except ModuleNotFoundError as err:
        return resError(err)
    except json.decoder.JSONDecodeError as err2:
        return resError(err2)


@get('/api/group')
def findGroup():
    print('findGroup')
    groupingRuleId = request.query.groupingRuleId
    print(groupingRuleId)
    if groupingRuleId is not None and groupingRuleId != "":
        rules = group.findByGroupingRuleId(groupingRuleId)
    else:
        rules = group.findAll()
    return resJSON(rules)

@get('/api/group/<id>')
def findGroup(id):
    print('findGroupid')
    rule = group.findOne(id)
    return resJSON(rule)

@post('/api/group')
def saveGroup():
    print('Request body: ' +  json.dumps(request.json))
    group.save(request.json)
    return resJSON({})

@delete('/api/group')
def deleteGroup():
    print('deleteGroup')
    groupingRuleId = request.query.groupingRuleId
    group.deleteByGroupingRuleId(groupingRuleId)
    return resJSON({})

@get('/api/groupScore')
def findGroupScore():
    print('findGroupScore')
    groupingRuleId = request.query.groupingRuleId
    print(groupingRuleId)
    if groupingRuleId is not None and groupingRuleId != "":
        rules = groupScore.findByGroupingRuleId(groupingRuleId)
    else:
        rules = groupScore.findAll()
    return resJSON(rules)

@get('/api/groupScore/<id>')
def findGroupScore(id):
    print('findGroupScoreid')
    rule = groupScore.findOne(id)
    return resJSON(rule)

@post('/api/groupScore')
def saveGroupScore():
    print('Request body: ' +  json.dumps(request.json))
    groupScore.save(request.json)
    return resJSON({})

@delete('/api/groupScore')
def deleteGroupScore():
    print('deleteGroupScore')
    groupingRuleId = request.query.groupingRuleId
    groupScore.deleteByGroupingRuleId(groupingRuleId)
    return resJSON({})

@get('/api/recommendFund')
def recommendFund():
    accountId = request.query.accountId
    activeGroupingRule = groupingRule.findActiveRule()
    attachedGroup = group.findAttachedGroup(accountId, activeGroupingRule["id"])
    selectRecommendRule = recommendRule.findOne(attachedGroup["recommendRuleId"])
    funds = recommendRule.execute(accountId, selectRecommendRule)
    return resJSON(funds)

@post('/dialogflow')
def dialogflow():
    print('Request body: ' +  json.dumps(request.json))
    action = request.json['result']['action'] # https://dialogflow.com/docs/actions-and-parameters
    parameters = request.json['result']['parameters'] # https://dialogflow.com/docs/actions-and-parameters
    contexts = request.json['result']['contexts']

    print('parameters:', parameters)
    print('contexts:', contexts)
    if contexts is None:
        contexts = []

    actionHandlers = {
        'action.switch.user': switch_user,
        'action.get.user': get_user,
        'action.suggestion': get_suggestion
    }
    if actionHandlers.get(action, None) is None:
        action = "default"

    body = actionHandlers[action](parameters, contexts)
    return dialogflowMessage(body, contexts)


def dialogflowMessage(body, contexts):
    if isinstance(body, str):
        body = {'speech': body, 'displayText': body}
    body['contextOut'] = contexts
    return resJSON(body, False)

def default_action(parameters, contexts):
    return '404 error'

def switch_user(parameters, contexts):
    account = parameters['account']
    putContext(contexts, 'account', account)
    return 'ユーザ "' + str(account) + '" に切り替えました'

def get_user(parameters, contexts):
    account = getContext(contexts, 'account')
    if account is None:
        account = '80100001'
        putContext(contexts, 'account', account)
    return '現在のユーザは "' + str(int(account)) + '" です'

def get_suggestion(parameters, contexts):
    accountId = getContext(contexts, 'account')
    if accountId is None:
        accountId = '80100001'
        putContext(contexts, 'account', accountId)
    activeGroupingRule = groupingRule.findActiveRule()
    attachedGroup = group.findAttachedGroup(accountId, activeGroupingRule["id"])
    if attachedGroup is None:
        return 'ユーザがどのグループにも紐付いていません'
    selectRecommendRule = recommendRule.findOne(attachedGroup["recommendRuleId"])
    funds = recommendRule.execute(accountId, selectRecommendRule)
    funds = map(lambda n:"「"+n+"」", funds)
    return 'あなたにおすすめの銘柄は'+('と'.join(funds))+'です'

def putContext(contexts, name, value):
    lifespan = 10

    context = None
    for i in contexts:
        if i['name'] == name:
            context = i

    if context is not None :
        context['lifespan'] = lifespan
        context['parameters']['value'] = value
    else:
        contexts.append({
            'name': name,
            'lifespan': lifespan,
            'parameters': {'value': value}
        })

def getContext(contexts, name):
    context = None
    for i in contexts:
        if i['name'] == name:
            context = i

    if context is not None:
        return context['parameters']['value']
    else:
        return None

run(host='0.0.0.0', port=3000)
