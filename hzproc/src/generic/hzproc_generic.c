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
#define THC_GENERIC_FILE "generic/hzproc_generic.c"
#else

/*
 * hzproc_affine_kernel.cu
 */
int HzProc_(affine_fast)(THCTensor *input_, THCTensor *output_,
			THCTensor *matrix_)
{
	HzProc_(Affine_Fast)(state, input_, output_, matrix_);
	return 0;
}

int HzProc_(affine_bili)(THCTensor *input_, THCTensor *output_, 
			THCTensor *matrix_)
{
	HzProc_(Affine_Bili)(state, input_, output_, matrix_);
	return 0;
}
/*
 * hzproc_crop_kernel.cu
 */
int HzProc_(crop_fast)(THCTensor *input_, THCTensor *output_, 
			int xi, int yi, int xo, int yo)
{
	HzProc_(Crop_Fast)(state, input_, output_, xi, yi, xo, yo);
	return 0;
}

int HzProc_(crop_bili)(THCTensor *input_, THCTensor *output_,	
			int xi, int yi, int xo, int yo)
{
	HzProc_(Crop_Bili)(state, input_, output_, xi, yi, xo, yo);
	return 0;
}

int HzProc_(crop_pad)(THCTensor *input_, THCTensor *output_,
							int xi, int yi, int pad)
{
	HzProc_(Crop_Pad)(state, input_, output_, xi, yi, pad);
	return 0;
}

int HzProc_(flip)(THCTensor *input_, THCTensor *output_)
{
	HzProc_(Flip)(state, input_, output_);
	return 0;
}

#endif
