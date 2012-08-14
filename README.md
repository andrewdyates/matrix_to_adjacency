matrix_to_adjacency
===================

Convert a numpy matrix into an integer-enumerated text adjacency list.

###Functions###
_Imported as module._

    def npy_to_adjlist(npyfname=None, M=None, threshold=None, thresh_cmp="greater", absvalue=False)
      "Yield row-wise adjacency list text lines from numpy matrix."

    def npy_to_mafia(empty_lines, **kwds)
      "Wrapper for npy_to_mafia: Filter empty lines and save their indices to a list."


###Example Use###
_Stand-alone script. See script.py source code for use in code._

    python $HOME/matrix_to_adjacency/script.py npyfname=$HOME/mymatrix_pcc.npy threshold=0.4 