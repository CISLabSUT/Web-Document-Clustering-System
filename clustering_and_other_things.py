import os, glob
import xlsxwriter
import zipfile
import operator
import collections
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans


class clusterigStuffs:

    def clustering(self, clusteringParam):
        myVictiorizer = TfidfVectorizer(use_idf=True, lowercase=False)
        owd = os.getcwd()
        fld = 'stops_removed/'
        os.chdir(fld)
        arr = []
        for file in glob.glob("*.txt"):
            with open(file, 'r', encoding='utf-8') as aFile:
                arr.append(aFile.read())
        os.chdir(owd)
        x = myVictiorizer.fit_transform(arr)

        km = KMeans(n_clusters=clusteringParam, precompute_distances=True)
        clustering = km.fit(x)
        return clustering, myVictiorizer

    def top_frequent_word_percluster(self, clustering, myVictiorizer, nFrequentWord):
        order_centroids = clustering.cluster_centers_.argsort()[:, ::-1]
        terms = myVictiorizer.get_feature_names()
        topFrequent = []
        for i in range(len(clustering.cluster_centers_)):
            tempArr = []
            for ind in order_centroids[i, :nFrequentWord]:
                tempArr.append(terms[ind])
            topFrequent.append(tempArr)
        return topFrequent

    def clustering_result(self, clustering):
        documentsNumber = list()
        result = list()
        wordOccurrencePerCluster = list()
        documentCountPerCluster = list()
        documentsID = list()
        MSE = clustering.inertia_
        owd = os.getcwd()
        fld = 'stops_removed/'
        os.chdir(fld)
        for file in glob.glob('*.txt'):
            documentsID.append(int(file[:-4]))
        os.chdir(owd)
        for i in range(len(clustering.cluster_centers_)):
            documentsNumber.append(list())
            result.append(list())
            wordOccurrencePerCluster.append(dict())
        for j in range(len(clustering.labels_)):
            documentsNumber[clustering.labels_[j]].append(documentsID[j])
        for k in range(len(documentsNumber)):
            documentCountPerCluster.append(len(documentsNumber[k]))
        owd = os.getcwd()
        fld = 'newSources/'
        os.chdir(fld)
        for i in range(len(documentsNumber)):
            for item in documentsNumber[i]:
                with open("{}.txt".format(item), 'r', encoding='utf-8') as aFile:
                    result[i].append(aFile.read() + "\n\n")
        os.chdir(owd)
        owd = os.getcwd()
        fld = 'results/'
        os.chdir(fld)
        if glob.glob('*.xlsx'):
            for file in glob.glob("*.xlsx"):
                os.remove(file)
        if glob.glob('*.zip'):
            for zips in glob.glob('*.zip'):
                os.remove(zips)
        for i in range(len(result)):
            workbook = xlsxwriter.Workbook('cluster_{}.xlsx'.format(i+1))
            worksheet = workbook.add_worksheet()
            for j in range(len(result[i])):
                worksheet.write_string("A{}".format(j+1), result[i][j])
            workbook.close()
            zip_file = zipfile.ZipFile("cluster_{}.zip".format(i+1), "w")
            zip_file.write('cluster_{}.xlsx'.format(i+1))
        os.chdir(owd)
        owd = os.getcwd()
        fld = 'stops_removed/'
        os.chdir(fld)
        wholeTexts = []
        for i in range(len(documentsNumber)):
            string = ""
            for j in range(len(documentsNumber[i])):
                with open("{}.txt".format(documentsNumber[i][j]), 'r', encoding='utf-8') as aFile:
                    string += aFile.read()
            wholeTexts.append(string)
        for i in range(len(wholeTexts)):
            temp = wholeTexts[i].split(" ")
            for j in range(len(temp)):
                wordOccurrencePerCluster[i][temp[j]] = wholeTexts[i].count(temp[j])
            sorted_w = sorted(wordOccurrencePerCluster[i].items(), key=operator.itemgetter(1), reverse=True)
            wordOccurrencePerCluster[i] = collections.OrderedDict(sorted_w)
        os.chdir(owd)
        return result, documentCountPerCluster, wordOccurrencePerCluster, MSE

    def main_progress(self, clustParam, nFrequentWord):
        clusters, vectorizer = clusterigStuffs().clustering(clustParam)
        topFrequent = clusterigStuffs().top_frequent_word_percluster(clusters, vectorizer, nFrequentWord)
        resultToShow , clustersMemberCount, wordFrequencyOnClusters, MSE = clusterigStuffs().clustering_result(clusters)
        return resultToShow, topFrequent, clustersMemberCount, wordFrequencyOnClusters, MSE
if __name__ == "__main__":
    clust, vector = clusterigStuffs().clustering(5)