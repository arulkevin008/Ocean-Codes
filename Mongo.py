from pymongo import MongoClient

URL=MongoClient("mongodb://localhost:27017/")

DB=URL["Students"]

Collection=DB["Records"]

Information=[
{

    "name":"Kevin",
    "email":"123@gmail.com",
    "address":"aaa",
    "mobile_no":34567878,
    "marks":[45,67,45,77,56]
},
{
    "name":"Arul",
    "email":"456@gmail.com",
    "address":"bbb",
    "mobile_no":46678774,
    "marks":[23,45,78,55,89]
},
{
    "name":"Bhuvan",
    "email":"678@gmail.com",
    "address":"ccc",
    "mobile_no":456788651,
    "marks":[56,78,80,67,34]
},
{
    "name":"Raj",
    "email":"890@gmail.com",
    "address":"ddd",
    "mobile_no":35456576,
    "marks":[34,45,56,67,78]
},
{
    "name":"Naren",
    "email":"012@gmail.com",
    "address":"eee",
    "mobile_no":34447885,
    "marks":[12,23,34,45,67]
},
{
    "name":"Kumar",
    "email":"234@gmail.com",
    "address":"fff",
    "mobile_no":45689533,
    "marks":[34,45,57,34,23]
},
{
    "name":"Mani",
    "email":"456@gmail.com",
    "address":"ggg",
    "mobile_no":345466772,
    "marks":[45,34,56,67,23]
},
{
    "name":"Maran",
    "email":"678@gmail.com",
    "address":"hhh",
    "mobile_no":45468432,
    "marks":[34,54,56,23,12]
},
{
    "name":"Ravichandran",
    "email":"awdd@gmail.com",
    "address":"jjj",
    "mobile_no":45575686,
    "marks":[34,45,21,23,45]
},
{
    "name":"Gurudev",
    "email":"rtr@gmail.com",
    "address":"kkk",
    "mobile_no":55768876,
    "marks":[45,23,23,12,23]
}
]

def userdata(scores):
    data=Collection.insert_many(scores)
    print("Data Created",len(Information))

# userdata(Information)

def total_marks():
    total=[{"$project":{"name":1,"total_marks":{"$sum":"$marks"}}},
           {"$sort":{"total_marks":-1}}]
    results=Collection.aggregate(total)
    rank=1
    for student in results:
        print(f"Rank {rank}:{student['name']} {student['total_marks']} marks")
        rank += 1
total_marks()