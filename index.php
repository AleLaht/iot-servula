<!DOCTYPE html>
<html>
<head>
	<link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>

<table>
<tr>
<td>
Entry
</td>
<td>
Datetime
</td>
<td>
Movement
</td>
<td>
Kuva
</td>
</tr>
<?php
$servername = "*IPADDRESS*";
$username = "*USERNAME*";
$password = "*PASSWORD*";
$dbname = "*DBNAME*";

//Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
//Check connection
if ($conn->connect_error) {
	die("Connection failed: " . $conn->connect_error);
}

$sql = "SELECT entry, datetime, movement, kuvaurl FROM raw_data";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
	// output data of each row
	while($row = $result->fetch_assoc()) {
		echo
		"<tr><td>".
		"Entry: ". $row["entry"].
		"</td><td>".
		" - Datetime: ". $row["datetime"].
		"</td><td>".
		" - Movement: ". $row["movement"].
		"</td><td>".
		" - Kuva: ". "<a href='". $row["kuvaurl"]. "'>kuva</a>". 
		"<div class='box'><iframe width='470px' height='350px' src='". $row["kuvaurl"]. "'></iframe></div>".
		"</td></tr>";
	}
} else {
	echo "0 results";
}

$conn->close();
?>
</table>

<div class="tila">&nbsp;</div>

</body>
</html> 
