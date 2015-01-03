<?php

/**
 * undocumented function
 *
 * @return int
 **/
function foo($num) {
	static $test;
	if (empty($test)) {
		$test = $num;
	}

	return $test;
}

for ($i=1; $i <= 10; $i++) { 
	echo $i . '  -   ' . foo($i) . '</br>';
}


?>