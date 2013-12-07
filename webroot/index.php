<?php
  // 
  // Emit headers before any other content 
  // 
  cache_control("public,max-age=10");
  expires( to_gmt( time() + 10 ) );
?>
<html>
  <head>
  </head>
  <body>  
    <?
     print 'Hello world! Time is: ' . to_gmt();
    ?> 
  </body>
</html>

<?php
  function to_gmt( $now = null ) {
    return gmdate( 'D, d M Y H:i:s',  ( $now == null ) ? time() : $now );
  }
  
  function last( $gmt ) {
    header("Last Modified: $gmt");
  }

  function expires( $gmt ) {
    header("Expires: $gmt");
  }

  function cache_control( $options ) {
    header("Cache-Control: $options");
  }
?>