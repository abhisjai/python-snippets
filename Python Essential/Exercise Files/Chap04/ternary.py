#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

hungry = True

# False, 0, "" (blank string) or None are all False in Python
x = 'Feed the bear now!' if hungry else 'Do not feed the bear.'
print(x)
