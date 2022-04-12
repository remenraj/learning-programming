# Program to find all pairs of integers whose sum is equal to a given number
# [2, 6, 3, 9, 11]  9 -> [6, 3]

# Questions to ask:
    # Does the array contain only positive or negative numbers?
    # Does the array contain duplicate numbers?
    # Does the array contain numbers in sorted order?
    # Does the array contain numbers in random order?
    # What if the array is empty?
    # What if the array contains only one element?
    # What if the same pair repeats twice, or more than twice, should we print it every time?
    # If the reverse of the pair is acceptable, e.g. can we print broth (4, 1) and (1, 4) if the given number is 5
    # Do we need to print only distinct pairs? Does (3, 3) is a valid pair for a given number of 6?
    # How big is the array?
    
# here pairs are distinct pairs 



def find_pairs(num_list: list, target: int):
    
    # loop through the array
    for i in range(len(num_list)):
        for j in range(i+1, len(num_list)):
            # skipping same number
            if num_list[i] == num_list[j]:
                continue
            # checking if the sum of the current element and the next element is equal to the given number
            if num_list[i] + num_list[j] == target:
                print([num_list[i], num_list[j]])
        
    
if __name__ == "__main__":
    
    my_list = [1, 2, 3, 23, 12, 7, 53, 4]
    find_pairs(my_list, 35)
    