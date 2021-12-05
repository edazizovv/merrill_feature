#
import setuptools
from setuptools import setup


metadata = {'name': 'merrill_feature',
            'maintainer': 'Edward Azizov',
            'maintainer_email': 'edazizovv@gmail.com',
            'description': 'A set of feature engineering tools',
            'license': 'MIT',
            'url': 'https://github.com/edazizovv/merrill_feature',
            'download_url': 'https://github.com/edazizovv/merrill_feature',
            'packages': setuptools.find_packages(),
            'include_package_data': True,
            'version': '0.1',
            'long_description': '',
            'python_requires': '>=3.7',
            'install_requires': []}


setup(**metadata)


