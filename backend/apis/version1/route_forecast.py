import folium
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from static.scripts.create_fcast import make_list1
import pandas as pd

forecast_router = APIRouter()
templates = Jinja2Templates(directory="templates")


@forecast_router.get("/forecast")
async def home(request: Request):

    mylist1 = make_list1()
    context = {"request": request, "mylist1": mylist1}

    return templates.TemplateResponse("/general_pages/forecast.html", context)
