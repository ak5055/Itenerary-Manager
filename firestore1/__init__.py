from google.cloud import firestore

# The `project` parameter is optional and represents which project the client
# will act on behalf of. If not supplied, the client falls back to the default
# project inferred from the environment.
db = None
def get_instance():
    global db
    if db is None:
        db = firestore.Client(database= "cloud-nosql")
        return db
    return db

def add_data_db(db):
    doc_ref = db.collection("users").document("Samhi").collection("fuck you").document("HI")
    doc_ref.set(***REMOVED***"first": "Ada", "last": "Lovelace", "born": 1815***REMOVED***)
    doc_ref = db.collection("users").document("Samhi").collection("fuck you").document("HI2")
    doc_ref.set(***REMOVED***"first": "Alan", "middle": "Mathison", "last": "Turing", "born": 1912***REMOVED***)

def read_data_db(db):
    users_ref = db.collection("users")
    docs = users_ref.stream()
    data = []
    for doc in docs:
        data.append(f"***REMOVED***doc.id***REMOVED*** => ***REMOVED***doc.to_dict()***REMOVED***")
    return data

def check_if_exists(db, userid: str, itenaryid: str = None) -> bool:
    '''
     Check if userid and itenary id exists in the firestore1 database
    :param db: nosql database object
    :param userid: The user id
    :param itenaryid: The itenary id
    :return: True or False, depending on the particular combination of userid and itenaryid exists in db or not
    '''
    user_doc = db.collection("users").document(userid)
    if user_doc.get().to_dict() is None:
        return False

    if itenaryid is None:
        return True

    itenary_doc = user_doc.collection('itenaries').document(itenaryid)
    if itenary_doc.get().to_dict() is None:
        return False

    return True

def delete_collection(db, col):
    if col is None:
        return
    for doc in list(col.stream()):
        doc_obj = col.document(doc.id)
        for c in doc_obj.collections():
            delete_collection(db, c)
        col.document(doc.id).delete()



