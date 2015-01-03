<?php
/**
 * Sample things....
 *
 */
$wordgroups = [
	['quick', 'slow', 'lazy', 'stupid', 'ugly'],
	['red', 'brown', 'black', 'green'],
	['dog', 'cat', 'bear'],
];


//---------------------------------------------
// Recursive version
//---------------------------------------------
traverse_words($wordgroups);

function traverse_words($all_words, $pos_o=0, $provided_words='', &$counter=0) {
	$look_ahead = $pos_o + 1;

	// For each word in this group, add to provided words and check to see if there
	// are additional groups which need to be discovered
	for ($a=0; $a < count($all_words[$pos_o]); $a++) {
		$this_word = $all_words[$pos_o][$a] . ' ';
		$current_words = $provided_words . $this_word;

		// if there are no more groups looking ahead, we found the last one
		if (empty($all_words[$look_ahead])) {
			$counter += 1;
			echo $counter . ') ' . $current_words . '<br />';
		} else {
			// keep digging....
			traverse_words($all_words, $look_ahead, $current_words, $counter);
		}
	}
}