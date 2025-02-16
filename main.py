from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from routers import math
from utils.render.html import Html

app = FastAPI()
app.include_router(math.router)

@app.get("/",response_class=HTMLResponse,status_code=200)
def read_root():
	return HTMLResponse(content=Html.home())
