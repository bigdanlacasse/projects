<?php

$path_info = pathinfo(__FILE__);

define('INCLUDE_PATH', $path_info['dirname'] . '\\');
unset($pathinfo);

require_once INCLUDE_PATH . 'utility_functions.php';

// debug(INCLUDE_PATH, 'Location of include path...');
// debug($_SERVER);
// die();