import folium
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

homepage_router = APIRouter()
templates = Jinja2Templates(directory="templates")


@homepage_router.get("/")
async def home(request: Request):

    start_coords = (49.7, 15.2)
    mymap = folium.Map(location=start_coords, zoom_start=8)
    folium.LayerControl().add_to(mymap)
    mymap1 = mymap._repr_html_()
    context = {"request": request, "mymap": mymap1}

    return templates.TemplateResponse("/general_pages/homepage.html", context)
