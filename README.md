# LearningSystem
Zignasa'25 Project of BullDogs 
<!DOCTYPE html>
<html>
<head>
  <title>AI Learning System - Login</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background: #4a6cf7;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      margin: 0;
      color: #333;
    }
    .box {
      width: 340px;
      background: white;
      padding: 20px;
      border-radius: 12px;
      box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    h2 { text-align: center; }
    input, button {
      width: 100%;
      padding: 8px;
      margin-top: 10px;
      border-radius: 6px;
      border: 1px solid #ccc;
    }
    button {
      background: #4a6cf7;
      color: white;
      border: none;
      cursor: pointer;
    }
    .switch {
      text-align: center;
      font-size: 12px;
      margin-top: 10px;
    }
    .switch span {
      color: blue;
      cursor: pointer;
    }
  </style>
</head>
<body>

<div class="box">
  <h2 id="title">Login</h2>

  <form id="loginForm">
    <input id="loginEmail" type="email" placeholder="Email" required />
    <input id="loginPass" type="password" placeholder="Password" required />
    <button type="submit">Login</button>
  </form>

  <form id="registerForm" style="display:none;">
    <input id="regName" type="text" placeholder="Full Name" required />
    <input id="regEmail" type="email" placeholder="Email" required />
    <input id="regPass" type="password" placeholder="Password" required />
    <button type="submit">Register</button>
  </form>

  <div class="switch">
    <span id="switchText">Don't have an account? Register</span>
  </div>
</div>

<script>
  const loginForm = document.getElementById("loginForm");
  const registerForm = document.getElementById("registerForm");
  const switchText = document.getElementById("switchText");
  const title = document.getElementById("title");
  let isLogin = true;

  switchText.onclick = () => {
    isLogin = !isLogin;
    loginForm.style.display = isLogin ? "block" : "none";
    registerForm.style.display = isLogin ? "none" : "block";
    title.textContent = isLogin ? "Login" : "Register";
    switchText.textContent = isLogin
      ? "Don't have an account? Register"
      : "Have an account? Login";
  };

  // LOGIN API
  loginForm.onsubmit = async (e) => {
    e.preventDefault();
    const email = loginEmail.value;
    const password = loginPass.value;

    const res = await fetch("/api/login", {
      method: "POST",
      headers: {"Content-Type":"application/json"},
      body: JSON.stringify({email, password})
    });

    const data = await res.json();

    if(data.success){
      window.location.href = "dashboard.html";
    } else {
      alert("Login failed");
    }
  };

  // REGISTER API
  registerForm.onsubmit = async (e) => {
    e.preventDefault();
    const name = regName.value;
    const email = regEmail.value;
    const password = regPass.value;

    const res = await fetch("/api/register", {
      method: "POST",
      headers: {"Content-Type":"application/json"},
      body: JSON.stringify({name, email, password})
    });

    const data = await res.json();

    if(data.success){
      alert("Registered! Please login.");
      switchText.click();
    } else {
      alert("Register failed");
    }
  };
</script>

</body>
</html>
