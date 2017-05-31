##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## Created by: Hang Zhang
## ECE Department, Rutgers University
## Email: zhang.hang@rutgers.edu
## Copyright (c) 2017
##
## This source code is licensed under the MIT-style license found in the
## LICENSE file in the root directory of this source tree 
##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

import math
import torch

def Identity():
	t = []
	t += [[1, 0, 0]]
	t += [[0, 1, 0]]
	t += [[0, 0, 1]]
	return torch.Tensor(t)

def Scale(sx, sy):
	t = []
	t += [[sx,  0,  0]]
	t += [[ 0, sy,  0]]
	t += [[ 0,  0,  1]]
	return torch.Tensor(t)

def Shift(tx, ty):
	t = []
	t += [[1, 0, tx]]
	t += [[0, 1, ty]]
	t += [[0, 0,  1]]
	return torch.Tensor(t)
	
def Rotate(theta):
	t = []
	t += [[ math.cos(theta), math.sin(theta), 0]]
	t += [[-math.sin(theta), math.cos(theta), 0]]
	t += [[               0,               0, 1]]
	return torch.Tensor(t)
	
def Shear(shx, shy):
	t = []
	t += [[  1, shx, 0]]
	t += [[shy,   1, 0]]
	t += [[  0,   0, 1]]
	return torch.Tensor(t)
	
def ScaleArround(sx, sy, x, y):
	return Shift(x, y) @ Scale(sx, sy) @ Shift(-x, -y)

def RotateArround(theta, x, y):
	return Shift(x, y) @ Rotate(theta) @ Shift(-x, -y)

def ShearArround(shx, shy, x, y):
	return Shift(x, y) @ Shear(shx, shy) @ Shift(-x, -y)

