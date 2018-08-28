# -*- coding: utf-8 -*-


import sys
import json
import redis


class PeersPool:

    def __init__(self):
        self.r = redis.StrictRedis(host="127.0.0.1", port=6379)
        try:
            self.r.get("foo")
        except redis.ConnectionError:
            print "Can not connect redis server......"
            sys.exit(0)

    def __del__(self):
        pass

    def add_peer(self, address):
        result = self.r.get("address")
        if not result:
            s = [address]
            self.r.set("address", json.dumps(s))
        else:
            result = json.loads(result)
            result.append(address)
            self.r.set("address", json.dumps(result))
    
    def is_exist(self, address):
        result = self.r.get("address")
        if not result:
            return False
        result = json.loads(result)
        for addr in result:
            if address[0] == addr[0] and address[1] == addr[1]:
                return True
        return False
    
    def peers(self):
        result = self.r.get("address")
        if not result:
            result = json.dumps([])
        return result


def test_main():
    pool = PeersPool()
    pool.add_peer(("127.0.0.1", 80))
    pool.add_peer(("127.0.0.1", 81))
    pool.add_peer(("127.0.0.1", 82))
    pool.add_peer(("127.0.0.1", 83))
    print pool.is_exist(("127.0.0.1", 83))
    print pool.peers()


if __name__ == "__main__":
    test_main()
