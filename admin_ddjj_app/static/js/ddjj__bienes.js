(function($){
$(window).bind('load', function(){
	// close all items when add new bien
	document.getElementById("bienes-group")
		.addEventListener('click', function(e){
			if(e.target.nodeName == "A" || e.target.parentElement.nodeName == "A" ){ // si es un <a>
				
				var btn_add_patt = /grp-add-handler\s?bienes-group/gi; //check if add bien
				if(btn_add_patt.test(e.target.className || e.target.parentElement.className)){
					open_only_last_bien();
				}

			}
		});

	document.getElementById("bienes-group")
		.addEventListener('change', function(e){
			var tipo_bien_patt = new RegExp('tipo_bien');
			if(tipo_bien_patt.test(e.target.id)){ // check if is tipo_bien
				// filter nombre_bien by tipo_bien
				// var selected = e.target.selectedOptions[0];
				var select = e.target;
				// var i = get_index_form_bien(select.id);
				set_url_btn_nombre_bien(select);
				// show_felds_for_tipo_bien(selected.text, i);
				show_felds_for_tipo_bien(select);
			}
		});


    // Lookup Nombre Bien
    $('.nombre_bien .related-lookup').click(function() {
        var tipo_bien_select_id = this.id.split('-')[1];
        var tipo_bien_id = $('#id_bienes-'+ tipo_bien_select_id +'-tipo_bien').val();
        var href_base, href;
        if(tipo_bien_id !== '') {
            href_base =  $(this).attr('href').split('?')[0];
            href = href_base + '?tipo_bien__id__exact=' + tipo_bien_id;
            $(this).attr('href', href);
        }
    });
    
    // Get TIPO BIENES
    var tipo_bienes = {'0': [], '1': [], '2': []}; // sorted by classification
    
    $.get( "/api/tipo_bien", function( data ) {
        var classification, pk;
        data.forEach(function(x) {
            classification = x.fields.clasificacion;
            if(classification !== null) {
                pk = x.pk;
                tipo_bienes[classification].push(pk);
            }
        });

        // busca en todos los bienes el select de tipo_bien y muestra los campos correspondientes al tipo_bien seleccionado
	    $("#bienes-group .grp-items > .grp-dynamic-form").each(function(i){
		    var select = $(".tipo_bien select", this)[0]; // toma el texto de la opcion seleccionada en el tipo bien
    	    show_felds_for_tipo_bien(select);
	    });
        
    }, 'json');

    // helpers
	function show_felds_for_tipo_bien(select) {
		/*
		* @param {string} \ select: es el <select> de tipo_bien seleccionado
		* muestra los campos relacionados al tipo de bien segun el combo de tipo bien
		*/
		var i = get_index_form_bien(select.id);
        var wrapper_bien = $("#bienes-"+i).length ? $("#bienes-"+i) : $("#bienes"+i);
        $("fieldset.bien-datos", wrapper_bien).hide(); // esconde todos
        
		var selected = select.selectedOptions[0].value;
		
		var datos_bien = null;
        if(selected != "") {
            // +selected = String --> Number
            if (tipo_bienes['0'].indexOf(+selected) >= 0) { 
			    datos_bien = $(".tipobien-0", wrapper_bien);
		    } else if(tipo_bienes['1'].indexOf(+selected) >= 0) {
			    datos_bien = $(".tipobien-1", wrapper_bien);
            } else if(tipo_bienes['2'].indexOf(+selected) >= 0) {
			    datos_bien = $(".tipobien-2", wrapper_bien);
		    } 

            if(datos_bien !== null) {
		        datos_bien.show(); // muestra solo el correspondiente
            }
        }
		
	}


	function open_only_last_bien(){
		var last = $("#bienes-group .grp-items > .grp-dynamic-form")
					.addClass('grp-closed').last()
			
		last.removeClass('grp-closed');
		var select_tipo_bien = $(".tipo_bien select", last)[0];
		show_felds_for_tipo_bien(select_tipo_bien);
	}


	function get_index_form_bien(_str){
		/*
		* @param {string} \ ex: "id_bienes-0-tipo_bien"
		* obtiene el indice en el que esta en el form
		*/
		var re = /\-([0-9]{1,})\-/;
		var match = re.exec(_str);
		if(match){
			var index = match[1];
	    	return index;
		}
	}


	function set_url_btn_nombre_bien(select){
		/*
		* @param {object} \ select: es el <select> de tipo_bien seleccionado
		* cambia la url del related_lookup de nombre_bien para que aparezcan filtrados solo los bienes pertenecientes el tipo_bien seleccionado
		*/

		var i = get_index_form_bien(select.id);
		var selected_val = select.selectedOptions[0].value
		var nom_bien_btn = $("#lookup_id_bienes-"+i+"-nombre_bien");
		url = nom_bien_btn.attr("href").split('?')[0],
			search = nom_bien_btn.attr("href").split('?')[1],
			o = JSON.parse('{"' + decodeURI(search).replace(/"/g, '\\"').replace(/&/g, '","').replace(/=/g,'":"') + '"}')
		
		o.tipo_bien__id__exact = selected_val;
		url += "?" +$.param(o);
		nom_bien_btn.attr("href", url);
	} 

});
})(grp.jQuery);
