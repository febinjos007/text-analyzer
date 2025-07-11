from fastapi import FastAPI
from fastapi.openapi.docs import get_redoc_html, get_swagger_ui_html
from fastapi.responses import HTMLResponse

from src.router import router as analyse_router

app = FastAPI(title="Customer Feedback Analyzer")
app.include_router(analyse_router)


# Include docs and redoc routes
@app.get("/docs", response_class=HTMLResponse, include_in_schema=False)
async def swagger_ui_html() -> HTMLResponse:
    return get_swagger_ui_html(openapi_url="/openapi.json", title="API Docs")


@app.get("/redoc", response_class=HTMLResponse, include_in_schema=False)
async def redoc_html() -> HTMLResponse:
    return get_redoc_html(openapi_url="/openapi.json", title="API Docs")
