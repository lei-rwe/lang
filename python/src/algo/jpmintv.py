from collections import frozenset
# Write a cache
# Two methods: entry - key

class CacheMonitor:
    def __init__(self):
        self.subscribers = []

    def notifyall(self, *args):
        print(args)
        for s in self.subscribers:
            s.callback(args)

    def register(self, obj):
        self.subscribers.append(obj)

class cache:
    def __init__(self, cacheMon):
        self.entries = {}
        self.cacheMon = cacheMon

    def add_entry(self, entry):
        if entry.key in self.entries:
            self.entries[entry.key] = entry.value
            self.cacheMon.notifyall('Updated', entry)
        else:
            self.entries[entry.key] = entry.value
            self.cacheMon.notifyall('added', entry)

    def get_value(self, key):
        return self.entries.get(key, None)
    def foo(self):
        s = set([self.entries[key] for key in self.entries])


class User:
    def __init__(self, cachemon):
        cachemon.register(self)

    def send_message(self, *args):
        print('send message', args)

    def callback(self, *args):
        self.send_message(*args)

class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value
