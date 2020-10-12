from q2 import create_checkpoint
from q1b import conn
from getpass import getpass
from my_devices import nxos1
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


if __name__ == '__main__':

    connect = conn(nxos1)
   # create_checkpoint(connect)

    #q4d
    print('Repacing the configuration')
    connect.load_replace_candidate(filename = 'chkpoint_modified.txt')
    print(connect.compare_config())

    print('discarding the config changed')
    connect.discard_config()
    print('comparing again after the discard')
    print(connect.compare_config())

    


