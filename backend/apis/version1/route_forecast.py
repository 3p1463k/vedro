import folium
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from static.scripts.parse_chmi import extract_chmi

forecast_router = APIRouter()
templates = Jinja2Templates(directory="templates")


@forecast_router.get("/forecast")
async def home(request: Request):

    data = extract_chmi()
    context = {"request": request, "data": data}

    return templates.TemplateResponse("/general_pages/forecast.html", context)
