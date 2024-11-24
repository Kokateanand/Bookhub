document.getElementById('signup-form').addEventListener('submit', function(e) {
    // Prevent form submission by default
    e.preventDefault();
  
    const email = document.getElementById('email').value;
    const mobile = document.getElementById('mobile').value;
    const password = document.getElementById('password').value;
    const confirmPassword = document.getElementById('confirmpassword').value;
  
    // Email validation
    const emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
    if (!emailPattern.test(email)) {
      alert("Please enter a valid email address.");
      return;
    }
  
    // Mobile number validation (10 digits, no special characters)
    const mobilePattern = /^[0-9]{10}$/;
    if (!mobilePattern.test(mobile)) {
      alert("Please enter a valid 10-digit mobile number.");
      return;
    }
  
    // Confirm password match
    if (password !== confirmPassword) {
      alert("Passwords do not match. Please try again.");
      return;
    }
  
    // Strong password validation (only if passwords match)
    const passwordPattern = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;
    if (!passwordPattern.test(password)) {
      alert("Password must be at least 8 characters long, include at least one uppercase letter, one number, and one special character.");
      return;
    }
  
    // If all validations pass, submit the form
    alert("Form submitted successfully!");
  
    // Submit the form
    // e.preventDefault(); // Uncomment this line if you want to let the form submit automatically
  });