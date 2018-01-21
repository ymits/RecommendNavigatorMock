storeData = [
  {
    'id': 'PresetGroup_1',
    'members': ['80100001','80100002','80100003','80300001','80300002'],
    'recommendRuleId': 'PresetRecommendRule_1',
    'groupingRuleId': 'PresetGroupingRule_2'
  },
  {
    'id': 'PresetGroup_2',
    'members': ['80200001','80200002','80200003','80300003','80400001'],
    'recommendRuleId': 'PresetRecommendRule_2',
    'groupingRuleId': 'PresetGroupingRule_2'
  },
];

def save(group):
    storedData = findOne(group['id'])
    if storedData is not None :
        storedData['members'] = group.get('members', [])
        storedData['recommendRuleId'] = group.get('recommendRuleId', None)
        storedData['groupingRuleId'] = group.get('groupingRuleId', None)
    else :
        storeData.append({
            'id': group.get('id', None),
            'members': group.get('members', []),
            'recommendRuleId': group.get('recommendRuleId', None),
            'groupingRuleId': group.get('groupingRuleId', None)
            })

def findOne(id):
    for data in storeData:
        if id == data['id']:
            return data
    return None

def findAll():
    return storeData

def findByGroupingRuleId(groupingRuleId):
    return [data for data in storeData if data.get('groupingRuleId', None) == groupingRuleId]

def deleteByGroupingRuleId(groupingRuleId):
    deleteTarges = findByGroupingRuleId(groupingRuleId)
    for deleteTarget in deleteTarges:
        storeData.remove(deleteTarget)
