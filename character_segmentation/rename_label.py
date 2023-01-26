import os


def rename_label():
    BASE_DIR = 'D:/Project/image_classifier/'
    crsPath = BASE_DIR+'images_dir/labels'
    crsDir = os.listdir(crsPath)
    for i in range(len(crsDir)):
        first_name = crsDir[i].split('_')[0]
        with open(os.path.join(crsPath, crsDir[i]), "r+") as file:

            for line in file:
                find_first = line.split(' ')[0]
                file_replace = line.replace(find_first, first_name)
                if('ba' in file_replace):
                    file_replace = file_replace.replace('ba', '10')
                if('pa' in file_replace):
                    file_replace = file_replace.replace('pa', '11')
                file.write(file_replace)
                print(crsDir[i], file_replace)
                break

        with open(os.path.join(crsPath, crsDir[i]), "r+") as fp:

            lines = fp.readlines()
        # move file pointer to the beginning of a file
            fp.seek(0)
            # truncate the file
            fp.truncate()
            if (len(lines) > 1):
                # start writing lines except the first line
                # lines[1:] from line 2 to last line
                fp.writelines(lines[1:])
            print(fp.read())


def readLines():
    BASE_DIR = 'D:/Project/image_classifier/dataset/labels'
    crsPath = BASE_DIR+'/val'
    crsDir = os.listdir(crsPath)
    for i in range(len(crsDir)):

        with open(os.path.join(crsPath, crsDir[i]), "r+") as fp:

            lines = len(fp.readlines())
            print(i)

            if(lines == 2):
                print(crsDir[i], "Yes")
                break
            else:
                print('No')


if __name__ == "__main__":
    readLines()
