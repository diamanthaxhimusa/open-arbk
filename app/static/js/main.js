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
            }

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


  Highcharts.chart('container2', {
    chart: {
        type: 'areaspline'
    },
    title: {
        text: 'Average fruit consumption during one week'
    },
    legend: {
        layout: 'vertical',
        align: 'left',
        verticalAlign: 'top',
        x: 150,
        y: 100,
        floating: true,
        borderWidth: 1,
        backgroundColor: (Highcharts.theme && Highcharts.theme.legendBackgroundColor) || '#FFFFFF'
    },
    xAxis: {
        categories: [
            'Monday',
            'Tuesday',
            'Wednesday',
            'Thursday',
            'Friday',
            'Saturday',
            'Sunday'
        ],
        plotBands: [{ // visualize the weekend
            from: 4.5,
            to: 6.5,
            color: 'rgba(68, 170, 213, .2)'
        }]
    },
    yAxis: {
        title: {
            text: 'Fruit units'
        }
    },
    tooltip: {
        shared: true,
        valueSuffix: ' units'
    },
    credits: {
        enabled: false
    },
    plotOptions: {
        areaspline: {
            fillOpacity: 0.5
        }
    },
    series: [{
        name: 'John',
        data: [3, 4, 3, 5, 4, 10, 12]
    }, {
        name: 'Jane',
        data: [1, 3, 4, 3, 3, 5, 4]
    }]
});

})
