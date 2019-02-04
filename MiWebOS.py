from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/pmu/<datapmu>')
def PmuDatas(datapmu = 0):
    return render_template('web.html',dato=datapmu)

if __name__ == "__main__":
    app.run(debug = True)