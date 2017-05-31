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
import torch
import platform
import subprocess
from torch.utils.ffi import create_extension

lib_path = os.path.join(os.path.dirname(torch.__file__), 'lib')
this_file = os.path.dirname(os.path.realpath(__file__))

# build kernel library
os.environ['TORCH_BUILD_DIR'] = lib_path
if platform.system() == 'Darwin':
	os.environ['TH_LIBRARIES'] = os.path.join(lib_path,'libTH.1.dylib')
	os.environ['THC_LIBRARIES'] = os.path.join(lib_path,'libTHC.1.dylib')
	HZPROC_LIB = os.path.join(lib_path, 'libHZPROC.dylib')
else:
	os.environ['TH_LIBRARIES'] = os.path.join(lib_path,'libTH.so.1')
	os.environ['THC_LIBRARIES'] = os.path.join(lib_path,'libTHC.so.1')
	HZPROC_LIB = os.path.join(lib_path, 'libHZPROC.so')

build_all_cmd = ['bash', 'hzproc/make.sh']
if subprocess.call(build_all_cmd, env=dict(os.environ)) != 0:
	sys.exit(1)

sources = ['hzproc/src/hzproc_lib.cpp']
headers = ['hzproc/src/hzproc_lib.h']
defines = [('WITH_CUDA', None)]
with_cuda = True 

include_path = [os.path.join(lib_path, 'include'),
								os.path.join(os.environ['HOME'],'pytorch/torch/lib/THC'), 
								os.path.join(lib_path,'include/HZPROC'), 
								os.path.join(this_file,'hzproc/src/')]

def make_relative_rpath(path):
	if platform.system() == 'Darwin':
		return '-Wl,-rpath,' + path
	else:
		return '-Wl,-rpath,' + path

ffi = create_extension(
	'hzproc._ext.hzproc_lib',
	package=True,
	headers=headers,
	sources=sources,
	define_macros=defines,
	relative_to=__file__,
	with_cuda=with_cuda,
		include_dirs = include_path,
		extra_link_args = [
			make_relative_rpath(lib_path),
			HZPROC_LIB,
		],
)

if __name__ == '__main__':
    ffi.build()
