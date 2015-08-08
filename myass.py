from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.debug = True
    app.run()

from pymongo import MongoClient

client = MongoClient()
db = client.test

from datetime import datetime
result = db.questions.delete_many({})
result = db.questions.insert_one(
    {
    "OP": "41704620",
    "Question": "41704620",

    }
)
cursor = db.restaurants.find()
for document in cursor:
    print(document)