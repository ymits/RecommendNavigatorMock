import _ from 'underscore';

const storeData = [
  { id: 'PresetRecommendRule_1', title: 'クイックスコアを利用した推奨', filename: 'sample1', params: '{\n  "key1": "value1",\n  "key2": "value2"\n}' },
  { id: 'PresetRecommendRule_2', title: 'クイックスコアと購入履歴を利用した推奨', filename: 'sample2', params: '{\n  "key1": "value1",\n  "key2": "value2"\n}' },
];

class RecommendRule {
  constructor(id, title, filename, params) {
    this.id = id;
    this.title = title;
    this.filename = filename;
    this.params = params;
  }

  save() {
    const id = this.id;
    const json = storeData.find(data => id === data.id);
    if (json) {
      json.title = this.title;
      json.filename = this.filename;
      json.params = this.params;
    } else {
      storeData.push({
        id: this.id,
        title: this.title,
        filename: this.filename,
        params: this.params });
    }
  }

  static of(title, filename, params) {
    const id = _.uniqueId('RecommendRule_');
    return new RecommendRule(id, title, filename, params);
  }

  static findOne(id) {
    const json = storeData.find(data => id === data.id);
    return json ? new RecommendRule(json.id, json.title, json.filename, json.params) : null;
  }

  static findAll() {
    return storeData.map((data) => {
      return new RecommendRule(data.id, data.title, data.filename, data.params);
    });
  }
}

export default RecommendRule;
