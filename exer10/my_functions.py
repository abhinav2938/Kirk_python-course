from netmiko import ConnectHandler

def ssh_command(a_device):
    print('#'*80)
    print()
    connect = ConnectHandler(**a_device)
    output = connect.send_command_expect('show version')
    print(output)
    connect.disconnect()
    print('#'*80)
    print()
    
def ssh_command2(a_device):
    print('#'*80)
    print()
    ssh_conn = ConnectHandler(**a_device)
    output = ssh_conn.send_command_expect('show version')
    ssh_conn.disconnect()
    return output
    print('#' * 80)
    print()


def ssh_command3(a_device):
    ssh_conn = ConnectHandler(**a_device)
    hostname = ssh_conn.find_prompt()
    if hostname == 'pyclass@srx1>':
        print('*'*80)
        print()
        output = ssh_conn.send_command('show arp')
        return (hostname, output)
        #return ('This is for hostname:{}'.format(hostname))
    else:
        print('#'*80)
        print()
        output = ssh_conn.send_command('show ip arp')
        return output




