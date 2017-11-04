<?php
$first = $_REQUEST['first'];
$last = $_REQUEST['last'];
$email = $_REQUEST['email'];
$data = array($first, $last, $email);
    
    $fp = fopen('names.csv', 'a');
    fputcsv($fp, $data);
    print("Data written successfully.");
    fclose($fp);


?>