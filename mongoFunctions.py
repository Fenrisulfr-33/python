# Helper functions

# Insert a document
def insert_test_doc(database):
    collection = database.tems
    tem_documnet = {
        'name': 'Mimit',
        'type': 'Digital'
    }
    inserted_id = collection.insert_one(tem_documnet).inserted_id
    print(inserted_id)

# Insert many Documnets into a Collection
def create_documnets(collection):
    first_names = ['Tim', 'Sarah', 'Jennifer', 'Jose', 'Brad', 'Allen']
    last_names = ['Rusica', 'Smith', 'Bart', 'Cater', 'Pit', 'Geral']
    ages = [22, 40, 23, 19, 34, 67]

    docs = [] # We would use this to insert an entire array of documents

    for first_name, last_name, age in zip(first_names, last_names, ages):
        doc = {"first_name": first_name, 'last_name': last_name, 'age': age}
        # collection.insert_one(doc) # This is how you could insert one at a time
        docs.append(doc) # This is appending to an array to insert the entire array

    collection.insert_many(docs)