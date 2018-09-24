for number in range(1000000000, 9999999999):
    list_digit = [i for i in str(number)]
    if int(list_digit[0]) % 1 == 0 and \
       int(list_digit[0]+list_digit[1]) % 2 == 0 and \
       int(list_digit[0]+list_digit[1]+list_digit[2]) % 3 ==0 and \
       int(list_digit[0]+list_digit[1]+list_digit[2]+list_digit[3]) % 4 == 0 and \
       int(list_digit[0]+list_digit[1]+list_digit[2]+list_digit[3]+list_digit[4]) % 5 == 0 and \
       int(list_digit[0]+list_digit[1]+list_digit[2]+list_digit[3]+list_digit[4]+list_digit[5]) % 6 == 0 and \
       int(list_digit[0] + list_digit[1] + list_digit[2] + list_digit[3] + list_digit[4] + list_digit[5] \
           +list_digit[6] % 7 == 0) and \
       int(list_digit[0] + list_digit[1] + list_digit[2] + list_digit[3] + list_digit[4] + list_digit[5] \
           +list_digit[6] + list_digit[7] % 8 == 0) and \
       int(list_digit[0] + list_digit[1] + list_digit[2] + list_digit[3] + list_digit[4] + list_digit[5] \
           + list_digit[6] + list_digit[7]+ list_digit[8] % 9 == 0) and \
       int(list_digit[0] + list_digit[1] + list_digit[2] + list_digit[3] + list_digit[4] + list_digit[5] \
           + list_digit[6] + list_digit[7] + list_digit[8]+list_digit[9] % 10 == 0):
        print(number)

    # else:
    #     print(list_digit)
    #     print(int(list_digit[0]+list_digit[1]))









