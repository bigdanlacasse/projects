<?php

/**
 * undocumented function
 *
 * @return void
 **/
function debug($var, $label='') {
	ob_start();
	var_dump($var);
	$output = ob_get_contents();
	ob_clean();

	$label = (string) $label;

	echo '<div style=" background-color: lightgreen; margin: 10px; padding: 20px;">' . 
		'<span style="display: inline-block">' . $label . '</span>' .
		$output . 
		'</div>';
}