import os
import json


class ConfigManager:
    def __init__(self, config_file="D:\\config.json"):
        self.config_file = config_file
        self.config = self.load_config()

    def load_config(self):
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, "r", encoding="utf-8") as file:
                    json.load(file)
            except json.JSONDecodeError:
                print("配置文件格式错误，使用默认配置")
                return {}
        return {}

    def save_config(self):
        with open(self.config_file, "w", encoding="utf-8") as file:
            json.dump(self.config, file, ensure_ascii=False, indent=2)

    def get(self, key, default=None):
        return self.config.get(key, default)

    def set(self, key, value):
        self.config[key] = value
        self.save_config()


config = ConfigManager()
config.set("theme", "dark")
config.set("language", "zh-CN")
config.save_config()
print(config.get("theme"))
