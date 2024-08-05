from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return{"hellow":"this is email api"}