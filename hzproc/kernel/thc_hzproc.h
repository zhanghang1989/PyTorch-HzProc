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
#include <THC/THC.h>
#include "THCDeviceTensor.cuh"
#include "THCDeviceTensorUtils.cuh"

// this symbol will be resolved automatically from PyTorch libs
extern THCState *state;

#define HzProc_(NAME) TH_CONCAT_4(HzProc_, Real, _, NAME)
#define THCTensor        TH_CONCAT_3(TH,CReal,Tensor)
#define THCTensor_(NAME) TH_CONCAT_4(TH,CReal,Tensor_,NAME)

#ifdef __cplusplus
extern "C" {
#endif

#include "generic/hzproc_kernel.h"
#include "THC/THCGenerateFloatType.h"

#ifdef __cplusplus
}
#endif
