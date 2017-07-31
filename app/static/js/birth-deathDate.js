$(document).ready(function(){
    $.ajax({
        url: "through-years",
        type: 'POST',
        data:{
            date_type: "applicationDate"
        },
        success: function(data){
            dates(data);
            $('#thruYearsLoader').hide();
        }
    });
    $('#date-type-b').on('change', function() {
        var dType = $(this).children(":selected").attr("value");
        $.ajax({
            url: "through-years",
            type: 'POST',
            data:{
                date_type: dType
            },
            beforeSend:function() {
                $('#thruYearsLoader').show();
            },
            success: function(data){
                dates(data);
                $('#thruYearsLoader').hide();
            }
        })
    });
    function dates(data) {
        if (document.documentElement.lang == 'sq') {
            Highcharts.chart('container2', {
                chart: {
                    type: 'line'
                },
                title: {
                    text: 'Paraqitja e bizneseve 2000-2016'
                },
                xAxis: {
                    title: {
                        text: 'vitet'
                    },
                    categories: ['2000','2001','2002','2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016']
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
                    data: [data.d0.Shuar+ data.d0.Aktiv, data.d1.Shuar+ data.d1.Aktiv, data.d2.Shuar+ data.d2.Aktiv, data.d3.Shuar+ data.d3.Aktiv , data.d4.Shuar+ data.d4.Aktiv , data.d5.Shuar+ data.d5.Aktiv , data.d6.Shuar+ data.d6.Aktiv , data.d7.Shuar+ data.d7.Aktiv , data.d8.Shuar+ data.d8.Aktiv , data.d9.Shuar+ data.d9.Aktiv , data.d10.Shuar+ data.d10.Aktiv , data.d11.Shuar+ data.d11.Aktiv , data.d12.Shuar+ data.d12.Aktiv , data.d13.Shuar+ data.d13.Aktiv , data.d14.Shuar+ data.d14.Aktiv , data.d15.Shuar+ data.d15.Aktiv , data.d16.Shuar+ data.d16.Aktiv],
                    color:'#0090FF'
                }, {
                    name: 'Aktive',
                    data: [data.d0.Aktiv, data.d1.Aktiv, data.d2.Aktiv, data.d3.Aktiv, data.d4.Aktiv, data.d5.Aktiv, data.d6.Aktiv, data.d7.Aktiv, data.d8.Aktiv, data.d9.Aktiv, data.d10.Aktiv, data.d11.Aktiv, data.d12.Aktiv, data.d13.Aktiv, data.d14.Aktiv, data.d15.Aktiv, data.d16.Aktiv],
                    color: '#50FF00'
                }, {
                    name: 'T\xeb Shuara',
                    data: [data.d0.Shuar, data.d1.Shuar, data.d2.Shuar, data.d3.Shuar, data.d4.Shuar, data.d5.Shuar, data.d6.Shuar, data.d7.Shuar, data.d8.Shuar, data.d9.Shuar, data.d10.Shuar, data.d11.Shuar, data.d12.Shuar, data.d13.Shuar, data.d14.Shuar, data.d15.Shuar, data.d16.Shuar],
                    color: '#FF0000'
                }]
            });
        }
        else{
            Highcharts.chart('container2', {
                chart: {
                    type: 'line'
                },
                title: {
                    text: 'Application of businesses 2000-2016'
                },
                xAxis: {
                    title: {
                        text: 'Years'
                    },
                    categories: ['2000','2001','2002','2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016']
                },
                yAxis: {
                    title: {
                        text: 'Number of businesses'
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
                    name: 'Created',
                    data: [data.d0.Dissolved+ data.d0.Active, data.d1.Dissolved+ data.d1.Active, data.d2.Dissolved+ data.d2.Active, data.d3.Dissolved+ data.d3.Active , data.d4.Dissolved+ data.d4.Active , data.d5.Dissolved+ data.d5.Active , data.d6.Dissolved+ data.d6.Active , data.d7.Dissolved+ data.d7.Active , data.d8.Dissolved+ data.d8.Active , data.d9.Dissolved+ data.d9.Active , data.d10.Dissolved+ data.d10.Active , data.d11.Dissolved+ data.d11.Active , data.d12.Dissolved+ data.d12.Active , data.d13.Dissolved+ data.d13.Active , data.d14.Dissolved+ data.d14.Active , data.d15.Dissolved+ data.d15.Active , data.d16.Dissolved+ data.d16.Active],
                    color:'#0090FF'
                }, {
                    name: 'Active',
                    data: [data.d0.Active, data.d1.Active, data.d2.Active, data.d3.Active, data.d4.Active, data.d5.Active, data.d6.Active, data.d7.Active, data.d8.Active, data.d9.Active, data.d10.Active, data.d11.Active, data.d12.Active, data.d13.Active, data.d14.Active, data.d15.Active, data.d16.Active],
                    color: '#50FF00'
                }, {
                    name: 'Dissolved',
                    data: [data.d0.Dissolved, data.d1.Dissolved, data.d2.Dissolved, data.d3.Dissolved, data.d4.Dissolved, data.d5.Dissolved, data.d6.Dissolved, data.d7.Dissolved, data.d8.Dissolved, data.d9.Dissolved, data.d10.Dissolved, data.d11.Dissolved, data.d12.Dissolved, data.d13.Dissolved, data.d14.Dissolved, data.d15.Dissolved, data.d16.Dissolved],
                    color: '#FF0000'
                }]
            });
        }
    }
});
