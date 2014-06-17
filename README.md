# Installation

Through pip:

    pip install tx-redis-poller

# Usage

Subclass and instantiate:

    from txredispoller import RedisPoller


    class MyPoller(RedisPoller):
        def on_message(self, message):
            # Do whatever you need to do when you receive a message
            print message

    poller = MyPoller("queue-to-listen-on")

    poller.start()

    # since it is Twisted-based, we'll need to start the reactor for anything
    # to happen
    reactor.run()

# Documentation

## RedisPoller

`__init__(self, queue_name, redis=None, redis_config=None, prefetch_count=10, poll_delay=0.1)`

Construct a new instance of a Redis poller.

* `queue_name` - (string) The queue that we want to listen on.
* `redis` - (txredis client) A connection to Redis using txredis that is already set up. Useful for when you have multiple queues you want to poll with, but only want one connection.
* `redis_config` - (tuple (host, port), default: ("localhost", 6379)) The hostname and port that Redis is listening on.
* `prefetch_count` - (int, default: 10) How many messages to fetch at a time from Redis.
* `poll_delay` - (float, default: 0.1) How long to wait in seconds between fetches. Higher numbers will be less CPU-intensive, lower numbers will mean your messages get received sooner.

`start(self)`

Start the Redis poller. This does not actually do anything until the Twisted reactor is started.
