// Handle the creation of the date picker.
// The form validation is made on the server on the back, NOT HERE
// Perform a rapid first check if the date are not available
// This first check has NO VALUE, it is just made for user conveniance

$(function() {

  $('input[name="date-range"]').daterangepicker({
  	minDate: moment(),
      autoUpdateInput: false,
      locale: {
          cancelLabel: 'Clear'
      }
  });

  $('input[name="date-range"]').on('apply.daterangepicker', function(ev, picker) {
      $(this).val(picker.startDate.format('MM/DD/YYYY') + ' - ' + picker.endDate.format('MM/DD/YYYY'));
  });

  $('input[name="date-range"]').on('cancel.daterangepicker', function(ev, picker) {
      $(this).val('');
  });

});