from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def healthy_check():
    return {'Working': True}
