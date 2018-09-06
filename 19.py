# Implement calculator program for using Argparse.

import argparse
 
#Addition function
def add(a,b):
    val = a+b
    return val
 
#Subtraction function
def sub(a,b):
    val = a-b
    return val
 
#Division function
def div(a,b):
    val = a/b
    return val
 
#Multiplication function
def multi(a,b):
    val = a*b
    return val
 
#Main function
def Main():
    parser = argparse.ArgumentParser()
 
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-a', '--add', help = 'Performs addition', action = 'store_true')
    group.add_argument('-s', '--sub', help = 'Performs subtraction', action = 'store_true')
    group.add_argument('-d', '--div', help = 'Performs division', action = 'store_true')
    group.add_argument('-m', '--mul', help = 'Performs multiplication', action = 'store_true')
 
    parser.add_argument('num1', help = 'Enter the first operand', type = float)
    parser.add_argument('num2', help = 'Enter the second operand', type = float)
 
    args = parser.parse_args()
     
#Optional arguments
    if args.add:
        print('The addition result of {} and {} is {}'.format(args.num1,args.num2,(add(args.num1,args.num2))))
    elif args.sub:
        print('The subtraction result of {} and {} is {}'.format(args.num1,args.num2,(sub(args.num1,args.num2))))
    elif args.div:
        print('The division result of {} and {} is {}'.format(args.num1,args.num2,(div(args.num1,args.num2))))
    elif args.mul:
        print('The multiplication result of {} and {} is {}'.format(args.num1,args.num2,(multi(args.num1,args.num2))))
    else:
        print('Error:Requires an argument to perform an action')
 
if __name__ == '__main__':
    Main()
