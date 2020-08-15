"""
Calculates higher order crossings of a singal.

Referred from the paper "Discrimination analysis of
discontinuous breath sounds using higher-order crossings"
Authored by, L. J. Hadjileontiadis

(C) 2020 Aditya Srivastava, Mumbai, India
GNU General Public License v3 (GPLv3)
email adityasrivastava301199@gmail.com
"""
import numpy


class PyHOC:
    """Contains the function/s which calculate hoc of a signal."""

    def sequence(self, signal, k):
        """
        Calculate Higher Order Crossings of a Singal.

        Inputs:
        signal: 1D numpy array of input signal or sequence
        k : number of terms to be included in HOC sequence

        Return:
        nzc: 1D numpy array of HOCs corresponding to sequence
             of high-pass filters
        """
        nzc = []    # list to store results
        try:

            for i in range(k):
                curr_diff = numpy.diff(signal, n=i)

                x_t = curr_diff >= 0   # binary time series signal
                x_t = numpy.diff(x_t)  # taking diff of x_t
                x_t = numpy.abs(x_t)   # taking abs value

                count = numpy.count_nonzero(x_t)
                nzc.append(count)

        except Exception as e:
            print(e)

        return numpy.array(nzc)
