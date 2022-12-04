from setuptools import setup

setup(
    name='pysnowflake',
    version='0.1.0',    
    description='A python package that makes it snow',
    url='https://github.com/danielw-mt/DSSS_5',
    author='Daniel Wagner',
    author_email='dan.wagner@fau.de',
    license='BSD 2-clause',
    packages=['snowflake'],
    install_requires=['turtle',
                      'numpy',                     
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
