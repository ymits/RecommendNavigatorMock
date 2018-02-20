<template>
  <div class="step4">
    <div class="qa-area">
      <div class="page-title">個別投信ロボ</div>
      <div class="section-title">
        <h2>
          質問４：興味のある地域を教えてください
        </h2>
      </div>
      <div class="select-btn">
        <el-row :gutter="30" style="display: none">
          <el-col :span="6">
            <el-button @click="select('1')" :class="{'is-active':value.indexOf('1') >= 0}">欧州</el-button>
          </el-col>
          <el-col :span="6">
            <el-button @click="select('2')" :class="{'is-active':value.indexOf('2') >= 0}">中近東</el-button>
          </el-col>
          <el-col :span="6">
            <el-button @click="select('3')" :class="{'is-active':value.indexOf('3') >= 0}">日本</el-button>
          </el-col>
          <el-col :span="6">
            <el-button @click="select('4')" :class="{'is-active':value.indexOf('4') >= 0}">北米</el-button>
          </el-col>
          <el-col :span="6">
            <el-button @click="select('5')" :class="{'is-active':value.indexOf('5') >= 0}">アジア</el-button>
          </el-col>
          <el-col :span="6">
            <el-button @click="select('6')" :class="{'is-active':value.indexOf('6') >= 0}">アフリカ</el-button>
          </el-col>
          <el-col :span="6">
            <el-button @click="select('7')" :class="{'is-active':value.indexOf('7') >= 0}">オセアニア</el-button>
          </el-col>
          <el-col :span="6">
            <el-button @click="select('8')" :class="{'is-active':value.indexOf('8') >= 0}">中南米</el-button>
          </el-col>
          <el-col :span="6">
            <el-button @click="select('9')" :class="{'is-active':value.indexOf('9') >= 0}">グローバル</el-button>
          </el-col>
          <el-col :span="6">
            <el-button @click="select('10')" :class="{'is-active':value.indexOf('10') >= 0}">エマージング</el-button>
          </el-col>
          <el-col :span="6">
            <el-button @click="select('11')" :class="{'is-active':value.indexOf('11') >= 0}">おまかせ</el-button>
          </el-col>
        </el-row>
      </div>
      <div id="map" style="position:relative; width: 943px; height: 330px;"></div>
    </div>
    <div class="action-btn">
      <el-button-group>
        <el-button icon="el-icon-arrow-left" @click="goBack">前の質問へ</el-button>
        <el-button type="primary" @click="goNext">次の質問へ<i class="el-icon-arrow-right el-icon-right"></i></el-button>
      </el-button-group>
    </div>
  </div>
</template>

<script>
import investAreas from '@/investAreaData';
import * as d3 from 'd3'
import Datamap from 'datamaps'
import _ from 'underscore'

const BTN_CLASS_UNSELECTED = "btn btn-default";
const BTN_CLASS_SELECTED = "btn btn-defalut active";
const AREA_LABELS = (function(){
  var result = [
    {id: 'JAPAN',              lat: 42,  lng: 149,  color: "#e377c2", countries: ["JPN"],                                     name: '日本'},
    {id: 'CHINA',              lat: 40,  lng: 100,  color: "#d62728", countries: ["CHN"],                                     name: '中国'},
    {id: 'INDIA',              lat: 20,  lng: 70,   color: "#2ca02c", countries: ["IND"],                                     name: 'インド'},
    {id: 'ASIA',               lat: 10,  lng: 110,  color: "#ff7f0e", countries: _.difference(investAreas["NA"], ["JPN"]),    name: 'アジア'},
    {id: 'NORTH_AMERIA',       lat: 50,  lng: -110, color: "#9467db", countries: investAreas["NA"],                           name: '北米'},
    {id: 'SOUTH_AMERIA',       lat: -10, lng: -70,  color: "#8c564b", countries: investAreas["SA"],                           name: '南米'},
    {id: 'EUROPE',             lat: 60,  lng: 15,   color: "#68b0dd", countries: investAreas["EU"],                           name: '欧州'},
    {id: 'AFRICA_MIDDLE_EAST', lat: 10,  lng: 10,   color: "#bcbd22", countries: investAreas["AF"].concat(investAreas["MW"]), name: '中東'},
    {id: 'OCEANIA',            lat: -20, lng: 130,  color: "#1f77b4", countries: investAreas["OC"],                           name: 'オセアニア'},
    {id: 'GLOBAL',             x: 0,     y: 0,      color: "#000000", countries: [],                                          name: 'グローバル'},
    {id: 'EMERGING',           x: 0,     y: 40,     color: "#000000", countries: [],                                          name: 'エマージング'}
  ];
  // 計算して適用されるプロパティを設定
  _.each(result, function(area, index) {
    // リセット時の色を設定
    // ファイライトの時の色をベースにHCL色空間で編集
    var hcl = d3.hcl(area.color);
    hcl.c = 5;
    hcl.l = 75;
    area.defaultColor = hcl.toString();
    area.updateObject = {};
    _.each(area.countries, function(country) {
      area.updateObject[country] = area.color;
    });
  });
})();
const COUNTRY_TO_AREA_MAP = (function() {
  var result = {};
  _.each(AREA_LABELS, function(area) {
    _.each(area.countries, function(country) {
      // 重複する場合は定義した順で優先的に設定
      if (result[country] == null) {
        result[country] = area;
      }
    });
  });
  return result;
});
export default {
  name: 'Step4',
  data () {
    return {
      value: []
    }
  },
  methods: {
    select(v) {
      let index = this.value.indexOf(v);
      if (index >= 0) {
        this.value.splice(index, 1);
      } else {
        this.value.push(v);
      }
    },
    // 前へボタン押下時
    goBack() {
      this.$router.go(-1);
    },
    // 次へボタン押下時
    goNext() {
      this.$router.push({ name: 'Step5' });
    }
  },
  mounted: function() {
    var map = new Datamap({
      element: document.getElementById('map'),
      fills: {
        // リセット時の色を設定
        defaultFill: function(data) {
          // 国コードから地域を逆引きし、色を設定する
          var area = COUNTRY_TO_AREA_MAP[data.id];
          return area ? area.defaultColor : "#fafafa";
        }
      },
      geographyConfig: {
        // 標準のハイライト機能、ポップオーバー機能はdisableにする
        highlightOnHover: false,
        popupOnHover: false
      },
      setProjection: function() {
        // メルカトル図法、日本中心とする
        var projection = d3.geo.mercator()
          .center([0, -20])
          .scale(130)
          .rotate([-155, 0, 0]);
        var path = d3.geo.path().projection(projection);
        return {path, projection}
      },
      data: COUNTRY_TO_AREA_MAP
    });

    map.addPlugin("customAddLabel", function(layer) {
      var data = AREA_LABELS;
      var _this = this;
      d3.select(map.options.element)
        .append("div")
        .attr("class", "invest-area-map-label")
        .selectAll(".invest-area-map-label")
        .data(data, JSON.stringify)
        .enter()
        .append("button")
        .attr("class", BTN_CLASS_UNSELECTED)
        .style("left", function(d) {
          if (d.x != null) {
            return d.x + "px"
          }
          // 経緯度からピクセル座標に変換
          var xy = _this.latLngToXY(d.lat, d.lng);
          return xy[0] + "px";
        })
        .style("top", function(d) {
          if (d.y != null) {
            return d.y + "px"
          }
          // 経緯度からピクセル座標に変換
          var xy = _this.latLngToXY(d.lat, d.lng);
          return xy[0] + "px"
        })
        .html(function(d){return d.name;})
        .on("mouseover", function(d) {return selectArea(d);})
        .on("mouseout", function() {return clearSelectionAll();})
        .on("click", function(d) {return notifyClickArea(d);});
    });
    map.addPlugin("customHandleMouseEvent", function(layer) {
      this.svg.selectAll(".datamaps-subunit")
      .on("mouseover", function(d) {return selectAreaByCountry(d.id);})
      .on("mouseout", function() {return clearSelectionAll();})
      .on("click", function(d) {return notifyClickArea(COUNTRY_TO_AREA_MAP[d.id]);});
    });

    var selectedArea = null;
    const clearSelectionAll = function() {
      selectedArea = null;
      map.updateChoropleth(null, {reset: true});
      updateButtonStatus(null);
    };
    const selectArea = function(area) {
      if (area && (selectedArea == null || selectedArea.id !== area.id)) {
        selectedArea = area;
        map.updateChoropleth(area.updateObject);
        updateButtonStatus(area);
      }
    };
    const selectAreaByCountry = function(country) {
      var area = COUNTRY_TO_AREA_MAP[country];
      selectArea(area);
    };
    const updateButtonStatus = function(area) {
      d3.select(map.options.element)
        .selectAll(".invest-area-map-label")
        .selectAll("button")
        .attr("class", function(item) {
          if (area && item.id === area.id) {
            return BTN_CLASS_SELECTED
          } else {
            return BTN_CLASS_UNSELECTED
          }
        });
    };
    const notifyClickArea = function(area) {
      console.log('click', area);
    };
    map.customAddLabel();
    map.customHandleMouseEvent();
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
#map {
  button {
    position: absolute;
  }
}
</style>
