from setuptools import setup

setup(
    name='sofficehelpers',
    version='0.1',
    packages=['sofficehelpers'],
    entry_points={
        'console_scripts': [
            'ssconverter = sofficehelpers.ssconverter:main'
        ]
    },
    url='http://www.quazartech.com/',
    license='GNU LGPLv2.1+',
    author='Chintalagiri Shashank',
    author_email='shashank@chintal.in',
    description='Helpers for LibreOffice integration with automated tools',
)
