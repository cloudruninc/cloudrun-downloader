from setuptools import setup

setup(
    name='cloudrun-downloader',
    version='0.1.0',
    description='CLI tool to query Cloudrun forecasts and download output files',
    author='Cloudrun Inc.',
    author_email='hello@cloudrun.co',
    url='https://github.com/cloudruninc/cloudrun-downloader',
    packages=['cloudrun_downloader'],
    install_requires=['requests'],
    entry_points={'console_scripts': ['cloudrun-downloader = cloudrun_downloader.cli:cli']},
    license='MIT'
)
