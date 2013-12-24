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
    units = {
        '1024': ['B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'], # Kilobyte
        '1000': ['B', 'kB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'] # Kibibyte
        }

    def convert(self, bytes=0, step=0, unit=None, multiple=1024):
        selected_byte_unit = self.units[str(multiple)]
        if unit is None:
            while bytes >= multiple and step < len(selected_byte_unit) - 1:
                bytes /= multiple
                step += 1
                self.convert(bytes=bytes, step=step, unit=unit, multiple=multiple)

        else: # convert to specific unit
            while step < len(selected_byte_unit) - 1 and selected_byte_unit.index(unit) != step:
                bytes /= multiple
                step += 1
                self.convert(bytes=bytes, step=step, unit=unit, multiple=multiple)

        return (bytes, step, selected_byte_unit[step])

    def format(self, bytes=0, unit=None, precision=2, comma=False):
        values = (('%.' + str(precision) + 'f') % bytes).split('.')
        if comma:
            values[0] = '{:,}'.format(int(values[0]))

        return ('.'.join(values)  + ' ' + unit)

if __name__ == '__main__':
    l_argv = len(sys.argv)
    parser = argparse.ArgumentParser(description='Format Bytes for Python')
    parser.add_argument('bytes', metavar='bytes', nargs=1, help='Bytes for Formatting.')
    parser.add_argument('-u', metavar='B|KB|MB|GB|TB|PB|EB|ZB|YB', nargs='?', default=None, help='Target unit to convert.')
    parser.add_argument('-p', metavar='integer', nargs='?', default=2, help='Precision of floating point.')
    parser.add_argument('-c', action='store_true', help='Print with commas.')
    parser.add_argument('-m', metavar='1024|1000', nargs='?', default='1024', help='Set the byte multiple.')
    args = parser.parse_args()

    if l_argv > 1:
        f = FormatBytes()
        bytes, step, unit = f.convert(bytes=int(args.bytes[0]), unit=args.u, multiple=int(args.m))
        result = f.format(bytes=bytes, unit=unit, precision=args.p, comma=args.c)
        print(result)

    else:
        print(args.accumulate(args.integers))
