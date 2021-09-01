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
    characters = '.?!@$%&*_^#'
    count = {'letter':0, 'character':0, 'number':0}
    translation = {'letter': string.ascii_letters, 'character': characters, 'number': string.digits}
    if num < 6 or num > 50:
        num = 8
    for i in range(num):
        integer = random.randint(1,3)
        if integer == 1:
            password += random.choice(string.ascii_letters)
            count['letter'] += 1
            pass
        elif integer == 2:
            password += random.choice(characters)
            count['character'] += 1
            pass
        else:
            password += random.choice(string.digits)
            count['number'] += 1
            pass
        pass
    for key, val in count.items():
        if val == 0:
            rep = 0
            for key2, val2 in count:
                if key2 != key & val2 > rep:
                    rep = val2
                    use = key2
                    pass
                pass
            for i in range(num):
                if password[i] in translation[use]:
                    password[:i] + random.choice(translation[key]) + password[i + 1:]
                    break
                pass
            pass
    return {"password": password}

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')