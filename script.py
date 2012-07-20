#!/usr/bin/python
"""Convert matrix to adjacency list.
Filter rows that do not have any transations

EXAMPLE USE:
  python $HOME/matrix_to_adjacency/script.py npyfname=$HOME/gse15745/gse15745_gpl8178_gpl6104_dcor.values.npy threshold=0.4 
"""
import sys
from __init__ import *

def main(**kwds):
  empty_lines = []
  for line in npy_to_mafia(empty_lines, **kwds):
    print line
  sys.stderr.write("\n".join(map(str, empty_lines)))
  
      
if __name__ == "__main__":
  main(**dict([s.split('=') for s in sys.argv[1:]]))
