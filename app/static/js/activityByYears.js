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
            name: 'biznese',
            data: [data.d3.all , data.d4.all , data.d5.all , data.d6.all , data.d7.all , data.d8.all , data.d9.all , data.d10.all , data.d11.all , data.d12.all , data.d13.all , data.d14.all , data.d15.all ,data.d16.all]
        }]
    });
}
