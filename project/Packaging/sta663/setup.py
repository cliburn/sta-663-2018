from distutils.core import setup

setup(name = "sta663",
      version = "1.0",
      author='Cliburn Chan',
      author_email='cliburn.chan@duke.edu',
      url='http://people.duke.edu/~ccc14/sta-663/',
      py_modules = ['sta663'],
      packages = ['pkg', 'pkg/sub1', 'pkg/sub2'],
      scripts = ['run_sta663.py']
      )
