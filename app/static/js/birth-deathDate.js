$(document).ready(function(){
    $.ajax({
        url: "/through-years",
        type: 'GET',
        success: function(data){
          dates(data);
          $('#thruYearsLoader').hide();
        }
    })
    function dates(data) {
        Highcharts.chart('container2', {
            chart: {
                type: 'line'
            },
            title: {
                text: 'Krijimi i bizneseve sipas viteve 2003-2016'
            },
            xAxis: {
                title: {
                    text: 'Data e aplikimit'
                },
                categories: ['2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016']
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
                name: 'T\xeb krijuara',
                data: [data.d3.Shuar+ data.d3.Aktiv , data.d4.Shuar+ data.d4.Aktiv , data.d5.Shuar+ data.d5.Aktiv , data.d6.Shuar+ data.d6.Aktiv , data.d7.Shuar+ data.d7.Aktiv , data.d8.Shuar+ data.d8.Aktiv , data.d9.Shuar+ data.d9.Aktiv , data.d10.Shuar+ data.d10.Aktiv , data.d11.Shuar+ data.d11.Aktiv , data.d12.Shuar+ data.d12.Aktiv , data.d13.Shuar+ data.d13.Aktiv , data.d14.Shuar+ data.d14.Aktiv , data.d15.Shuar+ data.d15.Aktiv , data.d16.Shuar+ data.d16.Aktiv],
                color:'#0090FF'
            }, {
                name: 'Aktive',
                data: [data.d3.Aktiv, data.d4.Aktiv, data.d5.Aktiv, data.d6.Aktiv, data.d7.Aktiv, data.d8.Aktiv, data.d9.Aktiv, data.d10.Aktiv, data.d11.Aktiv, data.d12.Aktiv, data.d13.Aktiv, data.d14.Aktiv, data.d15.Aktiv, data.d16.Aktiv],
                color: '#50FF00'
            }, {
                name: 'T\xeb Shuara',
                data: [data.d3.Shuar, data.d4.Shuar, data.d5.Shuar, data.d6.Shuar, data.d7.Shuar, data.d8.Shuar, data.d9.Shuar, data.d10.Shuar, data.d11.Shuar, data.d12.Shuar, data.d13.Shuar, data.d14.Shuar, data.d15.Shuar, data.d16.Shuar],
                color: '#FF0000'
            }]
        });
    }
});
