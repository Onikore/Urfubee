import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.api.api_v1.api import api_router
from app.db.session import db

app = FastAPI(title='URFUBEE', openapi_url='/api/v1/openapi.json', version='0.0.1')
app.include_router(api_router)

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


@app.on_event("startup")
async def startup():
    await db.connect()


@app.on_event("shutdown")
async def shutdown():
    await db.disconnect()


if __name__ == "__main__":
    uvicorn.run('main:app', host="127.0.0.1", port=5000, reload=True)
