(function($){
    $(function() {
        $('.tipo_bien select').on('change', function() {
            var bien_name = $(this).attr('name').split('-');
            var bien = bien_name[0] + bien_name[1];
            var bien_id = '#' + bien;
            $(bien_id + ' .bien-datos').hide();

            var tipo_bien = $(this).find(':selected').data('clasificacion');
            var tipo_bien_class = '.tipobien-' + tipo_bien;
            $(bien_id + ' ' + tipo_bien_class).show();
        });
    });
})(grp.jQuery);
