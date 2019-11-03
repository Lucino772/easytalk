import setuptools

with open('README.md','r') as f:
    long_description = f.read()

setuptools.setup(
    name="easytalk",
    version="0.1",
    author="Lucino772",
    author_email="lucapalmi772@gmail.com",
    description="Easy communication between everything !!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # url="https://github.com/Lucino772/service_lib",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)