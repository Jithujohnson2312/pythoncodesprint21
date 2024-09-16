from fastapi import FastAPI

app = FastAPI()

students = {
    1 : {
        "name" : "john",
        "age"  : "17",
        "class" : "mech",
    }

}
@app.get("/")
async def root():
    return {"message": "Hello World"} 


@app.get("/get-student/{student_id}")
def get_student(student_id : int):
    return students[student_id]