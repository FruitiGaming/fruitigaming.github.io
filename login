








<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8" />
    <title>Login</title>
    <link rel="stylesheet" type="text/css" href="style.css" />

    <style>
body {
  background-color: whitesmoke;
  }
      
h1 {
  text-align: center;
  font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
}
      
form {
  background-color: white;
  border: 0px solid black;
  margin: auto;
  width: 50%;
  padding: 10px;

}
      
input[type="text"],input[type="password"] {
  width: 80%;
  padding: 12px 20px;
  margin: 8px 0;
  display: inline-block;
  border: 1px solid #ccc;
  border-radius: 1px;
  box-sizing: border-box;
}
      
input[type="button"] {
  background-color: limegreen;
  border: none;
  color: white;
  padding: 8px 16px;
  text-decoration: none;
  margin: 4px 2px;
  cursor: pointer;
  border-radius: 1px;
}
    </style>
    
  </head>
  <body>
    
    <form>
      <h1>Login</h1>
      <label for="username">Username:</label>
      <input type="text" id="username" name="username" /><br />
      <label for="password">Password:</label> <br>
      <input type="password" id="password" name="password" />
      
      <br/>
      
      <input type="button" value="Login" onclick="attemptLogin()" />

      <h4>Don't know the username and password? <a href="https://www.youtube.com/@FruitiGamingYT">Subscribe and watch a FruitiGaming video to find out.
      
      </form>

    <script>
      var myusername = 'fruitigamingviewer';
      var mypassword = 'sub2fruitigaming';
      function attemptLogin() {
        const username = document.getElementById("username").value;
        const password = document.getElementById("password").value;
  
        if (username === myusername && password === mypassword) {         
          window.location.href = "home.html";
    
  }     else {
          alert("Incorrect username or password.");
  }
}
    </script>
    
  </body>
</html/