<?php
class Items extends CI_Controller {

    public function view($item_id = 0, $item_name = '') {
		// Load appropriate model
		$this->load->model('item_model');
		$this->item->load($item_id);

		// Setup data
		$data['page'] = 'gw2items';
		$data['title'] = 'Guild Wars 2 - ' . $item_name;
		$data['item'] = $this->item;

		// -- Load the view for this page
		$this->load->view('header', $data);
		$this->load->view('/item_view' , $data);
		$this->load->view('footer', $data);
    }
    
    public function browse() {
		// Use helper to get meta data for filters
		
		// Setup data
		$data['page'] = 'gw2items';
		$data['title'] = 'Guild Wars 2 - ' . $item_name;

		// -- Load the view for this page
		$this->load->view('header', $data);
		$this->load->view('/browse_view' , $data);
		$this->load->view('footer', $data);		
	}
	
	public function results() {
		
		
	}
}
?>
