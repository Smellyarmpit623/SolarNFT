from flask import Flask, render_template  # import flask
app = Flask(__name__)             # create an application instance called app


@app.route("/")
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/BuyNFTs')
def BuyNFTs():
    return render_template('BuyNFTs.html')

if __name__ == "__main__":
    host='192.168.0.198'
    port=8080
    app.run(host,port,debug=True)