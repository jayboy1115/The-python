def biggest_odd(num_str):
    
    num_list = [int(x) for x in num_str]
    
    odd_list = [x for x in num_list if x % 2 != 0]
   
    return max(odd_list)

print(biggest_odd('23569'))

