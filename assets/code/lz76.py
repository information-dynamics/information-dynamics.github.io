"""
Simple script implementing Kaspar & Schuster's algorithm for
Lempel-Ziv complexity (1976 version).

If you use this script, please cite the following paper containing a sample
use case and further description of the use of LZ in neuroscience:

Dolan D. et al (2018). The Improvisational State of Mind: A Multidisciplinary
Study of an Improvisatory Approach to Classical Music Repertoire Performance.
Front. Psychol. 9:1341. doi: 10.3389/fpsyg.2018.01341

Pedro Mediano and Fernando Rosas, 2019
"""
import numpy as np

def LZ76(ss):
    """
    Calculate Lempel-Ziv's algorithmic complexity using the LZ76 algorithm
    and the sliding-window implementation.

    Reference:

    F. Kaspar, H. G. Schuster, "Easily-calculable measure for the
    complexity of spatiotemporal patterns", Physical Review A, Volume 36,
    Number 2 (1987).

    Input:
      ss -- array of integers

    Output:
      c  -- integer
    """

    ss = ss.flatten().tolist()
    i, k, l = 0, 1, 1
    c, k_max = 1, 1
    n = len(ss)
    while True:
        if ss[i + k - 1] == ss[l + k - 1]:
            k = k + 1
            if l + k > n:
                c = c + 1
                break
        else:
            if k > k_max:
               k_max = k
            i = i + 1
            if i == l:
                c = c + 1
                l = l + k_max
                if l + 1 > n:
                    break
                else:
                    i = 0
                    k = 1
                    k_max = 1
            else:
                k = 1
    return c


if __name__ == '__main__':
    # Simple string, low complexity
    ss = np.array([0,0,0,0,0,0,0,1,1,1,1,1,1])
    print('The complexity of the string %s is %i'%(ss, LZ76(ss)))

    # Irregular string, high complexity
    ss = np.array([0,1,1,0,1,0,0,1,0,1,1,1,0])
    print('The complexity of the string %s is %i'%(ss, LZ76(ss)))

