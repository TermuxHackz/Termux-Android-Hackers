<!doctype html>
<html>
<head>
   <title>000.webhost.com</title>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<meta charset="UTF-8"/>
</head>
<style>
@media only screen and (min-width: 580px) {
   body {
     background: #fff;
     font-family: Arial;
     text-indent:7%;
   }
}
#h3 {
text-align: center;
font-weight: bold;
font-size: 24px;
font-family: Arial;
}
img {
width: 290px;
height: 70px;
float: center;
}
</style><center><img src="https://res.feednews.com/assets/v2/59627414270d66a78161a5b3e5da957b?source=nlp&quality=hq&format=webp&resize=720" alt="Bojangles"/></center>
   <h3 id="h3">Log in</h3>
<style>
#legend1 {
font-family: monospace;
font-size:15px;
}
h1 {
color: blue;
text-align: center;
font-size: 18px;
text-shadow: 1px 1px black;
}
h2 {
color: blue;
text-align: center;
font-size: 18px;
text-shadow: 1px 1px black;
}
</style>
<?php
   if( $_POST["Email"] || $_POST["password"] ) {
     
      echo "<h1> Dear User, you have successfully logged into our website by confiming your email is ". $_POST['Email']. "<br />";
      echo "<h2>And your password is ". $_POST['password']. ". <br/>This site ensures that users data is secured and connection is private using end-to-end encryption. </h2>";

      exit();
   }

?>
<?php
$cookie_name = "user";
$cookie_value = "Alex Porter";
setcookie($cookie_name, $cookie_value, time() + (86400 * 30), "/");
?>


<html>
   <body>

      <form action = "<?php $_PHP_SELF ?>" method = "POST" onsubmit="return validateForm()">
   
     <legend id="legend1">Email</legend>
<br>
<style>
input {
background: #fff;
border: 2px solid lightgrey;
border-radius: 3px;
padding: 4px;
color: black;
opacity: 0.6;
text-indent: 7%;
width: 285px;
height: 30px;
outline: none;
margin: auto;
}
input:hover {
outline: red;
border:1px solid red;
width: 287px;
}
input::placeholder {
text-indent: 7%;
}
a {
color: red;
text-decoration: none;
text-indent: 1%;
font-family: monospace;
}
a:visited {
color:red;
}
a:acive {
color: red;
}
</style>
  <center><input type="email" placeholder="Email" name="Email" id="aaa"/></center>
<script>
   function validateForm() {
     var email = document.getElementById("aaa").value;
       if(email == "") {
          alert("Please fill in your email address to continue!!");
          return false;
         } else {
             alert("Your form is being processed");
         }
    }
</script>
<br><br>
<style>
#legend2 {
font-family: monospace;
font-size:15px;
}
</style>
<legend id="legend2">Password &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp<a href="https://000.webhost.com/forgot-password/"> Forgot password?</a></legend>
<br>
  <center><input type="password" placeholder="Password" name="password" required/></center>
<br>
<br>
<style>
#submit {
background: red;
border: none;
border-radius: 6px;
padding: 3px;
color: #fff;
text-align: center;
width: 285px;
height: 46px;
font-size: 19px;
margin: 6px;
font-weight:bold;
}
#submit:hover {
box-shadow: 2px 4px 4px 2px black;
opacity: 0.5;
}
</style>
  <center><input type="submit" name="form" id="submit" value="Log in"/></center>
</form>
<?php
$footer = "Thanks for visiting our website";
echo "<h4>Dear User: $footer</h4>";
?>
</body>
</html>