storeData = [
  { 'id': 'PresetGroupingRule_1', 'title': '単一グループ', 'filename': 'sample1', 'params': '' },
  { 'id': 'PresetGroupingRule_2', 'title': 'ランダムグループ分け', 'filename': 'sample2', 'params': '{\n  "groupNum": 2\n}', 'active': True },
];

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
