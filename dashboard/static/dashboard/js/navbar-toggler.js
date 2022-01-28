$(document).ready(() => {

	let sidebar = $("#sidebar");
	let navbar = $("#navbar");

	$("#sidebartoggler").click(() => {
		if (window.screen.availWidth > 414) {
			sidebar.toggleClass("d-sm-flex");
		} else {
			sidebar.toggleClass("d-none");
		}
	});

	
	$(document).scroll(() => {
		const scrollTop = this.pageYOffset;

		if(scrollTop >= 20){
			navbar.addClass('shadow-sm');
		} else {
			navbar.removeClass('shadow-sm');
		}

	});

});
