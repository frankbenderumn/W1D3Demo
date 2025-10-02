import os

from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

templates = Jinja2Templates(directory="public/html")
app.mount("/asset", StaticFiles(directory="public/asset"), name="asset")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "title": "Landing", "host": "host"})

@app.get("/web3", response_class=HTMLResponse)
async def read_web3(request: Request):
    return templates.TemplateResponse("web3.html", {"request": request, "title": "Landing", "host": "host"})