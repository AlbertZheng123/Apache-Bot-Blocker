from setuptools import setup, find_packages

setup(
    name="apache-bot-blocker",
    version="0.1.0",
    author="Albert Zheng",
    author_email="anpei.zheng@gmail.com",
    description="Bot Blocker in Apache/Firewall Layer",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/your-repo",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        # List your dependencies here
    ],
)