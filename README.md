# Binary-Search

Implementation Details
The script uses the random module to generate a random array of integers within a specified range.
The array is then sorted using the .sort() method, which typically requires O(n log n) time complexity.
Binary search is applied to the sorted array to find a randomly selected target value.
The binary_search function follows the standard binary search algorithm, achieving an average-case time complexity of O(log n).
Space complexity remains O(1) as only a few variables are used regardless of the input size.


Considerations
Binary search is most efficient with sorted arrays. Sorting the array upfront ensures that binary search can be optimally utilized.
Keep in mind that sorting itself might introduce additional time complexity.
The specific benefits of binary search shine when searching within large, sorted datasets.
