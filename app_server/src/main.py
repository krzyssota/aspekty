from fastapi import FastAPI
app = FastAPI()
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/health_check")
async def root():
    return {"message": "im well tank u"}
