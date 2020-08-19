#!/usr/bin/python3
"""Module to find a peak in a list"""


def find_peak(list_of_integers):
    """Find a peak"""
    if list_of_integers:
        my_peaks = []
        for a in range(len(list_of_integers)):
            if a == 0:
                if list_of_integers[a] > list_of_integers[a + 1]:
                    my_peaks.append(list_of_integers[a])
                    continue
            elif a == len(list_of_integers):
                if list_of_integers[a] > list_of_integers[a - 1]:
                    my_peaks.append(list_of_integers[a])
                    continue
            else:
                if (list_of_integers[a] - list_of_integers[a - 1] > 0 and
                        list_of_integers[a] -
                        list_of_integers[a + 1] > 0):
                    my_peaks.append(list_of_integers[a])
        return my_peaks
    else:
        return None
