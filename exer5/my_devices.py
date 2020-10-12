from getpass import getpass

password = getpass()
nxos1 = {
    'device_type' : 'cisco_ios',
    'username' : 'pyclass',
    'password' : password,
    'host' : 'nxos1.lasthop.io'
}

nxos2 = {
    'host': 'nxos2.lasthop.io',
    'username': 'pyclass',
    'password': password,
    'device_type' : 'cisco_ios'
        }

