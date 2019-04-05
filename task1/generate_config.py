import jinja2
import yaml


def render_config(template, device):
    config = template.render(**device)
    return config


def load_template():
    with open('config.j2', 'r') as template_file:
        template_text = template_file.read()
        template = jinja2.Template(template_text)
        return template


def load_devices():
    with open('device_infos.yaml', 'r') as host_file:
        data = yaml.load(host_file.read(), Loader=yaml.FullLoader)
        return data


if __name__ == '__main__':
    devices = load_devices()
    template = load_template()
    for device_information in devices:
        config = render_config(template, device_information)
        print(config)
