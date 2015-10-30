(function($){
$(window).bind('load', function(){
	function set_persona_cargo_relation(persona_id){ 
		/*
		* @param {string|number} id_persona
		* setea el id_persona en el popup de persona cargo para traer solamente los cargos correspondientes a la misma
		*/
		if(!persona_id){ return false}
		var btn_persona_cargo = $("a#lookup_id_persona_cargo"),
			url_persona_cargo = btn_persona_cargo.attr("href").split('?')[0],
			search = $("a#lookup_id_persona_cargo").attr("href").split('?')[1],
			o = JSON.parse('{"' + decodeURI(search).replace(/"/g, '\\"').replace(/&/g, '","').replace(/=/g,'":"') + '"}')
		
		o.persona__id__exact = persona_id;
		url_persona_cargo += "?" +$.param(o);
		btn_persona_cargo.attr("href", url_persona_cargo);
	}

	function get_persona_id(_str){
		/*
		* @param {string} _str es el valor del \#id_persona-autocomplete
		* obtiene el id desde regex
		*/
		var re = /\(([0-9]{1,})\)/;
		var match = re.exec(_str);
		if(match){
			var persona_id = match[1];
	    	set_persona_cargo_relation(persona_id)
		}
	}

	var $persona = $("#id_persona"),
		$ui_persona = $('#id_persona-autocomplete');

	if($persona.val()){
		set_persona_cargo_relation($persona.val());
	}
	
	$persona.on('change', function() {
		get_persona_id($ui_persona.val());
	});

	$persona.on("blur", function() {
		get_persona_id($ui_persona.val());
	});

});
})(grp.jQuery);
