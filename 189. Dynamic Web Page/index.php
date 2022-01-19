<?php
$i = rand(0, 99999999);
if($i % 1332 == 0){
  echo ("Random value is " . $i);
} else {
  while($i % 1332 != 0) {
    $i = (rand(0, 99999999));
    if($i % 1332 == 0){
      echo ("Random value is " . $i);
    };
  };
};
?>