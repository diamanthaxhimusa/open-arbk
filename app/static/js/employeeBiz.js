$(document).ready(function(){
  $.ajax({
      url: "/employees",
      type: 'GET',
      success: function(data){
          employeesChart(data);
          $('#employeesLoader').hide();
      }
  });
});

function employeesChart(data) {
    // Create the chart
    Highcharts.setOptions({
        lang: {
            drillUpText: '< Kthehu prapa'
        }
    });
    Highcharts.getOptions().colors = Highcharts.map(Highcharts.getOptions().colors, function (color) {
        return {
            radialGradient: {
                cx: 0.5,
                cy: 0.3,
                r: 0.7
            },
            stops: [
                [0, color],
                [1, Highcharts.Color(color).brighten(-0.3).get('rgb')] // darken
            ]
        };
    });
    Highcharts.chart('empContainer', {
        chart: {
            type: 'pie'
        },
        title: {
            text: ''
        },
        plotOptions: {
            pie: {
               cursor: 'pointer',
               showInLegend: true
            },
            series: {
                dataLabels: {
                    enabled: true,
                    format: '{point.name}: {point.y:.1f}%'
                }
            }
        },
        tooltip: {
            headerFormat: '<span style="font-size:11px">{series.name}</span><br>',
            pointFormat: '<span style="color:{point.color}">{point.name}</span>: <b>{point.y:.2f}%</b> nga total<br/>'
        },
        legend: {
            labelFormatter: function () {
                return this.name+' ('+this.min+'-'+this.max+')';
            }
        },
        series: [{
            name: 'Biznese',
            colorByPoint: true,
            data: [{
                name: 'Mikrond\xebrmarrje',
                y: Math.round((data.micro.total / data.total * 100)*100)/100,
                drilldown: 'Micro',
                min:0,
                max:9
            }, {
                name: 'Nd\xebrmarrje e vog\xebl',
                y: Math.round((data.mini.total / data.total * 100)*100)/100,
                drilldown: 'mini',
                min:10,
                max:49
            }, {
                name: 'Ndermarrje e mesme',
                y: Math.round((data.middle.total / data.total * 100)*100)/100,
                drilldown: 'middle',
                min:50,
                max:249
            }, {
                name: 'Nd\xebrmarrje e madhe',
                y: Math.round((data.big.total / data.total * 100)*100)/100,
                drilldown: 'big',
                min:250,
                max:'\u221e'
            }]
        }],
        drilldown: {
            series: [{
                name: 'Mikrond\xebrmarrje',
                id: 'micro',
                data: [
                    ['Aktive', Math.round((data.micro.Aktiv / data.micro.total * 100)*100)/100],
                    ['Shuar', Math.round((data.micro.Shuar / data.micro.total * 100)*100)/100]
                ]
            }, {
                name: 'Nd\xebrmarrje e vog\xebl',
                id: 'mini',
                data: [
                    ['Aktive', Math.round((data.mini.Aktiv / data.mini.total * 100)*100)/100],
                    ['Shuar', Math.round((data.mini.Shuar / data.mini.total * 100)*100)/100]
                ]
            }, {
                name: 'Nd\xebrmarrje e mesme',
                id: 'middle',
                data: [
                    ['Aktive', Math.round((data.middle.Aktiv / data.middle.total * 100)*100)/100],
                    ['Shuar', Math.round((data.middle.Shuar / data.middle.total * 100)*100)/100]
                ]
            }, {
                name: 'Nd\xebrmarrje e madhe',
                id: 'big',
                data: [
                    ['Aktive', Math.round((data.big.Aktiv / data.big.total * 100)*100)/100],
                    ['Shuar', Math.round((data.big.Shuar / data.big.total * 100)*100)/100]
                ]
            }]
        }
    });
}
