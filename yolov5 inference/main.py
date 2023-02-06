from yolov5_tflite_webcam_inference import detect_video
if __name__ == "__main__":
    # detect plate
    value = detect_video(weights="./models/custom_plate.tflite", labels="./labels/plate.txt", conf_thres=0.25, iou_thres=0.45,
                         img_size=640, webcam=0)
    print("inside main", value)
    # detect_image(weights="./models/character.tflite", labels="./labels/number.txt", conf_thres=0.25, iou_thres=0.45,
    #              image_url="./output/cropped/cropped1.jpg", img_size=640)
    # detect character
