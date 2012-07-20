#!/usr/bin/python
"""Convert matrix to adjacency list.
Filter rows that do not have any transations

EXAMPLE USE:
  python $HOME/matrix_to_adjacency/script.py npyfname=$HOME/gse15745/gse15745_gpl8178_gpl6104_dcor.values.npy thresh=0.6
"""
import sys
import numpy as np

def main(npyfname, thresh, absvalue=False, neg=False, filter_blanks=False):
  thresh = float(thresh)
  M = np.load(npyfname)
  if absvalue:
    M = np.fabs(M)
  for i in xrange(np.size(M,0)):
    if neg:
      row = M[i,:] <= thresh
    else:
      row = M[i,:] >= thresh
    a = [str(x) for x in np.where(row)[0]]
    s = " ".join(a)
    if s == "" and filter_blanks:
      sys.stderr.write("%d\n"%i)
      continue
    print s
    


if __name__ == "__main__":
  args = dict([s.split('=') for s in sys.argv[1:]])
  main(**args)
