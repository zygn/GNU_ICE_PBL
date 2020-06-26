import PIL as pl
import tensorflow.keras
import numpy as np
import os
# from IPython.display import display

label = {
    0:'hat', 1:'hood', 2:'jean', 3:'longT', 4:'padding', 5:'shortbottom',
    6:'shortT', 7:'slacks'
}

def testing():
    dirlist = os.listdir('D:/ML/_run')

    model = tensorflow.keras.models.load_model('D:/ML/_model/50md.h5')

    for i in dirlist:
        a = pl.Image.open('D:/ML/_run/{}'.format(i))
        
        img = a.resize((300,300))
        img = img.convert('RGB')

        c = np.array(img)
        c = c/255
        c = np.resize(c, (1,300,300,3))

        b = model.predict(c)
        k = np.argmax(b)
        
        # display(img)
        # print(b,k)

        print(label[k])
        return label[k]

def modelReturn(img, model):
    a = pl.Image.open(img)
    model = tensorflow.keras.models.load_model(model)

    img = a.resize((300,300))
    img = img.convert('RGB')

    c = np.array(img)
    c = c/255
    c = np.resize(c, (1,300,300,3))

    b = model.predict(c)
    k = np.argmax(b)

    #print(label[k])
    return label[k]



#print(modelReturn("C:/Users/Yundo/Documents/GitHub/GNU_ICE_PBL/SampleCase/01.jpg", "C:/Users/Yundo/Documents/GitHub/GNU_ICE_PBL/SampleCase/50md.h5"))