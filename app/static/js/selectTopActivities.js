function selectActivities(){
    $('.topAct').html("");
    var maxCount = 10;
    var data = {};
    getAPI(0);
    function getAPI(selected) {
            $.ajax({
    data : {
        city : $('#top-act-municipalities').val(),
        status : $('#top-act-types').val()
    },
    type : 'POST',
    url : '/top-activities'
        }).done(function (dataAPI) {
                data = dataAPI;
                buildDropDown(dataAPI.activities.length);
                proccesAPI(data, 0, maxCount);
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
                $('.topAct').append('<option value='+max+' id='+((max+pak)-1)+'>'+max+'-'+(max+pak)+'</option>');
            }
        }
        function proccesAPI(data, min, max) {
            var start = min;
            var end = max;
            emri = [];
            vals = [];
            for(var i=start; i<=end;i++){
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
                text: 'Numri total i bizneseve'
              }
            },
            tooltip: {
                headerFormat: '<span style="font-size:11px">{series.x}</span><br>',
                pointFormat: '<span style="color:{point.color}">Total{point.name}</span>: <b>{point.y}</b> biznese<br/>'
            },

            xAxis: {
                categories: emri
            },

            series: [{
                type: 'column',
                colorByPoint: true,
                data: data,
                showInLegend: false
            }]

        });
        }
}
