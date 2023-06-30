<?php

// Function to sanitize input data
function sanitize_input($data) {
  $data = trim($data);
  $data = stripslashes($data);
  $data = htmlspecialchars($data);
  return $data;
}

// Check if the form was submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
  // Replace 'your-email@example.com' with your actual receiving email address
  $receiving_email_address = 'your-email@example.com';

  // Sanitize form data
  $name = sanitize_input($_POST['name']);
  $email = sanitize_input($_POST['email']);
  $subject = sanitize_input($_POST['subject']);
  $message = sanitize_input($_POST['message']);

  // Create the email content
  $email_content = "From: $name\n";
  $email_content .= "Email: $email\n";
  $email_content .= "Subject: $subject\n";
  $email_content .= "Message:\n$message\n";

  // Set up email headers
  $headers = "From: $name <$email>\r\n";
  $headers .= "Reply-To: $email\r\n";

  // Send the email
  if (mail($receiving_email_address, $subject, $email_content, $headers)) {
    // If the email is sent successfully, return a success message
    echo json_encode(array('status' => 'success', 'message' => 'Message sent successfully!'));
  } else {
    // If there is an error sending the email, return an error message
    echo json_encode(array('status' => 'error', 'message' => 'Error sending the message. Please try again later.'));
  }
} else {
  // If the form was not submitted, return an error message
  echo json_encode(array('status' => 'error', 'message' => 'Form submission failed. Please try again later.'));
}
