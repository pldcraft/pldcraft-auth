from flask import Flask

app = Flask(__name__)


@app.route("/hello")
def hello_world():
    return "Hello, world!"


# TODO: Configure whether we use the debug server
app.run(debug=True)
