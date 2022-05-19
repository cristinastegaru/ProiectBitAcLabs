from Event_Model import Event
from Response_Model import ResponseModel, Response
import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.post("/events", response_model=Response)
async def add_events(event: Event) -> Response:
    #   db = TestDatabase()
    # risk = await db.find_data(some_key=event.file.file_hash)
    # r = -1
    # if risk is not None:
    #   r = risk['risk_level']
    return Response(file=ResponseModel(hash=event.file.file_hash, risk_level=-1),
                    process=ResponseModel(hash=event.last_access.hash, risk_level=-1))


if __name__ == '__main__':
    uvicorn.run(app)


