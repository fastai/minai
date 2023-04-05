# miniminiai

The mini version of fastai's miniai PyTorch framework created during the fastai course 2022-2023.

## Installation

```bash
pip install miniminiai
```

or to install from source clone this repo and run:

```bash
pip install -e .
```

## Usage

This is still a work in progress - I'll add example usage soon. But in general, for examples from the course where you have `from miniai.something import X` you should be able to do `from miniminiai import X`. You can do `import miniminiai as mi` or even `from miniminiai import *` for quick access to all the functions and things, if you're so inclined. 

An example of the library in action: [this notebook](https://colab.research.google.com/drive/1b3CeZB2FfRGr5NPYDVvk34hyZFBtgub5?usp=sharing) shows how to train a diffusion model on spectrograms to generate birdcalls, using miniminiai. It is covered in the final lesson of Part 2 of the FastAI course.