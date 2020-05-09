import setuptools

with open("README.md", "r") as file:
    long_description = file.read()

setuptools.setup(
    name="emojimeals-recipes-bl", # TODO: update name once first release is ready
    version="0.0.1", # TODO: source from git tag as part of CI
    author="Bernard Laveaux",
    author_email="bernard@laveaux.me",
    description="Crowdsourced list of emoji recipes.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/EmojiMeals/recipes",
    packages=['recipes'],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    python_requires='>=3.6',
)
