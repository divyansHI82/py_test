const loginForm = document.getElementById("login-form");

const emailInput = document.getElementById("email");

const passwordInput = document.getElementById("password");



loginForm.addEventListener("submit", (e) => {

    e.preventDefault(); // Prevent default form submission



    const email = emailInput.value;

    // In a real application, you would send these credentials to a server for validation.

    // For this simulated login, we just check if fields are not empty.

    if (email && passwordInput.value) {

        // Simulate successful login

        localStorage.setItem("isLoggedIn", "true");

        localStorage.setItem("loggedInUserEmail", email);

        alert("Login successful!");

        window.location.href = "index.html"; // Redirect to the main page

    } else {

        alert("Please enter both email and password.");

    }

});
