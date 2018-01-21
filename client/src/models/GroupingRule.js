import _ from 'underscore';
import axios from 'axios';

/*
const storeData = [
  { id: 'PresetGroupingRule_1', title: '単一グループ', filename: 'sample1', params: '' },
  { id: 'PresetGroupingRule_2', title: 'ランダムグループ分け', filename: 'sample2', params: '{\n  "groupNum": 2\n}', active: true },
];

class GroupingRule {
  constructor(id, title, filename, params, active) {
    this.id = id;
    this.title = title;
    this.filename = filename;
    this.params = params;
    this.active = active;
  }

  save() {
    const id = this.id;
    const json = storeData.find(data => id === data.id);
    if (json) {
      json.title = this.title;
      json.filename = this.filename;
      json.params = this.params;
      json.active = this.active;
    } else {
      storeData.push({
        id: this.id,
        title: this.title,
        filename: this.filename,
        params: this.params,
        active: this.active,
      });
    }
  }

  static of(title, filename, params) {
    const id = _.uniqueId('RecommendRule_');
    return new GroupingRule(id, title, filename, params);
  }

  static findOne(id) {
    return new Promise((resolve) => {
      const json = storeData.find(data => id === data.id);
      const rule = json ? new GroupingRule(json.id, json.title, json.filename, json.params, json.active) : null;
      resolve(rule);
    });
  }

  static findAll() {
    return new Promise((resolve) => {
      const rules = storeData.map((data) => {
        return new GroupingRule(data.id, data.title, data.filename, data.params, data.active);
      });
      resolve(rules);
    });
  }
}
*/

class GroupingRule {
  constructor(id, title, filename, params, active) {
    this.id = id;
    this.title = title;
    this.filename = filename;
    this.params = params;
    this.active = active;
  }

  save() {
    axios.post('/api/groupingRule', this).then(() => {
      // no
    }, (error) => {
      console.log(error);
    });
  }

  static of(title, filename, params) {
    const id = _.uniqueId('GrouopingRule_');
    return new GroupingRule(id, title, filename, params);
  }

  static findOne(id) {
    return axios.get(`/api/groupingRule/${id}`).then((response) => {
      const json = response.data.data;
      return json ? new GroupingRule(json.id, json.title, json.filename, json.params, json.active) : null;
    }, (error) => {
      console.log(error);
    });
  }

  static findAll() {
    return axios.get('/api/groupingRule').then((response) => {
      return response.data.data.map((data) => {
        return new GroupingRule(data.id, data.title, data.filename, data.params, data.active);
      });
    }, (error) => {
      console.log(error);
    });
  }
}

export default GroupingRule;
