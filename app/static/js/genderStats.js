$(document).ready(function(){
  $.ajax({
      url: "/gender_owners",
      type: 'GET',
      success: function(data){
          proccesAPI(data);
      }
  });
  $('#getGen').on('click', function() {
      $.ajax({
          data : {
              biz_city_id : $('#muni_gen').val(),
              biz_status : $('#stat_gen').val()
          },
          url: "/gender_owners",
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
          var name = '';
          if (data.doc.result[i]['_id'] == 'male') {
              name = 'Meshkuj'
          }else if (data.doc.result[i]['_id'] == 'female') {
              name = 'Femra'
          }else {
              name = 'Papërcaktuar'
          }
          emri.push(name);
          vals.push(data.doc.result[i]['all']);
      }
      var total = data.total
      gender_owners(emri, vals, total);
  }
  function gender_owners(emri, vals, total) {
    Highcharts.chart('container6', {
        chart: {
            plotShadow: false,
            type: 'pie'
        },
        title: {
            text: 'Numri total i pronarëve në bazë të llojeve të biznesit'
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
            name: 'pronarë në perqindje',
            colorByPoint: true,
            data: [{
                name: emri[0],
                y: Math.round((vals[0] / total * 100)*100)/100
            }, {
                name: emri[1],
                y: Math.round((vals[1] / total * 100)*100)/100
            },
            {
                name: emri[2],
                y: Math.round((vals[2] / total * 100)*100)/100
            }]
        }]
    });
  }
})
