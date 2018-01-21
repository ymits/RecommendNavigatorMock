import _ from 'underscore';

const storeData = [
  {
    id: 'PresetGroup_1',
    memberCount: 300,
    recommendRule: 'PresetRecommendRule_1',
    recommendCount: 2155,
    viewCount: 1532,
    buyCount: 228,
    viewRatio: 71.1,
    buyRatio: 10.6,
  },
  {
    id: 'PresetGroup_2',
    memberCount: 300,
    recommendRule: 'PresetRecommendRule_2',
    recommendCount: 2217,
    viewCount: 1814,
    buyCount: 163,
    viewRatio: 81.8,
    buyRatio: 7.4,
  },
];

class Group {
  constructor(id, memberCount, recommendRule, recommendCount, viewCount, buyCount, viewRatio, buyRatio) {
    this.id = id;
    this.memberCount = memberCount;
    this.recommendRule = recommendRule;
    this.recommendCount = recommendCount;
    this.viewCount = viewCount;
    this.buyCount = buyCount;
    this.viewRatio = viewRatio;
    this.buyRatio = buyRatio;
  }

  save() {
    const id = this.id;
    const json = storeData.find(data => id === data.id);
    if (json) {
      json.memberCount = this.memberCount;
      json.recommendRule = this.recommendRule;
      json.recommendCount = this.recommendCount;
      json.viewCount = this.viewCount;
      json.buyCount = this.buyCount;
      json.viewRatio = this.viewRatio;
      json.buyRatio = this.buyRatio;
    } else {
      storeData.push({
        id: this.id,
        memberCount: this.memberCount,
        recommendRule: this.recommendRule,
        recommendCount: this.recommendCount,
        viewCount: this.viewCount,
        buyCount: this.buyCount,
        viewRatio: this.viewRatio,
        buyRatio: this.buyRatio,
      });
    }
  }

  static of(memberCount) {
    const id = _.uniqueId('RecommendRule_');
    return new Group(id, memberCount);
  }

  static findOne(id) {
    return new Promise((resolve) => {
      const json = storeData.find(data => id === data.id);
      const group = json ? new Group(json.id, json.memberCount, json.recommendRule, json.recommendCount, json.viewCount,
        json.buyCount, json.viewRatio, json.buyRatio) : null;
      resolve(group);
    });
  }

  static findAll() {
    return new Promise((resolve) => {
      const groups = storeData.map((data) => {
        return new Group(data.id, data.memberCount, data.recommendRule, data.recommendCount, data.viewCount, data.buyCount,
          data.viewRatio, data.buyRatio);
      });
      resolve(groups);
    });
  }

  static deleteAll() {
    storeData.length = 0;
  }
}

export default Group;
