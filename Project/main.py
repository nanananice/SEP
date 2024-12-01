from fastapi import FastAPI, Form, HTTPException, Depends,  status
from starlette.responses import RedirectResponse
from fastapi.responses import FileResponse, HTMLResponse, Response
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi.security import OAuth2PasswordBearer
import transaction
from db import get_db, User
from BTrees.OOBTree import BTree
import jwt
import datetime
import logging
from ZODB import FileStorage, DB
from persistent import Persistent
import googlemaps
from pathlib import Path
import routers


app = FastAPI()


app.mount("/static", StaticFiles(directory="static"), name="static")




app.include_router(routers.router)


