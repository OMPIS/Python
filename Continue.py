#Continue is used to skip the particualr thing in a flow and move with rest of the flow.

#!/usr/bin/env python

num = ['0','1','2','3','4','5','6','7']

for i in num:
    if i == '3':
        continue
    print("Added",i)
