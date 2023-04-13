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

Tutorial 1 has a minimal example of fitting a model using miniminiai - open it in Google colab [here](https://colab.research.google.com/github/johnowhitaker/miniminiai/blob/main/tutorial_01.ipynb). 

Tutorial 2 shows callbacks in action on a slightly more complex task - open it in Google colab [here](https://colab.research.google.com/github/johnowhitaker/miniminiai/blob/main/tutorial_02.ipynb). 


An example of the library in action: [this notebook](https://colab.research.google.com/drive/1b3CeZB2FfRGr5NPYDVvk34hyZFBtgub5?usp=sharing) shows how to train a diffusion model on spectrograms to generate birdcalls, using miniminiai. It is covered in the final lesson of Part 2 of the FastAI course.

And a lovely demo of use in the wild is [this report by Thomas Capelle](https://wandb.ai/capecape/miniai_ddpm/reports/Next-Frame-Prediction-Using-Diffusion-The-fastai-Approach--VmlldzozMzcyMTYy) where he uses diffusion models to predict the next frame of an image sequence.