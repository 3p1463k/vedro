from fastapi import APIRouter
from apis.version1 import route_home
from apis.version1 import route_home_dark
from apis.version1 import route_fcast
from apis.version1 import route_fcast_dark

from apis.version1 import route_radar


api_router = APIRouter()

api_router.include_router(route_home.homepage_router, prefix="", tags=["general_pages"])
api_router.include_router(
    route_home_dark.homepage_router_dark, prefix="", tags=["general_pages"]
)

api_router.include_router(route_fcast.fcast_router, prefix="", tags=["forecast"])
api_router.include_router(
    route_fcast_dark.fcast_router_dark, prefix="", tags=["forecast"]
)

api_router.include_router(route_radar.radar_router, prefix="", tags=["radar"])
