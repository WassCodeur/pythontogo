from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, PlainTextResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


from .database  import (
    get_all_events,
    get_swags,
    get_teams_members,
    get_event_by_id,
    get_parteners,
    galleries,
)
from datetime import datetime
import pycountry
import os
import json


app = FastAPI()


static_folder = os.path.join(os.path.dirname(__file__), "static")
templates_folder = os.path.join(os.path.dirname(__file__), "templates")
app.mount("/static", StaticFiles(directory=static_folder), name="static")
templates = Jinja2Templates(directory=templates_folder)
teams_members = get_teams_members()

year = datetime.now().year

flags = [
    pycountry.countries.get(alpha_2="US").flag,
    pycountry.countries.get(alpha_2="TG").flag,
]

languages = [
    {"name": "English", "code": "En", "flag": flags[0]},
    {"name": "French", "code": "Fr", "flag": flags[1]},
]


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="home.html",
        context={"year": year, "languages": languages, "teams": teams_members, "partners": get_parteners()},
    )


@app.get("/about", response_class=HTMLResponse)
def about(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="about.html",
        context={"year": year, "languages": languages},
    )


@app.get("/events")
def events(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="events.html",
        context={"year": year, "languages": languages},
    )

@app.get("/coc")
def coc(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="coc.html",
        context={"year": year, "languages": languages},
    )

@app.get("/mission_vision")
def mission_vision(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="mission_vision.html",
        context={"year": year, "languages": languages},
    )

@app.get("/shop", response_class=HTMLResponse)
def shop_swag(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="shop.html",
        context={"year": year, "languages": languages},
    )

@app.get("/gallery")
def gallery(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="gallery.html",
        context={"year": year, "languages": languages, "galleries": galleries},
    )

@app.get("/api/shop/swags", response_class=JSONResponse)
def swags(request: Request):
   
    return get_swags()

@app.get("/api/events", response_class=JSONResponse)
async def get_events(request: Request):
    return get_all_events()

@app.get("/api/events/{eventId}", response_class=JSONResponse)
async def get_event(eventId: int):
    return get_event_by_id(eventId)



@app.get("/contact", response_class=HTMLResponse)
def contact(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="contact.html",
        context={"year": year, "languages": languages},
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
