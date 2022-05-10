import json
username1=input("enter your user name...")
password=input("enter your password...")
with open("user1_details.json","r") as f:
    y=f.read()
    x=json.loads(y)
    for i,j in x.items():
        for k in j:
            if k["name"]==username1 and k["password"]==password:
                print("log in succesfully")
            else:
                print("invalid password")
                print("try again")



