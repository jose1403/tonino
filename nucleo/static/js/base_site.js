$(document).on('ready',inicio);

function inicio(){
	var alturaContentMain = $("#content-main").outerHeight(false);
	$("#content-related").css({'height': alturaContentMain+"px"});
	selectChecked();
	$.superbox();
	modificarTemplateLogin();
}


function selectChecked(){
	$("#main-box").on('change',function(){
		if(this.checked == true){
			$("table").find("input[type='checkbox']").each(function(){
				this.checked = true;
			});

		}else{
			$("table").find("input[type='checkbox']").each(function(){
				this.checked = false;
			});
		}
	});
}


function accion(e){
	var seleccionados = false;
	var elementos = [];
	if($("#select-accion").val() != 'seleccione'){
	  $("table").find("input[type='checkbox']").each(function(i){
			if(this.checked == true){
				seleccionados = true;
				elementos[i-1] = $(this).val();
			}
		});

	  if($("#select-accion").val() == 'Eliminar'){
			if(seleccionados){
				if(confirm("¿Seguro que desea eliminar?")){
					// var csrf = $("input[name*='csrfmiddlewaretoken']").val();
					// var url_view = $("#url-eliminar").val();
					// var request = $.ajax({
					// 	type: 'POST',
					// 	url: url_view,
					// 	data: {
					// 		'csrfmiddlewaretoken':csrf,
					// 		'elementos':elementos
					// 	},
					// });

					// request.done(function(response){
					// 	$("#superbox").html("eliminados");
					// });

					$("#form-accion").submit();
		 	 	}
			}else{

				var mensaje = "No hay Elementos Selecionados";
				alert(mensaje);
			}
		}
	}
}


function modificarTemplateLogin(){

	// alert(location.pathname);
	var nombre = "Silios Tonino";

	if(location.pathname == "/accounts/login/"){
		$("#content-main > h1").html("<span class='icono-lock' style='margin-right:5px;'></span>"+nombre);
	}
}