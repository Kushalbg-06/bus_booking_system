from fastapi import FastAPI
app=FastAPI()

@app.get("/")
def home():
    return {"server running on the port 8000"}