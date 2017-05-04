function selectDist() {
    $('.test').html('')
    $.ajax({
        data : {
            city_id : $('#city_id').val(),
            status : $('#biz_status').val()
        },
        type : 'POST',
        url : '/visualization',
        success: function(response) {
            var data = '<table class="table table-entities table-bordered table-striped table-hover">'+
            '<thead>'+
            '<th>#</th>'+
            '<th>Emri i Biznesit</th>'+
            '<th>Komuna</th>'+
            '<th>Statusi i Biznesit</th>'+
            '<th>Kapitali</th>'+
            '</thead>'+
            '<tbody>';
            var i = 1;
            $.each(response.result, function(key, val) {
                data +='<tr>'+
                '<td>'+i+'</td>'+
                '<td id="topname"><a href='+val.arbkUrl+'>'+val.name+'</a>'+
                '</td>'+
                '<td class="ksbk">'+val.municipality.municipality+
                '</td>'+
                '<td class="ksbk">'+val.status+
                '</td>'+
                '<td class="ksbk">'+val.capital+
                '</td>'+
                '</tr>';
                i++
            });
            data +='</tbody>'+'</table>';
            $('#topTable').html(data);
        },
        error: function(error) {
            console.log(error);
        }
    })
}
