#!/usr/bin/python
"""Convert matrix to adjacency list

EXAMPLE USE:
  python $HOME/matrix_to_adjacency/script.py npyfname=$HOME/gse15745/gse15745_gpl8178_gpl6104_dcor.values.npy thresh=0.6
"""
import sys
import numpy as np

def main(npyfname, thresh, absvalue=False):
  thresh = float(thresh)
  M = np.load(npyfname)
  if absvalue:
    M = np.fabs(M)
  for i in xrange(np.size(M,0)):
    print " ".join([str(x) for x in np.where(M[i,:]>=thresh)[0]])

    


if __name__ == "__main__":
  args = dict([s.split('=') for s in sys.argv[1:]])
  main(**args)
