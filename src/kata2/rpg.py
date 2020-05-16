#!/usr/bin/python

import random
import string

def RandomPasswordGenerator(passLen=10):
    
    token = string.ascii_letters

    return "".join(random.choice(token) for i in range(passLen))
