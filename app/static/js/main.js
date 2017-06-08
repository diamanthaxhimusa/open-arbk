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
      emri = [];
      vals = [];
      for(var i=0; i<data.doc.result.length;i++){
          emri.push(data.doc.result[i]['_id']);
          vals.push(data.doc.result[i]['total'] / data.total * 100);
      }
      business_type(emri, vals, data.total);
  }
  function business_type(emri, vals, total) {
    Highcharts.chart('container', {
        chart: {
            type: 'column'
        },
        title: {
            text: 'Përqindja e bizneseve në bazë të llojit'
        },
        xAxis: {
            categories: emri
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
            pointFormat: '<span style="color:{point.color}">{point.name}</span>: <b>{point.y:.2f}%</b> nga total '+total+'<br/>'
        },
        series: [{
            name: 'Biznese',
            colorByPoint: true,
            data: vals
        }]
    });
  }
$.ajax({
    url: "/active-inactive",
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
              text: 'Kompanitë e shuara dhe aktive gjatë viteve 2002-2018 nga '+data.total+' të themeluara në total.'
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
