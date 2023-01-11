#!/usr/bin/python3

class MyList(list):
    '''class MyList'''
    def print_sorted(self):
        '''Function that prints the list,
        but sorted (ascending sort)'''
        print(sorted(self))
