from formatbytes.formatbytes import FormatBytes

try:
    f = FormatBytes()

    for m in range(9):
        bytes, step, unit = f.convert(bytes=1024**m)
        result = f.format(bytes=bytes, unit=unit, precision=2)
        print(result)

    for m in range(9):
        bytes, step, unit = f.convert(bytes=1000**m, multiple=1000)
        result = f.format(bytes=bytes, unit=unit, precision=2)
        print(result)

    for m in range(9):
        bytes, step, unit = f.convert(bytes=1024**m, unit='KB')
        result = f.format(bytes=bytes, unit=unit, precision=2, comma=True)
        print(result)

    for m in range(9):
        bytes, step, unit = f.convert(bytes=1024**m, unit='kB', multiple=1000)
        result = f.format(bytes=bytes, unit=unit, precision=2, comma=True)
        print(result)

    exit(1)

except:
    exit(0)
