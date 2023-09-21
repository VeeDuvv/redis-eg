import time

def background_task(name):
    """ Function to simulate a background task. """
    print(f"Task {name} is running.")
    time.sleep(10)
    print(f"Task {name} completed.")
    return f"Task {name} result"
