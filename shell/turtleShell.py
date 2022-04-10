# !/usr/bin/python
# -*- coding: UTF-8 -*-

# awa~

'''
Created on 2022年4月10日 4.10 2022
@author: HXYMCH
'''

import cmd
from turtle import *
import sys, os
import platform


pyVer = platform.python_version()

'''
make a Turtle shell.
'''

class Turtle(cmd.Cmd):
    intro = 'Welcome to the turtle shell by HXYMCH.\n'+'Type help or ? to list commands.'+'\nYou are in python '+pyVer + '.\n'
    prompt = '>>Turtle>> '
    file = None
    
    def do_forward(self,arg):
        forward(*parse(arg))

    def do_right(self, arg):
        right(*parse(arg))
    
    def do_left(self, arg):
        left(*parse(arg))
    
    def do_goto(self, arg):
        goto(*parse(arg))
    
    def do_home(self, arg):
        home()
    
    def do_circle(self, arg):
        circle(*parse(arg))
    
    def do_position(self, arg):
        print('Current position is %d %d\n' % position())
    
    def do_heading(self, arg):
        print('Current heading is %d\n' % (heading(),)+'°')
    
    def do_color(self, arg):
        color(arg.lower())
    
    def do_undo(self, arg):
        'Undo (repeatedly) the last turtle action(s):  UNDO'
    
    def do_reset(self, arg):
        reset()
    
    def do_bye(self, arg):
        print('Thank you for using Turtle')
        self.close()
        bye()
        return True

    def emptyline(self):
        pass

    def default(self, arg):
        print('Please input something!')

def parse(arg):
    return tuple(map(int, arg.split()))


'''
run the Turtle shell
'''

if __name__ == '__main__':
    try:
        os.system('cls')
        shell = Turtle()
        shell.cmdloop()
    except:
        exit()
