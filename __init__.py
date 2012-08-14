#!/usr/bin/python
import numpy as np

THRESHOLDS = {
  "greater": lambda x,t: x >= t,
  "less": lambda x,t: x <= t,
}

def npy_to_adjlist(npyfname=None, M=None, threshold=None, thresh_cmp="greater", absvalue=False):
  """Yield row-wise adjacency list text lines from numpy matrix.
  """
  assert bool(npyfname is None) != bool(M is None)
  assert threshold is not None
  assert thresh_cmp in THRESHOLDS
  threshold = float(threshold)
  if M is None:
    M = np.load(npyfname)
  if absvalue:
    M = np.fabs(M)
  for i in xrange(np.size(M,0)):
    f = THRESHOLDS[thresh_cmp]
    yield " ".join([str(x) for x in np.where(f(M[i,:],threshold))[0]])

def npy_to_mafia(empty_lines, **kwds):
  """Wrapper for npy_to_mafia: Filter empty lines and save their indices to a list.
  """
  for i, line in enumerate(npy_to_adjlist(**kwds)):
    if line == "":
      empty_lines.append(i)
    else:
      yield line
