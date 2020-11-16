#Project ID: rtp-webapp
#By: Manuel Sudermann

#Google Cloud Platform - Standard App Engine - WebApp using Python27 and ndb datastore

#Documentation
 #for storing: https://download.huihoo.com/google/gdgdevkit/DVD1/developers.google.com/appengine/docs/python/datastore.html
 #for query: https://cloud.google.com/appengine/docs/standard/python/datastore/queryclass
 #for delete: https://www.programcreek.com/python/example/75158/google.appengine.ext.db.delete
 #for edits: https://www.oreilly.com/library/view/programming-google-app/9780596157517/ch04.html



############################## Imports + Init Start ####################################
import logging
from google.appengine.ext import ndb
from flask import Flask, render_template, request, redirect

app = Flask(__name__)
############################## Imports + Init Stop #####################################

############################## App Engine Functions Start ##############################
#Database Model
class Person(ndb.Model): 
    name = ndb.StringProperty(required=True)

#__NDB functions to store, retrieve, edit, and delete__
#start ADD
def add_person(person_name):
    person = Person(name=person_name)
    person.put()
#stop ADD

#start GET
def get_person_by_name(person_name):
    query = Person.query(Person.name == person_name)
    person = query.fetch()
    return person

def get_all_persons():
    all_persons = Person.query().fetch()
    return all_persons

def get_person_by_index(index):
    all_persons = get_all_persons()
    count = 0
    for person in all_persons:
        if count == index:
            return person
        count += 1
#stop GET

#start EDIT
def edit_person_name_at_index(index, new_name):
    all_persons = get_all_persons()
    count = 0
    for person in all_persons:
        if count == index:
            person.name = new_name
        count += 1
#stop EDIT

#start DELETE
def delete_person_by_name(person_name):
    person = get_person_by_name(person_name)
    person.key.delete()

def delete_person_by_index(index):
    all_persons = get_all_persons()
    count = 0
    for person in all_persons:
        if count == index:
            person.key.delete()
        count += 1
#stop DELETE

############################## App Engine Functions Stop ###############################

############################## Flask Code Start ########################################

#app starts here and displays all entries within database
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',persons=get_all_persons())

#if fields are filled out and add button is pushed
@app.route("/handle_add", methods=['POST'])
def handle_add():
    person_name = request.form['person_name']
    add_person(person_name) 
    return redirect("/", code=302)

@app.route("/handle_delete_or_edit", methods=['POST']) #reacts to actions within html form
def handle_delete_or_edit():
    button = request.form['modify_button'] #grabs value from button
    button_index = int(button[-1:]) #takes last char of button value to find index
    action = button[0: len(button)-1: 1] #removes last char (index) from string to compare

    if(action == "delete_entry"):
        delete_person_by_index(button_index) 
    if(action == "edit_entry"):
        new_person_name = request.form['new_person_name'] #grab user input for new name
        edit_person_name_at_index(button_index, new_person_name) 
    return redirect("/", code=302)

#Handle errors
@app.errorhandler(500)
def server_error(e):
    #Log the error and stacktrace
    logging.exception('An error occurred during a request. Error: ' + e)
    return 'An internal error occurred.', 500

############################## Flask Code Stop #########################################