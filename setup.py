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
    license='GNU GPLv3',
    author='Chintalagiri Shashank',
    author_email='chintal@quazartech.com',
    description='Helpers for LibreOffice integration with automated tools',
)
