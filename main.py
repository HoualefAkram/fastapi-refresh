from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from routers import math
from utils.render.html import Html
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (Adjust for security)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# Include routers
app.include_router(math.router)


@app.get("/",response_class=HTMLResponse,status_code=200)
def read_root():
	return HTMLResponse(content=Html.home())
