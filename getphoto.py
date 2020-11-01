import os
import shutil

path = "C:\\Users\\"+os.getlogin()+"\\AppData\\Local\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets\\"
path2 = "F:\\Dropbox\\python\\microsoft-photo\\portrait\\"
path3 = "F:\\Dropbox\\python\\microsoft-photo\\landscape\\"
if not os.path.exists(path2):
    os.makedirs(path2)
if not os.path.exists(path3):
    os.makedirs(path3)

filelist = os.listdir(path)
for x in filelist:
    filename = path+x
    filename2 = path2+x+'.jpg'
    filename3 = path3+x+'.jpg'

    #if (os.path.getsize(filename) > 102400):
        #shutil.copy(filename, filename2)

    if (os.path.getsize(filename) > 102400):
        with open(filename,'rb') as img_file:
            img_file.seek(163)
            a = img_file.read(2)
            height = (a[0] << 8) + a[1]

            if (height >1080):
                shutil.copy(filename, filename2)
            else:
                shutil.copy(filename, filename3)

