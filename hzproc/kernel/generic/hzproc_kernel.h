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
#define THC_GENERIC_FILE "generic/hzproc_kernel.h"
#else

void HzProc_(Affine_Fast)(THCState *state, THCTensor *input_, 
							THCTensor *output_, THCTensor *matrix_);
void HzProc_(Affine_Bili)(THCState *state, THCTensor *input_, 
							THCTensor *output_, THCTensor *matrix_);
void HzProc_(Crop_Fast)(THCState *state, THCTensor *input_, THCTensor 
							*output_, int xi, int yi, int xo, int yo);
void HzProc_(Crop_Bili)(THCState *state, THCTensor *input_, THCTensor 
							*output_,	int xi, int yi, int xo, int yo);
void HzProc_(Crop_Pad)(THCState *state, THCTensor *input_, THCTensor 
							*output_,	int xi, int yi, int pad);
void HzProc_(Flip)(THCState *state, THCTensor *input_, THCTensor *output_);


#endif
