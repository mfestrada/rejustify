from setuptools import setup
setup(
    name = 'rejustify',
    version = '0.0.1',
    packages = ['rejustify'],
    zip_safe = False,
    entry_points = {
        'console_scripts': [
            'rejustify = rejustify.__main__:main'
        ]
    })
