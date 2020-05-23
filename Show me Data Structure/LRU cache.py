from collections import OrderedDict
class LRU_Cache(object):

    def __init__(self, capacity):
        self.cacheDict = OrderedDict()
        self.maxlen = 0
        self.capacity = capacity

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        try :
            self.cacheDict.move_to_end(key, True)
            return self.cacheDict[key]
        except:
            return -1
    def set(self, key, value):

        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.

        if key not in self.cacheDict.keys():
            if self.maxlen < self.capacity:
                self.cacheDict.__setitem__(key,value)
                self.maxlen += 1
            else:
                dictAsList = list(self.cacheDict)
                self.cacheDict.pop(dictAsList[0])
                self.cacheDict.__setitem__(key,value)
        else:
            self.cacheDict[key] = value
            self.cacheDict.move_to_end( key, True )


our_cache = LRU_Cache(5)

print(our_cache.get(1))        #retrun -1   Empty cache

our_cache.set(1, 1)
print(our_cache.get(1))        #return 1
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)
our_cache.set(5, 5)

our_cache.set(1, 8)     #updated data
print(our_cache.get(1))        #return 8

print(our_cache.get(2))       # returns 3
print(our_cache.get(9))       #return -1 not present

#lru Element now is 3 so
our_cache.set(9, 9)
print(our_cache.get(3))

print(our_cache.get(9))     # return 9

print(our_cache.cacheDict)
    ###################################################
#in #  9:9  &   2:2   &   1:8   &   5:5    &   4:4    #  #out
    ###################################################