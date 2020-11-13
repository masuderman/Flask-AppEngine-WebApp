#Documentation for storing: https://download.huihoo.com/google/gdgdevkit/DVD1/developers.google.com/appengine/docs/python/datastore.html
#Documentation for query: https://cloud.google.com/appengine/docs/standard/python/datastore/queryclass
#Documentation for delete: https://www.programcreek.com/python/example/75158/google.appengine.ext.db.delete

############################## Imports + Init Start ####################################
from google.appengine.ext import db
from flask import Flask, render_template, request

app = Flask(__name__)
############################## Imports + Init Stop #####################################

############################## App Engine Functions Start ##############################
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
def delete_by_index(index):
    person_list = get_list(Person)
    count = 0
    for person in person_list:
        if count == index:
            Person.delete(person)
        count += 1

def delete_by_name(person_name):
    person = get_by_name(person_name)
    Person.delete(person)
#stop DELETE entry
############################## App Engine Functions Stop ###############################

############################## Python Placeholder Functions Start ######################
persons = [{'name': 'Jack Bauer'},{'name': 'James Ford'},{'name': 'Charlie Pace'}]

def py_add_person(person_name):
    persons.append({'name': person_name})

def py_get_list(person_model):
    return persons

def py_get_by_name(person_name):
    count = 0
    for person in persons:
        if person.name == person_name:
            return persons[count]
        count += 1

def py_delete_by_index(index):
    person_list = persons
    count = 0
    for person in person_list:
        if count == index:
            person_list.pop(count)
        count += 1

def py_delete_by_name(person_name):
    count = 0
    for person in persons:
        if person.name == person_name:
            persons.pop(count)
        count += 1
############################## Python Placeholder Functions Stop #######################

#start of Flask code

@app.route("/")
def home():
    return "Hello World!"

if __name__ == '__main__':
    app.run(debug=True)