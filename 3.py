# User input 
list1 = input("Enter the elements of list 1 : ")
list2 = input("Enter the elements of list 2 : ")

# Function to find common element
def find_common_elements(list1, list2):
    set_list1=set(list1)
    set_list2=set(list2)
    count=len(set_list1.intersection(set_list2))
    return count
print("The number of common elements are : ",find_common_elements(list1,list2))


