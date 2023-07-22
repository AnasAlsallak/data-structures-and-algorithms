from .hashmap_left_join_script import HashTable, left_join
from hash.hash_table import HashTable

# Happy Path Test
def test_left_join_happy_path():
    hashmap1 = HashTable()
    hashmap2 = HashTable()

    hashmap1.set("A", 70)
    hashmap1.set("B", 90)
    hashmap1.set("C", 80)
    hashmap2.set("A", "valueA")
    hashmap2.set("B", "valueB")

    result = left_join(hashmap1, hashmap2)
    assert result == [["B", 90, "valueB"], ["A", 70, "valueA"], ["C", 80, None]]

# Expected Failure Test
def test_left_join_expected_failure():
    hashmap1 = HashTable()
    hashmap2 = HashTable()

    hashmap1.set("A", 70)
    hashmap1.set("B", 90)
    hashmap2.set("C", "valueC")
    hashmap2.set("D", "valueD")

    result = left_join(hashmap1, hashmap2)
    assert result == [["B", 90, None], ["A", 70, None]]

# Edge Case Test - Empty Hashmaps
def test_left_join_empty_hashmaps():
    hashmap1 = HashTable()
    hashmap2 = HashTable()

    result = left_join(hashmap1, hashmap2)
    assert result == []

# Edge Case Test - Empty Hashmap1
def test_left_join_empty_hashmap1():
    hashmap1 = HashTable()
    hashmap2 = HashTable()

    hashmap2.set("X", "valueX")
    hashmap2.set("Y", "valueY")

    result = left_join(hashmap1, hashmap2)
    assert result == []

# Edge Case Test - Empty Hashmap2
def test_left_join_empty_hashmap2():
    hashmap1 = HashTable()
    hashmap2 = HashTable()

    hashmap1.set("X", "valueX")
    hashmap1.set("Y", "valueY")

    result = left_join(hashmap1, hashmap2)
    assert result == [["Y", "valueY", None], ["X", "valueX", None] ]
