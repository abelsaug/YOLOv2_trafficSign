# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 14:55:43 2015

This script is to convert the txt annotation files to appropriate format needed by YOLO 

@author: Guanghan Ning
Email: gnxr9@mail.missouri.edu
"""
"""
Modifications for GTSDB by @author Abel Augustine
"""

import os
from os import walk, getcwd
from PIL import Image


def convert(size, box):
    dw = 1./size[0]
    dh = 1./size[1]
    x = (box[0] + box[1])/2.0
    y = (box[2] + box[3])/2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)


# """ Configure Paths"""   
outpath = "FullIJCNN2013/"

txt_file =  open("FullIJCNN2013/gt.txt", "r")
lines = txt_file.read().split('\n')
ct = 0
print len(lines)
for line in lines:
# """ Open output text files """
    lineParts = line.split(';')
    if lineParts[0] == "":
        continue
    print lineParts
    if int(lineParts[5])>9:
        txt_outpath = outpath +  lineParts[0].strip(".ppm")+".txt"
    else:
        txt_outpath = outpath + lineParts[0].strip(".ppm")+".txt"
    print("Output:" + txt_outpath)
    txt_outfile = open(txt_outpath, "a")

    cls_id = lineParts[5]
# """ Convert the data to YOLO format """
    ct = ct + 1
    elems = lineParts
    xmin = elems[1]
    ymin = elems[2]
    xmax = elems[3]
    ymax = elems[4]

    img_path = str('FullIJCNN2013/%s'%(elems[0]))
    im=Image.open(img_path)
    w= int(im.size[0])
    h= int(im.size[1])
    b = (float(xmin), float(xmax), float(ymin), float(ymax))
    bb = convert((w,h), b)

    print(bb)
    # im.save('FullIJCNN2013/%s'%(elems[0].strip(".ppm")+".JPEG"))
    txt_outfile.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')
