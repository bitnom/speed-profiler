from setuptools import setup, find_packages

VERSION = '0.0.4'

long_description = open('README.md', encoding='utf-8').read()

setup(
    name='speed-profiler',
    version=VERSION,
    description='Accurate speed profiler for Python code using perf_counter.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/TensorTom/speed-profiler',
    author='TensorTom',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='profiler,speed',
    packages=find_packages(),
)
