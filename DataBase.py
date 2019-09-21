from pymongo import MongoClient

class connectToDB:
    def main_progress(self):
        client = MongoClient("localhost", 27017)
        docs = client.News.documents
        noffIds = dict()
        i = 0
        for doc in docs.find():
            noffIds[i] = (str(doc["_id"]))
            with open("newSources/{}.txt".format(i+1), "w", encoding="utf-8") as somethings:
                somethings.write(doc["description"])
            i = i + 1
        with open('ID-NumberPairs.txt', 'w') as aFile:
            for key in noffIds:
                aFile.write(str(key))
                aFile.write(' ')
                aFile.write(str(noffIds[key]))
                aFile.write("\n")
        return i
if __name__ == '__main__':
    conDB = connectToDB()
    conDB.main_progress()
