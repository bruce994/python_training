#-*- coding:utf-8-*-
import sys
import string
import time
import re
import commands
import random

def main():
    status, output = commands.getstatusoutput('/usr/bin/perl /usr/share/logwatch/scripts/logwatch.pl')
    print output
if __name__ == '__main__':
    main()
