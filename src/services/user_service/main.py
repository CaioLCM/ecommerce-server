from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health_route():
    return {"status": "ok!"}

