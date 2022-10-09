from setuptools import setup

setup(
    name='mathop',
    version='0.1.0',
    package_dir={'': 'src'},
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'mathop = mathop:cli',
        ],
    },
)