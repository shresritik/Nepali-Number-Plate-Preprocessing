from fastapi import FastAPI
from fastapi.responses import FileResponse
from yolov5_tflite_webcam_inference import detect_video
from fastapi.middleware.cors import CORSMiddleware
import os

import base64
app = FastAPI()

origins = [
    "http://127.0.0.1:5173",
    "http://localhost",
    "http://localhost:8080",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# listDir = os.getcwd()


@app.get("/")
async def root():
    value = detect_video(weights="./models/custom_plate.tflite", labels="./labels/plate.txt", conf_thres=0.25, iou_thres=0.45,
                         img_size=640, webcam=0)

    print("inside main", value)
    # file_path = listDir + '\output\cropped\cropped1.jpg'
    with open("./output/cropped/cropped1.jpg", "rb") as image2string:
        converted_string = base64.b64encode(image2string.read())
    # file = FileResponse(file_path, media_type='image/jpeg')
    return {"message": value, "file": converted_string}
