#! /usr/bin/python3

import os


def main():
    filetypes = ['pdf', 'epub', 'mobi']
    for filetype in filetypes:
        publish(filetype)

def publish(filetype):
    cmd = 'gitbook {0} ./ _book/ebooks/darkwater.{0}'.format(filetype)
    print(cmd)
    os.system(cmd)

if __name__ == '__main__':
    main()
