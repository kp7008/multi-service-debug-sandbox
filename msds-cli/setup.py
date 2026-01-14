from setuptools import setup
setup(
    name='msds-cli',
    version='0.1.0-alpha',
    packages=['msds'],
    install_requires=['click>=8.0', 'pyyaml>=6.0', 'requests>=2.28', 'tabulate>=0.9.0'],
    entry_points={'console_scripts': ['msds=msds.main:cli']},
)