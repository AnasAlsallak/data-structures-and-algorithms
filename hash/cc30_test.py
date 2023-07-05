from hash.hash_table import HashTable
import pytest

def test_set_and_get():
    hashtable = HashTable()
    hashtable.set("key1", "value1")
    assert hashtable.get("key1") == "value1"

def test_get_non_existing_key():
    hashtable = HashTable()
    assert hashtable.get("non_existing_key") is None

def test_unique_keys():
    hashtable = HashTable()
    hashtable.set("key2", "value2")
    hashtable.set("key3", "value3")
    hashtable.set("key4", "value4")
    keys = hashtable.keys()
    assert len(keys) == len(set(keys))

def test_collision_handling():
    hashtable = HashTable()
    hashtable.set("key5", "value5")
    hashtable.set("key6", "value6")
    assert hashtable.get("key5") == "value5"
    assert hashtable.get("key6") == "value6"

def test_hash_range():
    hashtable = HashTable()
    hashed_value = hashtable.custom_hash("some_key")
    assert 0 <= hashed_value < hashtable.size

