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
             plotBackgroundColor: null,
             plotBorderWidth: null,
             plotShadow: false,
             type: 'pie'
         },
         title: {
             text: ''
         },
         tooltip: {
             headerFormat: '<span style="font-size:11px">{series.name}</span><br>',
             pointFormat: '<span style="color:{point.color}">{point.name}</span>: <b>{point.y:.2f}%'
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
             colors:[{
                     radialGradient: { cx: 0.5, cy: 0.5, r: 0.5 },
                     stops: [
                        [0, '#99D5D2'],
                        [1, '#20A39E']
                     ]
                 },{
                     radialGradient: { cx: 0.5, cy: 0.5, r: 0.5 },
                     stops: [
                        [0, '#9B8B98'],
                        [1, '#23001E']
                     ]
                 }
             ],
             data: [{
                 name: 'Aktive ('+data.docs.result[0]['total']+')',
                 y: (data.docs.result[0]['total'] / data.total) * 100
             }, {
                 name: 'Shuar('+data.docs.result[1]['total']+')',
                 y: (data.docs.result[1]['total'] / data.total) * 100
             }]
         }]
     });
    }
})
