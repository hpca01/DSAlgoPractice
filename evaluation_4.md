## Solution

1. Why did you use that data structure?

    I used changed the underlying data structure in Group to use sets as this helps reduce duplicates makes the search constant time.

2. You also need to explain the efficiency (time and space) of your solution.

    The time complexity of my solution is O(n<sup>2</sup>) because we are traversing directory **and** subdirectory. In a worst case scenario if a directory had n subdirectories with each subdirectory having n subdirectories it would take O(n<sup>2</sup>) time to traverse. Space complexity is based on the call stack size, essentially it can be O(n<sup>2</sup>) if the aformentioned worst case scenario is assumed to be true.