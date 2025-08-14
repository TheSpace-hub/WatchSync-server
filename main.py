import asyncio

import uvicorn
from fastapi import FastAPI
from starlette.responses import JSONResponse

app = FastAPI()


@app.get('/taste')
async def websockets_connect():
    await asyncio.sleep(1)
    return JSONResponse({'delicious': True})


if __name__ == '__main__':
    uvicorn.run('main:app', port=22020)
