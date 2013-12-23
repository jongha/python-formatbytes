#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import division
import os
import sys
import string

try:
    import argparse
    
except ImportError:
    from optparse import OptionParser
    
class FormatBytes(object):
    unit = ['B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB']
    def get(self, bytes=0, step=0, unit='B'):
        while bytes >= 1024 and step < len(self.unit) - 1:
            bytes /= 1024
            step += 1
            self.get(bytes, step)
            
        return (bytes, step, self.unit[step])
         
if __name__ == '__main__':
    l_argv = len(sys.argv)
    parser = argparse.ArgumentParser(description='Format Bytes for Python')
    parser.add_argument('bytes', metavar='bytes', nargs=1, help='Bytes for Formatting.')
    args = parser.parse_args()

    if l_argv > 1:
        f = FormatBytes()
        result = f.get(int(sys.argv[1]))
        print(str(result[0]) + ' ' + result[2])
        
    else:
        print(args.accumulate(args.integers))
