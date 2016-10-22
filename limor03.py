

my_value = 15

my_switch = {
    10: 'picked 10',
    20: 'picked 20',
    30: 'picked 30'
}

print(my_value)
print(my_switch)

print(my_switch.get(my_value, 'picked default'))

print(my_switch.get(10,'limor'))