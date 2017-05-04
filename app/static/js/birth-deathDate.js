$(document).ready(function(){
    $.ajax({
        url: "/born",
        type: 'GET',
        success: function(data){
          dates(data)
        }
    })
    function dates(data) {
        Highcharts.chart('container2', {
            chart: {
                type: 'line'
            },
            title: {
                text: 'Krijimi/Mbyllja e bizneseve sipas viteve 2000-2018'
            },
            legend: {
                layout: 'vertical',
                align: 'right',
                verticalAlign: 'middle'
            },
            xAxis: {
                categories: ['2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017']
            },
            yAxis: {
                title: {
                    text: 'Numri i bizneseve'
                }
            },
            plotOptions: {
                line: {
                    dataLabels: {
                        enabled: true
                    },
                    enableMouseTracking: true
                }
            },
            series: [{
                name: 'Krijuara',
                data: [data.d2.Shuar+data.d2.Aktiv , data.d3.Shuar+ data.d3.Aktiv , data.d4.Shuar+ data.d4.Aktiv , data.d5.Shuar+ data.d5.Aktiv , data.d6.Shuar+ data.d6.Aktiv , data.d7.Shuar+ data.d7.Aktiv , data.d8.Shuar+ data.d8.Aktiv , data.d9.Shuar+ data.d9.Aktiv , data.d10.Shuar+ data.d10.Aktiv , data.d11.Shuar+ data.d11.Aktiv , data.d12.Shuar+ data.d12.Aktiv , data.d13.Shuar+ data.d13.Aktiv , data.d14.Shuar+ data.d14.Aktiv , data.d15.Shuar+ data.d15.Aktiv , data.d16.Shuar+ data.d16.Aktiv , data.d17.Shuar+ data.d17.Aktiv ]
            }, {
                name: 'Krijuara(shuar)',
                data: [data.d2.Shuar, data.d3.Shuar, data.d4.Shuar, data.d5.Shuar, data.d6.Shuar, data.d7.Shuar, data.d8.Shuar, data.d9.Shuar, data.d10.Shuar, data.d11.Shuar, data.d12.Shuar, data.d13.Shuar, data.d14.Shuar, data.d15.Shuar, data.d16.Shuar, data.d17.Shuar]
            }, {
                name: 'Krijuara(aktive)',
                data: [data.d2.Aktiv, data.d3.Aktiv, data.d4.Aktiv, data.d5.Aktiv, data.d6.Aktiv, data.d7.Aktiv, data.d8.Aktiv, data.d9.Aktiv, data.d11.Aktiv, data.d11.Aktiv, data.d12.Aktiv, data.d13.Aktiv, data.d14.Aktiv, data.d15.Aktiv, data.d16.Aktiv, data.d17.Aktiv]
            }]
        });
    }
});
