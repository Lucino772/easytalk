import setuptools

with open('README.md','r') as f:
    long_description = f.read()

setuptools.setup(
    name="easytalk",
    version="1.0",
    author="Lucino772",
    author_email="lucapalmi772@gmail.com",
    description="Easy communication between socket and sub-process",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Lucino772/easytalk",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
