# Format Bytes
[![Build Status](https://travis-ci.org/jongha/python-formatbytes.png?branch=master)](https://travis-ci.org/jongha/python-formatbytes)

Python-formatbytes is bytes to a readable string Converter. It supports the conversion of the unit such as B, KB, MB, GB, TB, PB, EB, ZB, YB. It also supports Kilobyte and Kibibyte.

## Usage

### Setup

    $ python ./setup.py install

### Test

    $ python ./run.py

### Using as a library

Copy formatbytes.py anywhere you want and create new file include below codes.

    from formatbytes.formatbytes import FormatBytes

    f = FormatBytes()
    bytes, step, unit = f.convert(bytes=1024)
    result = f.format(bytes=bytes, unit=unit, precision=2, comma=True)
    print(result)


### From the command line

    usage: formatbytes.py [-h] [-u [B|KB|MB|GB|TB|PB|EB|ZB|YB]] [-p [integer]]
                          [-c] [-m [1024|1000]]
                          bytes

    Format Bytes for Python

    positional arguments:
      bytes                 Bytes for Formatting.

    optional arguments:
      -h, --help            show this help message and exit
      -u [B|KB|MB|GB|TB|PB|EB|ZB|YB]
                            Target unit to convert.
      -p [integer]          Precision of floating point.
      -c                    Print with commas.
      -m [1024|1000]        Set the byte multiple.

## License

python-formatbytes is available under the terms of the MIT License.
