from napalm import get_network_driver
from getpass import getpass
from pprint import pprint

#supress  ssl warnings
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

#nneed to specify port for nexus devices
if __name__ == '__main__':
    nxos1 = dict(
        hostname= 'nxos1.lasthop.io',
        username = 'pyclass',
        password = getpass(),
        device_type = 'nxos',
        optional_args= {'port':8443}
    )

    device = nxos1.pop('device_type')
    driver = get_network_driver(device)
    dev = driver(**nxos1)

    print()
    print('\n\n>>>Test device open.')
    dev.open()

    print('\n>>> load config change(merge)\n')
    output = dev.load_merge_candidate(filename='nxos_merge.conf')
    pprint(dev.compare_config())

    #discard config changes
    #print('\n>>> discard config changes')
    #dev.discard_config()
    #again check comparision
    #print('changes after discard: {}'.format(dev.compare_config()))

    #commit a config
    print('\n>>> commiting the change:')
    out = dev.commit_config()
    print('changes commit: {}'.format(out))
    #  rollback a commit
    print('rolling back the commit')
    out = dev.rollback()
    print('commit rolled back: {}'.format(out))
