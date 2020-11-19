import os
import shutil
import pandas as pd

# 파일 복사 기준 갯수 csv 파일
cntBase = pd.read_csv('D:/project/task2/cnt.csv', header=None)

# 분류할 대상 폴더
files = os.listdir('D:/project/task2/data/raw/')

# 파일을 복사,분류할 경로
copyPATH = 'D:/project/task2/data/copy/'

# 분류 작업
n = 0
for i, index in enumerate(cntBase[1]):
    folder = os.listdir(copyPATH)[i]

    for j in range(0, index):
        shutil.copy('D:/project/task2/data/raw/' + files[n + j], copyPATH + folder + '/')

    n += index

print("Finish!")
