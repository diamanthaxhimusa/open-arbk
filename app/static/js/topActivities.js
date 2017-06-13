$(document).ready(function (){
    var maxCount = 10;
    var data = {};
    getAPI(0);
    function getAPI(selected) {
        $.getJSON('/top-activities', function (dataAPI) {
        }).done(function (dataAPI) {
            data = dataAPI;
            buildDropDown(dataAPI.activities.length);
            proccesAPI(data, 0, maxCount);
            $('#topActivitiesLoader').hide();
        });
    }
    $('.topAct').on('change', function() {
        var maxVal = $(this).children(":selected").attr("id");
        proccesAPI(data, parseInt($(this).val()), parseInt(maxVal));
    });
    function buildDropDown(actLength, data) {
        var list = actLength / maxCount;
        var plot = Math.floor(list);
        var pak = actLength % maxCount;
        min = 0;
        max = 0;
        for (var i = 0; i < plot; i++) {
            min = i * maxCount;
            max = min + maxCount;
            $('.topAct').append('<option value='+min+' id='+max+'>'+min+'-'+max+'</option>');
        }
        if (pak != 0) {
            $('.topAct').append('<option value='+max+' id='+((max+pak))+'>'+max+'-'+(max+pak)+'</option>');
        }
    }
    function proccesAPI(data, min, max) {
        var start = min;
        var end = max;
        emri = [];
        vals = [];
        for(var i=start; i<end;i++){
            emri.push(data.activities[i].details.activity);
            vals.push(data.activities[i].total_businesses);
        }
        top_activities(emri, vals);
    }

    function top_activities(emri, data){
    var chart = Highcharts.chart('container4', {
        title: {
            text: ''
        },
        legend: {
            enabled: false
        },
        yAxis: {
          title: {
            text: 'Numri i bizneseve'
          }
        },tooltip: {
            pointFormat: 'total: <b>{point.y} biznese</b>'
        },xAxis: {
            categories: emri
        },

        series: [{
            type: 'column',
            colorByPoint: true,
            data: data,
            showInLegend: false,
            colors: [
                {
                    linearGradient: { x1: 0, x2: 0, y1: 0, y2: 1 },
                    stops: [
                       [0, '#4A0D67'],
                       [1, '#7B4F90']
                    ]
                },
                {
                    linearGradient: { x1: 0, x2: 0, y1: 0, y2: 1 },
                    stops: [
                       [0, '#473198'],
                       [1, '#7969B4']
                    ]
                },
                {
                    linearGradient: { x1: 0, x2: 0, y1: 0, y2: 1 },
                    stops: [
                       [0, '#71B1AF'],
                       [1, '#8DDDDB']
                    ]
                },
                {
                    linearGradient: { x1: 0, x2: 0, y1: 0, y2: 1 },
                    stops: [
                       [0, '#C38537'],
                       [1, '#EFAA54']
                    ]
                },
                {
                    linearGradient: { x1: 0, x2: 0, y1: 0, y2: 1 },
                    stops: [
                       [0, '#BBFCA5'],
                       [1, '#D2FDC3']
                    ]
                },
                {
                    linearGradient: { x1: 0, x2: 0, y1: 0, y2: 1 },
                    stops: [
                       [0, '#4AAD52'],
                       [1, '#7BC381']
                    ]
                },
                {
                    linearGradient: { x1: 0, x2: 0, y1: 0, y2: 1 },
                    stops: [
                       [0, '#5C80BC'],
                       [1, '#88A2CE']
                    ]
                },
                {
                    linearGradient: { x1: 0, x2: 0, y1: 0, y2: 1 },
                    stops: [
                       [0, '#3D3B30'],
                       [1, '#95948E']
                    ]
                },
                {
                    linearGradient: { x1: 0, x2: 0, y1: 0, y2: 1 },
                    stops: [
                       [0, '#9E2B25'],
                       [1, '#B86460']
                    ]
                },
                {
                    linearGradient: { x1: 0, x2: 0, y1: 0, y2: 1 },
                    stops: [
                       [0, '#FFE066'],
                       [1, '#FFEB9D']
                    ]
                }
            ]
        }]

    });
    }
})
