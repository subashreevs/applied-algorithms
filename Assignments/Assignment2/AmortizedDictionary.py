class amor_dict:
    def __init__(self, num_list=[]):
        # Dictionary to store levels, where each level contains sorted elements
        self.levels = {}
        for num in num_list:
            self.insert(num)

    def merge(self, list1, list2):
        """ Merge two sorted lists """
        merged = []
        i = j = 0
        while i < len(list1) and j < len(list2):
            if list1[i] < list2[j]:
                merged.append(list1[i])
                i += 1
            else:
                merged.append(list2[j])
                j += 1
        # Add remaining elements from both lists
        merged.extend(list1[i:])
        merged.extend(list2[j:])
        return merged

    def insert(self, num):
        """ Insert a number into the amortized dictionary """
        # Start at level 0
        level = 0
        new_list = [num]

        # Keep merging with existing levels if they are non-empty
        while level in self.levels and self.levels[level]:
            new_list = self.merge(self.levels[level], new_list)  # Merge two sorted lists
            del self.levels[level]  # Clear the current level after merging
            level += 1

        # Place the merged list into the appropriate level
        self.levels[level] = new_list

    def search(self, num):
        """ Search for the number and return the level if found, else -1 """
        # Traverse through each level and search for the element
        for level, elements in self.levels.items():
            if elements and self.binary_search(elements, num):
                return level
        return -1

    def binary_search(self, lst, target):
        """ Perform binary search to find the target in a sorted list """
        left, right = 0, len(lst) - 1
        while left <= right:
            mid = (left + right) // 2
            if lst[mid] == target:
                return True
            elif lst[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False

    def print(self):
        """ Return a list of lists, each list containing elements of a level """
        # Return levels as a list of lists, sorted by level index
        max_level = max(self.levels.keys(), default=-1)
        return [self.levels.get(i, []) for i in range(max_level + 1)]