from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def root():
    return "Hola FastApi"

@app.get('/minombre')
async def root():
    return { "nombre": "Daniel"
            }

