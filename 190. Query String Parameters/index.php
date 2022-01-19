<?php
$name = $_GET["name"];
$year = $_GET["year"];
$month = $_GET["month"];
$day = $_GET["day"];

if(empty($name)) {
    $name = "Stranger";
};

$lucky = (strlen($name) * 14 + $month * 30 + $day * 11 + $year) % 31 + 1;

echo "Your lucky day is " . $lucky;
?>