from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World!"}


@app.get("/posts")
async def get_post():
    return {"data": "This is your data"}


@app.post("/posts")
async def create_posts(payload: dict = Body(...)):
    return {"new_post": f"title: {payload['title']} content: {payload['content']}"}
