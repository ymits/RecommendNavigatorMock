storeData = [
  { 'id': 'PresetRecommendRule_1', 'title': 'クイックスコアを利用した推奨', 'filename': 'sample1', 'params': '{\n  "key1": "value1",\n  "key2": "value2"\n}' },
  { 'id': 'PresetRecommendRule_2', 'title': 'クイックスコアと購入履歴を利用した推奨', 'filename': 'sample2', 'params': '{\n  "key1": "value1",\n  "key2": "value2"\n}' },
]

def save(recommendRule):
    storedData = findOne(recommendRule['id'])
    if storedData is not None :
        storedData['title'] = recommendRule['title']
        storedData['filename'] = recommendRule['filename']
        storedData['params'] = recommendRule['params']
    else :
        storeData.append({
            'id': recommendRule['id'],
            'title': recommendRule['title'],
            'filename': recommendRule['filename'],
            'params': recommendRule['params'] })

def findOne(id):
    for data in storeData:
        if id == data['id']:
            return data
    return None

def findAll():
    return storeData
