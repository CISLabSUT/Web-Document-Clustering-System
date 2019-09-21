# Web-Document-Clustering-System

<h1>Intoroduction</h1>
Document clustering, as one of the methods of unsupervised machine learning, is widely used in various fields of natural language processing such as information retrieval, automated multi-text summary, etc.
In this project we implement k-means algorithm on documents. This program can cluster news is run by python so you need to setup it on your local device.

<h1>Download</h1>

If you have not installed yet, you can download it from this link:
https://www.python.org/downloads/

Since this program uses some of those libraries which are not in default installation, so you must have downloaded and installed. 
For your convenience, you should have installed "pip" feature of your workspace. For this purpose you can visit this link: https://www.makeuseof.com/tag/install-pip-for-python/

Now you can execute the command line of your device and with help of "pip install" to setup libraries requirements
You must have setup this library before runs this program:
<ul>
  <li>pymongo</li>
  <li>hazm</li>
  <li>xlsxwriter</li>
   <li>scikit-learn </li>
</ul>
It is better to know that this program works with MongoDb, so it must have installed on your device. The installation file is available form this link:
https://www.mongodb.com/download-center/community

<h1>Documentation</h1>
After that you can go to mongodb path direction and execute "mongod" file.Mongo's Server now waiting for communication with your program. The default port of it are 27017.
<br>
You should have opened Command Line in the folder where "main.py" exists (Where you have copied and extracted the project zip file).Now you can type "python main.py" and enter in the command line space.
Finally you must have opened the browser and insert 127.0.0.1:5000.
<br>
Now, the purpose program is running and you can use it
<br>
<B>"Be notice that:</B>
This program is linked into a default data base which name is News
if you want to use the another one, it enough that you change the name of "News" to desirable database name in "DataBase.py"
(docs = client." The name of your desirable database".Documents)
