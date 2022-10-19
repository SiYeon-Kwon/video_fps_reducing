import numpy as np
from cv2 import VideoWriter, VideoWriter_fourcc
import os
import glob
import cv2
from pprint import pprint
import sys,os
from datetime import datetime

import datetime

strt_time = datetime.datetime.now()


FPS =30
seconds =1


cwd = os.getcwd()
input_dir = os.path.join(cwd,r'/home/kwon/compression/image_cjfl/')

def color_gray(input_dir):
    


    data_path = os.path.join(input_dir,'*.jpg')
    files = glob.glob(data_path)
    RGB=[]

    for f1 in sorted(files):
        RGB = cv2.imread(f1)
        h=RGB.shape

         
    output_dir=input_dir
    videoheight=h[0]

    videowidth=h[1]
 
   
    out_videoname='se'
    video_outputname=output_dir+"/"+out_videoname+'.mp4'
    video_out = os.path.join(output_dir, video_outputname)
######################################################################v##########################  
    files =  glob.glob(data_path)
    file_count = len(files)
    out = cv2.VideoWriter(video_out,cv2.VideoWriter_fourcc(*'MP4V'), float(FPS), (videowidth,videoheight))
    for f1 in sorted(files,key=os.path.getctime):
        print(f1)
        RGB = cv2.imread(f1)          
        out.write(RGB)

    out.release()

## Main Function 
color_gray(input_dir)

