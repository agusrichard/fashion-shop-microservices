import uvicorn
from fastapi import FastAPI

app = FastAPI(title='Fashio Shop Authentication Service')


@app.get('/auth-service')
def root():
    return 'You are cool'


if __name__ == '__main__':
    uvicorn.run(app)
