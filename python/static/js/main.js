$(document).ready(function() {
	
	// Only bind this if we actually have the right element.
	if ($('#count_down').length) {
		display_time();
		setInterval(display_time, 1000);
	}
      
	function display_time() {	
		if ($('#count_down').length) {
			arrival = moment('2015-02-20 16:30:00', 'YYYY-MM-DD HH:mm:ss');
			now = moment();
			
			dateDiff = moment.duration(arrival - now);
			
			numDays = dateDiff.days();
			numHours = dateDiff.hours();
			numMinutes = dateDiff.minutes();
			numSeconds = dateDiff.seconds();
			
			dayLabel = 'days';
			hourLabel = 'hours';
			minLabel = 'minutes';
			secLabel = 'seconds';
			
			if (numDays == 1) {
				dayLabel = 'day';
			}
			if (numHours == 1) {
				hourLabel = 'hour';
			}
			if (numMinutes == 1) {
				minLabel = 'minute';
			}
			if (numSeconds == 1) {
				secLabel = 'second';
			}
			
			timeString = numDays + ' ' + dayLabel + ' ' + 
						 numHours + ' ' + hourLabel  + ' ' +
						 numMinutes + ' ' + minLabel + ' ' +
						 numSeconds + ' ' + secLabel + '!';
			
			$('#count_down').text(timeString);	
		}		
	}
});
