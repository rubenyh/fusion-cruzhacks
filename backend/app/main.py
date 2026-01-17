from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import SmsService
from pydantic import BaseModel


app = FastAPI(title="Fusion")




origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class SmsRequest(BaseModel):
    to: str
    body: str

@app.get("/")
def root():
    return {"message": "FastAPI backend running"}


@app.post("/sms")
async def sendSmS(sms_request:SmsRequest):
    try:
        message = SmsService.sendSms(sms_request.to,sms_request.body)
        return message
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
    