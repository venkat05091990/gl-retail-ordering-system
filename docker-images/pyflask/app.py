from flask import Flask

app = Flask(__name__)

@app.route("/hello")
def index():
        return "Hello World!"

# main driver function
if __name__ == '__main__':
    app.run(host="0.0.0.0")
