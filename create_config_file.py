from jinja2 import Environment, FileSystemLoader
import yaml

env = Environment(loader=FileSystemLoader('template'), trim_blocks=True, lstrip_blocks=True)
template = env.get_template('manage_router.txt')

devices = yaml.load(open('config_info.yaml'), Loader=yaml.FullLoader)

path = 'router_info/'
for device in devices:
    config_file = path + device['name'] + '_config.txt'
    with open(config_file, 'w') as f:
        f.write(template.render(device))
