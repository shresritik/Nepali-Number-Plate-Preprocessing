import os
import shutil
import cv2
imgs = []
xmls = []
classes = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'ba', 'pa']
BASE_DIR = 'D:/Project/image_resizer/'

crsPath = BASE_DIR+'images/images_dir'


try:
    for i in range(len(os.listdir(crsPath))):
        crslen = os.path.join(crsPath, classes[i])
        files = os.listdir(crslen)
        try:
            os.makedirs('resized_images/'+classes[i])
        except:
            pass
        # print(files)
        for filename in files:
            file_pattern = crsPath+'/'+classes[i]+'/'

            if filename.endswith('.jpg'):
                path_to_resize = os.path.join(file_pattern, filename)

                image = cv2.imread(path_to_resize)
                imgResized = cv2.resize(image, (128, 128))
                # os.mkdir(classes[i]):
                if(classes[i] == '0'):

                    cv2.imwrite('resized_images/0/' +
                                filename, imgResized)
                elif (classes[i] == '1'):

                    cv2.imwrite('resized_images/1/' +
                                filename, imgResized)
                elif (classes[i] == '2'):

                    cv2.imwrite('resized_images/2/' +
                                filename, imgResized)
                elif (classes[i] == '3'):

                    cv2.imwrite('resized_images/3/' +
                                filename, imgResized)
                elif (classes[i] == '4'):

                    cv2.imwrite('resized_images/4/' +
                                filename, imgResized)
                elif (classes[i] == '5'):

                    cv2.imwrite('resized_images/5/' +
                                filename, imgResized)
                elif (classes[i] == '6'):

                    cv2.imwrite('resized_images/6/' +
                                filename, imgResized)
                elif (classes[i] == '7'):

                    cv2.imwrite('resized_images/7/' +
                                filename, imgResized)
                elif (classes[i] == '8'):

                    cv2.imwrite('resized_images/8/' +
                                filename, imgResized)
                elif (classes[i] == '9'):

                    cv2.imwrite('resized_images/9/' +
                                filename, imgResized)
                elif (classes[i] == 'ba'):

                    cv2.imwrite('resized_images/ba/' +
                                filename, imgResized)
                elif (classes[i] == 'pa'):

                    cv2.imwrite('resized_images/pa/' +
                                filename, imgResized)

            else:
                print("No file with .jpg")
except:
    pass
