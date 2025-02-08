"""Setup script for the calculator project."""
from setuptools import setup, find_packages

setup(
    name="calculator-project",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        # List your project's dependencies here
    ],
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "pytest-cov>=4.1.0",
            "black>=23.7.0",
            "flake8>=6.1.0",
            "mypy>=1.4.1",
            "pre-commit>=3.3.3",
        ],
    },
    python_requires=">=3.9",
)
