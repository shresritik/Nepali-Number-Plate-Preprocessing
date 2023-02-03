from yolov5_tflite_image_inference import detect_image
if __name__ == "__main__":
    # detect plate
    # detect_image(weights="./models/custom_plate.tflite", labels="./labels/plate.txt", conf_thres=0.25, iou_thres=0.45,
    #              image_url="./images/1.jpg", img_size=640)
    # detect character
    detect_image(weights="./models/character.tflite", labels="./labels/number.txt", conf_thres=0.25, iou_thres=0.45,
                 image_url="./output/cropped/test.jpg", img_size=640)
