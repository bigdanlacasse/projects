/*****************************************************************************************************
 * 
 * 
 * 
 * 
 * 
 * 
 *****************************************************************************************************/

// Trigger & Bind events
$(document).ready(
	function(){
		toggleSubTypes();
		
		$('#item_type').on('change', toggleSubTypes)
	}
);


/**
 * Filter out any subtypes which aren't relevant to this primary item type 
 * 
 */
function toggleSubTypes() {
	type_ele = $('#item_type');
	selected_type = type_ele.val();
	
	if (selected_type) {
	    $('#sub_type').find('option').hide();
		$('#sub_type').find('[data-parent=' + selected_type + ']').show();

	} else {
		$('#sub_type').find('option').hide()
	}

}