import os
import shutil
from pathlib import Path
from fastapi_quickstart.main import create_fastapi_app

def test_create_fastapi_app():
    test_app_name = "test_app"
    test_output_dir = Path("test_output")
    
    # Ensure the test output directory doesn't exist
    if test_output_dir.exists():
        shutil.rmtree(test_output_dir)
    
    # Create the FastAPI app
    create_fastapi_app(test_app_name, str(test_output_dir))
    
    # Check if the app directory was created
    app_dir = test_output_dir / test_app_name
    assert app_dir.exists()
    
    # Check if main.py and models.py were created
    assert (app_dir / "app" / "main.py").exists()
    assert (app_dir / "app" / "models.py").exists()
    
    # Check if requirements.txt was created
    assert (app_dir / "requirements.txt").exists()
    
    # Clean up
    shutil.rmtree(test_output_dir)

if __name__ == "__main__":
    test_create_fastapi_app()
    print("All tests passed!")
