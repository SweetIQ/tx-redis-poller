from setuptools import setup, find_packages

setup(
    name='tx-redis-poller',
    version='1.0',
    author='SweetIQ',
    author_email='rob@sweetiq.com',
    description=('A little Twisted-based tool to poll a Redis queue periodically for messages.'),
    packages=find_packages(),
    install_requires=[
        'Twisted==14.0.0',
        'txredis==2.3'
    ],
)
