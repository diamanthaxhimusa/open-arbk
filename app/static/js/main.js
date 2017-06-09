$(document).ready(function(){
    $.ajax({
      url: "/businesses-type",
      type: 'GET',
      success: function(data){
        proccesAPI(data);
      }
    });
    $('#getBizTypes').on('click', function() {
      $.ajax({
          data : {
              biz_city_id : $('#biz_city_id').val(),
              biz_status : $('#biz_status').val()
          },
          url: "/businesses-type",
          type: 'POST',
          success: function(data){
              proccesAPI(data);
          },
          error: function(error) {
          }

      });
    });
    function proccesAPI(data) {
      resultData = [];
      for(var i=0; i<data.doc.result.length;i++){
          resultData.push({"name":data.doc.result[i]['_id'],"y":data.doc.result[i]['total'] / data.total * 100, "tot":data.doc.result[i]['total']});
      }
      business_type(resultData, data.total);
    }
    function business_type(data, total) {
        Highcharts.chart('container', {
            chart: {
                type: 'pie'
            },
            title: {
                text: 'Përqindja e bizneseve në bazë të llojit'
            },
            legend: {
                enabled: false
            },
            plotOptions: {
                pie: {
                    allowPointSelect: true,
                    cursor: 'pointer',
                    dataLabels: {
                        enabled: true,
                        format: '<b>{point.name}</b>: {point.percentage:.3f} %',
                        style: {
                            color: (Highcharts.theme && Highcharts.theme.contrastTextColor) || 'black'
                        }
                    }
                }
            },
            tooltip: {
                formatter: function () {
                    return ''+this.point.name+': <b>'+this.point.tot+'<b><br>'+
                        ''+this.point.name+': <b>'+Highcharts.numberFormat(this.point.y, 3, '.')+' %</b> nga total <b>'+total+'</b><br/>';
                }
            },
            series: [{
                name: 'Biznese',
                colorByPoint: true,
                data: data
            }]
        });
    }
    $.ajax({
        url: "/active-inactive",
        type: 'GET',
        success: function(data){
            active_inactive_chart(data)
        }
    })
    function active_inactive_chart(data){
      $('#totalBiznese').html(data.total);
      Highcharts.chart('container3', {
            chart: {
                type: 'solidgauge',
                marginTop: 50
            },
            title: {
                text: 'Activity',
                style: {
                    fontSize: '24px'
                }
            },
            tooltip: {
                borderWidth: 0,
                backgroundColor: 'none',
                shadow: false,
                style: {
                    fontSize: '16px'
                },
                pointFormat: '{series.name}<br><span style="font-size:2em; color: {point.color}; font-weight: bold">{point.y: .0f}%</span>',
                positioner: function (labelWidth) {
                    return {
                        x: 200 - labelWidth/2,
                        y: 180
                    };
                }
            },
            pane: {
                startAngle: 0,
                endAngle: 360,
                background: [
                { // Track for Aktive
                    outerRadius: '112%',
                    innerRadius: '88%',
                    backgroundColor: Highcharts.Color(Highcharts.getOptions().colors[0])
                        .setOpacity(0.3)
                        .get(),
                    borderWidth: 0
                },
                { // Track for Shuar
                    outerRadius: '87%',
                    innerRadius: '63%',
                    backgroundColor: Highcharts.Color(Highcharts.getOptions().colors[1])
                        .setOpacity(0.3)
                        .get(),
                    borderWidth: 0
                }]
            },
            yAxis: {
                min: 0,
                max: 100,
                lineWidth: 0,
                tickPositions: []
            },
            plotOptions: {
                solidgauge: {
                    dataLabels: {
                        enabled: false
                    },
                    linecap: 'round',
                    stickyTracking: false,
                    rounded: true
                }
            },
            series: [{
                name: 'Aktive',
                data: [{
                    color: Highcharts.getOptions().colors[0],
                    radius: '112%',
                    innerRadius: '88%',
                    y: (data.docs.result[0]['total'] / data.total) * 100
                }]
            }, {
                name: 'Shuar',
                data: [{
                    color: Highcharts.getOptions().colors[1],
                    radius: '87%',
                    innerRadius: '63%',
                    y: (data.docs.result[1]['total'] / data.total) * 100
                }]
            }]
        },
         function callback() {
             // Active icon
             this.renderer.path(['M', 0, 8, 'L', 0, -8, 'M', -8, 0, 'L', 0, -8, 8, 0])
             .attr({
                 'stroke': '#303030',
                 'stroke-linecap': 'round',
                 'stroke-linejoin': 'round',
                 'stroke-width': 2,
                 'zIndex': 10
             })
             .translate(460,26)
             .add(this.series[1].group);
             // InActive icon
             this.renderer.path(['M', -8, 0, 'L', 8, 0, 'M', 0, -8, 'L', 8, 0, 0, 8])
             .attr({
                 'stroke': '#ffffff',
                 'stroke-linecap': 'round',
                 'stroke-linejoin': 'round',
                 'stroke-width': 2,
                 'zIndex': 10
             })
             .translate(460,61)
             .add(this.series[1].group);
      });
     // Highcharts.chart('container3', {
     //     chart: {
     //         plotBackgroundColor: null,
     //         plotBorderWidth: null,
     //         plotShadow: false,
     //         type: 'pie'
     //     },
     //     title: {
     //         text: ''
     //     },
     //     tooltip: {
     //         headerFormat: '<span style="font-size:11px">{series.name}</span><br>',
     //         pointFormat: '<span style="color:{point.color}">{point.name}</span>: <b>{point.y:.2f}%'
     //     },
     //     plotOptions: {
     //         pie: {
     //             allowPointSelect: true,
     //             cursor: 'pointer',
     //             dataLabels: {
     //                 enabled: false
     //             },
     //             showInLegend: true
     //         }
     //     },
     //     series: [{
     //         name: 'Numri i kompanive',
     //         colorByPoint: true,
     //         data: [{
     //             name: 'Aktive ('+data.docs.result[0]['total']+')',
     //             y: (data.docs.result[0]['total'] / data.total) * 100
     //         }, {
     //             name: 'Shuar('+data.docs.result[1]['total']+')',
     //             y: (data.docs.result[1]['total'] / data.total) * 100
     //         }]
     //     }]
     // });
    }
})
