import folium
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from static.scripts.create_list import make_list
import pandas as pd

fcast_router = APIRouter()
templates = Jinja2Templates(directory="templates")


@fcast_router.get("/fcast")
async def home(request: Request):

    mylist = make_list()
    context = {"request": request, "mylist": mylist}

    return templates.TemplateResponse("/general_pages/forecastcz.html", context)
