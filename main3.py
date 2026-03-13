from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles  # Добавлен недостающий импорт
import uvicorn

app = FastAPI()

# Подключаем статические файлы
app.mount("/static", StaticFiles(directory="static"), name="static")  # Исправлено: обычно статические файлы монтируются на "/static"

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

if __name__ == "__main3__":
    uvicorn.run("main3:app", host="127.0.0.1", port=8080, reload=True)