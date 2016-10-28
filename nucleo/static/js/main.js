$(document).on('ready',inicio);

function inicio(){
	/*Variables Globales*/
	asideLargo = $('aside').height();
	iconoMenu = $(".nav_movil >.icon-menu");
	menu = $('.nav_principal');


	contador = 0;
	/*Todas las funciones ejecutadas al cargar la pagina*/
	largo_section();
	menu_pegajoso();
	menu_movil();
	menu_admin();
	mostrar_menu_lg();
}


/*Adapta el largo del section a un tamaño mayor al del aside*/
function largo_section(){
	$('section').css({'minHeight':asideLargo+50+'px'});
}

/*El menu se queda pegado en la parte superior de la pagina*/
function menu_pegajoso(){
	if($(window).width() > 768){
		
		$(window).scroll(function(){
			if($(window).scrollTop() > $('header').height()){
				$('nav').addClass('menu_pegajoso');
				$('section').css({'marginTop':$('nav').height()+'px'});
				$('aside').css({'marginTop':$('nav').height()+'px'});
			}else{
				$('nav').removeClass('menu_pegajoso');
				$('section').css({'marginTop':'0px'});
				$('aside').css({'marginTop':'0px'});
			}
		});
	}
}

/*Ejecuta el evento para desplegar el menu en dispositivos moviles*/
function menu_movil(){
	iconoMenu.on('click',function(){
		if(contador==0){
			menu.slideDown('medium');
			contador=1;
		}else{
			menu.slideUp('medium');
			contador =0;
		}
	});
}

/*Cambia el menu de movil al redimecionar la ventana a una resolucion mayor de 768px*/

function mostrar_menu_lg(){
	$(window).resize(function(){
		
		if($(window).width() > 768){
			menu.css({'display':'block'});
		}else{
			menu.hide();
		}
	});
}


