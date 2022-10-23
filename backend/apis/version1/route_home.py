import folium
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from static.scripts.parse_inpo import extract_inpo


homepage_router = APIRouter()
templates = Jinja2Templates(directory="templates")


@homepage_router.get("/")
async def home(request: Request):

    data = extract_inpo()
    context = {"request": request, "data": data}

    return templates.TemplateResponse("/general_pages/homepage.html", context)
