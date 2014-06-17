"""
neptune.redis - Redis-specific details for Neptune

@copyright sweetiQ 2014
@author Rob Britton <rob@sweetiq.com>

"""

import logging
from txredis.client import RedisClient
from twisted.internet import reactor, defer, protocol

logger = logging.getLogger("redis-poller")


class RedisPoller():
    ''' A class to handle polling a Redis queue for messages. '''
    def __init__(self, queue_name, redis=None, redis_config=None,
                 prefetch_count=10, poll_delay=0.1):
        ''' Initialize the poller.
        Arguments:
            - `queue_name` - The Redis queue to poll from
            - `redis` - An already instantiated txredis connection
            - `redis_config` - A tuple for the Redis connection: (hostname,
            port), ignored if `redis` is passed.
            - `prefetch_count` - The number of messages to pull on each poll
            - `poll_delay` - How long to wait between polls
        '''

        if redis is not None:
            self.redis = redis
        elif redis_config is not None:
            self._connect(redis_config)

        self.queue_name = queue_name
        self.prefetch_count = prefetch_count
        self.poll_delay = poll_delay

    @defer.inlineCallbacks
    def _connect(self, redis_config):
        client = protocol.clientCreator(reactor, RedisClient)
        self.redis = yield client.connectTcp(*redis_config)

    @defer.inlineCallbacks
    def start(self):
        yield self._load_lua_scripts()
        self._poll()

    @defer.inlineCallbacks
    def _load_lua_scripts(self):
        poll_script = """
        local res = redis.call("lrange", ARGV[1], 0, tonumber(ARGV[2]) - 1)
        redis.call("ltrim", ARGV[1], tonumber(ARGV[2]), -1)
        return res
        """

        self.poll_script = yield self.redis.script_load(poll_script)

    @defer.inlineCallbacks
    def _poll_helper(self):
        ''' Poll the queue for messages, trigger a callback on each one. '''

        # Grab a bunch of messages, pass them off if needed
        messages = yield self.redis.evalsha(
            self.poll_script,
            args=(self.queue_name, self.prefetch_count)
        )

        for message in messages:
            self.on_message(message)

    @defer.inlineCallbacks
    def _poll(self):
        ''' Trigger a poll on the queues we're listening on. '''
        yield self._poll_helper()
        reactor.callLater(self.poll_delay, self._poll)
