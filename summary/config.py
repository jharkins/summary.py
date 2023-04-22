import os
import configparser

CONFIG_FILE = os.path.join(os.path.dirname(__file__), "config.ini")


def get_config():
    config = configparser.ConfigParser()
    if os.path.exists(CONFIG_FILE):
        config.read(CONFIG_FILE)
        return config
    else:
        return None


def save_config(config):
    with open(CONFIG_FILE, "w") as f:
        config.write(f)


def get_api_key():
    config = get_config()
    if config is None:
        config = configparser.ConfigParser()
        config.add_section("OpenAI")
        api_key = input("Please enter your OpenAI API key: ")
        config.set("OpenAI", "api_key", api_key)
        save_config(config)
        return api_key
    else:
        return config.get("OpenAI", "api_key", fallback=None)