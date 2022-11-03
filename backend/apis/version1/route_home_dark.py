from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from static.scripts.create_list import make_list


homepage_router_dark = APIRouter()
templates = Jinja2Templates(directory="templates")


@homepage_router_dark.get("/dark")
async def home(request: Request):

    mylist = make_list()
    context = {"request": request, "mylist": mylist}

    return templates.TemplateResponse("/general_pages/homedark.html", context)
