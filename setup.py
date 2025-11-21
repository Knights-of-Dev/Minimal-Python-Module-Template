from setuptools import setup

setup(
    name='moduleName',
    version='0.1.0',    
    description='description here. each time you want to update your module, make sure the version above doesnt already exist!',
    url='GitHub Repo URL here',
    author='author. dont change the below if you dont want to get doxxed somehow. if your module uses only built-in ones, dont change install_requires please.',
    author_email='example@example.com',    
    license='MIT',
    packages=['moduleName'],
    install_requires=[],

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: Freeware',  
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Programming Language :: Python :: 3.14',
        'Programming Language :: Python :: 3.15'
    ],
)    
