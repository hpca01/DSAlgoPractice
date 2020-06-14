## Solution

1. Why did you use that data structure?

   I used sets because of the constant look up time as well as the ability to weed out duplicates. For the union function, it is imperative to get unique values between both input lists. For the intersection function it was imperative to get unique values present in both lists.
    

2. You also need to explain the efficiency (time and space) of your solution.

    For the union function both of the lists are iterated through and added to the set. Set look up is constant time, assuming you have 2 lists with `n` size all including unique elements, at worst you would have `n + n + 2n` iterations. Simplified = `O(n)` to signify linear growth in time complexity. The space complexity is also similar `O(n)`

    For the intersection functions list one is iterated through and entered into a set, then the second list is iterated through for matches and added to a sublist if a match is found. Assuming that both lists have `n` elements, you would have a worst case scenario of `n + n` iterations Simplified = `O(n)` to signify linear growth in time complexity. The space complexity is also similar `O(n)`.
    