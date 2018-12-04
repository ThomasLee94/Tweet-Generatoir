#!python

from linkedlist import LinkedList

class HashTable(object):

    def __init__(self, init_size=8):
        """Initialise this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = [LinkedList() for _ in range(init_size)]

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
        # TODO: Running time: O(???) Why and under what conditions?"""
        # Runtime = O(n)
        # Collect all keys in each bucket
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
        # TODO: Running time: O(???) Why and under what conditions?"""
        # Runtime = O(n)
        # TODO: Loop through all buckets
        # TODO: Collect all values in each bucket

        bucket_values = []

        for bucket in self.buckets:
            for key, value in bucket.items():
                bucket_values.append(value)
        return bucket_values

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        # TODO: Running time: O(???) Why and under what conditions?"""
        # Runtime = O(n)
        # Collect all pairs of key-value entries in each bucket
        all_items = []
        for bucket in self.buckets:
            # Extending all items in the list of bucket.items
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        # TODO: Running time: O(???) Why and under what conditions?"""
        # Runtime = O(n)
        # TODO: Loop through all buckets
        # TODO: Count number of key-value entries in each bucket

        total_pairs = 0

        for bucket in self.buckets:
            total_pairs += bucket.length()
        return total_pairs

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        # TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket

        # Find bucket containing key-value pair. 
        bucket_index = self._bucket_index(key)
        node = buckets[bucket_index].find(key)
        return (node != None)

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, return value associated with given key
        # TODO: Otherwise, raise error to tell user get failed
        # Hint: raise KeyError('Key not found: {}'.format(key))

        bucket_index = self._bucket_index(key)
        node = buckets[bucket_index].find(key)

        if node is None:
            raise KeyError('Key not found: {}'.format(key))
        else:
            return node[1]

    def set(self, key, value):
        """Insert or update the given key with its associated value.
        # TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, update value associated with given key
        # TODO: Otherwise, insert given key-value entry into bucket

        bucket_index = self._bucket_index(key)
        bucket = self.buckets[bucket_index]
        node = buckets[bucket_index].find(key)

        if node is not None:
            bucket.delete(node)
            # Append key-value pair as a tuple after deleting. 
            bucket.append((key,value))
        else:
            # Append new key-value pair as a tuple. 
            bucket.append((key,value))
            

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        # TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, delete entry associated with given key
        # TODO: Otherwise, raise error to tell user delete failed
        # Hint: raise KeyError('Key not found: {}'.format(key))


