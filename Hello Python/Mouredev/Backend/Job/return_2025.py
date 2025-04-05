from fastapi import FastAPI

root = FastAPI()


@root.get("/")
async def main():
  return 'Hola'