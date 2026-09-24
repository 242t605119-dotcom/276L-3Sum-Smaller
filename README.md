# 3Sum Smaller

LeetCode 259

## Problem Statement

Given an integer array `nums` and an integer `target`, return the number of index triplets `(i, j, k)` where:

`i < j < k`

and

`nums[i] + nums[j] + nums[k] < target`.

## Solution

This solution first sorts the array and then uses the two-pointer technique.

For each element, two pointers are used to find pairs whose sum with the current element is smaller than the target. When a valid combination is found, all elements between the two pointers can also form valid triplets.

## Example

### Input

```text
nums = [-2,0,1,3]
target = 2
```

### Output

```text
2
```

### Explanation

The valid triplets are:

```text
[-2, 0, 1] = -1
[-2, 0, 3] = 1
```

Both sums are smaller than `2`.

Therefore, the answer is:

```text
2
```

## Approach

1. Sort the array.
2. Fix one element using index `i`.
3. Set `left = i + 1` and `right = n - 1`.
4. Calculate the sum of the three elements.
5. If the sum is smaller than the target, all elements between `left` and `right` form valid triplets with the fixed element.
6. Increase `left`.
7. Otherwise, decrease `right`.
8. Continue until all possible triplets are checked.

## Algorithm

1. Sort `nums`.
2. Initialize `count = 0`.
3. For every index `i` from `0` to `n - 3`:

   * Set `left = i + 1`.
   * Set `right = n - 1`.
4. While `left < right`:

   * Calculate `nums[i] + nums[left] + nums[right]`.
   * If the sum is less than `target`, add `right - left` to `count` and move `left` forward.
   * Otherwise, move `right` backward.
5. Return `count`.

## Complexity

* Time Complexity: O(n²)
* Space Complexity: O(1)

## Author

T. Nandhini
