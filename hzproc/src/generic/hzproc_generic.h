/*+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 * Created by: Hang Zhang
 * ECE Department, Rutgers University
 * Email: zhang.hang@rutgers.edu
 * Copyright (c) 2017
 *
 * This source code is licensed under the MIT-style license found in the
 * LICENSE file in the root directory of this source tree 
 *+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 */
#ifndef THC_GENERIC_FILE
#define THC_GENERIC_FILE "generic/encoding_generic.h"
#else

/*
 * hzproc_affine_kernel.cu
 */
int HzProc_(affine_fast)(THCTensor *input_, THCTensor *output_,
			THCTensor *matrix_);

int HzProc_(affine_bili)(THCTensor *input_, THCTensor *output_, 
			THCTensor *matrix_);
/*
 * hzproc_crop_kernel.cu
 */
int HzProc_(crop_fast)(THCTensor *input_, THCTensor *output_, 
			int xi, int yi, int xo, int yo);

int HzProc_(crop_bili)(THCTensor *input_, THCTensor *output_,	
			int xi, int yi, int xo, int yo);

int HzProc_(crop_pad)(THCTensor *input_, THCTensor *output_,
							int xi, int yi, int pad);

int HzProc_(flip)(THCTensor *input_, THCTensor *output_);

#endif
