from setuptools import setup, find_packages

setup(
    name='covid_analysis',
    version='1.0.0',
    author='Firasath ali mohammes. Afnan faaz mohammed. Abdul sameer mohammed',
    author_email='fmohamm1@mail.yu.edu. amohamm7@mail.yu.edu. amohamm8@mail.yu.edu',
    description='A package for analyzing COVID-19 data',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Firasathalimohammed/COVID',
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
