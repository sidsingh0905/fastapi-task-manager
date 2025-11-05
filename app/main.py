from fastapi import FastAPI
from sqlalchemy import inspect
from app.api import routes_tasks
from app.db.database import Base, engine

app = FastAPI(title="Task Manager API")

@app.on_event("startup")
def on_startup():
    inspector = inspect(engine)
    existing_tables = inspector.get_table_names()

    # List all tables defined in models
    defined_tables = Base.metadata.tables.keys()

    missing_tables = [t for t in defined_tables if t not in existing_tables]

    if missing_tables:
        print(f"🔹 Creating missing tables: {missing_tables}")
        Base.metadata.create_all(bind=engine)
        print("✅ All missing tables created!")
    else:
        print("✅ All tables already exist, skipping creation.")

# Include routers
app.include_router(routes_tasks.router)

@app.get("/")
def root():
    return {"message": "Welcome to Task Manager! Visit /mypage to view tasks."}


print("test commit for ecr and github actions so that image can push to ecr")
