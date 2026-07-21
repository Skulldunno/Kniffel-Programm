import json
import os


class GameSettings:
    def __init__(self):
        self.__data = self.__load_data()

    def __load_data(self):
        if not os.path.exists("settings.json") or os.path.getsize("settings.json") == 0:
            return self.__create_default_settings()

        try:
            with open("settings.json", "r", encoding="utf-8") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return self.__create_default_settings()

    def __create_default_settings(self):
        default_data = {
            "skinset": "black"
            }
        with open("settings.json", "w", encoding="utf-8") as file:
            json.dump(default_data, file, indent=4, ensure_ascii=False)
        return default_data

    def __save_data(self):
        with open("settings.json", "w", encoding="utf-8") as file:
            json.dump(self.__data, file, indent=4, ensure_ascii=False)

    def get_value(self, setting):
        return self.__data.get(setting)

    def set_value(self, setting, value):
        self.__data[setting] = value
        self.__save_data()
