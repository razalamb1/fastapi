from fastapi import FastAPI
import uvicorn
import random
import string

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to random password generator, test change"}

@app.get("/generate/{num}")
async def generate(num: int):
    """Generate a random password of length num"""
    if num < 3:
        num = 3
    if num > 50:
        num = 50
    password = ""
    count = num // 3
    remainder = num % 3
    characters = '.?!@$%&*_^#'
    len_let = count + remainder - 1
    password += random.choice(string.ascii_uppercase)
    for _ in range(len_let):
        password += random.choice(string.ascii_letters)
    for _ in range(count):
        password += random.choice(characters)
        password += random.choice(string.digits)
    password = ''.join(random.sample(password, len(password)))
    return {"password": password}

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')
