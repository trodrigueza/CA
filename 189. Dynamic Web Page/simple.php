<!DOCTYPE html>
<html>
  <head>
    <title>Embed PHP in a .html File</title>
  </head>
  <body>
    <h1>
        <?php
        $i = 3;
        while($i % 1600 != 0) {
            $i = (rand());
            if($i % 1600 == 0){
                echo ("Random value is " . $i);
            };
        };
        ?>
    </h1>
  </body>
</html>
