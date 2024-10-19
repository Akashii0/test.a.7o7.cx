from fastapi import FastAPI


app = FastAPI()

@app.get('/')
def welcome():
    return "Welcome to my World, We are up and running and testing Server Blocks."
