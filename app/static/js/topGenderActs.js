$('document').ready(function() {
    $.ajax({
        url: "/top-10-gender-activities",
        type: 'GET',
        success: function(data){
          proccesAPIFemra(data.females.activities);
          proccesAPIMeshkuj(data.males.activities);
          $('#genderActivitiesLoader').hide()
        }
    })
})
function proccesAPIMeshkuj(data) {
    emri = [];
    vals = [];
    for(var i=0; i<data.length;i++){
        emri.push(data[i].details.activity);
        vals.push(data[i].total_businesses);
    }
    topGenderActivitiesMeshkuj(vals, emri);
}
function proccesAPIFemra(data) {
    emri = [];
    vals = [];
    for(var i=0; i<data.length;i++){
        emri.push(data[i].details.activity);
        vals.push(data[i].total_businesses);
    }
    topGenderActivitiesFemra(vals, emri);
}
function topGenderActivitiesFemra(data, categories) {
    Highcharts.chart('container8', {
        chart: {
            plotBackgroundColor: null,
            plotBorderWidth: null,
            plotShadow: false,
            type: 'bar'
        },
        title: {
            text: 'Femra'
        },
        xAxis: {
            categories: categories,
            title: {
                text: null
            }
        },
        yAxis: {
            min: 0,
            title: {
                text: 'Numri i Bizneseve',
                align: 'high'
            },
            labels: {
                overflow: 'justify'
            }
        },
        tooltip: {
            pointFormat: '<span style="color:{point.color}"><b>{point.y:,.0f}</b> biznese</span><br/>'
        },
        plotOptions: {
            series: {
                stacking: 'normal'
            }
        },
        legend: {
            enabled: false
        },
        credits: {
            enabled: false
        },
        series: [{
            colors: ['#041D2F','#21283E','#242B44','#3E3F60','#4B5166','#4F506E', '#61617C', '#72738B','#848499', '#9596A8'],
            colorByPoint: true,
            data: data
        }]
    });
}

function topGenderActivitiesMeshkuj(data, categories) {
    Highcharts.chart('container7', {
        chart: {
            plotBackgroundColor: null,
            plotBorderWidth: null,
            plotShadow: false,
            type: 'bar'
        },
        title: {
            text: 'Meshkuj'
        },
        xAxis: {
            categories: categories,
            title: {
                text: null
            }
        },
        yAxis: {
            min: 0,
            title: {
                text: 'Numri i Bizneseve',
                align: 'high'
            },
            labels: {
                overflow: 'justify'
            }
        },
        tooltip: {
            pointFormat: '<span style="color:{point.color}"><b>{point.y:,.0f}</b> biznese</span><br/>'
        },
        plotOptions: {
            series: {
                stacking: 'normal'
            }
        },
        legend: {
            enabled: false
        },
        credits: {
            enabled: false
        },
        series: [{
            colors: ['#5C0722','#6B0827','#700829','#7A092D','#890A32','#980B38','#A70C3D','#AF224E','#B73860','#BF4E71'],
            colorByPoint: true,
            data: data
        }]
    });
}
