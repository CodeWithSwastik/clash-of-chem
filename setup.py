import setuptools


# The full version, including alpha/beta/rc tags
# with open("clash_of_chem/__init__.py", "r", encoding="utf-8") as f:
#     __version__ = (
#             re.search(
#                 r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE
#             ).group(1)
#             or ""
#     )

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name="temp",  # Name TBD to avoid name-squatting
    version="0.0.1",
    author="Swas.py",
    author_email="cwswas.py@gmail.com",
    description="It's Clash of Code, but Organic Chemistry",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CodeWithSwastik/clash-of-chemists",
    download_url="https://github.com/CodeWithSwastik/clash-of-chemists/releases",
    packages=setuptools.find_packages(exclude=["tests*", "build.py"]),
    include_package_data=True,
    classifiers=[
        "Environment :: Console",
        "Topic :: Scientific/Engineering :: Chemistry",
        "Development Status :: 2 - Pre-Alpha"
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    license="MIT",
    project_urls={
        "Source": "https://github.com/CodeWithSwastik/clash-of-chemists",
        "Tracker": "https://github.com/CodeWithSwastik/clash-of-chemists/issues",
    },
    scripts=[
        "bin/coc",
    ],
)
