from fastapi import FastAPI
from sqlalchemy import inspect
from app.api import routes_tasks
from app.db.database import Base, engine

# Prometheus Instrumentation
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI(title="Task Manager API")

# Routers must be included BEFORE instrumentation
app.include_router(routes_tasks.router)


@app.on_event("startup")
async def startup():
    # Initialize Prometheus metrics AFTER routers are loaded
    Instrumentator().instrument(app).expose(app)

    # DB table creation logic
    inspector = inspect(engine)
    existing_tables = inspector.get_table_names()
    defined_tables = Base.metadata.tables.keys()

    missing_tables = [t for t in defined_tables if t not in existing_tables]

    if missing_tables:
        print(f"🔹 Creating missing tables: {missing_tables}")
        Base.metadata.create_all(bind=engine)
        print("✅ All missing tables created!")
    else:
        print("✅ All tables already exist, skipping creation.")


@app.get("/")
def root():
    return {"message": "Welcome to Task Manager via ArgoCD!! Visit /mypage to view tasks"}
