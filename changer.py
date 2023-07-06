#!/usr/bin/env python3

import subprocess
import optparse


def get_args():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-a", "--address", dest="new_mac", help="The new MAC address")
    (options, arguments) = parser.parse_args()
    return options.interface, options.new_mac


def change_mac(interface, new_mac):
    print(f"[*] Changing MAC address for {interface} to {new_mac}")
    subprocess.call(f'ifconfig {interface} down', shell=True)
    subprocess.call(f'ifconfig {interface} hw ether {new_mac}', shell=True)
    subprocess.call(f'ifconfig {interface} up', shell=True)


def main():
    interface, new_mac = get_args()
    change_mac(interface, new_mac)


if __name__ == '__main__':
    main()