#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# x = [ 1, 2, 3, 4, 5 ]
# for i in x:
#     print('i is {}'.format(i))

x = {"one": 1, "two": 2, "three": 3, "four": 4}

# for i in x:
#     print("key {}".format(i))

# for key, value in x.items():
#     print("key {0:<5} value {1:<5}".format(key, value))

#Dictionaries are mutable - you can change value after initial assignment
# x['three'] = 42
# for key, value in x.items():
#     print("key {0:<5} value {1:<5}".format(key, value))

x['five'] = 5
for key, value in x.items():
    print("key {0:<5} value {1:<5}".format(key, value))