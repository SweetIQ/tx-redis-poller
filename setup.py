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
    url='http://github.com/SweetIQ/redis-poller',
    keywords=["redis", "polling", "twisted"],
    package_data={"tx-redis-poller": ["requirements.txt"]},
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers"
    ],
    long_description="""\
  Poller for Redis
  ---------------------------------

  Event-driven handler for Redis - listen on a Redis queue for messages.
""",
)
