from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="nesa-portfolio-builder",
    version="0.1.0",
    author="NESA Stage 6 IT Multimedia",
    description="A tool to help students create and manage their IT Multimedia portfolios",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/nesa-portfolio-builder",
    packages=find_packages(),
    package_data={
        'app': ['templates/*', 'data/*'],
    },
    install_requires=[
        'google-generativeai>=0.3.0',
        'python-dotenv>=0.19.0',
        'typing-extensions>=4.0.0',
    ],
    entry_points={
        'console_scripts': [
            'nesa-portfolio=app.__main__:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
