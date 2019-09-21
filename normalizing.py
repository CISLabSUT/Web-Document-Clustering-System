import nltk, re, pprint
from hazm import *
import sys, glob, os
from imp import reload
import nltk
reload(sys)


class rempunct:
    def __init__(self):
        sw = open('newEditedSwords.txt', 'r', encoding="utf-8").read()
        self.swords = sw.split(sep=' ')
        print(len(self.swords), "stopwords present!")

    def allfiles(self, foldername):
        owd = os.getcwd()
        fld = foldername + "/"
        os.chdir(fld)
        arr = []
        for file in glob.glob("*.txt"):
            arr.append(file)
        os.chdir(owd)
        print(self.swords)
        print("All filenames extracted!")
        return arr

    def rem_stop(self, fname, ofilename):
        rawlines = open(fname, encoding="utf-8").readlines()
        lenl = len(rawlines)
        of = open(ofilename, 'w', encoding="utf-8")
        for r in range(lenl):
            linex = Normalizer().normalize(rawlines[r])
            linex2 = "".join([c for c in linex if (c not in (
                '!', '.', '/',  ':', ',', '?', "؟", ';', '،', '؛', ',', 'ً', 'ٌ', 'ٍ', 'ُ', 'ُ', 'ِ', 'ّ', '»', '«', '``', '&', '-', '"', '(', ')', '[', ']', '۰', '۱', '۲', '۳', '۴', '۵', '۶', '۷', '۸', '۹', '0', '1', '2', '3', '4', '5', '6',
                '7', '8', '9'))])
            linex2 = linex2.replace('\u200c', " ")
            linex3 = linex2.split(sep=" ")
            # prog = (r + 1) / len(rawlines)
            for s in range(len(linex3)):
                noword = linex3[s]
                if noword not in self.swords:
                    of.write(noword)
                    of.write(" ")
            of.write("\n")

    def drawProgressBar(self, percent, barLen=50):
        sys.stdout.write("\r")
        progress = ""
        for i in range(barLen):
            if i < int(barLen * percent):
                progress += "="
            else:
                progress += " "
        sys.stdout.write("[ %s ] %.2f%%" % (progress, percent * 100))
        sys.stdout.flush()

    def allremove(self, numOne, numTwo):
        array1 = self.allfiles('newSources')
        # lenv = len(array1)
        owd = os.getcwd()
        fld = "stops_removed/"
        os.chdir(fld)
        # arr = []
        if glob.glob('*.txt'):
            for file in glob.glob("*.txt"):
                os.remove(file)
        os.chdir(owd)

        for k in range(numOne, ((numTwo) + 1)):
            in1 = 'newSources/{}.txt'.format(k)
            out1 = 'stops_removed/{}.txt'.format(k)  # foldername of the output folder, create the folder first, if does not exist
            self.rem_stop(in1, out1)


if __name__ == '__main__':
    rp = rempunct()
    rp.allremove(500, 510)
