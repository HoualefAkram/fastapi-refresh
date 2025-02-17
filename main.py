from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from routers import math
from utils.render.html import Html
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(math.router)
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/",response_class=HTMLResponse,status_code=200)
def read_root():
	return HTMLResponse(content=Html.home())
