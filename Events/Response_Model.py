from pydantic import BaseModel


class ResponseModel(BaseModel):
    hash: str
    risk_level: int


class Response(BaseModel):
    file: ResponseModel
    process: ResponseModel

