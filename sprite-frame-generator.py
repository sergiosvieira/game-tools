#!/usr/bin/env python

import sys, getopt

def help(exit_code):
    print('./sprite-frame-generator -r <rows> -c <cols> -w <frame width> -h <frame height>')
    sys.exit(exit_code)

def main(argv):
    rows = 0
    cols = 0
    width = 0
    height = 0
    try:
        array = [
            "rows=",
            "cols=",
            "width=",
            "height="
        ]
        opts, args = getopt.getopt(argv, "i:r:c:w:h:", array)
    except getopt.GetoptError:
        help(2)
    if len(opts) == 0:
        help(2)
    for opt, arg in opts:
        if opt == '-i':
            help(0)
        elif opt in ("-r", "--rows"):
            rows = int(arg)
        elif opt in ("-c", "--cols"):
            cols = int(arg)
        elif opt in ("-w", "--width"):
            width = int(arg)
        elif opt in ("-h", "--height"):
            height = int(arg)
    for row in range(0, rows + 1):
        for col in range(0, cols + 1):
            sx = col * width
            sy = row * height
            output = "{%d, %d}, " % (sx, sy)
            print(output, end="")
        print()
if __name__ == "__main__":
    main(sys.argv[1:])
