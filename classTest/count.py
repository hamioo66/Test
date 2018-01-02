# -*- coding=UTF-8 -*-
"""
author:hamioo
date:2018/1/2
describle:
"""
# 用于判断素数
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True