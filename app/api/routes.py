from app.api.route_router import router
from app.api.misc_api import misc_router


ROUTES = {
    "": misc_router,
    "/routes": router,
}
