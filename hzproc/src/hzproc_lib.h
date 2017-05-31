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

/*
#include <THC/THC.h>

#define HzProc_(NAME)    TH_CONCAT_4(HzProc_, Real, _, NAME)
#define THCTensor        TH_CONCAT_3(TH,CReal,Tensor)
#define THCTensor_(NAME) TH_CONCAT_4(TH,CReal,Tensor_,NAME)

#include "generic/hzproc_generic.h"
#include "THC/THCGenerateFloatType.h"
*/

/*
 * hzproc_affine_kernel.cu
 */
int HzProc_Float_affine_fast(THCudaTensor *input_, THCudaTensor *output_,
			THCudaTensor *matrix_);

int HzProc_Float_affine_bili(THCudaTensor *input_, THCudaTensor *output_, 
			THCudaTensor *matrix_);
/*
 * hzproc_crop_kernel.cu
 */
int HzProc_Float_crop_fast(THCudaTensor *input_, THCudaTensor *output_, 
			int xi, int yi, int xo, int yo);

int HzProc_Float_crop_bili(THCudaTensor *input_, THCudaTensor *output_,	
			int xi, int yi, int xo, int yo);

int HzProc_Float_crop_pad(THCudaTensor *input_, THCudaTensor *output_,
							int xi, int yi, int pad);

int HzProc_Float_flip(THCudaTensor *input_, THCudaTensor *output_);
