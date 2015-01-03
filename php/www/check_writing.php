<?php
/**
 * Check writing...
 *
 *
 * 350.25 -> Three Hundred fifty Dollars and twenty five cents
 * 1613.43 -> One Thousand Six hundred thirteen Dollars and 43 cents
 * 1219.00 -> One Thousand Two Hundred nineteen dollars
 *
 *  {3} {10^{index}} ({2}{1}|{1}) Dollars (AND ({2}{1}|{1}) CENTS)
 */

$amount = 350.25;

echo convert_to_english($amount);

/*****************************************************************/

/**
 * undocumented function
 *
 * @return void
 * @author 
 **/
function convert_to_english($amount=0) {
	$return_value = '';
	$amount_str = (string)$amount;
	$currency_parts = explode('.', $amount_str);

	// Deal with portions before & after decimal point
	for ($index=0; $index < count($currency_parts); $index++) { 
		$return_value .= convert_to_text($currency_parts[$index]) . map_denomination($index);

		die();
		if ($index < count($currency_parts) - 1) {
			$return_value .= ' AND ';
		}
	}

	return $return_value;
}

/**
 * undocumented function
 *
 * @return void
 * @author 
 **/
function map_denomination($pos) {
	$map = ['dollars', 'cents'];

	return ' ' . $map[$pos];
}

/**
 * undocumented function
 *
 * @return void
 * @author 
 **/
function convert_to_text($number_string) {
	$map = [
	    '0' => '',
		'1' => 'one',
		'2' => 'two',
		'3' => 'three',
		'4' => 'four',
		'5' => 'five',
		'6' => 'six',
		'7' => 'seven',
		'8' => 'eight',
		'9' => 'nine',
		'10' => 'ten',
		'11' => 'eleven',
		'12' => 'twelve',
		'13' => 'thirteen',
		'14' => 'fourteen',
		'15' => 'fifteen',
		'16' => 'sixteen',
		'17' => 'seventeen',
		'18' => 'eighteen',
		'19' => 'nineteen',
		'20' => 'twenty',
		'30' => 'thirty',
		'40' => 'fourty',
		'50' => 'fifty',
		'60' => 'sixty',
		'70' => 'seventy',
		'80' => 'eighty',
		'90' => 'ninety'
	];

	// 1,000,000
	$map_tens_place = [
	 //    '2' => 'hundred',
		// '3' => 'thousand',
		// '6' => 'million',
		// '9' => 'billion',
		'bananas' => 'trillion'
	];

	$all_digits = str_split($number_string);
	var_dump($all_digits);
	var_dump($map_tens_place);

	$place = 0;
	for ($y=count($all_digits)-1; $y>=0; $y--) {
		echo $all_digits[$y];
		
		$current_place = (string) $place;

		echo ' --- place:' . $current_place . '<br />';
		//echo $map_tens_place[$current_place];
		//var_dump(in_array($current_place, $map_tens_place));
		var_dump(in_array('bananas', $map_tens_place));

		if (in_array($current_place, $map_tens_place)) {
			echo ' ' . $map_tens_place[$current_place];
		}

		$place++;
	}

	// @todo - Figure out how to deal with splitting this into groups and calling recursively.
	//$groups = str_split($number, 3);

}
