#!/usr/bin/python
import sh
import os
import subprocess
import argparse

__version__ = 'MegaPy v.1'
__author__ = 'Riley - riley@fasterdevops.com'

megapath = "/opt/MegaCli/"
megadir = os.path.dirname(megapath)
megainstall = ['/usr/bin/yum',
               'install',
               'imh-megapkg',
               '-y']


def main():
    if not os.path.exists(megadir):
        install = raw_input('MegaCLI does not exist on this server! Would you like ' +
                        'to install it now?(yes/no): ').lower()
    if install in ('yes', 'y'):
        subprocess.Popen(megainstall)
    if install in ('no', 'n'):
        print('Closing....')
    else:
        print('Please enter yes or no. Closing...')
if os.path.exists(megadir):

    print __version__

    '''
    Entry point for arguments. Parsing those arguments
    '''
    parser = argparse.ArgumentParser(description='A wrapper to make MegaCLI commands more ' +
                                     ' user friendly and easier to remember'
                                     )
    parser.add_argument('--enclosure',
                        help='View the servers enclosure information',
                        dest='encl'
                        )
    parser.add_argument('--physical',
                        help='View the servers physical drive information',
                        dest='phys'
                        )
    parser.add_argument('--vdrive',
                        help='View the servers virtual drive information',
                        dest='vdrive'
                        )
    parser.add_argument('--controller',
                        help='View the servers controller information',
                        dest='control'
                        )

    args = parser.parse_args()

if __name__ == '__main__':
    main()
