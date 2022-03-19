import os
import time
import random
from os import listdir
from os.path import isfile, join
from random import randint
from InstagramAPI import *

from PIL import Image

imagesFolder = ""  # Change Directory to Folder with Pics that you want to upload
IGUSER = ""  # Change to your Instagram USERNAME
PASSWD = ""  # Change to your Instagram Password

IGCaption = ""
os.chdir(imagesFolder)
listImages = sorted([f for f in listdir(imagesFolder) if isfile(join(imagesFolder, f))])
print("Total Photo in this folder:" + str(len(listImages)))

# #Start Login and Uploading Photo
igapi = InstagramAPI(IGUSER, PASSWD)
igapi.login()  # login



while True:
    error = False

    photo = listImages[0]
    if (photo.lower().endswith(".png")):
        im = Image.open(photo)
        fill_color = (255, 255, 255)  # your new background color
        im = im.convert("RGBA") 
        if im.mode in ('RGBA', 'LA'):
            background = Image.new(im.mode[:-1], im.size, fill_color)
            background.paste(im, im.split()[-1])  # omit transparency
            im = background

        im.convert("RGB").save(photo.replace("png", "jpg"), quality=95)
        newImg = photo.replace("png", "jpg")
        os.remove(photo)
        print("trasformed png to jpg")
        photo = newImg

    print(str(len(listImages)-1)+ " images left")
    print("Now Uploading this photo to instagram: " + photo)
    try:
        igapi.uploadPhoto(photo, caption=IGCaption, upload_id=None)
    except :
        print("unsupported format")
        error=True
    os.remove(photo)
    listImages = sorted([f for f in listdir(imagesFolder) if isfile(join(imagesFolder, f))])

    if str(len(listImages)) == "0":
        print("no images left")
        break
    if not error:
        print("Sleep upload for 1 hour")
        time.sleep(5400)

