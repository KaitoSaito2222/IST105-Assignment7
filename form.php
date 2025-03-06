<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Input Form</title>
</head>
<body>
    <h2>Welcome to the Python application</h2>
    <form action="process.php" method="POST">
        <div>
            <label for="integers">Enter integers separated by commads:</label>
            <input type="text" id="integers" name="integers" required/>
        </div>
        <div>
            <label for="threshold">Threshold:</label>
            <input type="number" id="threshold" name="threshold" required/>
        </div>
        <button type="submit">Submit</button>
    </form>
</body>
</html>