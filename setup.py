from distutils.core import setup

setup(
    name='NearDuplicatesDetection',
    version='0.2.0',
    author='Parker Moore',
    author_email='parkrmoore@gmail.com',
    packages=['ndd', 'ndd.unit'],
    url='https://github.com/parkr/near-dup-detection',
    license='LICENSE.txt',
    description='Identifies near-duplicates in a corpus',
    long_description=open('README.markdown').read()
)
