<?php

include "dbconnect.php";

$cfxres = mysqli_real_escape_string($con, $_GET['cfxres']);

if(!$apikey || !$cfxres) {die('cfx.re/join/4ar4k5, ex: cfx.php?key=puturkeyhere&cfxres=4ar4k5 ');}
	
$url = "https://servers-frontend.fivem.net/api/servers/single/$cfxres";
$json = file_get_contents($url);
$json_data = json_decode($json, true);

$backend = $json_data["Data"]["connectEndPoints"][0];
$players = $json_data["Data"]["clients"];
$owner = $json_data["Data"]["ownerProfile"];
$maxplayers = $json_data["Data"]["svMaxclients"];
$Queue = $json_data["vars"]["Queue"];
$servername = $json_data["Data"]["hostname"];

$marks = array("Backend"=>$backend, "Players"=>"[$players]$maxplayers", "Owner"=>$owner);

$make = str_replace("\/\/", "//",json_encode($marks));

echo str_replace("\/", "/", $make);


?>
