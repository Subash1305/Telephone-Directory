import pymongo

client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')

mydb = client["Telephone_Directory"]

db = mydb.new

directory = {
    "Name"          : "Subash",
    "PhoneNumber"   : "9876543210",
    "Place"         : "Chennai"  
}

print(db.insert_one(directory))

directory = [
   {
    "Name"         : "Kishore",
    "PhoneNumber" : "9876543210",
    "Place"       : "Chennai"
   },
   {
    "Name"        : "Hari",
    "PhoneNumber" : "7894561230",
    "Place"       : "Kanchipuram" 
   },
   {
    "Name"        : "Naveen",
    "PhoneNumber" : "7896541230",
    "Place"       : "Delhi"
   }
]

print(db.insert_many(directory))

print(db.db.find())

print(db.delete_one({"Name" : "Subash"}))

print(db.update_one(
    {"Name" : "Subash"},
    {
        "$set" : {"PhoneNumber" : 8976541320, "Place" : "Mumbai"}
    }
))