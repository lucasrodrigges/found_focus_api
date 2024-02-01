from fastapi import FastAPI
from found_focus_api.routes import users

app = FastAPI()

app.include_router(users.router)


@app.get("/")
def read_root():
    return {"message": "Api is running!"}
