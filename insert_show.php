<html>
	<head>
		<title>注册页面</title>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	</head>

	<body>
		<h1>新用户注册</h1>
		<hr>

		<form method="post" action="">
			<table>
				<tr>
					<td>请输入用户名：<input type="text" name="username"></td>
				</tr>
	
				<tr>
					<td>请输入first_id：    <input type="text" name="first_id"></td>
				</tr>



				<tr>
					<td><input type="submit" value="提交">
					
				</tr>
			</table>
		</form>
	</body>
</html>

<?php
$servername = "127.0.0.1";
$username = "root";
$password = "root";
$dbname = "dvwa";
 
// 创建连接
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("连接失败: " . $conn->connect_error);
} 
$username = $_POST['username'];
$first_id = $_POST['first_id'];
$sql = "insert into users (user_id,first_name,last_name,user,password,avatar,last_login,failed_login) values ('$first_id','$username','jumbo','jumbo','jumbo','jumbo','2016-05-06','0')";
$result = $conn->query($sql);
?>
<html>
<head>
  <title>dropdown from mysql</title>
</head>
<body>
  <h1>用户名如下</h1>
<select>
<option value=0>--请选择--</option>
<?php
$sql2 = "SELECT * from users";
$result2 = $conn->query($sql2);
if ($result2->num_rows > 0) {
    while($row2 = $result2->fetch_assoc()) {
        echo "<option value='$row2[first_name]'>$row2[first_name]</option>";;
    }
} else {
    echo "0 结果";
}
$conn->close();
?>
</select>
  </form>
</body>
</html>
