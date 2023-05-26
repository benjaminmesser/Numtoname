from distutils.core import setup
setup(
  name = 'Numtoname',         # How you named your package folder (MyLib)
  packages = ['Numtoname'],   # Chose the same as "name"
  version = '0.1',
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'A python module to convert a number or list of numbers into a variable name or list of variable names',
  author = 'Ben Messer',
  author_email = 'benjamin.messer@outlook.com',
  url = 'https://github.com/benjaminmesser/Numtoname',
  download_url = 'https://github.com/benjaminmesser/Numtoname/archive/v_01.tar.gz',
  keywords = ['tools', 'development', 'naming'],
  install_requires=[],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
  ],
)
