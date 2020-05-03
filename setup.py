import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bk_packages", 
    version="0.0.1",
    author="byunghyun_kang",
    author_email="danjong99@gmail.com",
    description="A small python package which downsizes input scRNAseq matrix",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/danjong99/project_spring_2020",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',

)
