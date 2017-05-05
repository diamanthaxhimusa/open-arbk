$(document).ready(function(){

  $.ajax({
      url: "/top_activities",
      type: 'GET',
      success: function(data){
        top_activities(data)
      }
  })

  function top_activities(data){
    var chart = Highcharts.chart('container4', {

        title: {
            text: ''
        },
        legend: {
            enabled: false
        },
        yAxis: {
          title: {
            text: 'Numri total i bizneseve'
          }
        },
        tooltip: {
            headerFormat: '<span style="font-size:11px">{series.x}</span><br>',
            pointFormat: '<span style="color:{point.color}">Total{point.name}</span>: <b>{point.y}</b> biznese<br/>'
        },

        xAxis: {
            categories: [data.activities[0].details.activity, data.activities[1].details.activity, data.activities[2].details.activity, data.activities[3].details.activity, data.activities[4].details.activity, data.activities[5].details.activity, data.activities[6].details.activity, data.activities[7].details.activity, data.activities[8].details.activity, data.activities[9].details.activity]
        },

        series: [{
            type: 'column',
            colorByPoint: true,
            data: [data.activities[0].total_businesses, data.activities[1].total_businesses, data.activities[2].total_businesses, data.activities[3].total_businesses, data.activities[4].total_businesses, data.activities[5].total_businesses, data.activities[6].total_businesses, data.activities[7].total_businesses, data.activities[8].total_businesses, data.activities[9].total_businesses],
            showInLegend: false
        }]

    });
  }

})
