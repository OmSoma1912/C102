import cv2
import dropbox
import time
import random

start_time = time.time()

def take_snapshot():
    number = random.randint(0, 100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    
    while(result):
        ret, frame = videoCaptureObject.read()
        img_name = "img" + str(number) + ".png"
        cv2.imwrite(img_name, frame)
        start_time = time.time()
        result = False

    return img_name
    print("Picture Taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def upload_snapshot(img_name):
    access_token = "sl.AsAPb5jDzKUhbUgYoHB1J4v8eSogt06upTuUT1xLcIeZW-Vz89ogLWeLtzo8f0k6mp_sInci1vnVdgpfbjX3wFU-AYS8Vg2a8nBWNUx6VwIvF9uIIJHxsev7ctach11M6sFfShk"
    file = img_name
    file_from = file
    file_to = "/test/" + (img_name)
    dbx = dropbox.Dropbox(access_token)
    
    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to, mode = dropbox.files.WriteMode.overwrite)
        print("File Uploaded")

def main():
    while(True):
        if((time.time() - start_time) >= 5):
            name = take_snapshot()
            upload_snapshot(name)

main()