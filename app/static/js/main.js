$(document).ready(function(){

  $.ajax({
      url: "/businesses-type",
      type: 'GET',
      success: function(data){
        // $('#name').text(data.result[0]['_id']);
        business_type(data)
      }
  })


  function business_type(data) {
    Highcharts.chart('container', {
        chart: {
            type: 'column'
        },
        title: {
            text: 'Numri total i bizneseve në bazë të llojeve të biznesit'
        },
        xAxis: {
            type: 'category'
        },
        yAxis: {
            title: {
                text: 'Numri total i bizneseve'
            },
            min: 0,
            max: 12

        },
        legend: {
            enabled: false
        },
        plotOptions: {
            series: {
                borderWidth: 0,
                dataLabels: {
                    enabled: true,
                    format: '{point.y:.1f}%'
                }
            }
        },
        tooltip: {
            headerFormat: '<span style="font-size:11px">{series.name}</span><br>',
            pointFormat: '<span style="color:{point.color}">{point.name}</span>: <b>{point.y:.2f}%</b> of total<br/>'
        },
        series: [{
            name: 'Brands',
            colorByPoint: true,
            data: [{
                name: data.doc.result[0]['_id'],
                y: (data.doc.result[0]['total'] / data.total) * 100
            }, {
                name: data.doc.result[1]['_id'],
                y: (data.doc.result[1]['total'] / data.total) * 100
            }, {
              name: data.doc.result[2]['_id'],
              y: (data.doc.result[2]['total'] / data.total) * 100
            }, {
              name: data.doc.result[3]['_id'],
              y: (data.doc.result[3]['total'] / data.total) * 100
            }, {
              name: data.doc.result[4]['_id'],
              y: (data.doc.result[4]['total'] / data.total) * 100
            }, {
              name: data.doc.result[5]['_id'],
              y: (data.doc.result[5]['total'] / data.total) * 100
            }, {
              name: data.doc.result[6]['_id'],
              y: (data.doc.result[6]['total'] / data.total) * 100
            }, {
              name: data.doc.result[7]['_id'],
              y: (data.doc.result[7]['total'] / data.total) * 100
            }, {
              name: data.doc.result[8]['_id'],
              y: (data.doc.result[8]['total'] / data.total) * 100
            }, {
              name: data.doc.result[9]['_id'],
              y: (data.doc.result[9]['total'] / data.total) * 100
            }]
        }]
    });
  }
$.ajax({
    url: "/active_inactive",
    type: 'GET',
    success: function(data){
      // $('#name').text(data.result[0]['_id']);
      active_inactive_chart(data)
    }
})

function active_inactive_chart(data){
  Highcharts.chart('container3', {
          chart: {
              plotBackgroundColor: null,
              plotBorderWidth: null,
              plotShadow: false,
              type: 'pie'
          },
          title: {
              text: 'Numri i kompanive aktive dhe te shuara mes viteve 2000 - 2018'
          },
          tooltip: {
              pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
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
          series: [{
              name: 'Numri i kompanive',
              colorByPoint: true,
              data: [{
                  name: 'Aktive',
                  y: (data.docs.result[0]['total'] / data.total) * 100
              }, {
                  name: 'Shuar',
                  y: (data.docs.result[1]['total'] / data.total) * 100
              }]
          }]
      });
}
})
