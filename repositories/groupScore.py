import repositories.group as group

storeData = [
  {
    'groupId': 'PresetGroup_1',
    'recommendCount': 2155,
    'viewCount': 1532,
    'buyCount': 228,
    'viewRatio': 71.1,
    'buyRatio': 10.6,
  },
  {
    'groupId': 'PresetGroup_2',
    'recommendCount': 2217,
    'viewCount': 1814,
    'buyCount': 163,
    'viewRatio': 81.8,
    'buyRatio': 7.4,
  },
];

def save(groupScore):
    storedData = findOne(groupScore['groupId'])
    if storedData is not None :
        storedData['recommendCount'] = groupScore.get('recommendCount', 0)
        storedData['viewCount'] = groupScore.get('viewCount', 0)
        storedData['buyCount'] = groupScore.get('buyCount', 0)
        storedData['viewRatio'] = groupScore.get('viewRatio', 0)
        storedData['buyRatio'] = groupScore.get('buyRatio', 0)
    else :
        storeData.append({
            'groupId': groupScore.get('groupId', None),
            'recommendCount': groupScore.get('recommendCount', 0),
            'viewCount': groupScore.get('viewCount', 0),
            'buyCount': groupScore.get('buyCount', 0),
            'viewRatio': groupScore.get('viewRatio', 0),
            'buyRatio': groupScore.get('buyRatio', 0)
            })

def findOne(id):
    for data in storeData:
        if id == data['groupId']:
            return data
    return None

def findAll():
    return storeData

def findByGroupingRuleId(groupingRuleId):
    groups = group.findByGroupingRuleId(groupingRuleId)
    return list(map(lambda group: findOne(group['id']), groups))

def deleteByGroupingRuleId(groupingRuleId):
    deleteTarges = findByGroupingRuleId(groupingRuleId)
    for deleteTarget in deleteTarges:
        storeData.remove(deleteTarget)
