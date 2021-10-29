$(document).ready(function () {
    $('#id_informacionAdicional').height("150px");

    bootstrapValidate('#id_nombre', 'max:100:No debe superar los 100 caracteres!|required:Por favor rellene este campo!');
    //bootstrapValidate('#id_telefonoContacto', 'regex:^[0-9]+$:Por favor solo ingrese caracteres numéricos!|min:8:Debe contener 8 digitos!|max:8:Debe contener 8 digitos!');
    
    reportar = function (name, id) {
        $('#idPaciente').val(id);
        $('#reportText').text("Desea reportar el registro: " + name);
    };
    reportar();

    $('#addDonante').on('hidden.bs.modal', function () {
        //$("#id_telefonoContacto").val('');
        $("#id_nombre").val('');
        $("#id_informacionAdicional").val('');
    })


    $('#tableDonante').DataTable({
        "order":[],
        "aaSorting":[],

        "language": {
            "sProcessing": "Procesando...",
            "sLengthMenu": "Mostrar _MENU_ registros",
            "sZeroRecords": "No se encontraron resultados",
            "sEmptyTable": "Ningún dato disponible en esta tabla",
            "sInfo": "Mostrando _START_ al _END_ de _TOTAL_ registros",
            "sInfoEmpty": "Ningún dato disponible",
            "sInfoFiltered": "(filtrado de un total de _MAX_ registros)",
            "sInfoPostFix": "",
            "sSearch": "Buscar:",
            "sUrl": "",
            "sInfoThousands": ",",
            "sLoadingRecords": "Cargando...",
            "oPaginate": {
                "sFirst": "Primero",
                "sLast": "Último",
                "sNext": "Siguiente",
                "sPrevious": "Anterior"
            },
            "oAria": {
                "sSortAscending": ": Activar para ordenar la columna de manera ascendente",
                "sSortDescending": ": Activar para ordenar la columna de manera descendente"
            },
            "buttons": {
                "copy": "Copiar",
                "colvis": "Visibilidad"
            }
        }
    });

});