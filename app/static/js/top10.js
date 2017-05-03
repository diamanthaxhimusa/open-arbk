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
            '<th>Emri i Biznesit</th>'+
            '<th>Komuna</th>'+
            '<th>Statusi i Biznesit</th>'+
            '<th>Linku per ne ARBK</th>'+
            '<th>Kapitali</th>'+
            '</thead>'+
            '<tbody>';
            $.each(response.result, function(key, val) {
                data +='<tr>'+
                '<td>'+val.name+
                '</td>'+
                '<td>'+val.municipality.municipality+
                '</td>'+
                '<td>'+val.status+
                '</td>'+
                '<td>'+
                '<a href="'+val.arbkUrl+'">linku</a>'+
                '</td>'+
                '<td>'+val.capital+
                '</td>'+
                '</tr>';
            });
            data +='</tbody>'+'</table>';
            $('#topTable').html(data);
        },
        error: function(error) {
            console.log(error);
        }
    })
}
