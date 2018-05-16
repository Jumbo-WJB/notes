<?php
$servername = "127.0.0.1";
$username = "root";
$password = "root";
$dbname = "vuln";
$conn = mysqli_connect($servername, $username, $password, $dbname);
mysqli_query($conn, "set character set 'utf8'");
mysqli_query($conn,"set names 'utf8'");
// $conn->set_charset("utf8mb4");
?>
<html>
	<head>
		<title>漏洞查询</title>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />  
	</head>

	<body>
		<h1>漏洞录入</h1>
		<hr>

		<form method="post" action="">
			<table>
				<tr>
					<td>师傅名字：    <input type="text" name="username1"></td>
				</tr>
	
				<tr>
					<td>项目名称：    <input type="text" name="project1"></td>
				</tr>
				<tr>
					<td>高危数量：    <input type="text" name="high1"></td>
				</tr>
				<tr>
					<td>中危数量：    <input type="text" name="medium1"></td>
				</tr>
				<tr>
					<td>低危数量：    <input type="text" name="low1"></td>
				</tr>
				<tr>
					<td><input type="submit" value="提交">
					
				</tr>
			</table>
		</form>


<?php
$username1 = $_POST['username1'];
$project1 = $_POST['project1'];
$high1 = $_POST['high1'];
$medium1 = $_POST['medium1'];
$low1 = $_POST['low1'];
$sql = "insert into vuln (username,project,high,medium,low) values ('$username1','$project1','$high1','$medium1','$low1')";
$result =  mysqli_query($conn,$sql)
?>


  <h1>漏洞查询</h1>
  <hr>
  根据姓名查询
  <br>
<form action="" method="POST">
<select name="username">
<option value=0>--用户名--</option>
<?php
$sql2 = "SELECT * from vuln";
$result2 = mysqli_query($conn,$sql2);
if ($result2->num_rows > 0) {
    while($row2 = $result2->fetch_assoc()) {
        echo "<option value='$row2[username]'>$row2[username]</option>";
    }
}

?>


</select>
<input type="submit" value="查询">
</form>
<br>
根据项目查询
<br>
<form action="" method="POST">
<select name="project">
<option value=0>--项目名称--</option>
<?php
$result2 = mysqli_query($conn,$sql2);
if ($result2->num_rows > 0) {
    while($row2 = $result2->fetch_assoc()) {
        echo "<option value='$row2[project]'>$row2[project]</option>";
    }
}

?>


</select>
<input type="submit" value="查询">
</form>
<br>

<?php
$username = $_POST['username'];
$project = $_POST['project'];
$sql3 = "SELECT * from vuln where username = '$username' or project = '$project'";
$result3 = mysqli_query($conn,$sql3);
echo "<h1>漏洞提交信息</h1>";
echo "<hr>"; 
echo "<table width='700px' border='1px'>";  
echo "<tr>";
echo "<th>姓名</th><th>项目名称</th><th>高危数量</th><th>中危数量</th><th>低危数量</th>";
echo "</tr>";  
while($row3 = $result3->fetch_assoc()) {
    echo "<tr>"; 
    echo "<td>{$row3['username']}</td><td>{$row3['project']}</td><td>{$row3['high']}</td><td>{$row3['medium']}</td><td>{$row3['low']}</td>";
    echo "</tr>";  
}
echo "</table>";  
?>
</body>
</html>
//CREATE DATABASE vuln;
//use vuln;
//create table vuln(username varchar(20),project varchar(100), high int(100), medium int(100), low int(100));
//desc vuln;
//insert into users (username,project,high,medium,low) values ('姓名','客户','10','2','20');
//show create table vuln;
//alter table vuln convert to character set utf8;      
