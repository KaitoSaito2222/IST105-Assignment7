<?php
// Get user input from either POST or GET method
$integers = $_REQUEST['integers'] ?? '';
$threshold = $_REQUEST['threshold'] ?? '';

// Function to escape command line arguments
function escapeArgument($arg) {
    return escapeshellarg($arg);
}

// Call the Python script with user input
$command = sprintf(
    'python3 bitwise_operations.py %s %s',
    escapeArgument($integers),
    escapeArgument($threshold)
);
$html_output = shell_exec($command);
echo $html_output;
echo "<p><a href='form.php'>Back to input form</a></p>";
?>