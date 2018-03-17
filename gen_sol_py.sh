#!/bin/sh

File=$1
Descripton=$2
Now=$(date +%Y-%m-%d\ %H:%M:%S)

cat  << EOF > python/$1.py
#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author:      nick <starshiping[at]gmail.com>
# File:        $1.py
# Create Date: $Now
# Usage:       $1.py
# Descripton:  $2


class Solution:

# debug
s = Solution()
EOF