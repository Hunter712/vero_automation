import configparser
import os


def parser_obj():
    parser = configparser.ConfigParser()
    parser.read(os.path.join(get_project_dir(), 'config.ini'))
    return parser


def get_project_dir():
    return os.path.split(os.path.split(os.path.split(__file__)[0])[0])[0]


def get_base_url():
    return parser_obj().get('test_info', 'base_url')


def get_browser_name():
    return parser_obj().get('test_info', 'browser')
