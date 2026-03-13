from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel

app = FastAPI()

books = [
    {
        "id": 1,
        "title": "Асинхронность в python",
        "author": "Мэттью",
    },
    {
        "id": 2,
        "title": "Backend разработка в python",
        "author": "Артём",
    },
]

@app.get(

    "/books",
    tags=["Книги"],
    summary="Получить все книги")
def read_books():
    return books

@app.get("/books/{book_id}",
         tags=["Книги "],
         summary="Получить конкретную книжку")
def read_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Книга не найдена")



class NewBook(BaseModel):
    title:str
    author:int


@app.post("/books", tags=["Книги"])
def create_book(new_book: NewBook):

    books.append({
        "id": new_id,
        "title": new_book.title,
        "author": new_book.author,
    })
    return {"success": True, "message": "Книга успешно добавлена", "id": new_id}
 



if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)