from flask import Flask, render_template, request, send_file, redirect, url_for
conToDb = __import__('DataBase')
removeStops = __import__('normalizing')
clusteringThings = __import__('clustering_and_other_things')
nums = conToDb.connectToDB()
num = nums.main_progress()
app = Flask(__name__)


@app.route("/")
def template():

    return render_template('form.html', numOfDocs=num)


@app.route('/result', methods=["POST"])
def resulting():
    num1 = int(request.form['from'])
    num2 = int(request.form['to'])
    parameter = int(request.form['parameter'])
    nFrequent = int(request.form['n-frequent'])
    removeStops.rempunct().allremove(num1, num2)
    resultForShow, topFrequent, clustersMemberCount, wordFrequencyOnClusters, MSE = clusteringThings.clusterigStuffs().main_progress(parameter, nFrequent)
    return render_template('resultPage.html', finalResult=resultForShow, countDocument=clustersMemberCount, nFrequentWords=nFrequent,  topFrq=topFrequent, wordFrequency=wordFrequencyOnClusters, mse=MSE)


@app.route('/download', methods=["POST"])
def download_file():
    path = request.form['fileForDownload']
    return send_file(path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
