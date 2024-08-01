import os
import configparser


def init_config(config_file):
    """
    Initialize the configuration file. If it doesn't exist, create it with default settings.
    """
    config = configparser.ConfigParser()
    if not os.path.exists(config_file):
        config['Settings'] = {
            'path': '~/Documents/CPAP_Data/SD_card',
            'url': 'http://192.168.4.1/dir?dir=A:',
            'import_oscar': 'False',
            'quit_after_completion': 'False'
        }
        config['WiFi'] = {
            'ssid': 'ez Share',
            'psk': '88888888'
        }
        config['Window'] = {
            'x': '100',
            'y': '100'
        }
        with open(config_file, 'w') as configfile:
            config.write(configfile)
    else:
        config.read(config_file)
        if 'Settings' not in config:
            config['Settings'] = {
                'path': '~/Documents/CPAP_Data/SD_card',
                'url': 'http://192.168.4.1/dir?dir=A:',
                'import_oscar': 'False',
                'quit_after_completion': 'False'
            }
        if 'WiFi' not in config:
            config['WiFi'] = {
                'ssid': 'ez Share',
                'psk': '88888888'
            }
        if 'Window' not in config:
            config['Window'] = {
                'x': '100',
                'y': '100'
            }
    return config


def save_config(config, config_file):
    """
    Save the current configuration to the specified file.
    """
    with open(config_file, 'w') as configfile:
        config.write(configfile)
