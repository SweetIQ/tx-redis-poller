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
