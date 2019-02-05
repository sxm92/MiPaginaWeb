from flask import Flask
from flask import render_template

application = Flask(__name__)

@application.route("/")
def home():
    return render_template('index.html')

@application.route('/pmu/<datapmu>')
def PmuDatas(datapmu = 0):
    return render_template('web.html',dato=datapmu)

if __name__ == "__main__":
    application.run(debug = True)
