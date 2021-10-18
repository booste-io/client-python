from distutils.core import setup
import setuptools
setup(
  name = 'banana_dev',
  packages = ['banana_dev'],
  version = '0.0.1',
  license='MIT',
  description = 'The banana package is a python client to interact with your machine learning models hosted on Banana',   # Give a short description about your library
  author = 'Erik Dunteman',
  author_email = 'erik@banana.dev',
  url = 'https://www.banana.dev',
  keywords = ['Banana client', 'API wrapper', 'Banana', 'SDK'],
  setup_requires = ['wheel'],
  install_requires=[],
  classifiers=[
    'Development Status :: 4 - Beta',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)
