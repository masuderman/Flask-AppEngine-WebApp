#Project ID: rtp-webapp
#By: Manuel Sudermann

#Google Cloud Platform - App Engine - WebApp using Python27 and db datastore

#Documentation
 #for storing: https://download.huihoo.com/google/gdgdevkit/DVD1/developers.google.com/appengine/docs/python/datastore.html
 #for query: https://cloud.google.com/appengine/docs/standard/python/datastore/queryclass
 #for delete: https://www.programcreek.com/python/example/75158/google.appengine.ext.db.delete
 #for edits: https://www.oreilly.com/library/view/programming-google-app/9780596157517/ch04.html

############################## Imports + Init Start ####################################
from google.appengine.ext import db
from flask import Flask, render_template, request, redirect

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

def edit_name_at_index(index, new_name):
    person_list = get_list(Person)
    count = 0
    for person in person_list:
        if count == index:
            person.name = new_name
        count += 1

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

def py_edit_name_at_index(index, new_name):
    count = 0
    person_list = persons
    for person in person_list:
        if count == index:
            person_list[count]  = {'name': new_name}
        count += 1

############################## Python Placeholder Functions Stop #######################

#start of Flask code

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',persons=persons)

@app.route("/handle_add", methods=['POST'])
def handle_add():
    person_name = request.form['person_name']
    add_person(person_name) #add py_ in front of method name to run python method
    return redirect("/", code=302)

@app.route("/handle_delete_or_edit", methods=['POST']) #reacts to actions within html form
def handle_delete_or_edit():
    button = request.form['modify_button'] #grabs value from button
    button_index = int(button[-1:]) #takes last char of button value to find index
    action = button[0: len(button)-1: 1] #removes last char (index) from string to compare

    if(action == "delete_entry"):
        delete_by_index(button_index) #add py_ in front of method name to run python method
    if(action == "edit_entry"):
        new_person_name = request.form['new_person_name'] #grab user input for new name
        edit_name_at_index(button_index, new_person_name) #add py_ in front of method name to run python method
    return redirect("/", code=302)
if __name__ == '__main__':
    app.run(debug=True)