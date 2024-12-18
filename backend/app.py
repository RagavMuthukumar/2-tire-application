from flask import Flask, request, render_template, make_response

app = Flask(__name__, template_folder="../frontend")

# Hardcoded users for demonstration purposes
USERS = {"ragav": "ragav", "devops": "12345"}

@app.route("/")
def home():
    # Render the login page
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    
    # Validate user credentials
    if username in USERS and USERS[username] == password:
        # HTML for success
        success_html = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Hello Boss</title>
            <style>
                body {{
                    font-family: 'Poppins', Arial, sans-serif;
                    background: linear-gradient(45deg, #914bdb, #0b8181, #829fd0);
                    color: white;
                    text-align: center;
                    margin: 0;
                    padding: 0;
                    height: 100vh;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                }}
                .container {{
                    background: rgba(255, 255, 255, 0.1);
                    backdrop-filter: blur(10px);
                    border-radius: 25px;
                    padding: 50px;
                    width: 50%;
                    box-shadow: 0 4px 30px rgba(0, 0, 0, 0.2);
                }}
                h2 {{
                    font-size: 2.5rem;
                    font-weight: bold;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <h2>🎉 Welcome {username}! Login Successful. 🎉</h2>
            </div>
        </body>
        </html>
        """
        return make_response(success_html)

    else:
        # HTML for failure
        failure_html = """
   <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login Failed</title>
    <style>
        body {
            font-family: 'Poppins', Arial, sans-serif;
            background: linear-gradient(45deg, #df7751, #e46b6b, #d08282); /* Beautiful gradient background */
            color: white; /* White text for contrast */
            text-align: center;
            margin: 0;
            padding: 0;
            height: 100vh; /* Full height */
            display: flex;
            justify-content: center;
            align-items: center;
            animation: backgroundAnimation 8s ease infinite;
        }

        .container {
            background: rgba(255, 255, 255, 0.1); /* Semi-transparent background for glassmorphism */
            backdrop-filter: blur(10px); /* Glassmorphism blur effect */
            border-radius: 25px;
            padding: 50px;
            width: 50%;
            box-shadow: 0 4px 30px rgba(0, 0, 0, 0.2);
            animation: fadeInUp 1s ease-out;
        }

        h1 {
            font-size: 2.5rem;
            margin-top: 20px;
            font-weight: bold;
            color: #ffffff;
            animation: bounceIn 1.5s ease;
        }

        @keyframes fadeInUp {
            0% {
                opacity: 0;
                transform: translateY(30px);
            }
            100% {
                opacity: 1;
                transform: translateY(0);
            }
        }

        @keyframes bounceIn {
            0% {
                transform: scale(0);
            }
            50% {
                transform: scale(1.1);
            }
            100% {
                transform: scale(1);
            }
        }

    </style>
</head>
<body>
    <div class="container">
        <h2>❌ Invalid Username or Password ❌</h2>
    </div>
</body>
</html>

        """
        return make_response(failure_html)

if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")
