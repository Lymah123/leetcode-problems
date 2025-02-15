# Top 150 Interview
# Question 380: Insert Delete GetRandom O(1)
# Difficulty level: Medium
# Implement the RandomizedSet class:
# - RandomizedSet() Initializes the RandomizedSet object.
# - bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
# - bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
# - int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.

# You must implement the functions of the class such that each function works in average O(1) time complexity.

# Example 1:
# Input
# ["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
# [[], [1], [2], [2], [], [1], [2], []]
# Output
# [null, true, false, true, 2, true, false, 2]

# Explanation
# RandomizedSet randomizedSet = new RandomizedSet();
# randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
# randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
# randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
# randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
# randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
# randomizedSet.insert(2); // 2 was already in the set, so return false.
# randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.

# Constraints:

# -2^31 <= val <= 2^31 - 1
# At most 10^5 calls will be made to insert, remove, and getRandom.
# There will be at least one element in the data structure when getRandom is called.

# Approach:
# We use a dictionary to store the values and their indices in the array. We also use a list to store the values. We use the dictionary to check if the value is already present in the array. If it is, we return False. If it is not, we append the value to the list and add the value and its index to the dictionary. We use the dictionary to check if the value is present in the array. If it is, we remove the value from the list and the dictionary. We use the random module to return a random element from the list.

from typing import List
import random

class RandomizedSet:
    def __init__(self):
        self.values = []
        self.indices = {}

    def insert(self, val: int) -> bool:
        if val in self.indices:
            return False

        self.values.append(val)
        self.indices[val] = len(self.values) - 1

        return True

    def remove(self, val: int) -> bool:
        if val not in self.indices:
            return False

        index = self.indices[val]
        last_val = self.values[-1]

        self.values[index] = last_val
        self.indices[last_val] = index

        self.values.pop()
        del self.indices[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.values)

# Time complexity analysis:
# The time complexity for the insert and remove functions is O(1) on average. The time complexity for the getRandom function is O(1). The space complexity is O(n) where n is the number of elements in the set.


