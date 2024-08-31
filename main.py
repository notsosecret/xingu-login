from fastapi import FastAPI, Request, status, Form
from typing import Annotated

from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/index")
def index(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")


@app.post("/login")
def login(request: Request, email: Annotated[str, Form()], password: Annotated[str, Form()]):
    if email == "admin@xingu-ad.com" and password == "admin":
        return RedirectResponse("/secret", status.HTTP_302_FOUND)
    else:
        return templates.TemplateResponse(request=request, name="index.html", status_code=status.HTTP_401_UNAUTHORIZED,
                                          context={"error": True, "email": email, "password": password})


@app.get("/secret")
def read_secret():
    return {"Very": "secret"}
