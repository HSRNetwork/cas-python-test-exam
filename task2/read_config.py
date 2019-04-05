import yaml
import requests


def get_url(ip_address, url):
    return f'https://{ip_address}:55443/api/v1{url}'


def get_interfaces(device_information):
    response = requests.get(get_url(device_information['connection_address'], '/interfaces'))
    if response.status_code == 200:
        return response.json()
    else:
        print(f'Error while querying interfaces of device {device_information["connection_address"]}')
        print(f'{response.status_code}: {response.reason}')

def load_devices():
    with open('device_infos.yaml', 'r') as host_file:
        data = yaml.load(host_file.read(), Loader=yaml.FullLoader)
        return data


if __name__ == '__main__':
    devices = load_devices()
    for device_information in devices:
        interfaces = get_interfaces(device_information)
