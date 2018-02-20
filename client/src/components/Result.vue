<template>
  <div class="result">
    <div class="result-area">
      <div class="section-title">
        <h2>
          お客様におすすめの投資信託はこちらです。
        </h2>
      </div>
      <el-row>
        <el-col :span=24>
          おすすめ①：<span class="fund-name">{{ fund1 }}</span>
        </el-col>
      </el-row>
      <el-row :gutter="30">
        <el-col :span="8">
          <table class="table table-bordered">
            <tr>
              <th>対象資産</th>
              <td>株式</td>
            </tr>
            <tr>
              <th>対象地域</th>
              <td>国内</td>
            </tr>
            <tr>
              <th>購入時手数料</th>
              <td class="text-right">0%</td>
            </tr>
            <tr>
              <th>信託報酬</th>
              <td class="text-right">1.3175%</td>
            </tr>
            <tr>
              <th>決算頻度</th>
              <td>年１回</td>
            </tr>
            <tr>
              <th>為替ヘッジ</th>
              <td>-</td>
            </tr>
            <tr>
              <th>運用手法</th>
              <td>アクティブ型</td>
            </tr>
          </table>


        </el-col>
        <el-col :span="16">
          <chartjs-radar :width="300" :height="300" :datalabel="chartlabel" :labels="chartlabels" :data="data1"></chartjs-radar>
        </el-col>
      </el-row>
      <el-row class="space"></el-row>
      <el-row>
        <el-col :span=24>
          おすすめ②：<span class="fund-name">{{ fund2 }}</span>
        </el-col>
      </el-row>
      <el-row :gutter="30">
        <el-col :span="8">
          <table class="table table-bordered">
            <tr>
              <th>対象資産</th>
              <td>株式</td>
            </tr>
            <tr>
              <th>対象地域</th>
              <td>国内</td>
            </tr>
            <tr>
              <th>購入時手数料</th>
              <td class="text-right">0%</td>
            </tr>
            <tr>
              <th>信託報酬</th>
              <td class="text-right">1.3175%</td>
            </tr>
            <tr>
              <th>決算頻度</th>
              <td>年１回</td>
            </tr>
            <tr>
              <th>為替ヘッジ</th>
              <td>-</td>
            </tr>
            <tr>
              <th>運用手法</th>
              <td>アクティブ型</td>
            </tr>
          </table>


        </el-col>
        <el-col :span="16">
          <chartjs-radar :width="300" :height="300" :datalabel="chartlabel" :labels="chartlabels" :data="data2"></chartjs-radar>
        </el-col>
      </el-row>
      <el-row class="space"></el-row>
      <el-row>
        <el-col :span=24>
          おすすめ③：<span class="fund-name">{{ fund3 }}</span>
        </el-col>
      </el-row>
      <el-row :gutter="30">
        <el-col :span="8">
          <table class="table table-bordered">
            <tr>
              <th>対象資産</th>
              <td>株式</td>
            </tr>
            <tr>
              <th>対象地域</th>
              <td>国内</td>
            </tr>
            <tr>
              <th>購入時手数料</th>
              <td class="text-right">0%</td>
            </tr>
            <tr>
              <th>信託報酬</th>
              <td class="text-right">1.3175%</td>
            </tr>
            <tr>
              <th>決算頻度</th>
              <td>年１回</td>
            </tr>
            <tr>
              <th>為替ヘッジ</th>
              <td>-</td>
            </tr>
            <tr>
              <th>運用手法</th>
              <td>アクティブ型</td>
            </tr>
          </table>


        </el-col>
        <el-col :span="16">
          <chartjs-radar :width="300" :height="300" :datalabel="chartlabel" :labels="chartlabels" :data="data3"></chartjs-radar>
        </el-col>
      </el-row>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'Result',
  data () {
    return {
      chartlabel : '投信スコア',
      chartlabels : ['リスク', 'リターン', '下値抵抗力', '投信コスト', '分配金健全度'],
      data1 : [70, 55, 80, 100, 100],
      data2 : [60, 100, 70, 70, 80],
      data3 : [80, 60, 80, 90, 80],
      fund1 : "ひふみ",
      fund2 : "",
      fund3 : ""
    }
  },
  methods: {
  },
  mounted: function() {
    var accountId = localStorage.getItem('userId');
    axios.get('/api/recommendFund', {
      params: {
        accountId,
      },
    }).then((response) => {
      var data = response.data.data;
      this.fund1 = data[0];
      this.fund2 = data[1];
      this.fund3 = data[2];
    }, (error) => {
      console.log(error);
    });
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
.table-bordered {
    border: 1px solid #dee2e6;

    td,th {
        border: 1px solid #dee2e6;
    }
}
.table {
    width: 100%;
    max-width: 100%;
    margin-bottom: 1rem;
    background-color: transparent;
    border-collapse: collapse;

    td,
    th {
        padding: .5rem;
        vertical-align: top;
        border-top: 1px solid #dee2e6;
    }

    td {
      text-align: center;
    }
    th {
      text-align: left;
      width: 175px;
      background: #195547;
      color: #fff;
      font-weight: normal;
    }
}

.text-right {
  text-align: right;
}

.fund-name {
  font-size: 24px;
  font-weight: bold;
}
</style>
