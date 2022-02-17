from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name = 'qm',
    version = '0.0.1',
    url = 'https://github.com/jungwon-moon/qm.git',
    py_modules = ['scraping', 'backtesting'],
    packages = find_packages(),
    classifiers=[
        "Programming Language :: python :: 3",
    ],
    install_requires = requirements,
)
