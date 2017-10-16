$(document).ready(function(){
  $.ajax({
      url: "gender-owners",
      type: 'GET',
      success: function(data){
          proccesAPI(data);
          $('#genderLoader').hide();
      }
  });
  $('#getGen').on('click', function() {
      $.ajax({
          data : {
              biz_city_id : $('#muni_gen').val(),
              biz_status : $('#stat_gen').val()
          },
          url: "gender-owners",
          type: 'POST',
          beforeSend: function () {
              $('#genderLoader').show();
          },
          success: function(data){
              proccesAPI(data);
              $('#genderLoader').hide();
          },
          error: function(error) {
          }
      });
  });
  function proccesAPI(data) {
      var emri = [];
      var vals = [];
      var gen_data = {}
      gen_data.total = data.total
      for(var i=0; i<data.doc.result.length;i++){
          var name = '';
          if (document.documentElement.lang == 'sq') {
              if (data.doc.result[i]['_id'] == 'male') {
                  gen_data.males = {"name":"Burra", "result":data.doc.result[i]['all']}
              }else if (data.doc.result[i]['_id'] == 'female') {
                  gen_data.females = {"name":"Gra", "result":data.doc.result[i]['all']}
              }else {
                  gen_data.unknown = {"name":"E Panjohur", "result":data.doc.result[i]['all']}
              }
          }
          else{
              if (data.doc.result[i]['_id'] == 'male') {
                  gen_data.males = {"name":"Men", "result":data.doc.result[i]['all']}
              }else if (data.doc.result[i]['_id'] == 'female') {
                  gen_data.females = {"name":"Women", "result":data.doc.result[i]['all']}
              }else {
                  gen_data.unknown = {"name":"Unknown", "result":data.doc.result[i]['all']}
              }
          }
      }
      gender_owners(gen_data);
  }
  function gender_owners(data) {
      if (document.documentElement.lang == 'sq') {
          Highcharts.chart('container6', {
              chart: {
                  plotShadow: false,
                  type: 'pie'
              },
              title: {
                  text: 'P\xebrqindja e pronar\xebve sipas gjinis\xeb'
              },
              plotOptions: {
                  pie: {
                      allowPointSelect: true,
                      cursor: 'pointer',
                      dataLabels: {
                          enabled: false
                      },
                      showInLegend: true
                  }
              },
              tooltip: {
                  pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
              },
              series: [{
                  name: 'Pronar\xeb n\xeb p\xebrqindje',
                  // colors: ['#E0777D','#4C86A8', '#E1DD8F'],
                  colors: [{
                      radialGradient: { cx: 0.5, cy: 0.5, r: 0.5 },
                      stops: [
                         [0, '#BF4E71'],
                         [1, '#700829']
                      ]
                  },{
                      radialGradient: { cx: 0.5, cy: 0.5, r: 0.5 },
                      stops: [
                         [0, '#9596A8'],
                         [1, '#242B44']
                      ]
                  },{
                      radialGradient: { cx: 0.5, cy: 0.5, r: 0.5 },
                      stops: [
                         [0, '#F1EFCC'],
                         [1, '#E1DD8F']
                      ]
                  }
                  ],
                  colorByPoint: true,
                  data: [{
                      name: data.males.name,
                      y: Math.round((data.males.result / data.total * 100)*100)/100
                  }, {
                      name: data.females.name,
                      y: Math.round((data.females.result / data.total * 100)*100)/100
                  },
                  {
                      name: data.unknown.name,
                      y: Math.round((data.unknown.result / data.total * 100)*100)/100
                  }]
              }]
          });
      }
      else{
          Highcharts.chart('container6', {
              chart: {
                  plotShadow: false,
                  type: 'pie'
              },
              title: {
                  text: 'Percentage of owners by gender'
              },
              plotOptions: {
                  pie: {
                      allowPointSelect: true,
                      cursor: 'pointer',
                      dataLabels: {
                          enabled: false
                      },
                      showInLegend: true
                  }
              },
              tooltip: {
                  pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
              },
              series: [{
                  name: 'Owners by percentage',
                  // colors: ['#E0777D','#4C86A8', '#E1DD8F'],
                  colors: [{
                      radialGradient: { cx: 0.5, cy: 0.5, r: 0.5 },
                      stops: [
                         [0, '#BF4E71'],
                         [1, '#700829']
                      ]
                  },{
                      radialGradient: { cx: 0.5, cy: 0.5, r: 0.5 },
                      stops: [
                         [0, '#9596A8'],
                         [1, '#242B44']
                      ]
                  },{
                      radialGradient: { cx: 0.5, cy: 0.5, r: 0.5 },
                      stops: [
                         [0, '#F1EFCC'],
                         [1, '#E1DD8F']
                      ]
                  }
                  ],
                  colorByPoint: true,
                  data: [{
                      name: data.males.name,
                      y: Math.round((data.males.result / data.total * 100)*100)/100
                  }, {
                      name: data.females.name,
                      y: Math.round((data.females.result / data.total * 100)*100)/100
                  },
                  {
                      name: data.unknown.name,
                      y: Math.round((data.unknown.result / data.total * 100)*100)/100
                  }]
              }]
          });
      }
  }
})
