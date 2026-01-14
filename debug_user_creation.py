import sys
import os
import traceback

# Add current dir to path
sys.path.append(os.getcwd())

from blog import models, schema, database
from blog.hashing import Hash
from sqlalchemy.orm import Session

def test_create_user():
    print("Initializing Database...")
    models.Base.metadata.create_all(bind=database.engine)
    
    db = database.SessionLocal()
    try:
        print("Creating dummy user request...")
        # Create a schema.User object
        user_request = schema.User(name="Debug User", email="debug@example.com", password="password123")
        
        print("Hashing password...")
        hashed = Hash.bcrypt(user_request.password)
        print(f"Hash generated: {hashed}")
        
        print("Creating DB Model...")
        new_user = models.User(name=user_request.name, email=user_request.email, password=hashed)
        
        print("Adding to DB...")
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        print(f"User created successfully with ID: {new_user.id}")
        
        # Cleanup
        db.delete(new_user)
        db.commit()
        print("Cleanup successful.")

    except Exception:
        print("\n!!! EXCEPTION CAUGHT !!!")
        traceback.print_exc()
    finally:
        db.close()

if __name__ == "__main__":
    test_create_user()
