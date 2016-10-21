from setuptools import setup


setup(
    name='soccer-hack',
    version='0.0.1',
    description='A library for dealing with soccer data',
    author='Kenta Muramatsu',
    author_email='ohmurakendev@gmail.com',
    url = 'https://github.com/ohmuraken/soccer-hack',
    platforms = 'any',
    entry_points='',
    packages=['sh'],
    package_dir={'nutritionlib':'sh'},
    package_data={'nutritionlib':['sh/data']},
    install_requires=['pandas', 'numpy'],
    license='MIT',
    classifiers=[
        'Operating System :: OS Independent',
        'Environment :: Console',
        'Programming Language :: Python :: 3.5',
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: CGI Tools/Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities'
    ]
)
