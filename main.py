
import cv2,time
from PIL import Image
import numpy as np
class Dishwasher:
	def __init__(self):
		self.rgb = (170,9,5)
		self.is_program_stopped = True
		self.preview = 0
		self.width = 240
		self.height = 320
		self.file_name = 'preview.jpg'
		self.hsv=0
		self.red = ((128,0,0),
 		(139,0,0),
 		(165,42,42),
 		(178,34,34),
 		(220,20,60),
 		(255,0,0),
 		(255,99,71),
 		(255,127,80))

	

	def isProgramStopped(self):
		cap = cv2.VideoCapture(0)
		ret,frame = cap.read()
		cv2.imwrite(self.file_name, frame)
		img = cv2.imread('preview.jpg')
		RED_MIN = np.array([160, 100, 100],np.uint8)
		RED_MAX = np.array([179, 255, 255],np.uint8)
		hsv_img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
		frame_threshed = cv2.inRange(hsv_img, RED_MIN, RED_MAX)
		cv2.imwrite('output2.jpg', frame_threshed)
		res = cv2.bitwise_and(img,img, mask= frame_threshed)
		if (res.any()):
			print("Wykryto czerwony")
			self.is_program_stopped = True
		else:	
			self.is_program_stopped = False
	
	
		
		
		
def main():
	print("Zmywaaarka")
	dishwasher = Dishwasher()
	while True:
		dishwasher.isProgramStopped()
		time.sleep(10)
	
if __name__ == "__main__":
	main()
   