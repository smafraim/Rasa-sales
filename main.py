# Import the required modules
import uvicorn
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from news_articles_features import NewsArticleShares
import pandas as pd
import pickle
import numpy as np

# Create the FastAPI app
RasaNaming = FastAPI()
templates = Jinja2Templates(directory="templates")

@RasaNaming.get("/")
async def render_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})



# # Run the API with uvicorn
# '''if __name__ == '__main__':
#     uvicorn.run("app:NewsArticle", host='0.0.0.0', port=8005, reload=True, debug=True, workers=3)
# '''