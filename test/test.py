##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## Created by: Hang Zhang
## ECE Department, Rutgers University
## Email: zhang.hang@rutgers.edu
## Copyright (c) 2017
##
## This source code is licensed under the MIT-style license found in the
## LICENSE file in the root directory of this source tree 
##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

import os
import cv2
import numpy as np
from PIL import Image

import torch
import hzproc

def tensor_load_rgbimage(filename, size=None, scale=None, keep_asp=False):
	img = Image.open(filename).convert('RGB')
	if size is not None:
		if keep_asp:
			size2 = int(size * 1.0 / img.size[0] * img.size[1])
			img = img.resize((size, size2), Image.ANTIALIAS)
		else:
			img = img.resize((size, size), Image.ANTIALIAS)

	elif scale is not None:
		img = img.resize((int(img.size[0] / scale), int(img.size[1] / scale)),
			Image.ANTIALIAS)
	img = np.array(img).transpose(2, 0, 1)
	img = torch.from_numpy(img).float()
	return img


def tensor_to_bgrimage(img):
	(b, g, r) = torch.chunk(img, 3)
	img = torch.cat((r, g, b))
	img = img.numpy().transpose(1, 2, 0).astype('uint8')
	return img
	
	

def test():
	simg = tensor_load_rgbimage('test/lena.jpg')
	transform = hzproc.Compose([
		hzproc.RandomAffine(0.4, 20, 12, 1.25,fast=False),
	])
	simg = simg.cuda()
	
	idx = 0
	while True:
		idx += 1
		img = transform(simg).cpu()
		img = tensor_to_bgrimage(img)
		cv2.imshow('HzProc Demo', img)
		cv2.imwrite('demo/%i.jpg'%idx,img)
		key = cv2.waitKey(150)
		if key == 27:
			break
	cv2.destroyAllWindows()
	

if __name__ == "__main__":
	test()
