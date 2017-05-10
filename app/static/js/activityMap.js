$(document).ready(function() {
    $.ajax({
        url: "/mapAPI",
        type: 'GET',
        success: function(data){
          proccesAPI(data);
        }
    });

    var data2 = [
        {//Prishtina
            "name": "Prishtinë",
            "value": 13,
            "hc-key": "kv-7310",
            "id": 0
        },
        {//Gjilani
            "name": "Gjilan",
            "value": 23,
            "hc-key": "kv-842"
        },
        {//Prizereni
            "name": "Prizren",
            "value": 2323,
            "hc-key": "kv-843"
        },
        {
            "name": "Ferizaj",
            "value": 53,
            "hc-key": "kv-7324"
        },
        {
            "name": "Lipjan",
            "value": 43,
            "hc-key": "kv-7311"
        },
        {
            "name": "Podujevë",
            "value": 43,
            "hc-key": "kv-7309"
        },
        {
            "name": "Obiliq",
            "value": 43,
            "hc-key": "kv-7308"
        },
        {
            "name": "Gllogoc",
            "value": 43,
            "hc-key": "kv-7307"
        },
        {
            "name": "Malishevë",
            "value": 24,
            "hc-key": "kv-7317"
        },
        {
            "name": "Gjakovë",
            "value": 24,
            "hc-key": "kv-7321"
        },
        {
            "name": "Rahovec",
            "value": 24,
            "hc-key": "kv-7322"
        },
        {
            "name": "Klinë",
            "value": 24,
            "hc-key": "kv-7319"
        },
        {
            "name": "Deçan",
            "value": 24,
            "hc-key": "kv-7320"
        },
        {
            "name": "Istog",
            "value": 24,
            "hc-key": "kv-7318"
        },
        {//Skenderaj
            "name": "Skënderaj",
            "value": 24,
            "hc-key": "kv-7305"
        },
        {//Vushtri
            "name": "Vushtri",
            "value": 24,
            "hc-key": "kv-7304"
        },
        {//Artanë
            "name": "Novobërdë",
            "value": 27,
            "hc-key": "kv-7313"
        },
        {//kamenice
            "name": "Kamenicë",
            "value": 27,
            "hc-key": "kv-7314"
        },
        {//Mitrovice
            "name": "Mitrovicë",
            "value": 27,
            "hc-key": "kv-7303"
        },
        {//Suharek
            "name": "Suhareka",
            "value": 27,
            "hc-key": "kv-7316"
        },
        { //shtime
            "name": "Shtime",
            "value": 27,
            "hc-key": "kv-7323"
        },
        { //Vitia
            "name": "Viti",
            "value":21,
            "hc-key": "kv-7312"
        },
        { // Shterpce
            "name": "Shtërpcë",
            "value": 20,
            "hc-key": "kv-7325"
        },
        { // Kaqanik
            "name": "Kaçanik",
            "value": 31,
            "hc-key": "kv-7326"
        },
        {
            "name": "Zveçan",
            "value": 10,
            "hc-key": "kv-844"
        },
        {
            "name": "Leposaviq",
            "value": 10,
            "hc-key": "kv-7302"
        },
        {
            "name": "Zubin Potok",
            "value": 10,
            "hc-key": "kv-7306"
        },
        {
            "name": "Fushë Kosovë",
            "value": 30,
            "hc-key": "kv-845"
        },
        {
            "name": "Dragash",
            "value": 30,
            "hc-key": "kv-7315"
        },
        {
            "name": "Pejë",
            "value": 30,
            "hc-key": "kv-841"
        }
    ];
    mapActs(data2);
    // function proccesAPI(data) {
    //     city = [];
    //     var j = 0;
    //     for(var i=0; i<data.length;i++){
    //         // city.push([data2[i][0], data.result[i]['count']]);
    //         j++
    //     }
    //     mapActs(city);
    // }
    function mapActs(data) {
        // Create the chart
        Highcharts.mapChart('mapContainer', {
            chart: {
                map: 'countries/kv/kv-all'
            },

            title: {
                text: 'Highmaps basic demo'
            },

            subtitle: {
                text: 'Kosovo'
            },

            mapNavigation: {
                enabled: true,
                buttonOptions: {
                    verticalAlign: 'bottom'
                }
            },

            colorAxis: {
                min: 0
            },

            series: [{
                data: data,
                name: 'Random data',
                states: {
                    hover: {
                        color: '#BADA55'
                    }
                },
                dataLabels: {
                    enabled: true,
                    format: '{point.name}'
                },
                tooltip: {
                    pointFormat: '{point.name}'
                }
            }]
        });
    }
});
