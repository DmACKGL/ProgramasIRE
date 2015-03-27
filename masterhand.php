<?php
# GamerLive 2015
 
 
// Una MasterHand será el controlador del nodo, que se conecta a la API ubicada en cada máquina y se encarga de brindar las funciones necesarias para
class MasterHand {
 
  public $api_url = NULL;
  public $api_secret = NULL;
  public $api_status = 'ok';
 
  function __construct($api_url, $api_secret) {
    $this->api_url = $api_url;
    $this->api_secret = $api_secret;
  }
  public function doAPI($command, $arg1 = null, $arg2 = null, $arg3 = null) {
    switch($command) {
 
      // parametros: $path - ruta que se desea consultar
      case 'is_dir':
        if($arg1 === NULL) {
          return false;
        }
        $data = array('act' => 'is_dir','path' => $arg1);
        if($ret = $this->doCurl($data)) {
          return $ret['is_dir'];
        } else {
          if($this->lastAPIStatus() == 'error') {
            return '!ERROR';
          }
          return false;
        }
        break;
 
      // parametros: $path - ruta que se desea consultar
      case 'file_exists':
        if($arg1 === NULL) {
          return false;
        }
        $data = array('act' => 'file_exists','path' => $arg1);
        if($ret = $this->doCurl($data)) {
          return $ret['file_exists'];
        } else {
          if($this->lastAPIStatus() == 'error') {
            return '!ERROR';
 
          }
          return false;
        }
        break;
      // parametros: $path - ruta que se desea consultar
      // @return string con contenido del archivo
      case 'file_get_contents':
        if($arg1 === NULL) {
          return false;
        }
        $data = array('act' => 'file_get_contents','path' => $arg1);
        if($ret = $this->doCurl($data)) {
          return base64_decode($ret['file_get_contents']);
        } else {
          if($this->lastAPIStatus() == 'error') {
            return '!ERROR';
 
          }
          return false;
        }
        break;
 
      // parametros: $path - ruta que se desea consultar
      //             $contenido - contenido a escribir
      // @return true si es que esta todo ok
      case 'file_put_contents':
        if($arg1 === NULL || $arg2 === NULL) {
          return false;
        }
        $data = array('act' => 'file_put_contents','path' => $arg1, 'content' => base64_encode($arg2));
        if($ret = $this->doCurl($data)) {
          return true;
        } else {
          if($this->lastAPIStatus() == 'error') {
            return '!ERROR';
 
          }
          return false;
        }
      break;
   
      // parametros: $comando - comando que se desea ejecutar
      case 'shell_exec':
        if($arg1 === NULL) {
          return false;
        }
        $data = array('act' => 'shell_exec','cmd' => base64_encode($arg1));
        if($ret = $this->doCurl($data)) {
          return base64_decode($ret['shell_exec']);
        } else {
          if($this->lastAPIStatus() == 'error') {
            return '!ERROR';
 
          }
          return false;
        }
        break;
 
    }
  }
  private function lastAPIStatus() {
   return $this->api_status;
  }
  private function doCurl($post = null) {
    $api_auth = array('password' => $this->api_secret);
    $data = array_merge($api_auth, $post);
    // Inicializamos CURL con las opciones necesarias
    $ch = curl_init($this->api_url);
    curl_setopt($ch, CURLOPT_HEADER, false);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    // Insertamos el contenido POST
    curl_setopt($ch, CURLOPT_POSTFIELDS, $data);
 
   // Ejecutamos la conexión
   $response = curl_exec($ch);
   curl_close($ch);
   if($response == '') {
    $response = 'blahh}';
   }
   $ret = json_decode($response, true);
   if(json_last_error() === JSON_ERROR_NONE && isset($ret['status']) && $ret['status'] == 'ok' ) {
     $this->api_status = 'ok';
     return $ret;
   } else {
     if (! (json_last_error() === JSON_ERROR_NONE) ) {
       $this->api_status = 'error';
     }
     return false;
   }
  }
}
 
?>
