from flask import Flask
from data_ingestion import DataIngestion
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello World'

@app.route('/test')
def hello_world1():
   print('test')
   obj=DataIngestion()
   test_data=obj.initiate_data_ingestion()
   return 'Hello World - test1'

if __name__ == '__main__':
   app.run()
