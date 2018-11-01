
numbers = range(100000)
 
# Example 1, list comprehension. No streaming.
# First create an array of squares, then sum it.
# Note the inner array is simply looped over: no random access, just iteration.
# Wasteful, isn't it?
sum([n**2 for n in numbers])
333328333350000
 
# Generator: square and sum one value after another
# No extra array created = lazily evaluated stream of numbers!
sum(n**2 for n in numbers)
333328333350000


"""
The difference between iterables and generators: once you’ve burned through a generator once, you’re done, no more data: 
"""
generator = (word + '!' for word in 'baby let me iterate ya'.split())
# The generator object is now created, ready to be iterated over.
# No exclamation marks added yet at this point.
 
for val in generator: # real processing happens here, during iteration
    print(val ,end=' ')

baby! let! me! iterate! ya!
 
for val in generator:
    print(val ,end=' ')
# Nothing printed! No more data, generator stream already exhausted above.



On the other hand, an iterable creates a new iterator every time it’s looped over (technically, every time iterable.__iter__() is called, such as when Python hits a “for” loop): 

class BeyonceIterable(object):
    def __iter__(self):
        """
        The iterable interface: return an iterator from __iter__().
 
        Every generator is an iterator implicitly (but not vice versa!),
        so implementing `__iter__` as a generator is the easiest way
        to create streamed iterables.
 
        """
        for word in 'baby let me iterate ya'.split():
            yield word + '!'  # uses yield => __iter__ is a generator
 
iterable = BeyonceIterable()
 
for val in iterable:  # iterator created here
    print(val ,end=' ')

 
for val in iterable:  # another iterator created here
    print(val ,end=' ')
