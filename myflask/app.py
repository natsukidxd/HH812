from flask import Flask, request, render_template
from dbhelper import validate_user

app = Flask(__name__)  # create a Flask instance

@app.route("/validate", methods=['POST'])
def validate() -> None:
    message: str = "Palyar pagka login"
    username: str = request.form['username']
    password: str = request.form["password"]
    if validate_user(username, password):
        message = "Sakto imong login"
    return message


@app.route("/login")
def login() -> None:
    return render_template("index.html")
    #return """
    #            <form method='POST' action='validate'>
    #                <input type='text' name='username' placeholder='username'/>
    #                <input type='password' name='password' placeholder='password'/>
    #                <input type='submit' value='LOGIN'/>
    #            </form>
    #        """


@app.route("/")
def index() -> None:
    return "Hello, Flask from Python"


def main() -> None:
    app.run(debug=True)


if __name__ == "__main__":
    main()
