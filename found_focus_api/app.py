from fastapi import FastAPI
from found_focus_api.routes import users
from found_focus_api import __version__

app = FastAPI()

app.include_router(users.router)


@app.get("/")
def read_root():
    message = f"Api is running at version {__version__} 🚀"
    return {"message": message}
