from setuptools import setup, find_packages

setup(
    name='schedulizer',
    version='0.1.0',
    author='@thisishusseinali',
    author_email='thisishusseinali@outlook.com',
    description='A description of your project',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/thisishusseinali/schedulizer',
    packages=find_packages(),
    install_requires=[
        # List your project's dependencies here
        'dependency1',
        'dependency2',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

