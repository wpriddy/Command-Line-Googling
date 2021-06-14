#%%
from setuptools import setup

setup(
    name='main',
    version='0.1',
    py_modules=['main'],
    install_requires=[
        'click'
    ],
    entry_points='''
        [console_scripts]
        search=main:main
    ''',
)
