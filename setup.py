import setuptools

setuptools.setup(
    name="cel_utils",
    version="0.1",
    author="Kiran Karra",
    author_email="kiran.karra@gmail.com",
    description="Useful Decorators and other utilies for every-day tasks",
    project_urls={
        "Documentation": "https://github.com/kkarrancsu/cel_utils",
        "Source": "https://github.com/kkarrancsu/cel_utils",
    },
    packages=setuptools.find_packages(),
    install_requires=["matplotlib"],
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)