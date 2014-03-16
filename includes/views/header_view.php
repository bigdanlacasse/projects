<html>
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <meta name="description" content="">
        <meta name="author" content="Dan LaCasse">
        <title><?=$title?></title>
        
        <!-- Bootstrap core CSS -->
        <link href="/bootstrap.min.css" rel="stylesheet">
        <link rel="stylesheet" type="text/css" href="/main.css">
    </head>
    <body>
		<div class="header" role="navigation">
			<div class="container">
				<ul class="nav nav-pills pull-right">
					<li <?php if ($page=='home'){ echo 'class="active"';} ?>>
						<a href="/page/view/home">Home</a>
					</li>
					<li <?php if ($page=='gw2items'){ echo 'class="active"';} ?>>
						<a href="/items/browse">Guild Wars 2 Items</a>
					</li>
					<li <?php if ($page=='about'){ echo 'class="active"';} ?>>
						<a href="/page/view/about">About</a>
					</li>
				</ul>
			</div>
		</div>		
