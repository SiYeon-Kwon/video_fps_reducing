import cv2
vidcap = cv2.VideoCapture('/home/kwon/compression/data/hanriver.mp4')
success,image = vidcap.read()
count = 0
success = True
while success:
  success,image = vidcap.read()
  cv2.imwrite("/home/kwon/compression/image/%d.jpg" % count, image)     # save frame as JPEG file
  if cv2.waitKey(10) == 27:                     # exit if Escape is hit
      break
  count += 1