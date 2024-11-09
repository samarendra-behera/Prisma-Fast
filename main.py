import uvicorn
from contextlib import asynccontextmanager
from fastapi import FastAPI

from Config.Connection import prisma_connection

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup logic
    print("Start the server!")
    await prisma_connection.connect()
    yield
    # Shutdown logic
    await prisma_connection.disconnect()
    print("Shutdown the server")

def init_app():
    app = FastAPI(
        title="Prisma Fast",
        description="Prisma Fast . Try this ORM",
        version="0.1.0",
        lifespan=lifespan
    )

    @app.get('/')
    def home():
        return "Welcome to home!"

    # include all routes
    from Controller import post
    
    app.include_router(post.router)

    return app


app = init_app()


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)