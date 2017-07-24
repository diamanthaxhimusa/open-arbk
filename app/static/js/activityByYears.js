$(document).ready(function() {
    $('.selected-value').html("Kultivimi i drith\xebrave (p\xebrveç orizit), i bim\xebve bishtajore dhe i far\xebrave vajore");
    $.ajax({
        data : {
            activity: 'Kultivimi i drith\xebrave (p\xebrveç orizit), i bim\xebve bishtajore dhe i far\xebrave vajore'
        },
        url: "/activities-years",
        type: 'POST',
        beforeSend:function() {
            $('#activityYearsLoader').show();
        },
        success: function(data){
            dates(data);
            $('#activityYearsLoader').hide();
        },
        error: function(error) {
        }
    });
});
function onActivitySelection(name) {
    $('.selected-value').html(name);
    $.ajax({
        data : {
            activity : name
        },
        url: "/activities-years",
        type: 'POST',
        beforeSend:function() {
            $('#activityYearsLoader').show();
        },
        success: function(data){
            dates(data);
            $('#activityYearsLoader').hide();
        },
        error: function(error) {
        }
    });
}
function dates(data) {
    Highcharts.chart('container9', {
        chart: {
            type: 'line'
        },
        title: {
            text: 'Krijimi i bizneseve gjat\xeb viteve 2003-2016 sipas aktivitetit'
        },
        xAxis: {
            title: {
                text: 'Data e aplikimit'
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
