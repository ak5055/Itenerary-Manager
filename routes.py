import uuid

from flask import Blueprint, request
from firestore1 import get_instance, check_if_exists, delete_collection

# from Amadeus.FlightsService.search import FlightsService
# from ExchangeRates.rates import ExchangeRatesService

routes = Blueprint('routes', __name__)


@routes.get('/')
def health():
    return ***REMOVED***
        "health": "up and running"
    ***REMOVED***



@routes.get('/getItenaries/<userid>')
def getItenaries(userid):
    '''
    Gets all the user itenaries information (flights, car rentals, hotels).
    :param userid: User id
    :return: dict of all the necessary information about flights, car rentals and hotels.
    '''
    db = get_instance()
    itenary_info = ***REMOVED******REMOVED***
    itenary_docs = db.collection("users").document(userid).collection("itenaries")

    if not check_if_exists(db, userid):
        return ***REMOVED***
            "error": f"User with id ***REMOVED***userid***REMOVED*** doesn't exist"
        ***REMOVED***

    for doc in itenary_docs.stream():
        it_id = doc.id
        itenary_info[it_id] = doc.to_dict()
        itenary_info[it_id]["flights"] = ***REMOVED******REMOVED***
        itenary_info[it_id]["hotels"] = ***REMOVED******REMOVED***
        itenary_info[it_id]["car_rentals"] = ***REMOVED******REMOVED***
        itenary_info[it_id]["tourism"] = ***REMOVED******REMOVED***
        doc_obj = itenary_docs.document(doc.id)
        flights = doc_obj.collection("flights")
        car_rentals = doc_obj.collection("car_rentals")
        hotels = doc_obj.collection("hotels")
        tourism = doc_obj.collection("tourism")
        for flight_doc in flights.stream():
            itenary_info[it_id]["flights"][flight_doc.id] = flight_doc.to_dict()
        for car_rentals_doc in car_rentals.stream():
            itenary_info[it_id]["car_rentals"][car_rentals_doc.id] = car_rentals_doc.to_dict()
        for hotels_doc in hotels.stream():
            itenary_info[it_id]["flights"][hotels_doc.id] = hotels_doc.to_dict()
        for tourism_doc in tourism.stream():
            itenary_info[it_id]["tourism"][tourism_doc.id] = tourism_doc.to_dict()

    return itenary_info

@routes.put('/updateItenary')
def update_itenary():
    input = request.json
    db = get_instance()
    userid = input["userid"]
    itnerary_id = input["itenaryid"]

    if not check_if_exists(db, userid, itnerary_id):
        return ***REMOVED***
            "error": f"User with userid as ***REMOVED***userid***REMOVED*** and itenary id as ***REMOVED***itnerary_id***REMOVED*** doesn't exist in the database"
        ***REMOVED***

    update_info = ***REMOVED***
        "flights": input.get("flights", []),
        "hotels": input.get("hotels", []),
        "car_rentals": input.get("car_rentals", []),
        "tourism": input.get("tourism", [])
    ***REMOVED***

    itenary_doc = db.collection("users").document(userid).collection("itenaries").document(itnerary_id)
    updated_itenary = ***REMOVED***
        "flights": [],
        "hotels": [],
        "car_rentals": [],
        "tourism": [],
        "itenaryid": itnerary_id,
        "userid": userid
    ***REMOVED***

    for update_key, update_val in update_info.items():
        if len(update_val) > 0:
            delete_collection(db, itenary_doc.collection(update_key))
            for val in update_val:
                unique_id = uuid.uuid4().hex
                itenary_doc.collection(update_key).document(unique_id).set(val)

        updated_itenary[update_key] = [doc.to_dict() for doc in itenary_doc.collection(update_key).stream()]

    return updated_itenary


@routes.post("/createItenary")
def create_itenary():
    input = request.json
    db = get_instance()
    userid = input["userid"]
    create_info = ***REMOVED***
        "flights": input.get("flights", []),
        "hotels": input.get("hotels", []),
        "car_rentals": input.get("car_rentals", []),
        "tourism": input.get("tourism", [])
    ***REMOVED***

    if not check_if_exists(db, userid):
        return ***REMOVED***
            "error": f"User with userid as ***REMOVED***userid***REMOVED*** doesn't exist in the database"
        ***REMOVED***

    itenary_id = uuid.uuid4().hex
    success_msg = ***REMOVED***
        "userid": userid,
        "itenaryid": itenary_id
    ***REMOVED***

    itenary_doc = db.collection("users").document(userid).collection("itenaries").document(itenary_id)
    for key, vals in create_info.items():
        for val in vals:
            unique_id = uuid.uuid4().hex
            itenary_doc.collection(key).document(unique_id).set(val)

    return success_msg

@routes.delete("/deleteItenary")
def delete_itenary():
    input = request.json
    db = get_instance()
    userid = input["userid"]
    itenary_id = input["itenaryid"]

    if not check_if_exists(db, userid, itenary_id):
        return ***REMOVED***
            "error": f"User with userid as ***REMOVED***userid***REMOVED*** and itenary id as ***REMOVED***itenary_id***REMOVED*** doesn't exist in the database"
        ***REMOVED***

    for c in db.collection("users").document(userid).collection("itenaries").document(itenary_id).collections():
        delete_collection(db, c)

    db.collection("users").document(userid).collection("itenaries").document(itenary_id).delete()

    return ***REMOVED***
        "message": "Delete is successful"
    ***REMOVED***