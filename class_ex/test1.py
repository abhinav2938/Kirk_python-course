from netmiko import ConnectHandler
from getpass import getpass

ssh_connect = ConnectHandler(
        host = 'cisco3.lasthop.io',
        username = 'pyclass',
        password = getpass(),
        device_type = 'cisco_ios',
        session_log = 'my_session.txt' 
        )

print(ssh_connect.find_prompt())
