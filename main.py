from fastapi import FastAPI 
import requests

app = FastAPI()

#query = {"slackUsername":"Wathuku", "backend":True, "age":32, "bio":"Always learning new things"}

@app.get('/')
def hello_world():
    return {"slackUsername":"Lizthuku", "backend":True, "age":32, "bio":"Always learning new things"}
