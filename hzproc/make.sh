#!/usr/bin/env bash

mkdir -p hzproc/build && cd hzproc/build
# compile and install
cmake ..
make install
cd ..
