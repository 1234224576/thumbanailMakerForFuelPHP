<?php

class Controller_Thumbanail extends Controller_Rest{
    
    public function action_index(){
    	$url = Input::get('url', 'http://google.com');

    	Asset::add_path('assets/py/', 'py');
    	$path = Asset::find_file('thumbnail.py', 'py');
    	$command = "python ".$path." ".$url;
    	$result = shell_exec($command);

        return $this->response(array(
                'result' => $result,
           )); 
    }
}
