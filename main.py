#Documentation for storing: https://download.huihoo.com/google/gdgdevkit/DVD1/developers.google.com/appengine/docs/python/datastore.html
#Documentation for query: https://cloud.google.com/appengine/docs/standard/python/datastore/queryclass
#Documentation for delete: https://www.programcreek.com/python/example/75158/google.appengine.ext.db.delete

from google.appengine.ext import db
from flask import Flask, render_template, request

app = Flask(__name__)

#Database Model
class Person(db.Model): #A simple model to familiarize myself with Datastore and Google App Engine
    name = db.StringProperty(required=True)

#start ADD entry 
def add_person(person_name): #pass string
    person = Person(name=person_name) 
    db.put(person) #puts entity with passed attributes
#stop ADD entry

#start GET entry
def get_list(person_model): #literally pass db.Model name "Person"
    q = db.Query(person_model)
    return q #q is like list and can iterate using for loop

def get_by_name(person_name):
    person = Person.get(person_name)
    return person
#stop GET entry

#start DELETE entry
def delete_by_name(person_name):
    person = get_by_name(person_name)
    Person.delete(person)
#stop DELETE entry

#start of Flask code
if __name__ == '__main__':
    app.run(debug=True)