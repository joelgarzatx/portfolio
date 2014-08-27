class Publisher:
    def __init__(self):
        self.subscribers  = []
    def subscribe(self, subscriber):
        if subscriber in self.subscribers:
            raise ValueError("Multiple subscriptions are not allowed")
        self.subscribers.append(subscriber)
    def unsubscribe(self, subscriber):
        if subscriber not in self.subscribers:
            raise ValueError("Can only unsubscribe subscribers")
#        self.subscribers.remove(subscriber)
        spot = self.subscribers.index(subscriber)
        self.subscribers[spot] = None # by setting the bound function to None, we don't mess with the number/position of list elements in the middle of an iteration
#        print("removed", subscriber)
    def purge(self): # here's the magic, do a purge at the end of the publish cycle
        for subscriber in self.subscribers:
            if subscriber:
                pass
            else:
                self.subscribers.remove(subscriber)
    def publish(self, s):
#        print(self.subscribers)
        for subscriber in self.subscribers:
            subscriber(s)
        self.purge() # see, here is where it happens

if __name__ == '__main__':
    def multiplier(s):
        print(2*s)
        
    class SimpleSubscriber:
        def __init__(self, name, publisher):
            self.name = name
            self.publisher = publisher
            self._processcall = 0
            publisher.subscribe(self.process)
        def process(self, s):
            print(self.name, ":", s.upper())
            self._processcall += 1
#            print("Subscriber {0} process call {1}".format(self.name, self._processcall))
            if self._processcall >= 3:
                self.publisher.unsubscribe(self.process)
        def __repr__(self):
            return self.name

    publisher = Publisher()
    publisher.subscribe(multiplier)
    for i in range(10):
        newsub = SimpleSubscriber("Sub"+str(i), publisher)
        line = input("Input {}: ".format(i))
        
#        print(publisher.subscribers)
        publisher.publish(line)

