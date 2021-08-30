"""
Run all starting with test

"""

import sys
import os
import nose

def main() -> object:
    sys.path.insert(0, os.path.dirname(__file__))
    nose.main()
    sys.exit(0)

if __name__ == '__main__':
    main()
