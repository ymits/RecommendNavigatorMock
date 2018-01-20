# -*- coding: utf-8 -*-
from bottle import route, run, static_file, template, request, HTTPResponse
import json
import repositories.recommendRule as recommendRule

@route('/static/<file_path:path>')
def static(file_path):
    return static_file(file_path, root='./client/dist/static')

@route('/app')
def app():
    return static_file('index.html', root='./client/dist')

@route('/bot')
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

<iframe
    width="350"
    height="500"
    src="https://console.dialogflow.com/api-client/demo/embedded/93173144-ecfd-42ac-a300-3afb166cbaca">
</iframe>
  </body>
</html>
    ''')

def resJSON(body):
    print(json.dumps(body))
    res = HTTPResponse(status=200, body={'data': body})
    res.set_header('Content-Type', 'application/json')
    res.set_header('Access-Control-Allow-Origin', '*')
    res.set_header('Access-Control-Allow-Methods', 'PUT, GET, POST, DELETE, OPTIONS')
    res.set_header('Access-Control-Allow-Headers', 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token')
    return res

@route('/dialogflow', method="POST")
def dialogflow():
    # print('Dialogflow Request body: ' +  json.dumps(request.body))
    body = {'speech': 'hello world', 'displayText': 'hello world'}
    return resJSON(body)

@route('/api/recommendRule', method='GET')
def findRecommendRule():
    rules = recommendRule.findAll()
    return resJSON(rules)

@route('/api/recommendRule/<id>')
def findRecommend(id):
    rule = recommendRule.findOne(id)
    return resJSON(rule)

@route('/api/recommendRule', method='POST')
def saveRecommendRule():
    print('Request body: ' +  json.dumps(request.json))
    recommendRule.save(request.json)
    return resJSON({})

run(host='0.0.0.0', port=3000)
