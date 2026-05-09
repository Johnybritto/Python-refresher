# GenAI Prep Day 11 practice
# Write code that:
# - imports FastAPI
# - creates app = FastAPI()
# - adds one GET route for "/"
# - returns {"message": "Hello from FastAPI"}


# Add one GET route below.

from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def read_route():
    return {"message": "Hello from FastAPI and Johny "}