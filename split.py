import os, glob
import shutil

PATH = 'D:/project/task2/data/copy/'

folderList = os.listdir(PATH)

for folder in folderList:
    raw = glob.glob(os.path.join(PATH, folder, '*.jpg'))
    raw = [i.replace('\\', '/') for i in raw]

    testCnt = int(len(raw) * 0.2)
    trainCnt = len(raw) - testCnt

    if not os.path.isdir(PATH + folder + '/' + 'train/'):
        os.mkdir(PATH + folder + '/' + 'train/')
    if not os.path.isdir(PATH + folder + '/' + 'test/'):
        os.mkdir(PATH + folder + '/' + 'test/')

    [shutil.move(raw[i], PATH + folder + '/' + 'test/') for i in range(0, testCnt)]
    [shutil.move(raw[testCnt+i], PATH + folder + '/' + 'train/') for i in range(0, trainCnt)]

print("Finish!")