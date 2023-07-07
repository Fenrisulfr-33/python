from pymongo import MongoClient
from dotenv import load_dotenv, find_dotenv
import os
import pprint
from mongoFunctions import *
load_dotenv(find_dotenv())

# Created string connection env variables
user_name = os.environ.get('MONGODB_UN')
password = os.environ.get('MONGODB_PWD')

# Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
client = MongoClient(f"mongodb+srv://{user_name}:{password}@cluster0.spj8q.mongodb.net/test")

# Create the database for our example (we will use the same database throughout the tutorial
dbs = client.list_database_names()
# print(dbs)

pokemondb = client.pokemon
collections = pokemondb.list_collection_names()
# print(collections)

# Imported from database functions
insert_test_doc(pokemondb)

# If the database doesnt exist in mongodb then it will create a new database with that name
test = client.test
# Same thing, if the collection doesn't exist and you declare it, mongodb will create a new collection
test_collection = test.test_collection

# Adds documnets to collections
create_documnets(test_collection)