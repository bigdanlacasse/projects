<?php
class Item extends CI_Model {
    public $b_loaded = false;
    public $errors = array();
    private $dao;

    /**
     * Setup connectivity
     **/
    public function __construct() {
        parent::__construct();
        $mongo = new MongoClient();
		$db = $mongo->gw2;
		$this->dao = $db->items;
    }

    /**
     * Load this item
     **/
    public function load($item_id=0) {
        $data = $this->dao->findOne(['item_id'=>$item_id]);
        if (!empty($data)) {
	    $this->populate($data);
	    $b_loaded = true;
	} else {
	    $this->errors[] = 'Item not found!';
	}
    }

    /**
     * Populate properties dynamically
     **/
    public function populate($data=array()) {
	$exclude = array('w', 'wtimeout', '_id', '$id');

	foreach ($data as $key => $value) {	    
	    if (!in_array($key, $exclude)) {
	        $this->$key = $value;
	    }
	}
    }
}
?>
