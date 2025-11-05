from sqlalchemy import text
from app.db.database import engine

def check_connection():
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT 1"))
            print("✅ Database connection successful:", result.scalar())
    except Exception as e:
        print("❌ Database connection failed:", e)

if __name__ == "__main__":
    check_connection()
