
# todo Sum of Missing Numbers
# ? Create a function that returns the sum of missing numbers.

# ! Examples
# * sum_missing_numbers([1, 3, 5, 7, 10]) ➞ 29
# * # 2 + 4 + 6 + 8 + 9

# * sum_missing_numbers([10, 7, 5, 3, 1]) ➞ 29

#  * sum_missing_numbers([10, 20, 30, 40, 50, 60]) ➞ 1575
# ! Notes
# ? The minimum and maximum value of the given list are the inclusive bounds of the numeric range to consider when searching for missing numbers.




def sum_missing_numbers(lst):
    maxnum = max(lst)
    minnum = min(lst)
    sumnum = sum(lst)
    
    
    newlst = [item for item in range(minnum, maxnum + 1)]
    
    
    return sum(newlst) - sumnum


print(sum_missing_numbers([1, 3, 5, 7, 10]))  
print(sum_missing_numbers([10, 7, 5, 3, 1]))  
print(sum_missing_numbers([10, 20, 30, 40, 50, 60]))  


# ! ///////////////////////////////////////////////////////////



def sum_missing_numbers(lst):
   
    min_val = min(lst)
    max_val = max(lst)
    
    
    complete_range = set(range(min_val, max_val + 1))
    
    
    missing_numbers = complete_range - set(lst)
    
    
    return sum(missing_numbers)

# Test cases
print(sum_missing_numbers([1, 3, 5, 7, 10]))  # ➞ 29
print(sum_missing_numbers([10, 7, 5, 3, 1]))  # ➞ 29
print(sum_missing_numbers([10, 20, 30, 40, 50, 60]))  # ➞ 1575
