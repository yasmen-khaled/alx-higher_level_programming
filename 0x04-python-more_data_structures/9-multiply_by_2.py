#!/usr/bin/python3

def multiply_by_2(a_dictionary):

        _dir = a_dictionary.copy()
            _keys = list(_dir.keys())
                for x in _keys:
                            _dir[x] *= 2

                                return (_dir)

