import subprocess
import optparse
import re

def input_arguments():
    parser = optparse.OptionParser()
    parser.add_option('-i', '--interface', dest='interface', help='Enter a network interface')
    parser.add_option('-m', '--mac', dest='mac', help='Enter a new MAC address')
    (options, arguments) = parser.parse_args()
    
    if not options.interface:
        parser.error('[-] Please specify an interface, use --help for more info.')
    elif not options.mac:
        parser.error('[-] Please specify a new MAC address, use --help for more info.')
    
    return options

def change_mac(interface, mac):
    print(f"[+] Changing MAC address for {interface} to {mac}")
    subprocess.call(['ifconfig', interface, 'down'])
    subprocess.call(['ifconfig', interface, 'hw', 'ether', mac])
    subprocess.call(['ifconfig', interface, 'up'])

def get_current_mac(interface):
    try:
        ifconfig_result = subprocess.check_output(['ifconfig', interface]).decode('utf-8')
        mac_address_search = re.search(r'(\w\w:){5}\w\w', ifconfig_result)
        if mac_address_search:
            return mac_address_search.group(0)
        else:
            print("[-] Could not read MAC address.")
            return None
    except subprocess.CalledProcessError:
        print("[-] Could not execute ifconfig.")
        return None

# Main flow
options = input_arguments()
current_mac = get_current_mac(options.interface)
print(f"[+] Current MAC address: {current_mac}")

change_mac(options.interface, options.mac)

new_mac = get_current_mac(options.interface)
if new_mac == options.mac:
    print(f"[+] MAC address was successfully changed to {new_mac}")
else:
    print("[-] MAC address did not change.")
