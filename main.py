from fastapi import FastAPI
import uvicorn
import random
import string

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to random password generator"}

@app.get("/generate/{num}")
async def generate(num: int):
    """Generate a random password of length num"""
    password = ""
    for i in range(num):
        integer = random.randint(1,3)
        if integer == 1:
            password += random.choice(string.ascii_letters)
            pass
        elif integer == 2:
            password += random.choice(string.punctuation)
            pass
        else:
            password += random.choice(string.digits)
            pass
    return {"password": password}

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')