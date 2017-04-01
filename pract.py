def main():
    #define size of list SIZE = 5 (NOT NEEDED)
    #define list data type Integer (NOT NEEDED)
    #declare a loop counter index = 0
    #declare a Boolean variable as a flag, found = False
    #user inputs a number to find in the list
    #print('Your number is in the list,')
    #or print('Your number is not in the list')
    # if x in collection
    
    n = int(input())
    search_list = [24, 68, 1, 0, 99]
    if n in search_list:
        print("it was in the list")
    else:
        print("no it wasn't")
    
main()
