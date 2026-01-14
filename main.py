from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

students = {
    1: {
        "name":"Luan",
        "age":20,
        "class":"3rd year"
    }
}

class Student(BaseModel):
    name: str
    age: int
    year: str

class UpdateStudent(BaseModel):
    name: str | None = None
    age: int | None = None
    year: str | None = None 


@app.get("/")

def index():
    return {"name": "First Data"}


@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(description="The ID of the student", gt=0, le=3)):
    return students[student_id]


@app.get("/get-by-name/{student_id}")
def get_student(*,student_id: int, name : str | None = None, test: int | None = None):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data": "Not found"}

@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"Error": "Student already exists"}
    students[student_id] = student
    return students[student_id]    

@app.put("/update-student/{student_id}")

def update_student(student_id: int, student: UpdateStudent):
    if student.name != None:
        students[student_id].name = student.name
    
    if student.age != None:
        students[student_id].age = student.age
        
    if student.year != None:    
        students[student_id].year = student.year
    
    return students[student_id]

@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"Error": "Student not found"}
    del students[student_id]
    return "Student deleted"