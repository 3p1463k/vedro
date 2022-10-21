from fastapi import APIRouter
from apis.version1 import route_home


api_router = APIRouter()

api_router.include_router(route_home.homepage_router, prefix="", tags=["general_pages"])
# api_router.include_router(route_upload.upload_router, prefix="", tags=["map"])
