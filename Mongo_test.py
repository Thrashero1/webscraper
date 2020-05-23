from pymongo import MongoClient
import datetime
import pymongo

# you can access a data base in one of wto ways: using the default localhost:
from pymongo.errors import DuplicateKeyError

client = MongoClient()

'''or specifying the path and port:
client = MongoClient('mongodb://localhost:27017/)'''
 
# opens or creates the database
db = client.pytests

# you can create or access it this way if you have dashes or spaces in the name:
# db = client["py_tests"]

# this opens or creates a collection
users = db.users

'''# This will be an entry into the collection:
multiple_users = [{"username": "Jill", "Password": "My_Password_4", "favourite_number": 13,
                   "hobbies": ["reading", "cooking", "art", "gardening", "films"]},
                  {"username": "Hans", "Password": "My_Password_5", "favourite_number": 4,
                   "hobbies": ["reading", "cooking", "Pianio", "gardening", "walking"]},
                  {"username": "Rachel", "Password": "My_Password_6", "favourite_number": 1,
                   "hobbies": ["running", "art", "gardening", "films"]},
                  {"username": "Dawm", "Password": "My_Password_7", "favourite_number": 87,
                   "hobbies": ["Pottery", "Swimming"]}]

# we insert the entry while recording the _id (we use mongo db syntax)
user_id = users.insert_one(user1).inserted_id

print(user_id)

# insert many entries
# result = db.users.insert_many([multiple_users[i] for i in range(len(multiple_users))])

# or this way
result = db.users.insert_many(multiple_users)

print(result.inserted_ids)'''
# count the amount of documents in the collection users
print(db.users.count_documents({}))
print("dawn:", db.users.count_documents({"username": "Jill"}))

current_date = datetime.datetime.now()
print(current_date)

old_date = datetime.datetime(2017, 9, 18)

new_user = {"username": "David", "date": current_date}

try:
    new_one = db.users.insert_one(new_user)
    print(new_one.inserted_id)
except DuplicateKeyError:
    print("This is bad")
# gt= greater then, gte = greater then or equal, lt = less then, lte = less then or equal
print(db.users.count_documents({"date": {"$gte": old_date}}))
# checks is a field exists in a collection
print(db.users.count_documents({"hobbies": {"$exists": True}}))
# checks if the following field variable is not equal (ne) to a value
print(db.users.count_documents({"username": {"$ne": "David"}}))

# db.users.replace_one({"username": "red"}, {"username": "qwerty"})

# create an index for the inputs which improves speed when searching througha large amount of documents
# db.users.create_index([("username", pymongo.ASCENDING)], unique=True)
