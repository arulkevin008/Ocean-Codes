Students=[
{"name":"Alice","Scores":[95,88,92]},
{"name":"Bob","Scores":[72,65,70]}]
for Data in Students:
    Students_name=Data["name"]
    Students_score=Data["Scores"]
    Sum=0
    for i in Students_score:
        Sum+=i
    avg=Sum/len(Students_score)
    if (90<avg<=100):
        rank = "Great"
    elif (70<avg<= 90):
        rank = "Good"
    elif (40<avg<=70):
        rank = "Not Bad"
    else:
        rank = "Fail"
    print(Students_name,int(avg),rank)