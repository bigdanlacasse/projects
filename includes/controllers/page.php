<?php
class Page extends CI_Controller {
	/*
	    View simple pages
	*/
	public function view($page = 'home') {
	    if ( ! file_exists(APPPATH . '/views/'.$page.'_view.php')) {
	        // Whoops, we don't have a page for that!
		show_404();
	    }
	    $data['title'] = ucfirst($page); // Capitalize the first letter
	    $data['page'] = $page;

	    $this->load->view('header', $data);
	    $this->load->view('/' . $page . '_view' , $data);
	    $this->load->view('footer', $data);
	}
	
}
?>
