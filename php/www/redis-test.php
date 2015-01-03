<?php
	error_reporting(E_ALL);
	ini_set('display_errors', 'On');

	define('INCLUDES_PATH', dirname(__FILE__) . '/../includes');
	define('WEB_ROOT', dirname(__FILE__));
	
	require INCLUDES_PATH . '/libraries/predis/autoload.php';
	
	
	
?>
<html>
  <head>
  </head>
  <body> 
	<div>
    <?php 
		// since we connect to default setting localhost
		// and 6379 port there is no need for extra
		// configuration. If not then you can specify the
		// scheme, host and port to connect as an array
		// to the constructor.
		try {
			$redis = new Predis\Client();

			echo "Successfully connected to Redis";
			$redis->set('item123', 'sword');
		}
		catch (Exception $e) {
			echo "Couldn't connected to Redis";
			echo $e->getMessage();
		}
    ?> 
	</div>
  </body>
</html>
