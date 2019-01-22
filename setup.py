import os
from setuptools import setup, find_packages
try: # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError: # for pip <= 9.0.3
    from pip.req import parse_requirements

BASE_PATH = os.path.dirname(__file__)

install_reqs = parse_requirements(os.path.join(BASE_PATH, 'bs', 'requirements.txt'), session=False)
REQUIREMENTS = [str(ir.req) for ir in install_reqs]

with open(os.path.join(BASE_PATH, 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

VERSION = os.getenv('RELEASE_VERSION', '0.0.1')

setup(
    name='bs',
    version=VERSION,
    packages=find_packages(),  # include all packages under src
    #package_dir={'':'src'},   # tell distutils packages are under src
    package_data={
        # If any package contains *.txt files, include them:
        '': ['config.yml'],
        # And include any *.dat files found in the 'data' subdirectory
        # of the 'mypkg' package, also:
        # 'mypkg': ['data/*.dat'],
    },
    install_requires=REQUIREMENTS,
    license='MIT License',
    description='OpenShift Template Executor without the Blue Stuff',
    long_description=README,
    url='',
    author='Ross Crawford-d\'Heureuse',
    author_email='ross.crawford@mindcurv.com',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
    entry_points={'console_scripts': [
        'bs=bs.cli:bs',
    ], },
)