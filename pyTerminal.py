#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on 2022年3月24日
@author: HXYMCH
'''

import cmd, sys, time, platform, os


pyVer = platform.python_version()

name = input('Please enter your ID(if you don*t have an ID please leave it blank to register):')
if name == '':
    newName = input('please enter your New ID:')
    newPassword = input('please enter your New Password:')
    print('You are registing...')
    u = open('uid.txt','r')
    uid = u.read()
    u.close()
    newuid = eval(uid)
    newuid.append({'name':newName, 'password':newPassword})
    u = open('uid.txt','w')
    u.seek(0)
    u.truncate()
    u.write(str(newuid))
    u.close()
    print('You are in the shell!\n')
else:
    password = input('Please enter your Password:')
    u = open('uid.txt','r')
    uid = u.read()
    u.close()
    uid = eval(uid)
    for i in uid:
        if i['password'] == password and i['name'] == name:
            print('You are in the shell!\n')
            time.sleep(0.5)

class pyTerminal(cmd.Cmd):
    intro = 'Welcome to the pyTerminal shell by HXYMCH.\n'+'Type help or ? to list commands.'+'\nYou are in python '+pyVer + '.\n'
    prompt = ''
    file = None

    def do_none(self,arg):
        print('')
        return None
    
    def help_none(self):
        print('Use it for None.\n')
    
    def do_calc(self,arg):
        os.system('app\calc.py')
        return 0
    
    def help_calc(self):
        print('open a calculator.')

    def do_cmd(self,arg):
        os.system(arg)
        return 0

    def help_cmd(self):
        print('Do like cmd.\n')

    def do_stop(self, arg):
        print('Thank you for using pyTerminal, and the shell will be close in 2 seconds.')
        for i in range(1, 4):
            print("\r", end="")
            print("Stopping".format(i), "." * (i//1), end="")
            sys.stdout.flush()
            time.sleep(0.4)
        sys.exit()
        return True

    def help_stop(self):
        print('Use it to close the shell.\n')

def parse(arg):
    return tuple(map(int, arg.split()))

if __name__ == '__main__':
    pyTerminal().cmdloop()
