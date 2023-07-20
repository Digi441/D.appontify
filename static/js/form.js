var database = firebase.database('https://dappontify-default-rtdb.firebaseio.com/');
var usersRef = database.ref("users");

// Handle form submission
var form = document.getElementById("registrationForm");
form.addEventListener("submit", function(event) {
  event.preventDefault();

  // Retrieve form input values
  var name = document.getElementById("name").value;
  var email = document.getElementById("email").value;
  var phnno = document.getElementById("phn").value;
  var password = document.getElementById("password").value;

  // Create user object
  var newUser = {
    name: name,
    email: email,
    password: password,
    phnno:phn
  };

  // Save user data to Firebase Realtime Database
  usersRef.push(newUser)
    .then(function() {
      console.log("User registered successfully!");
      // Add any desired success handling here
    })
    .catch(function(error) {
      console.error("Error registering user:", error);
      // Add error handling here
    });
});
