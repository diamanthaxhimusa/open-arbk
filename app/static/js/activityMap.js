$(document).ready(function() {
    $('.selected-value').html("Aktivitetet e tjera p.k.t.");
    $.ajax({
        url: "/mapi",
        type: 'GET',
        success: function(data){
            proccesAPI(data);
        },
        error: function(error) {
        }
    });
});
function onActivitySelection(name) {
    $('.selected-value').html(name);
    $.ajax({
        data : {
            activity_name : $('.selected-value').html()
        },
        url: "/mapi",
        type: 'POST',
        success: function(data){
            proccesAPI(data);
        },
        error: function(error) {
        }
    });
}
var data2 = [
    {//Prishtina
        "name": "Prishtinë",
        "value": 0,
        "hc-key": "kv-7310",
        "id": 0
    },
    {//Gjilani
        "name": "Gjilan",
        "value": 0,
        "hc-key": "kv-842"
    },
    {//Prizereni
        "name": "Prizren",
        "value": 0,
        "hc-key": "kv-843"
    },
    {
        "name": "Ferizaj",
        "value": 0,
        "hc-key": "kv-7324"
    },
    {
        "name": "Lipjan",
        "value": 0,
        "hc-key": "kv-7311"
    },
    {
        "name": "Podujevë",
        "value": 0,
        "hc-key": "kv-7309"
    },
    {
        "name": "Obiliq",
        "value": 0,
        "hc-key": "kv-7308"
    },
    {
        "name": "Gllogoc",
        "value": 0,
        "hc-key": "kv-7307"
    },
    {
        "name": "Malishevë",
        "value": 0,
        "hc-key": "kv-7317"
    },
    {
        "name": "Gjakovë",
        "value": 0,
        "hc-key": "kv-7321"
    },
    {
        "name": "Rahovec",
        "value": 0,
        "hc-key": "kv-7322"
    },
    {
        "name": "Klinë",
        "value": 0,
        "hc-key": "kv-7319"
    },
    {
        "name": "Deçan",
        "value": 0,
        "hc-key": "kv-7320"
    },
    {
        "name": "Istog",
        "value": 0,
        "hc-key": "kv-7318"
    },
    {//Skenderaj
        "name": "Skënderaj",
        "value": 0,
        "hc-key": "kv-7305"
    },
    {//Vushtrri
        "name": "Vushtrri",
        "value": 0,
        "hc-key": "kv-7304"
    },
    {//Artanë
        "name": "Novobërdë",
        "value": 0,
        "hc-key": "kv-7313"
    },
    {//kamenice
        "name": "Kamenicë",
        "value": 0,
        "hc-key": "kv-7314"
    },
    {//Mitrovice
        "name": "Mitrovicë",
        "value": 0,
        "hc-key": "kv-7303"
    },
    {//Suharek
        "name": "Suhareka",
        "value": 0,
        "hc-key": "kv-7316"
    },
    { //shtime
        "name": "Shtime",
        "value": 0,
        "hc-key": "kv-7323"
    },
    { //Vitia
        "name": "Viti",
        "value":0,
        "hc-key": "kv-7312"
    },
    { // Shterpce
        "name": "Shtërpcë",
        "value": 0,
        "hc-key": "kv-7325"
    },
    { // Kaqanik
        "name": "Kaçanik",
        "value": 0,
        "hc-key": "kv-7326"
    },
    {
        "name": "Zveçan",
        "value": 0,
        "hc-key": "kv-844"
    },
    {
        "name": "Leposaviq",
        "value": 0,
        "hc-key": "kv-7302"
    },
    {
        "name": "Zubin Potok",
        "value": 0,
        "hc-key": "kv-7306"
    },
    {
        "name": "Fushë Kosovë",
        "value": 0,
        "hc-key": "kv-845"
    },
    {
        "name": "Dragash",
        "value": 0,
        "hc-key": "kv-7315"
    },
    {
        "name": "Pejë",
        "value": 0,
        "hc-key": "kv-841"
    }
];
function proccesAPI(data) {
    var dupli = []
    $.each(data, function(key, val) {
        $.each(data2, function(key2, val2) {
            if (key == val2.name) {
                val2.value = val;
            }
        });
        if (key == "Hani i Elezit")dupli.push({"muni":key,"val":val});
        else if (key == "Mamushë")dupli.push({"muni":key,"val":val});
        else if (key == "Ranillugë")dupli.push({"muni":key,"val":val});
        else if (key == "Partesh")dupli.push({"muni":key,"val":val});
        else if (key == "Kllokot")dupli.push({"muni":key,"val":val});
        else if (key == "Junik")dupli.push({"muni":key,"val":val});
        else if (key == "Graçanicë")dupli.push({"muni":key,"val":val});
    });
    $.each(data2, function(key2, val2) {
        $.each(dupli, function(key, val) {
            if (val.muni == "Hani i Elezit" && val2.name == "Ferizaj")val2.value += val.val;
            else if (val.muni == "Mamushë" && val2.name == "Prizren")val2.value += val.val;
            else if (val.muni == "Ranillugë" && val2.name == "Gjilan")val2.value += val.val;
            else if (val.muni == "Partesh" && val2.name == "Gjilan")val2.value += val.val;
            else if (val.muni == "Kllokot" && val2.name == "Gjilan")val2.value += val.val;
            else if (val.muni == "Junik" && val2.name == "Gjakovë")val2.value += val.val;
            else if (val.muni == "Graçanicë" && val2.name == "Prishtinë")val2.value += val.val;
        });
    });
    mapActs(data2)
}
Highcharts.setOptions({
    lang:{
        downloadJPEG: "Shkarko JPG",
        downloadPDF: "Shkarko PDF",
        downloadPNG: "Shkarko FOTO",
        downloadSVG: "Shkarko SVG",
        printChart: "Printo Grafikun"
    }
});

function mapActs(data) {
    // Create the chart
    Highcharts.mapChart('mapContainer', {
        chart: {
            map: 'countries/kv/kv-all'
        },
        title: {
           text: ''
       },
        mapNavigation: {
            enableMouseWheelZoom: false,
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
            name: 'Biznese',
            states: {
                hover: {
                    color: '#BADA55'
                }
            },
            dataLabels: {
                enabled: true,
                allowOverlap: true,
                format: '{point.options.name}'
            },
            tooltip: {
                pointFormat: '{point.options.name}: '+'{point.options.value}'
            }
        }]
    });
}
