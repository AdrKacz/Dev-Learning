// Create the DatePickers
const dates = document.querySelectorAll("div.date-container");
const start_date = new Datepicker(dates[0]);
const end_date = new Datepicker(dates[1]);

const start_date_input = document.querySelector("input#id_start_date");
const end_date_input = document.querySelector("input#id_end_date");

const today = new Date()

// Function for the DatePickers
function enabled_days_start(date) {
	return true;
};

function enabled_days_end(date) {
	if (enabled_days_start(date)) {
		return true;
	}
	return false;
};

function format_date_start(date) {
	const date_number = '0' + date.getDate();
	const month_number = '0' + (date.getMonth() + 1);

	// Set input
	start_date_input.value = [
		date.getFullYear(),
		month_number.substring(month_number.length - 2),
		date_number.substring(date_number.length - 2),
		].join('-');


	// Set visible value
	dates[0].childNodes[0].textContent = [
		WEEKDAYS_SHORT[date.getDay()],
		date.getDate(),
		MONTHS_SHORT[date.getMonth()],
		date.getFullYear(),
		].join(' ');

	return '';
};

function format_date_end(date) {
	const date_number = '0' + date.getDate();
	const month_number = '0' + (date.getMonth() + 1);

	// Set input
	end_date_input.value = [
		date.getFullYear(),		
		month_number.substring(month_number.length - 2),
		date_number.substring(date_number.length - 2),
		].join('-');


	// Set visible value
	dates[1].childNodes[0].textContent = [
		WEEKDAYS_SHORT[date.getDay()],
		date.getDate(),
		MONTHS_SHORT[date.getMonth()],
		date.getFullYear(),
		].join(' ');

	return '';
};


// Config the DatePickers
start_date.config({
	first_date: today,
    initial_date: today,
    enabled_days: enabled_days_start,
    format: format_date_start,
    first_day_of_week: "Monday",
});

end_date.config({
	first_date: today,
    initial_date: today,
    enabled_days: enabled_days_end,
    format: format_date_end,
    first_day_of_week: "Monday",
});


// Display Arrivée / Départ at the beginning
function remove_start_text() {
	dates[0].childNodes[0].setAttribute("class","")
	dates[0].childNodes[1].setAttribute("class","hidden")
	dates[0].removeEventListener("click", remove_start_text);
}

function remove_end_text() {
	dates[1].childNodes[0].setAttribute("class","")
	dates[1].childNodes[1].setAttribute("class","hidden")
	dates[1].removeEventListener("click", remove_end_text);
}

dates[0].addEventListener("click", remove_start_text);
dates[1].addEventListener("click", remove_end_text);

// Handle the process for the initial dates (HAVE TO BE DONE)