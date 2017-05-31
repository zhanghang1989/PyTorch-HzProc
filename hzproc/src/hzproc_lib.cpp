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
#include <thc_hzproc.h>

extern THCState *state;

#ifdef __cplusplus
extern "C" {
#endif

#include "generic/hzproc_generic.c"
#include "THC/THCGenerateFloatType.h"

#ifdef __cplusplus
}
#endif
