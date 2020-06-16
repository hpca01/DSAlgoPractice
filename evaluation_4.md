## Solution

1. Why did you use that data structure?

    I used changed the underlying data structure in Group to use sets as this helps reduce duplicates makes the search constant time.

2. You also need to explain the efficiency (time and space) of your solution.

    The time complexity of my solution is `O(n)` because we are traversing subgroups. In a worst case scenario if a group had n subgroups with each subgroup having k subgroups it would take `O(n+k)` time to traverse, simplified to `O(n)`. Space complexity is based on the call stack size, essentially it can be O(n) if the aformentioned worst case scenario is assumed to be true.