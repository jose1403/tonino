$(document).on('ready',inicio);

function inicio(){
	btnProductos = $('#btnProductos');
	btnArticulos = $('#btnArticulos');
	productos = $('#productos');
	articulos = $('#articulos');

	btnProductos.on('click',function(){
		mostrar('productos');
	});
	btnArticulos.on('click',function(){
		mostrar('articulos');
	});
}


function mostrar(modulo){
	if(modulo == 'productos'){
		btnArticulos.css({'backgroundColor':'#fff','color':'#000'});
		articulos.slideUp('fast',function(){
			productos.slideDown('fast');
			btnProductos.css({'backgroundColor':'#79CDA3','color':'#fff'});
		});
		
	}else{
		btnProductos.css({'backgroundColor':'#fff','color':'#000'});
		productos.slideUp('fast',function(){
			articulos.slideDown('fast');
			btnArticulos.css({'backgroundColor':'#79CDA3','color':'#fff'});
		});
		
	}
}