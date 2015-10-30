(function($) {

    $(document).ready(function() {
        $('#grappelli_save').click(function (e) {
            $('#grappelli_save').click(false);
            $('#grappelli_saveasnew').click(false);
            $('#grappelli_addanother').click(false);
            $('#grappelli_continue').click(false);
        });
        $('#grappelli_saveadd').click(function (e) {
            $('#grappelli_save').click(false);
            $('#grappelli_saveasnew').click(false);
            $('#grappelli_addanother').click(false);
            $('#grappelli_continue').click(false);
        });
        $('#grappelli_savecont').click(function (e) {
            $('#grappelli_save').click(false);
            $('#grappelli_saveasnew').click(false);
            $('#grappelli_addanother').click(false);
            $('#grappelli_continue').click(false);
        });
        $('#grappelli_saveasnew').click(function (e) {
            $('#grappelli_save').click(false);
            $('#grappelli_saveasnew').click(false);
            $('#grappelli_addanother').click(false);
            $('#grappelli_continue').click(false);
        });
    });
    
})(grp.jQuery);
