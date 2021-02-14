from setuptools import setup, find_packages
import pathlib
import os
import re
here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')

with open(os.path.join(here, "MalwareProxyX", "version.py")) as f:
    match = re.search(r'__version__ = "(.+?)"', f.read())
    assert match
    VERSION = match.group(1)

setup(
    name='malwareproxyx',
    version=VERSION,
    description='Real Time Malware Payload Injection In User Binary Downloads Utilising MITM Proxy',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/darshkpatel/MalwareProxyX',
    author='Darsh Patel',
    author_email='darshkpatel@gmail.com',
    classifiers=[
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Security',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
    ],
    keywords='mitmproxy, malware, security',
    packages=find_packages(where='.'),
    python_requires='>=3.6, <4',
    install_requires=['mitmproxy>=5.3.0'],
    extras_require={
        'test': ['coverage', 'pytest', 'flake8', 'check-manifest'],
    },
    entry_points={
        'console_scripts': [
            'malwareproxyx=MalwareProxyX:entrypoint',
        ],
    },
    project_urls={
        'Bug Reports': 'https://github.com/darshkpatel/MalwareProxyX/issues',
        'Say Thanks!': 'https://darshkpatel.com/',
        'Source': 'https://github.com/darshkpatel/MalwareProxyX/',
    },
)
