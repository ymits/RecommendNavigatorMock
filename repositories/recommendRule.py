storeData = [
  { 'id': 'PresetRecommendRule_1', 'title': 'クイックスコアを利用した推奨', 'filename': 'sample1', 'params': '{\n  "key1": "value1",\n  "key2": "value2"\n}' },
  { 'id': 'PresetRecommendRule_2', 'title': 'クイックスコアと購入履歴を利用した推奨', 'filename': 'sample2', 'params': '{\n  "key1": "value1",\n  "key2": "value2"\n}' },
]

def save(recommendRule):
    storedData = findOne(recommendRule['id'])
    if storedData is not None :
        storedData['title'] = recommendRule.get('title', None)
        storedData['filename'] = recommendRule.get('filename', None)
        storedData['params'] = recommendRule.get('params', None)
    else :
        storeData.append({
            'id': recommendRule.get('id', None),
            'title': recommendRule.get('title', None),
            'filename': recommendRule.get('filename', None),
            'params': recommendRule.get('params', None) })

def findOne(id):
    for data in storeData:
        if id == data['id']:
            return data
    return None

def findAll():
    return storeData
