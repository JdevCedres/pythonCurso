from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# uvicorn users:app --reload

# entidad user
class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int

  
users_list = [User (id=1,name="Jose", surname="Gonzalez", url="https://moure.dev", age=46),
        User (id=2,name="Manuel", surname="Gonzalez", url="https://manu.dev",age=5),
        User (id=3,name="Elena", surname="Gonzalez", url="https://elen.dev", age=4)]
        





@app.get("/usersjson")
async def usersjson():
    return [{"name":"Jose", "surname": "Gonzalez", "url":"https://moure.dev", "age":46},
            {"name":"Manuel", "surname": "Gonzalez", "url":"https://manu.dev", "age":5},
            {"name":"Elena", "surname": "Gonzalez", "url":"https://elen.dev", "age":4}]



@app.get("/users")
async def users():
    return users_list

# Por un Path
@app.get("/user/{id}")
async def user(id: int):
    return search_user(id)


# Por una Query
@app.get("/user/")
async def user(id: int):
   return search_user(id)


# Post (insertar datos)
@app.post("/user/", status_code=201)
async def user(user:User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=404, detail="El usuario ya existe")
       
    else:
        users_list.append(user)
        return user


@app.put("/user/")
async def user(user:User):
   
   found = False

   for index, saved_user in enumerate(users_list):
      if saved_user.id == user.id:
         users_list[index]= user
         found = True
    
   if not found:
      return {"error":"No se ha actualizado el usuario"}
   else:
      return user


@app.delete("/user/{id}")
async def user(id: int):

    found = False

    for index, saved_user in enumerate(users_list):
      if saved_user.id == id:
         del users_list[index]
         found = True
    if not found:
      return {"error":"No se ha eliminado el usuario"}
    else:
       return{"correcto":"Usuario eliminado"}




def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
     return list(users)[0]
    except:
       return {"error":"No se ha encontrado el usuario"}
