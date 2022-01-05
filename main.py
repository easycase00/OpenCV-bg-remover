import cv2
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import os

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
segmentor = SelfiSegmentation()
fpsReader = cvzone.FPS()
imgBg= cv2.imread("Images/1.jpg")

listImg= os.listdir("Images")
print(listImg)
imgList= []
for imgPath in listImg:
    img = cv2.imread(f'Images/{imgPath}')
    imgList.append(img)
print(len(imgList))

indexImg = 0


while True:
    success,  img = cap.read()
    imgOut= segmentor.removeBG(img,imgList[indexImg], threshold=0.3)

    imgStacked= cvzone.stackImages([img, imgOut],2,1)
    fps, imgStacked = fpsReader.update(imgStacked)
    print((indexImg))

    cv2.imshow("Image", imgStacked)

    key= cv2.waitKey(1)
    if key == ord('a'):
        if indexImg>0:
            indexImg -=1
    elif key == ord('d'):
        if indexImg < len(imgList)-1:
            indexImg +=1
    elif key == ord('q'):
        break