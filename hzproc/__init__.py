##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## Created by: Hang Zhang
## ECE Department, Rutgers University
## Email: zhang.hang@rutgers.edu
## Copyright (c) 2017
##
## This source code is licensed under the MIT-style license found in the
## LICENSE file in the root directory of this source tree 
##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

import torch
import random
import math
from . import affine 
from .function import *

# ref torchvision.transform
class Compose(object):
	"""Composes several transforms together.
	Args:
		transforms (List[Transform]): list of transforms to compose.
	Example:
		>>> hzproc.Compose([
		>>>	 hzproc.CenterCrop(10),
		>>> ])
	"""
	def __init__(self, transforms):
		self.transforms = transforms

	def __call__(self, img):
		for t in self.transforms:
			img = t(img)
		return img

class RandomAffine(object):
	def __init__(self, sh, deg, sc, asp, fast=False):
		self.sh  = sh
		self.deg = deg
		self.sc  = sc
		self.asp = asp
		self.mapping = AffineTransform(fast)

	def __call__(self, img):
		# shearing and rotate
		shx = random.uniform(-0.5, 0.5)*self.sh
		shy = random.uniform(-0.5, 0.5)*self.sh
		theta  = random.uniform(- 0.5, 0.5) * self.deg * math.pi / 180
		# scaling params
		scale  = random.uniform(1.0, self.sc)
		aspect = random.uniform(1/self.asp, self.asp)
		scx = math.sqrt(scale * aspect)
		scy = math.sqrt(scale / aspect)
		# affine matrix
		mat = affine.Identity()
		mat = mat @ affine.ScaleArround(scx, scy, img.size(2)/2, 
										img.size(1)/2)
		mat = mat @ affine.ShearArround(shx, shy, img.size(2)/2, 
										img.size(1)/2)
		mat = mat @ affine.RotateArround(theta, img.size(2)/2, 
										img.size(1)/2)
		mat = mat.cuda()
		return self.mapping(img, mat)
		
