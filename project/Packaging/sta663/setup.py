from setuptools import setup

setup(name = "sta663-cliburn",
      version = "1.0",
      author='Cliburn Chan',
      author_email='cliburn.chan@duke.edu',
      url='http://people.duke.edu/~ccc14/sta-663-2018/',
      py_modules = ['sta663'],
      packages=setuptools.find_packages(),
      scripts = ['run_sta663.py'],
      python_requires='>=3',
      )