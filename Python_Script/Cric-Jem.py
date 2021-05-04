#Data Flow A-->B-->C
#-----------------------------------A-----------------------------------
import json as js
from time import time , sleep
Stop =True
import requests as rq
KEY ="------------------------" # Get Your own KEY On http://cricapi.com
m = rq.get("https://cricapi.com/api/matches/"+KEY).content
data = js.loads(m)
count=0

for matches_data in data["matches"] :
    print("Match "+str(count+1)+"\n"
           +matches_data["team-1"]+" Vs "+ matches_data["team-1"]+"\n")
    count =count+1
id = ((data["matches"])[(int(input("Which One To See Score"))-1)])["unique_id"]

#-----------------------------------C-----------------------------------
#For Live Score 
def live_score(id):
   global Stop
   score_data1 =rq.get("http://cricapi.com/api/cricketScore/"+KEY+"?unique_id="+str(id)).content
   score_json = js.loads(score_data1)
   if score_json["matchStarted"]== True:
       lastScore =""
       score = score_json["stat"]
       if len(score)>2:
           if score!=lastScore:
               print(score)

       else :
           Stop = False
           print("Sorry :( Match Not Covered Due To Some Problem !!!")


   else:
       Stop = False
       print("Match Not Started Yet")

#-----------------------------------B-----------------------------------       
while Stop ==True:
    print(time()%60)
    sleep(5)
    print(60 - time() % 60)
    live_score(id)

