import os
import zipfile

zf = zipfile.ZipFile("/home/yuvrajksi199/Desktop/snowproDE.zip", "w") # destination file path
for dirname, subdirs, files in os.walk("/home/yuvrajksi199/Desktop/snowpro-DE"): #source file path to zip
    zf.write(dirname)
    for filename in files:
        zf.write(os.path.join(dirname, filename))

zf.close()
