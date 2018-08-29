from datetime import datetime

from flask import (
    make_response,
    abort
)


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

# Data to serve with our API
PEOPLE = {
    "Karan": {
        "fname": "Karan",
        "lname": "Kamatgi",
        "timestamp": get_timestamp()
    },
    "Ramya": {
        "fname": "Ramyashree",
        "lname": "DG",
        "timestamp": get_timestamp()
    },
    "Raghotam": {
        "fname": "Raghotam",
        "lname": "Talwai",
        "timestamp": get_timestamp()
    }
}

# Create a handler for our GET API
def read():
    
    #This function responds to a request for /api/people
    #with the complete lists of people in our initial data structure.

    
    
    # Create the list of people from our data
    return [PEOPLE[key] for key in sorted(PEOPLE.keys())]

def create(person):

    fname=person.get('fname', None)
    lname=person.get('lname', None)

    #check if the person already exists

    if lname not in PEOPLE and lname is not None:
        PEOPLE[lname] = {
        'lname': lname,
        'fname': fname,
        'timestamp': get_timestamp()
        }

        return make_response('{lname} successfully created'.format(lname=lname),201)
    
    else:
        #person with same lname already exists
        abort(406, 'person with {lname} already exists'.format(lname=lname))