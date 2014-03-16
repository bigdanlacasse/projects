<div class="container">
<div class="jumbotron">
    <h3 class="<?=$item->rarity?>"><?=$item->name?></h3>
    <div class="">
	<img class="item" src="<?=$item->image_url?>" />
    </div>
    <p>
	<?=$item->type?>
    </p>
    <p>
	<?=$item->description?>
    </p>
    <p>
	<?=$item->rarity?>
    </p>
    <p>
	<?=$item->vendor_value?>
    </p>
</div>
<pre><?=var_dump($this->item->weapon)?></pre>
</div>
