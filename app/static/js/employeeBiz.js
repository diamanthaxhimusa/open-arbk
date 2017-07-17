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
            formatter: function () {
                var num = Highcharts.numberFormat(this.point.totalD, 0);
                if (num==0) {
                    num = '';
                }
                return '<span style="font-size:11px">'+this.series.name+': '+
                            num+
                            '</span><br><span style="color:{point.color}">'+
                            this.point.name+
                            '</span>: <b>'+
                            Highcharts.numberFormat(this.point.y, 2, '.')+
                            '%</b> nga total<br/>';
            }
            // headerFormat: '',
            // pointFormat: '<span style="font-size:11px">{series.name}: {point.totalD}</span><br><span style="color:{point.color}">{point.name}</span>: <b>{point.y:.2f}%</b> nga total<br/>'
        },
        legend: {
            labelFormatter: function () {
                var val = '';
                if (this.min != undefined)
                    val = ' ('+this.min+''+this.max+')';
                return this.name+val;
            }
        },
        series: [{
            name: 'Biznese',
            colorByPoint: true,
            data: [{
                name: 'Mikrond\xebrmarrje',
                y: Math.round((data.micro.total / data.total * 100)*100)/100,
                drilldown: 'micro',
                totalD:data.micro.total,
                min:'1',
                max:'-9'
            }, {
                name: 'Nd\xebrmarrje e vog\xebl',
                y: Math.round((data.mini.total / data.total * 100)*100)/100,
                drilldown: 'mini',
                totalD:data.mini.total,
                min:'10',
                max:'-49'
            }, {
                name: 'Nd\xebrmarrje e mesme',
                y: Math.round((data.middle.total / data.total * 100)*100)/100,
                drilldown: 'middle',
                totalD:data.middle.total,
                min:'50',
                max:'-249'
            }, {
                name: 'Nd\xebrmarrje e madhe',
                y: Math.round((data.big.total / data.total * 100)*100)/100,
                drilldown: 'big',
                totalD:data.big.total,
                min:'250+',
                max:''
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
