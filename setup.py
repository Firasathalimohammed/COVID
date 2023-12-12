from setuptools import setup, find_packages

setup(
    name='covid_analysis',
    version='1.0.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A package for analyzing COVID-19 data',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/covid_analysis',
    packages=find_packages(),
    install_requires=[
        'pandas>=1.1.5',
        'matplotlib>=3.3.3',
        'seaborn>=0.11.0',
        'scikit-learn>=0.23.2',
        'beautifulsoup4>=4.9.3',
        'requests>=2.25.0',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.6',
)
