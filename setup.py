from distutils.core import setup
setup(
  name = 'pykemo',
  packages = ['pykemo'],
  version = 'v1.0.0',
  license='MIT',
  description = 'make a Fuzzy C-Means Clustering model in just 1 line of code ',
  author = 'kareem negm ',
  author_email = 'eng.kareem.negm@gmail.com',
  url = 'https://github.com/Kareem-negm',
  download_url = 'https://github.com/Kareem-negm/pykemo/archive/refs/tags/v1.0.0.tar.gz',
  keywords = ['fuzzy', 'clustering', 'machine learning', 'fuzzy c-means'],
  install_requires=[
          'numpy',  # for the matrix operations
          'pandas',  # for the dataframe operations'
          'matplotlib',  # for the plotting operations
          'random'  # for the random operations'
          'sys'  # for the system operations''
          ],
  classifiers=[  # Optional
    # How mature is this project? Common values are
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable
    'Development Status :: 3 - Alpha',

    # Indicate who your project is intended for
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',

    # Pick your license as you wish
    'License :: OSI Approved :: MIT License',

    # Specify the Python versions you support here. In particular, ensure
    # that you indicate whether you support Python 2, Python 3 or both.
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)