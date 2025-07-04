from pymongo import MongoClient
from bson import ObjectId
mongoURL= MongoClient("mongodb://localhost:27017/")

DB=mongoURL["MyProject"]

Collection=DB["UserData"]

Information={
    "name":"Kevin",
    "roll no":23456,
    "class":"B2",
    "record":"Good"
}

def userdetail(data):
    user=Collection.insert_one(data)
    print("Insert One Data Created")

#userdetail(Information)

Information2=[
{
    "name":"Kevin",
    "roll no":23456,
    "class":"B2",
    "record":"Good"
},

{
    "name":"Naren",
    "roll no":1760,
    "class":"A3",
    "record":"Excellent"
},

{
    "name":"Bhuvan",
    "roll no":3572,
    "class":"B1",
    "record":"Bad"
}

]

def data(i):
    data2=Collection.insert_many(i)
    print("Insert many Data Created")

#data(Information2)

def getbyId(Id):
    try:
        getdata=Collection.find({"_id":ObjectId(Id)})
        if getdata:
            for i in getdata:
                print(i)
        else:
            print("User not found")
    except Exception as e:
        print("Error:",e)

#getbyId('685e2ac2ed2a1a70aaa8976b')

def getall(Id):
        getdata=Collection.find({})
        for i in getdata:
            print(i)

#getall('685e2ac2ed2a1a70aaa8976b')
newValue = {
    "name":"Guru dev"
}

def updateid(update):
    try:
        updatedata=Collection.find_one_and_update({"_id":ObjectId(update)},{"$set":newValue})
        if updatedata:
            print("User data updated successfully")
        else:
            print("User not found")
    except Exception as e:
        print("Error:",e)

#updateid('685e2da396b4a8e62572e2a5')

def deleteid(delete):
    try:
        delete=Collection.find_one_and_delete({"_id":ObjectId(delete)})
        if delete:
            print("User deleted")
        else:
            print("user not found")
    except Exception as e:
        print("Error",e)

#deleteid('685e2da396b4a8e62572e2a5')



