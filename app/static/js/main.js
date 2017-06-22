$(document).ready(function(){
    $.ajax({
      url: "/businesses-type",
      type: 'GET',
      success: function(data){
        proccesAPI(data);
        $('#bizTypesLoader').hide();
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
          beforeSend: function() {
            $('#bizTypesLoader').show();
          },
          success: function(data){
              proccesAPI(data);
              $('#bizTypesLoader').hide();
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
                text: 'P\xebrqindja e bizneseve n\xeb baz\xeb t\xeb llojit'
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
                        ''+this.point.name+': <b>'+Highcharts.numberFormat(this.point.y, 3, '.')+' %</b> nga total <b>'+Highcharts.numberFormat(this.point.y, 2,'.', ',')+'</b><br/>';
                }
            },
            series: [{
                name: 'Biznese',
                colorByPoint: true,
                data: data,
                colors: [{
                    radialGradient: { cx: 0.5, cy: 0.5, r: 0.5 },
                    stops: [
                       [0, '#9578AD'],
                       [1, '#684A7F']
                    ]
                },{
                    radialGradient: { cx: 0.5, cy: 0.5, r: 0.5 },
                    stops: [
                       [0, '#85BBB9'],
                       [1, '#218380']
                    ]
                },{
                    radialGradient: { cx: 0.5, cy: 0.5, r: 0.5 },
                    stops: [
                       [0, '#EFBEA0'],
                       [1, '#DD7230']
                    ]
                },{
                    radialGradient: { cx: 0.5, cy: 0.5, r: 0.5 },
                    stops: [
                       [0, '#6D1B5D'],
                       [1, '#A26D97']
                    ]
                },{
                    radialGradient: { cx: 0.5, cy: 0.5, r: 0.5 },
                    stops: [
                       [0, '#69A2B0'],
                       [1, '#BAD4DB']
                    ]
                },{
                    radialGradient: { cx: 0.5, cy: 0.5, r: 0.5 },
                    stops: [
                       [0, '#C7D7C1'],
                       [1, '#659157']
                    ]
                }
                ]
            }]
        });
    }
    $.ajax({
        url: "/active-inactive",
        type: 'GET',
        success: function(data){
            active_inactive_chart(data);
            $('#ActInactLoader').hide();
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
             pointFormat: '<span style="color:{point.color}">{point.name}</span>: <b>{point.y:,.0f}%'
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
