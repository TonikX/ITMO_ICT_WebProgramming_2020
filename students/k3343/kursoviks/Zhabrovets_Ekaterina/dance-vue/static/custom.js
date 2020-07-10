// templatemo 467 easy profile

// PRELOADER
$(window).load(function(){
    $('.preloader').delay(90).fadeOut("slow"); // set duration in brackets
});

// HOME BACKGROUND SLIDESHOW
$(function(){
    jQuery(document).ready(function() {
		$('body').backstretch([
			"1.jpg",
			"2.jpg",
			"3.jpg",
	 			], 	{duration: 5000, fade: 1300});
		});
})

