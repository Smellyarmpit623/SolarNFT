from flask import Flask, render_template  # import flask
app = Flask(__name__)             # create an application instance called app


@app.route("/")
@app.route('/index')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    host='127.0.0.1'
    port=8080
    app.run(host,port,debug=True)