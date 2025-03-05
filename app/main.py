from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from datetime import datetime
import pycountry


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

year = datetime.now().year

flags = [
    pycountry.countries.get(alpha_2="US").flag,
    pycountry.countries.get(alpha_2="TG").flag,
]

languages = [
    {"name": "English", "code": "En", "flag": flags[0]},
    {"name": "French", "code": "Fr", "flag": flags[1]},
]
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="home.html",
        context={"year": year, "languages": languages},
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


@app.get("/shop", response_class=HTMLResponse)
def shop_swag(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="shop.html",
        context={"year": year, "languages": languages},
    )


@app.get("/contact", response_class=HTMLResponse)
def contact(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="contact.html",
        context={"year": year, "languages": languages},
    )


if __name__ == "__main__":
    import uvicorn
    

    uvicorn.run(app, host="0.0.0.0", port=8000)