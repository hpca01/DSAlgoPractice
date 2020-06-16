## Solution

1. Why did you use that data structure?

    I used recursion because the task was to get into each directory and list file contents. This required that for each directory there needed to be a printout of files for all the child subdirectories. I could have used a stack, by pushing directories into the stack and print all the contents of the directory. However, I like my solution as it is the essentially the same and slightly easier to visualize.

2. You also need to explain the efficiency (time and space) of your solution.

    The time complexity of my solution is O(n) because we are traversing `n` subdirectories inside the given directory. In a worst case scenario if a directory had n subdirectories with each subdirectory having k subdirectories it would take `O(n + k)` time to traverse, simplied into `O(n)`. Space complexity is based on the call stack size, essentially it can be `O(n)` if the aformentioned worst case scenario is assumed to be true.