#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

a = True
b = False
x = ( 'bear', 'bunny', 'tree', 'sky', 'rain' )
y = 'bear'

if a or b:
    print('expression is true')
else:
    print('expression is false')

if y in x[0]:
     print('expression is true')
else:
    print('expression is false')

if 'tree' in x:
    print('expression is true')
else:
    print('expression is false')

# Conditional Operators
# True, False
# Identity operator to test if 2 objects are same or not: is, is not
# Membership Operator to test if a variable is a member of a collection:  in, not in