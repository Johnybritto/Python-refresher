# GenAI Prep Day 12 practice
# Write code that:
# - imports FastAPI
# - creates app = FastAPI()
# - adds one POST route for "/echo"
# - accepts data: dict
# - returns {"received": data}

from fastapi import FastAPI

app = FastAPI()


# Add one POST route below.
@app.post("/echo")
def read_route(data: dict):
    return {"received" : data }