from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

@app.post("/items/")
def create_item(item: Item):
    return {"name": item.name, "price": item.price}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id, "name": "Sample Item"}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_id": item_id, "name": item.name, "price": item.price}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {"message": "Item deleted"}

# 학생 정보 조회
class Student(BaseModel):
    student_id :int
    name: str
    email: str

@app.get("/student/{student_id}")
def searchStudent(student_id: int):
    return {"student_id": student_id, "name": "Sample name", "email": "Sample email" }


# 아이템 등록
@app.post("/item/")
def createItem(item:Item):
    return {"name": item.name, "description": item.description}


# 프로젝트 아이템 삭제
class Projects(BaseModel):
    project_id : int
    name : str
    description : str

@app.delete("/projects/{project_id}")
def delete_project(project_id: int):
    return {"message": "Project deleted successfully"}