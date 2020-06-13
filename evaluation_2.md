## Solution

1. Why did you use that data structure?

    I used recursion because the task was to get into each directory and list file contents. This required that for each directory there needed to be a printout of files for all the child subdirectories. I could have used a stack, by pushing directories into the stack and print all the contents of the directory. However, I like my solution as it is the essentially the same and slightly easier to visualize.

2. You also need to explain the efficiency (time and space) of your solution.

    The time complexity of my solution is O(n<sup>2</sup>) because we are traversing directory **and** subdirectory. In a worst case scenario if a directory had n subdirectories with each subdirectory having n subdirectories it would take O(n<sup>2</sup>) time to traverse. Space complexity is based on the call stack size, essentially it can be O(n<sup>2</sup>) if the aformentioned worst case scenario is assumed to be true.