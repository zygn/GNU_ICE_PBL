##############
#   라벨링   #
##############

from PIL import Image
import os, glob, numpy as np
from sklearn.model_selection import train_test_split

caltech_dir = "D:/ML/smp" # 디렉토리 경로
categories = ['hat','hood','jean','longT','padding','shortbottom','shortT','slacks'] # 지정경로의 하위 폴더
nb_classes = len(categories) 

image_w = 300
image_h = 300

X = []
y = []

for idx, cat in enumerate(categories): #idx=index cat=catalog


    label = [0 for i in range(nb_classes)]
    label[idx] = 1

    image_dir = caltech_dir + "/" + cat
    files = glob.glob(image_dir + "/*.jpg")
    print(cat, " 파일 길이 : ", len(files))
    for i, f in enumerate(files):
        img = Image.open(f)
        img = img.convert("RGB")
        img = img.resize((image_w, image_h))
        data = np.asarray(img)

        X.append(data)
        y.append(label)


X = np.array(X)
y = np.array(y)

X_train, X_test, y_train, y_test = train_test_split(X, y)
x = (X_train, X_test)
y = (y_train, y_test)

np.save("D:/ML/X1.npy", x)
np.save("D:/ML/Y1.npy", y)

print("ok", len(y))