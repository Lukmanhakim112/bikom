(() => {
  'use strict';
  window.addEventListener('load', () => {
    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    let forms = $('#login-form');
    let loginButton = $('#login-button');
    // Loop over them and prevent submission
    let validation = Array.prototype.filter.call(forms, function(form) {
      form.addEventListener('submit', (e) => {
        if (form.checkValidity() === false) {
          e.preventDefault();
          e.stopPropagation();
        }
          loginButton.prop('disabled', true);
          loginButton.html('<div class="spinner-border spinner-border-sm text-light" role="status"><span class="visually-hidden">Loading...</span></div>');
      }, false);
    });
  }, false);
})();
