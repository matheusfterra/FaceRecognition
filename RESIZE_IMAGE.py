import cv2
import os

#resize_img=False
#path='known_faces/Matheus'
#img='20200206_100455.jpg'

def resize(path,img):

	resize_img=False

	original_image = cv2.imread(os.path.join(path,img), cv2.IMREAD_UNCHANGED)

	image_width=original_image.shape[1]
	image_height=original_image.shape[0]
	relation=image_height/image_width

	print("Figura:{}\nAltura:{}\nLargura:{}".format(img,image_height,image_width))

	if image_height>600:
		fat=600/image_height
		image_height=600
		image_width=image_width*fat
		resize_img=True

	if image_width>600:
		fat=600/image_width
		image_width=600
		image_height=image_height*fat
		resize_img=True

	if resize_img==True:
		print("A nova altura é:{} e a nova largura é:{}".format(image_height,image_width))

		width = int(image_width)
		height = int(image_height)

		dsize = (width, height)

		output = cv2.resize(original_image, dsize)
		os.remove(os.path.join(path,img))

		cv2.imwrite(os.path.join(path,img),output) 

		new_image = cv2.imread(os.path.join(path,img),0)

		cv2.imshow(img,new_image)
		cv2.waitKey(0)
		cv2.destroyAllWindows()
	else:
		print("A imagem não necessita de redimensionamento!\n")