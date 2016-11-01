import random


def randchar(filename, digit=12, num=200):
    source = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    f = open(filename, 'a')
    for i in range(0, num):     
        for m in range(0, digit):
            f.write(random.choice(source))
        f.write('\n')
    f.close()
    print('Done!')

if __name__ == '__main__':
    filename2 = 'random_char.txt'
    digit2 = 12
    num2 = 10
    randchar(filename2, digit2, num2)
