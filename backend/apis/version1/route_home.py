import folium
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

homepage_router = APIRouter()
templates = Jinja2Templates(directory="templates")


@homepage_router.get("/")
async def home(request: Request):

    context = {"request": request}

    return templates.TemplateResponse("/general_pages/homepage.html", context)
