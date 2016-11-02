$(document).ready(inicio);


function inicio(){

	$(".file_wrapper>input").on('change',function(){
		readURL(this);
	});
}

function readURL(input) {

    if(input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onload = function (e) {
            $('#imagen_rubro').attr('src',e.target.result);
        }

        reader.readAsDataURL(input.files[0]);
    }
}