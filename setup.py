import setuptools

setuptools.setup(name='pytest-cov',
                 version='1.7.0',
                 description='py.test plugin for coverage reporting with '
                 'support for both centralised and distributed testing, '
                 'including subprocesses and multiprocessing',
                 long_description=open('README.rst').read().strip(),
                 author='Marc Schlaich',
                 author_email='marc.schlaich@gmail.com',
                 url='https://github.com/schlamar/pytest-cov',
                 py_modules=['pytest_cov'],
                 install_requires=['py>=1.4.22',
                                   'pytest>=2.6.0',
                                   'cov-core>=1.14.0'],
                 entry_points={'pytest11': ['pytest_cov = pytest_cov']},
                 license='MIT License',
                 zip_safe=False,
                 keywords='py.test pytest cover coverage distributed parallel',
                 classifiers=['Development Status :: 4 - Beta',
                              'Intended Audience :: Developers',
                              'License :: OSI Approved :: MIT License',
                              'Operating System :: OS Independent',
                              'Programming Language :: Python',
                              'Programming Language :: Python :: 2.4',
                              'Programming Language :: Python :: 2.5',
                              'Programming Language :: Python :: 2.6',
                              'Programming Language :: Python :: 2.7',
                              'Programming Language :: Python :: 3.0',
                              'Programming Language :: Python :: 3.1',
                              'Topic :: Software Development :: Testing'])
