from distutils.core import setup
import setuptools
setup(
  name = 'banana_dev',
  packages = ['banana_dev'],
  version = '2.0.0',
  license='MIT',
  description = 'The banana package is a python client to interact with your machine learning models hosted on Banana',   # Give a short description about your library
  author = 'Erik Dunteman',
  author_email = 'erik@banana.dev',
  url = 'https://www.banana.dev',
  keywords = ['Banana client', 'API wrapper', 'Banana', 'SDK'],
  setup_requires = ['wheel'],
  install_requires=[
    "certifi==2021.10.8",
    "charset-normalizer==2.0.7",
    "idna==3.3",
    "requests==2.26.0",
    "urllib3==1.26.7",
  ],
  classifiers=[
    'Development Status :: 5 - Production/Stable',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)
