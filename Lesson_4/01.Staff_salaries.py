from sys import argv

if argv.count() == 5 and 'salary' in argv[1] and argv[2].isdigit() and argv[3].isdigit() and argv[4].isdigit():
    print((argv[2] * argv[3]) + argv[4])
