$(document).ready(function(){
  $.ajax({
      url: "/gender-owners",
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
          url: "/gender-owners",
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
          if (data.doc.result[i]['_id'] == 'male') {
              gen_data.males = {"name":"Meshkuj", "result":data.doc.result[i]['all']}
          }else if (data.doc.result[i]['_id'] == 'female') {
              gen_data.females = {"name":"Femra", "result":data.doc.result[i]['all']}
          }else {
              gen_data.unknown = {"name":"Papërcaktuar", "result":data.doc.result[i]['all']}
          }
      }
      gender_owners(gen_data);
  }
  function gender_owners(data) {
    Highcharts.chart('container6', {
        chart: {
            plotShadow: false,
            type: 'pie'
        },
        title: {
            text: 'Përqindja e pronarëve sipas gjinisë'
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
            name: 'Pronarë në perqindje',
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
})
