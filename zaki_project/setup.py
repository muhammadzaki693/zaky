import setuptools

with open("zaki_project/README.md", "r") as fhandle:
    long_description = fhandle.read() # Your README.md file will be used as the long description!

setuptools.setup(
    name="zaki", # Put your username here!
    version="0.0.5", # The version of your package!
    author="muhammad zaky ramadhan", # Your name here!
    author_email="rzaki9353@gmail.com", # Your e-mail here!
    description="A small pack of function", # A short description here!
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/muhammadzaki693/zaky", # Link your package website here! (most commonly a GitHub repo)
    packages=setuptools.find_packages(), # A list of all packages for Python to distribute!
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ], # Enter meta data into the classifiers list!
    python_requires='>=3.6', # The version requirement for Python to run your package!
)
