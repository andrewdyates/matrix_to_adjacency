#!/usr/bin/python
"""Convert matrix to adjacency list

EXAMPLE USE:
  python $HOME/matrix_to_adjacency/script.py npyfname $HOME/gse15745/gse15745_gpl8178_gpl6104_dcor.values.npy 0.7
"""

def main(npyfname, thresh):
  thresh = float(thresh)
  M = np.load(npyfname)
  for i in xrange(np.size(M,0)):
    s = " ".join(np.where(M[i,:]>=thresh))
    print s
    


if __name__ == "__main__":
  main(**dict([s.split('=') for s in sys.argv[1:]]))
