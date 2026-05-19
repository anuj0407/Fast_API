from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"Message":"Hello world"}

@app.get("/about")
def about():
    return {"Message":"Welcome to our about page."}
