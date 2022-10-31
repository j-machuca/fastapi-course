from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World!"}


@app.get('/posts')
async def get_post():
    return {"data": "This is your data"}
