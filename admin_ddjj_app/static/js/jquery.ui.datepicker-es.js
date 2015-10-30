/* Written by Keith Wood (kbwood@virginbroadband.com.au) and StÃ©phane Nahmani (sholby@sholby.net). */
(function($){
        $.datepicker.regional['es'] = {
                closeText: 'Cerrar',
                prevText: 'Anterior',
                nextText: 'Siguiente',
                currentText: 'Hoy',
                monthNames: ['Enero','Febrero','Marzo','Abril','Mayo','Junio',
                'Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre'],
                monthNamesShort: ['Ene','Feb','Mar','Abr','May','Jun',
                'Jul','Ago','Sep','Oct','Nov','Dic'],
                dayNames: ['Domingo','Lunes','Martes','Miércoles','Jueves','Viernes','Sábado'],
                dayNamesShort: ['Dom','Lun','Mar','Mie','Jue','Vie','Sab'],
                dayNamesMin: ['Do','Lu','Ma','Mi','Ju','Vi','Sa'],
                dateFormat: 'yy-mm-dd', firstDay: 1,
                isRTL: false};
        $.datepicker.setDefaults($.datepicker.regional['es']);
})(grp.jQuery);
