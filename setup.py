from setuptools import setup, find_packages

with open('requirements.txt') as f:
    content = f.readlines()
requirements = [x.strip() for x in content if 'git+' not in x]

setup(
    name='GeoData-Engineering',
    version='0.1.0',
    author='Simon Hosny',
    author_email='simonhosny@laposte.net',
    description='This package gathers possible applications of data science applied to geotechnical engineering.',
    url='https://github.com/SmnHsn/GeoData-Engineering',
    packages=find_packages(exclude=['tests']),
    install_requires=requirements,
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
    ],
)
