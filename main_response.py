from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    age: int

@app.get("/user/{user_id}", response_model=User)  # response_model로 지정된 모델의 필드를 따르겠다
def get_user(user_id: int):
    # 실제 구현에서는 데이터베이스에서 사용자 정보를 조회하겠지만, 여기서는 예시 데이터를 사용
    return User(name="Alice", age=30)
    return {"name":"Alice", "age":30, "more":"good"}


# 기본 GET 엔드포인트 생성
@app.get("/hello")
def hello(user_id: int):
    return {"message" : "Hello, LikeLion!"}

# 간단한 사용자 정보 반환
@app.get("/user/{user.id}")
def get_id_user(user_id: int):
    return{"name": "user_name" , "email": "user_email"}

# post 요청 처리
class Student(BaseModel):
    student_id :int
    name: str
    email: str

@app.post("/students")
def createStudent(student: Student):
    return {"name": student.name, "price": student.email}

# 항목 삭제
class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {"message": "Item deleted"}

# 조건부 응답
@app.get("/age/{age}")
def ageGet(user_id: int):
    return User (name="Alice", age=30)

# 상태 코드 반환
from fastapi import status

@app.get("/create_student", status_code=status.HTTP_201_CREATED)
def statusStudent(student: Student):
    return {"message": "User created successfully", "student": student}

# 리스트 반환
@app.get("/students")
def allStudent(student: Student):
    return {}

# 응답 모델 사용
@app.get("/user/{user_id}", response_model=User)
def get_user(user_id: int):
    return {"name": "Alice", "age": 25}

# 경로 파라미터와 쿼리 파라미터 조합
@app.get("/search")
def search_items(q: str):
    return {"results": ["item1", "item2", "item3"], "query": q}

# 커스텀 상태 코드와 에러 메시지
from fastapi.exceptions import HTTPException

@app.get("/error")
def custom_error():
    raise HTTPException(status_code=400, detail="Invalid request")


# 대학 행사 등록
from datetime import datetime

app = FastAPI()

class Event(BaseModel):
    name: str
    date: datetime
    attendees: int

@app.post("/events")
def create_event(event: Event):
    return {"message": "Event registered successfully", "event": event}


# 도서 대출 기록
from datetime import date

app = FastAPI()

class Book(BaseModel):
    title: str
    author: str
    borrowed_on: date

@app.post("/books")
def record_book(book: Book):
    return {"message": "Book recorded successfully", "book": book}

# 멋쟁이사자처럼 회원 등록
from pydantic import EmailStr

app = FastAPI()

class Member(BaseModel):
    name: str
    email: EmailStr
    registered_on: date

@app.post("/members")
def register_member(member: Member):
    return {"message": "Member registered successfully", "member": member}


# 학식 메뉴 등록
app = FastAPI()

class Menu(BaseModel):
    name: str
    price: float
    served_on: date

@app.post("/menus")
def create_menu(menu: Menu):
    return {"message": "Menu registered successfully", "menu": menu}


# 스터디 그룹 생성
app = FastAPI()

class StudyGroup(BaseModel):
    name: str
    topic: str
    max_members: int

@app.post("/study-groups")
def create_study_group(group: StudyGroup):
    return {"message": "Study group created successfully", "group": group}