#!/usr/bin/python
# -*- coding: utf-8 -*-

import time

t = time.localtime(time.time())
localtime = time.asctime(t)
str = "当前时间:" + time.asctime(t)

print(str)
