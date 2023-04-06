from setuptools import setup, find_packages

exec(open("miniminiai/version.py").read())

setup(
    name="miniminiai",
    packages=find_packages(),
    version=__version__,
    license="MIT",
    description="A mini version of fastai's miniai",
    author="Johno Whitaker",
    url="https://github.com/johnowhitaker/miniminiai",
    long_description_content_type="text/markdown",
    keywords=[
        "artificial intelligence",
        "pytorch",
        "machine learning",
        "machine learning framework",
        "fastai",
    ],
    install_requires=[
        "torch",
        "fastcore",
        "fastprogress",
        "numpy",
        "matplotlib",
        "torcheval",
        "torchvision",
        "fastprogress",
        "einops",
        "accelerate",

    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
    ],
)