import threading
import time

# Create an Event object
event = threading.Event()

# Example function that waits for the event to be set
def wait_for_event():
    print("Waiting for event to be set...")
    event.wait()  # This blocks until the event is set
    print("Event is set!")

# Start a thread to run the function
thread = threading.Thread(target=wait_for_event)
thread.start()

# Simulate some work
time.sleep(3)

# Set the event
event.set()
