from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#Entidad User
class User(BaseModel):
    id: int
    name: str
    surname: str
    email: str
    age: int


users_list = [User(id=1, name= "Daniel", surname= "Lozano",email=  "dlozano@gmail.com",age= 23),
         User(id=2, name= "Leonardo",surname=  "Mosquera", email= "leonardo@gmail.com", age= 24),
         User(id=3, name= "Amy",surname= "Hernandez",email=  "amy@gmail.com", age=  25)]

@app.get("/usersjson/")
async def usersjson():
    return [{
        "name": "Daniel", "surname": "Lozano","email": "dlozano@gmail.com", "age": 23
    },
    {
        "name": "Leonardo", "surname": "Mosquera","email": "leonardo@gmail.com", "age": 24
    },
    {
        "name": "Amy", "surname": "Hernandez","email": "amy@gmail.com", "age": 25
    },
    ]

@app.get("/users")
async def users():
    return users_list


@app.get("/users/{id}")
async def user(id: int):
    return search_user(id)
    

@app.get("/userquery/")
async def user(id: int):
    return search_user(id)
    
def search_user(id:int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error ": "No se encuentra el usuario"}