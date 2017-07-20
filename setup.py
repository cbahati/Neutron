try:
        from setuptools import setup
except ImportError:
        from distutils.core import setup

        config = {
            'description': 'Twitter text and image processor',
            'author': 'Christian Bahati',
            'url': '',
            'download_url': '',
            'author_email': 'cnbahati@gmail.com',
            'version': '0.1',
            'install_requires': ['nose', 'TensorFlow', 'tweepy'],
            'packages': ['NAME'],
            'scripts': [],
            'name': 'Neutron'
        }

setup(**config)
