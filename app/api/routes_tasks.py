from fastapi import APIRouter, Depends, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app.db import models
from app.db.database import get_db

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

# ---------- HTML ROUTES ----------

@router.get("/mypage", response_class=HTMLResponse)
def show_tasks(request: Request, db: Session = Depends(get_db)):
    tasks = db.query(models.Task).all()
    return templates.TemplateResponse("tasks.html", {"request": request, "tasks": tasks})


@router.post("/add-task")
def add_task(title: str = Form(...), description: str = Form(None), db: Session = Depends(get_db)):
    new_task = models.Task(title=title, description=description)
    db.add(new_task)
    db.commit()
    return RedirectResponse(url="/mypage", status_code=303)


@router.get("/delete-task/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(task)
    db.commit()
    return RedirectResponse(url="/mypage", status_code=303)


@router.post("/update-task/{task_id}")
def update_task(task_id: int, title: str = Form(...), description: str = Form(None), db: Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    task.title = title
    task.description = description
    db.commit()
    return RedirectResponse(url="/mypage", status_code=303)


# ---------- JSON API ROUTES (Optional for Postman/Frontend) ----------

@router.get("/tasks/", response_model=list[dict])
def get_tasks(db: Session = Depends(get_db)):
    tasks = db.query(models.Task).all()
    return [{"id": t.id, "title": t.title, "description": t.description} for t in tasks]
