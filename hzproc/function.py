##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## Created by: Hang Zhang
## ECE Department, Rutgers University
## Email: zhang.hang@rutgers.edu
## Copyright (c) 2017
##
## This source code is licensed under the MIT-style license found in the
## LICENSE file in the root directory of this source tree 
##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

from ._ext import hzproc_lib
from torch.autograd import Function

class AffineTransform:
	def __init__(self, fast=False):
		if fast:
			self.affine = hzproc_lib.HzProc_Float_affine_fast
		else:
			self.affine = hzproc_lib.HzProc_Float_affine_bili

	def __call__(self,input, matrix):
		output = input.new().resize_as_(input)
		self.affine(input, output, matrix)
		return output

class CropScale:
	def __init__(self, fast=False):
		if fast:
			self.function = hzproc_lib.HzProc_Float_crop_fast
		else:
			self.function = hzproc_lib.HzProc_Float_crop_bili

	def __call__(self, input, x1, y1, width, height, x2=None, y2=None):
		output = input.new().resize(input.size(0), height, width)
		if x2 is None or y2 is None:
			x2 = x1 + width
			y2 = y2 + height
		self.function(input, output, x1, y1, x2, y2)
		return output
	
class PadCrop():
	def __call__(self, input, x1, y1, width, height, pad):
		output = input.new().resize(input.size(0), height, width)
		hzproc_lib.HzProc_Float_crop_pad(input, output, x1, y1, pad)
		return output
	
class HorizontalFlip(Function):
	def __call__(input):
		output = input.new().resize_as_(input)
		hzproc_lib.HzProc_Float_flip(input, output)
		return output
	
