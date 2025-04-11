from setuptools import setup, find_packages

# Define the main package information
NAME = "calibration"
VERSION = "0.1.0"
DESCRIPTION = "A brief description of your package."
LONG_DESCRIPTION = """
A longer description of your package that provides more context about what it does.
"""
AUTHOR = "Your Name"
AUTHOR_EMAIL = "your.email@example.com"
URL = "https://github.com/yourusername/your_package_name"

# Define the required dependencies
# REQUIREMENTS = [
#     "numpy>=1.21.0",
#     "pandas>=1.3.0",
#     "requests>=2.25.0",
# ]


# Run the setup function
setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",  # If using Markdown for long description
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    packages=find_packages(),  # Automatically discover all packages
    # install_requires=REQUIREMENTS,
    python_requires=">=3.8",  # Specify the minimum Python version required
    include_package_data=True,  # Include non-code files specified in MANIFEST.in
    license="MIT",  # Specify the license under which your package is distributed
)