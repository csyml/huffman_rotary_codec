#encoding=utf-8
"""
Author:renyubin
Datetime:20201211
Function:image editing.
"""
import cv2
import numpy as np
from PIL import Image
from os import path
# Mirror conversion
def mirroring(img,mode):
    dir=path.split(img)[0]
    img=cv2.imread(img)
    img_shape=img.shape
    img_height=img_shape[0]
    img_width=img_shape[1]
    img_deep=img_shape[2]
    reflex_shape = (img_height, img_width, img_deep)
    reflex_img = np.zeros(reflex_shape, np.uint8)
    if mode =="reflex_right":
        for i in range(img_height):
            for j in range(img_width):
                reflex_img[i,img_width-1-j]=img[i,j]
        cv2.imwrite(dir+"/eflex_right.bmp",reflex_img)
        cv2.imshow("reflex_right_img",reflex_img)
        cv2.waitKey(0)
    elif mode=="reflex_down":
        for i in range(img_height):
            for j in range(img_width):
                reflex_img[img_height-i-1,j]=img[i,j]
        cv2.imwrite(dir+"/reflex_down.bmp",reflex_img)
        cv2.imshow("reflex_down_img",reflex_img)
        cv2.waitKey(0)
    elif mode=="reflex_cross":
        for i in range(img_height):
            for j in range(img_width):
                reflex_img[img_height-1-i,img_width-1-j]=img[i,j]
        cv2.imwrite(dir+"/reflex_cross.bmp",reflex_img)
        cv2.imshow("reflex_cross_img", reflex_img)
        cv2.waitKey(0)
    return


# color editing
def modify_color(img_name,target_img,target_hsv=None):
    if target_hsv is None:
        target_hsv = [60, 255, 124]
    img = cv2.imread(img_name)
    # The image is converted to HSV pixel space because HSV space is sensitive to color
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Set the thresholds of red and green in HSV color space
    lower_red = np.array([0, 43, 46])
    upper_red = np.array([10, 255, 255])

    # The inrange function is used to get the index of the target color in the image
    mask_red = cv2.inRange(hsv, lower_red, upper_red)
    img_target = np.copy(img)
    # Assign a value to the target pixel
    img_target[mask_red != 0] = target_hsv
    # cv2.imshow("img_target",img_target)
    # cv2.waitKey(0)
    cv2.imwrite(target_img, img_target)
    return

def portion_rotate(init_img,target_img,dev,area=(4, 10, 11, 12)):
    img=Image.open(init_img)
    img_matrix=np.array(img)
    print(img_matrix)
    inlay=img.crop(area).rotate(dev)
    img.paste(inlay, area)
    img.save(target_img)
    return



def main():
    init_img= "img_file/mahjong.bmp"
    path_ls = path.splitext(init_img)
    target_img=path_ls[0]+"_color_modify"+path_ls[1]
    color_green = [60, 255, 124]
    modify_color(init_img,target_img,color_green)


if __name__=="__main__":
    main()




































