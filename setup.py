"""
picasa
----------

picasa-downloader is a script that automatically downloads all images from a Picasa Web Album.
"""

from setuptools import setup, find_packages

setup(
    name='picasa-downloader',
    version='0.1',
    author='Kunal Mehta',
    author_email='legoktm@gmail.com',
    packages=find_packages(),
    url='https://github.com/legoktm/picasa/',
    license='MIT License',
    description='A script that automatically downloads all images from a Picasa Web Album.',
    long_description=open('README').read(),
    install_requires=open('requirements.txt').read().split("\n"),
    package_data={
        '': ['*.txt', '*.md']
    },
    classifiers=[
      'License :: OSI Approved :: MIT License',
      'Operating System :: MacOS :: MacOS X',
      'Operating System :: Microsoft :: Windows',
      'Operating System :: POSIX',
      'Intended Audience :: End Users/Desktop',
      'Environment :: Console',
      'Programming Language :: Python',
    ],
    entry_points = {
        'console_scripts': [
            'picasa = picasa:main'
        ],
    }
)
