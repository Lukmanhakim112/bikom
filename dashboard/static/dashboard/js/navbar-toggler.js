$(document).ready(() => {

	let sidebar = $("#sidebar");

	$("#sidebartoggler").click(() => {
		if (window.screen.availWidth > 414) {
			sidebar.toggleClass("d-sm-flex");
		} else {
			sidebar.toggleClass("d-none");
		}
	});

});
