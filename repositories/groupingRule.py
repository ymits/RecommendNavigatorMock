import importlib
import json
import utils.idGenerator as idGenerator
import repositories.account as account

storeData = [
  { 'id': 'PresetGroupingRule_1', 'title': '単一グループ', 'filename': 'singleGrouping', 'params': '' },
  { 'id': 'PresetGroupingRule_2', 'title': 'ランダムグループ分け', 'filename': 'randamGrouping', 'params': '{\n  "groupNum": 2\n}', 'active': True },
]

def save(groupingRule):
    storedData = findOne(groupingRule['id'])
    if storedData is not None :
        storedData['title'] = groupingRule.get('title', None)
        storedData['filename'] = groupingRule.get('filename', None)
        storedData['params'] = groupingRule.get('params', None)
        storedData['active'] = groupingRule.get('active', False)
    else :
        storeData.append({
            'id': groupingRule.get('id', None),
            'title': groupingRule.get('title', None),
            'filename': groupingRule.get('filename', None),
            'params': groupingRule.get('params', None),
            'active': groupingRule.get('active', False) })

def findOne(id):
    for data in storeData:
        if id == data['id']:
            return data
    return None

def findAll():
    return storeData

def findActiveRule():
    for data in storeData:
        if data.get('active', False):
            return data

def trialGrouping(groupingRule):
    m = importlib.import_module('rules.group.' + groupingRule["filename"])
    params = json.loads(groupingRule.get("params", {}))
    groupsMembers = m.execute(account.findAllAccounts(), params)
    return list(map(lambda members: {'id': idGenerator.generate('Group_'), 'members': members}, groupsMembers))
