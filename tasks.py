import time
import requests
from app_factory import create_app

app = create_app()


def background_task(name, app):
    print(f"app: {id(app)}")
    with app.app_context():
        """Function to simulate a background task."""
        print(f"Task {name} is running.")
        # print IDs of current_app and app using fstring formatting

        # Simulating an API call by reversing the string
        time.sleep(2)  # Simulating delay
        reversed_string = name[::-1]

        print(f"Task {name} completed.")
        return f"Transformed String: {reversed_string}"
