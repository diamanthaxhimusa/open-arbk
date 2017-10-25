$(document).ready(function() {
    if (document.documentElement.lang == 'sq') {
        $('.selected-value').html("T\xeb gjitha");
        $('.selected-value-status').html("T\xeb gjitha");
    }
    else {
        $('.selected-value').html("All");
        $('.selected-value-status').html("All");
    }
    $.ajax({
        url: "mapi",
        type: 'GET',
        success: function(data){
            proccesAPI(data);
            $(".overllay").hide();
        },
        error: function(error) {
        }
    });
});

function onStatusSelection(name) {
    if (name == "Shuar") {
        if (document.documentElement.lang == 'sq') {
            $('.selected-value-status').html("I shuar");
        }
        else {
            $('.selected-value-status').html("Dissolved");
        }
    } else if (name == "Aktiv") {
        if (document.documentElement.lang == 'sq') {
            $('.selected-value-status').html("Aktiv");
        }
        else{
            $('.selected-value-status').html("Active");
        }
    } else {
        if (document.documentElement.lang == 'sq') {
            $('.selected-value-status').html("T\xeb gjitha");
        }
        else {
            $('.selected-value-status').html("All");
        }
    }

    var actDrop = $('.selected-value').html();
    if (actDrop == "T\xeb gjitha" || actDrop == "All") {
          actDrop = "all";
    }

    $.ajax({
        data : {
            activity_name : actDrop,
            status: name
        },
        url: "mapi",
        type: 'POST',
        beforeSend: function(){
            $(".overllay").show();
        },
        success: function(data){
            proccesAPI(data);
            $(".overllay").hide();
        },
        error: function(error) {
        }
    });
}

function onActivitySelection(name, code) {
    if (name == "all") {
        if (document.documentElement.lang == 'sq') {
            $('.selected-value').html("T\xeb gjitha");
        }
        else{
            $('.selected-value').html("All");
        }
    }
    else {
        $('.selected-value').html(name);
        $('.selected-value').attr('data-code', code);
    }

    if (document.documentElement.lang == 'sq') {
        $('.selected-value-status').html("T\xeb gjitha");
    }
    else {
        $('.selected-value-status').html("All");
    }

    $.ajax({
        data : {
            activity_name : name,
            status: 'T\xeb gjitha'
        },
        url: "mapi",
        type: 'POST',
        beforeSend: function(){
           $(".overllay").show();
        },
        success: function(data){
            proccesAPI(data);
            $(".overllay, #businessbyMunicipality").hide();
        },
        error: function(error) {
        }
    });
}

var cities = [];
if(document.documentElement.lang == 'sq') {
  cities = [
      {//Prishtina
          "name": "Prishtin\xeb",
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
          "name": "Podujev\xeb",
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
          "name": "Malishev\xeb",
          "value": 0,
          "hc-key": "kv-7317"
      },
      {
          "name": "Gjakov\xeb",
          "value": 0,
          "hc-key": "kv-7321"
      },
      {
          "name": "Rahovec",
          "value": 0,
          "hc-key": "kv-7322"
      },
      {
          "name": "Klin\xeb",
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
          "name": "Sk\xebnderaj",
          "value": 0,
          "hc-key": "kv-7305"
      },
      {//Vushtrri
          "name": "Vushtrri",
          "value": 0,
          "hc-key": "kv-7304"
      },
      {//Artan\xeb
          "name": "Novob\xebrd\xeb",
          "value": 0,
          "hc-key": "kv-7313"
      },
      {//kamenice
          "name": "Kamenic\xeb",
          "value": 0,
          "hc-key": "kv-7314"
      },
      {//Mitrovice
          "name": "Mitrovic\xeb",
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
          "name": "Sht\xebrpc\xeb",
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
          "name": "Fush\xeb Kosov\xeb",
          "value": 0,
          "hc-key": "kv-845"
      },
      {
          "name": "Dragash",
          "value": 0,
          "hc-key": "kv-7315"
      },
      {
          "name": "Pej\xeb",
          "value": 0,
          "hc-key": "kv-841"
      }
  ];
} else {
  cities = [
      {//Prishtina
          "name": "Pristina",
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
          "name": "Podujevo",
          "value": 0,
          "hc-key": "kv-7309"
      },
      {
          "name": "Obilic",
          "value": 0,
          "hc-key": "kv-7308"
      },
      {
          "name": "Glogovac",
          "value": 0,
          "hc-key": "kv-7307"
      },
      {
          "name": "Malisheve",
          "value": 0,
          "hc-key": "kv-7317"
      },
      {
          "name": "Gjakova",
          "value": 0,
          "hc-key": "kv-7321"
      },
      {
          "name": "Rahovec",
          "value": 0,
          "hc-key": "kv-7322"
      },
      {
          "name": "Klina",
          "value": 0,
          "hc-key": "kv-7319"
      },
      {
          "name": "Decan",
          "value": 0,
          "hc-key": "kv-7320"
      },
      {
          "name": "Istog",
          "value": 0,
          "hc-key": "kv-7318"
      },
      {//Skenderaj
          "name": "Skenderaj",
          "value": 0,
          "hc-key": "kv-7305"
      },
      {//Vushtrri
          "name": "Vushtrri",
          "value": 0,
          "hc-key": "kv-7304"
      },
      {//Artan\xeb
          "name": "Novo Brdo",
          "value": 0,
          "hc-key": "kv-7313"
      },
      {//kamenice
          "name": "Kamenica",
          "value": 0,
          "hc-key": "kv-7314"
      },
      {//Mitrovice
          "name": "Mitrovica",
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
          "name": "Shtrpce",
          "value": 0,
          "hc-key": "kv-7325"
      },
      { // Kaqanik
          "name": "Kacanik",
          "value": 0,
          "hc-key": "kv-7326"
      },
      {
          "name": "Zvecan",
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
          "name": "Fushe Kosove",
          "value": 0,
          "hc-key": "kv-845"
      },
      {
          "name": "Dragash",
          "value": 0,
          "hc-key": "kv-7315"
      },
      {
          "name": "Peja",
          "value": 0,
          "hc-key": "kv-841"
      }
  ];
}

function proccesAPI(data) {
    var dupli = []
    $.each(data, function(key, val) {
        $.each(cities, function(key2, val2) {
            if (key == val2.name) {
                val2.value = val;
            }
        });
        if(document.documentElement.lang == 'sq') {
            if (key == "Hani i Elezit")dupli.push({"muni":key,"val":val});
            else if (key == "Mamush\xeb")dupli.push({"muni":key,"val":val});
            else if (key == "Ranillug\xeb")dupli.push({"muni":key,"val":val});
            else if (key == "Partesh")dupli.push({"muni":key,"val":val});
            else if (key == "Kllokot")dupli.push({"muni":key,"val":val});
            else if (key == "Junik")dupli.push({"muni":key,"val":val});
            else if (key == "Graçanic\xeb")dupli.push({"muni":key,"val":val});
        } else {
            if (key == "Hani i Elezit")dupli.push({"muni":key,"val":val});
            else if (key == "Mamush")dupli.push({"muni":key,"val":val});
            else if (key == "Ranilug")dupli.push({"muni":key,"val":val});
            else if (key == "Partesh")dupli.push({"muni":key,"val":val});
            else if (key == "Klokot")dupli.push({"muni":key,"val":val});
            else if (key == "Junik")dupli.push({"muni":key,"val":val});
            else if (key == "Gracanice")dupli.push({"muni":key,"val":val});
        }
    });

    $.each(cities, function(key2, val2) {
        if(document.documentElement.lang == 'sq') {
            $.each(dupli, function(key, val) {
                if (val.muni == "Hani i Elezit" && val2.name == "Ferizaj")val2.value += val.val;
                else if (val.muni == "Mamush\xeb" && val2.name == "Prizren")val2.value += val.val;
                else if (val.muni == "Ranillug\xeb" && val2.name == "Gjilan")val2.value += val.val;
                else if (val.muni == "Partesh" && val2.name == "Gjilan")val2.value += val.val;
                else if (val.muni == "Kllokot" && val2.name == "Gjilan")val2.value += val.val;
                else if (val.muni == "Junik" && val2.name == "Gjakov\xeb")val2.value += val.val;
                else if (val.muni == "Graçanic\xeb" && val2.name == "Prishtin\xeb")val2.value += val.val;
            });
          } else {
            $.each(dupli, function(key, val) {
                if (val.muni == "Hani i Elezit" && val2.name == "Ferizaj")val2.value += val.val;
                else if (val.muni == "Mamush" && val2.name == "Prizren")val2.value += val.val;
                else if (val.muni == "Ranilug" && val2.name == "Gjilan")val2.value += val.val;
                else if (val.muni == "Partesh" && val2.name == "Gjilan")val2.value += val.val;
                else if (val.muni == "Klokot" && val2.name == "Gjilan")val2.value += val.val;
                else if (val.muni == "Junik" && val2.name == "Gjakova")val2.value += val.val;
                else if (val.muni == "Gracanice" && val2.name == "Pristina")val2.value += val.val;
            });
          }
    });

    mapActs(cities)
}

function mapActs(data) {
    if (document.documentElement.lang == 'sq') {
        Highcharts.setOptions({
            lang:{
                downloadJPEG: "Shkarko JPG",
                downloadPDF: "Shkarko PDF",
                downloadPNG: "Shkarko FOTO",
                downloadSVG: "Shkarko SVG",
                printChart: "Printo Grafikun"
            }
        });
        // Create the chart
        Highcharts.mapChart('mapContainer', {
            chart: {
                map: 'countries/kv/kv-all'
            },
            title: {
                text: ''
            },
            legend: {
                title: {
                    text: 'Numri i bizneseve',
                    style: {
                        color: (Highcharts.theme && Highcharts.theme.textColor) || 'black'
                    }
                },
                align: 'right',
                verticalAlign: 'bottom',
                floating: true,
                layout: 'vertical',
                valueDecimals: 0,
                backgroundColor: (Highcharts.theme && Highcharts.theme.legendBackgroundColor) || 'rgba(255, 255, 255, 0.85)',
                symbolRadius: 0,
                symbolHeight: 14
            },
            mapNavigation: {
                enableMouseWheelZoom: false,
                enabled: true,
                buttonOptions: {
                    verticalAlign: 'bottom'
                }
            },
            colorAxis: {
                // minColor: '#fff',
                // maxColor: '#274866',
                dataClasses: [{
                    to: 3
                }, {
                    from: 3,
                    to: 10
                }, {
                    from: 10,
                    to: 30
                }, {
                    from: 30,
                    to: 100
                }, {
                    from: 100,
                    to: 300
                }, {
                    from: 300,
                    to: 1000
                }, {
                    from: 1000
                }]
            },
            plotOptions: {
              series: {
                cursor: 'pointer',
                events: {
                  click: function(e) {
                      // Clearing data of datatable
                      $('#businessesTable').DataTable().clear();
                      // Showing datatable section if hidden
                      $('#businessbyMunicipality').show();

                      // Scrolling to table with animation
                      $('html, body').stop().animate({
                          scrollTop: ($('#businessbyMunicipality').offset().top - 150)
                      }, 600, 'easeInOutExpo');

                      // Properties and building the URL
                      let clickedMunicipality = e.point.options.name

                      // If activity is selected
                      if($('.selected-value').html() != "Të gjitha") {
                        var selectedActivity = $('.selected-value').attr('data-code');
                      } else {
                        selectedActivity = '';
                      }

                      // If status is selected
                      if($('.selected-value-status').html() != "Të gjitha") {
                        if ($('.selected-value-status').html() == "I shuar"){
                          var selectedStatus = "Shuar";
                        } else {
                          selectedStatus = $('.selected-value-status').html();
                        }
                      } else {
                        selectedStatus = '';
                      }

                      // Showing the municipality in DOM
                      $('#searchedMuni').text(clickedMunicipality);
                      $('#businessesTable').DataTable({
                        destroy: true,
                        "bInfo" : false,
                        "language": {
                          "url": "//cdn.datatables.net/plug-ins/1.10.16/i18n/Albanian.json"
                        },
                        'ajax': {
                          url: `/sq/show-businesses?municipality=${clickedMunicipality}&activity=${selectedActivity}&status=${selectedStatus}`,
                          type: 'GET'
                        },
                        "columns": [
                          { "data": "name" },
                          { "data": "status.sq" },
                          { "data": "municipality.place" },
                          { "data": "owners[, ].name" },
                          { "data": "authorized[, ].name" }
                        ]
                      });
                  }
                }
              }
            },
            series: [
                {
                    nullColor: '#f7f7f7'
                },{
                data: data,
                name: 'Bizneset',
                nullColor: '#f7f7f7',
                states: {
                    hover: {
                        color: '#2bb9ae'
                    }
                },
                dataLabels: {
                    enabled: true,
                    allowOverlap: true,
                    format: '{point.options.name}'
                },
                tooltip: {
                    pointFormat: '{point.options.name}: '+'{point.options.value:,.0f}'
                }
            }]
        });
    }
    else {
        Highcharts.setOptions({
            lang:{
                downloadJPEG: "Download JPG",
                downloadPDF: "Download PDF",
                downloadPNG: "Download FOTO",
                downloadSVG: "Download SVG",
                printChart: "Print Chart"
            }
        });
        // Create the chart
        Highcharts.mapChart('mapContainer', {
            chart: {
                map: 'countries/kv/kv-all'
            },
            title: {
                text: ''
            },
            legend: {
                title: {
                    text: 'Number of businesses',
                    style: {
                        color: (Highcharts.theme && Highcharts.theme.textColor) || 'black'
                    }
                },
                align: 'right',
                verticalAlign: 'bottom',
                floating: true,
                layout: 'vertical',
                valueDecimals: 0,
                backgroundColor: (Highcharts.theme && Highcharts.theme.legendBackgroundColor) || 'rgba(255, 255, 255, 0.85)',
                symbolRadius: 0,
                symbolHeight: 14
            },
            mapNavigation: {
                enableMouseWheelZoom: false,
                enabled: true,
                buttonOptions: {
                    verticalAlign: 'bottom'
                }
            },
            colorAxis: {
                // minColor: '#fff',
                // maxColor: '#274866',
                dataClasses: [{
                    to: 3
                }, {
                    from: 3,
                    to: 10
                }, {
                    from: 10,
                    to: 30
                }, {
                    from: 30,
                    to: 100
                }, {
                    from: 100,
                    to: 300
                }, {
                    from: 300,
                    to: 1000
                }, {
                    from: 1000
                }]
            },
            plotOptions: {
              series: {
                cursor: 'pointer',
                events: {
                  click: function(e) {
                      // Clearing data of datatable
                      $('#businessesTable').DataTable().clear();
                      // Showing datatable section if hidden
                      $('#businessbyMunicipality').show();

                      // Scrolling to table with animation
                      $('html, body').stop().animate({
                          scrollTop: ($('#businessbyMunicipality').offset().top - 150)
                      }, 600, 'easeInOutExpo');

                      // Properties and building the URL
                      let clickedMunicipality = e.point.options.name

                      // If activity is selected
                      if($('.selected-value').html() != "All") {
                        var selectedActivity = $('.selected-value').attr('data-code');
                      } else {
                        selectedActivity = '';
                      }

                      // If status is selected
                      if($('.selected-value-status').html() != "All") {
                        if ($('.selected-value-status').html() == "Dissolved"){
                          var selectedStatus = "Dissolved";
                        } else {
                          selectedStatus = "Active"
                        }
                      } else {
                        selectedStatus = '';
                      }

                      // Showing the municipality in DOM
                      $('#searchedMuni').text(clickedMunicipality);
                      $('#businessesTable').DataTable({
                        destroy: true,
                        "bInfo" : false,
                        'ajax': {
                          url: `/en/show-businesses?municipality=${clickedMunicipality}&activity=${selectedActivity}&status=${selectedStatus}`,
                          type: 'GET'
                        },
                        "columns": [
                          { "data": "name" },
                          { "data": "status.sq" },
                          { "data": "municipality.place" },
                          { "data": "owners[, ].name" },
                          { "data": "authorized[, ].name" }
                        ]
                      });
                  }
                }
              }
            },
            series: [{
                data: data,
                name: 'Businesses',
                states: {
                    hover: {
                        color: '#2bb9ae'
                    }
                },
                dataLabels: {
                    enabled: true,
                    allowOverlap: true,
                    format: '{point.options.name}'
                },
                tooltip: {
                    pointFormat: '{point.options.name}: '+'{point.options.value:,.0f}'
                }
            }]
        });
    }
}
