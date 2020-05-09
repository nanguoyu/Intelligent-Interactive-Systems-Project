"""
@File : setup.py
@Author: Dong Wang
@Date : 2020/5/4
"""

import setuptools

setuptools.setup(
    name='RPSLSPlayer',
    version='0.1.1',
    description='The project of group 6 for 1MD032 at Uppsala University, 2020 VT.',
    url='https://github.com/nanguoyu/Intelligent-Interactive-Systems-Project',
    license='MIT',
    author='Dong Wang (nanguoyu)',
    author_email='admin@nanguoyu.com',
    maintainer='Dong Wang (nanguoyu)',
    maintainer_email='admin@nanguoyu.com',
    packages=setuptools.find_packages(),
    install_requires=['numpy', 'matplotlib'],
    setup_requires=["numpy>=1.14.0"],
    python_requires='>=3.6'
)
