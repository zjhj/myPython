# -*- coding:utf-8 -*-
import io
import sys
import re

def main():
    if len(sys.argv) == 1:
        print( "Please input the filename!\nUsage: %s filename" % sys.argv[0] )

    try:
        fd = io.open( sys.argv[1] )

        p = re.compile( r'^ao' )

        for cline in fd.readlines():
            if p.search( cline ):
                print( cline )
            else:
                print( "no match" )
    except Exception as err:
        print( err )

if __name__ == '__main__':
    main()
