# PyTorch-HzProc
Created by [Hang Zhang](http://www.hangzh.com)

HzProc is a fast data augmentation toolbox supporting affine transformation with GPU backend. ([Torch version](https://github.com/zhanghang1989/HzProc) is also provide.) The name of "HzProc" means high speed image processing, where "Hz" (hertz) 
is the unit of frequency and "Proc" is abbreviation of processing. HZ is also the initial of the author. 

## Installation
- Install PyTorch from **source**
	* Install PyTorch from source to the `$HOME` directory, you can follow the [PyTorch tutorial](https://github.com/pytorch/pytorch#install-pytorch). 

- Install the package
	* Clone the repo
	```bash
	git clone git@github.com:zhanghang1989/PyTorch-Encoding-Layer.git && cd PyTorch-Encoding-Layer
	```
	* On Linux
	```bash
	python setup.py install
	```
	* On OSX
	```bash
	MACOSX_DEPLOYMENT_TARGET=10.9 CC=clang CXX=clang++ python setup.py install
	```
	
## Test & Demo
- Affine Transformation
```bash
python test/test.py
```
![](test/myimage.gif)
- This is an on-going project, will be added with more features when the author have time. Feel free to request any feature. 