import os
from random import choice
import shutil
# arrays to store file names
imgs = []
xmls = []
classes = ['rect']
BASE_DIR = 'D:/Project/image_preprocessing/number_plate_detection/'
# setup dir names
trainPath = BASE_DIR+'images/train'
valPath = BASE_DIR+'images/val'
crsPath = BASE_DIR+'images_dir'

# setup ratio (val ratio = rest of the files in origin dir after splitting into train and test)
train_ratio = 0.8
val_ratio = 0.2
try:
    for i in range(len(os.listdir(crsPath))):
        filename = os.listdir(crsPath)

        if filename[i].endswith('.txt'):
            # creating file of format 0_1.txt for label txt of 0 and so on
            # new_fileName = os.rename(
            #     file_pattern+filename, file_pattern + classes[i]+"_"+filename)
            try:
                label_folder = os.path.join(crsPath, 'labels')
                os.mkdir(label_folder)

            except:
                pass
            shutil.copy(os.path.join(crsPath, filename[i]),
                        os.path.join(crsPath, 'labels'))
            xmls.append(filename[i])

        else:
            # creating file of format 0_1.jpg for image of 0 and so on

            # new_fileName = os.rename(
            #     file_pattern+filename, file_pattern + classes[i]+"_"+filename)

            try:

                images_folder = os.path.join(crsPath, 'images')
                os.mkdir(images_folder)

            except:
                pass
            shutil.copy(os.path.join(crsPath, filename[i]),
                        os.path.join(crsPath, 'images'))
            imgs.append(filename[i])
except:
    pass
countForTrain = int(len(imgs)*train_ratio)
countForVal = int(len(imgs)*val_ratio)
print("training images are : ", countForTrain)
print("Validation images are : ", countForVal)
root_path = BASE_DIR+"/dataset"
if(os.path.exists(root_path)):
    print("Root exist")
    pass
else:
    os.mkdir('dataset')
    up_list = ['images', 'labels']
    down_list = ['train', 'val']

    for up in up_list:
        path = os.path.join(root_path, up)
        os.mkdir(path)
        for down in down_list:
            inner_path = os.path.join(root_path, up, down)
            os.mkdir(inner_path)


trainimagePath = BASE_DIR+'dataset/images/train'
trainlabelPath = BASE_DIR+'dataset/labels/train'
valimagePath = BASE_DIR+'dataset/images/val'
vallabelPath = BASE_DIR+'dataset/labels/val'


for x in range(countForTrain):

    fileJpg = choice(imgs)
    print('images', fileJpg)  # get name of random image from origin dir
    # get name of corresponding annotation file
    fileXml = fileJpg[:-4] + '.txt'

    shutil.copy(os.path.join(crsPath+'/images', fileJpg),
                os.path.join(trainimagePath, fileJpg))
    shutil.copy(os.path.join(crsPath+'/labels', fileXml),
                os.path.join(trainlabelPath, fileXml))
    # remove files from arrays
    imgs.remove(fileJpg)
    xmls.remove(fileXml)

# cycle for test dir
for x in range(countForVal):

    fileJpg = choice(imgs)  # get name of random image from origin dir
    # get name of corresponding annotation file
    fileXml = fileJpg[:-4] + '.txt'

    # move both files into train dir
    #shutil.move(os.path.join(crsPath, fileJpg), os.path.join(valimagePath, fileJpg))
    #shutil.move(os.path.join(crsPath, fileXml), os.path.join(vallabelPath, fileXml))
    shutil.copy(os.path.join(crsPath+'/images', fileJpg),
                os.path.join(valimagePath, fileJpg))
    shutil.copy(os.path.join(crsPath+'/labels', fileXml),
                os.path.join(vallabelPath, fileXml))

    # remove files from arrays
    imgs.remove(fileJpg)
    xmls.remove(fileXml)
