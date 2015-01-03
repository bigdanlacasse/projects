<?php
	error_reporting(E_ALL);
	ini_set('display_errors', 'On');
	
	$m = new MongoClient();
	$db = $m->gw2;
	$collection = $db->items;
	$cursor = $collection->find(['type'=>'Weapon'])->limit(1000);
?>

<html>
	<head>
		<title>Sample - Web Page</title>
		<link rel="stylesheet" type="text/css" href="main.css">
	</head>
	<body>
		<table>
		<tr>
			<th>#</th>
			<th>ID</th>
			<th>Image</th>
			<th>Name</th>
			<th>Rarity</th>
			<th>Type</th>
			<th>Description</th>
		</tr>
		<?php
		$counter = 0;
		foreach ($cursor as $document) {
			$counter++;
			echo '<tr>' . 
			'<td>' . $counter . '</td>' .
			'<td>' . $document['item_id'] . '</td>' .
			'<td><img class="item" src="' . $document['image_url'] . '" /></td>' .
			'<td><a class="' . $document['rarity'] . '" href="' . $document['url'] .'">' . $document['name'] . '</a></td>' .
			'<td>' . $document['rarity'] . '</td>' .
			'<td>' . $document['type'] . '</td>' .
			'<td>' . $document['description'] . '</td>' .
			
			'</tr>';
		}

		?>
		</table>
	</body>
</html>
