$(document).on('ready',inicio);


function inicio(){

	$("#next").on("click",next);
	$("#previous").on("click",previous);			
	$("#slideshow > div.item:gt(0)").hide();

	slide = setInterval(change,4000);

}

function change(){
	
	$("#slideshow > div.item:first")
	.fadeOut(1000)
	.next()
	.fadeIn(1000)
	.end()
	.appendTo("#slideshow");
}

function next(){
	
	$("#slideshow > div.item:first")
	.fadeOut(200)
	.next()
	.fadeIn(100)
	.end()
	.appendTo("#slideshow");
	clearInterval(slide);
	slide = setInterval(change,4000);
}

function previous(){
	$("#slideshow > div.item:first")
	.fadeOut(200)
	.prev()
	.fadeIn(100)
	.end()
	.appendTo("#slideshow");
	clearInterval(slide);
	slide = setInterval(change,4000);
}