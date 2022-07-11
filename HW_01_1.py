"""Напишите классы сериализации контейнеров с данными Python в json, bin файлы. Сами классы должны соответствовать
общему интерфейсу (абстрактному базовому классу) SerializationInterface."""
import json
import pickle
from abc import ABCMeta, abstractmethod


class SerializationInterface(metaclass=ABCMeta):
    @abstractmethod
    def write_to_file(self, filename, content):
        pass

    @abstractmethod
    def read_from_file(self, filename):
        pass


class SerBin(SerializationInterface):
    def write_to_file(self, filename, content):
        with open(filename, "wb") as fh:
            pickle.dump(content, fh)

    def read_from_file(self, filename):
        with open(filename, 'rb') as fh:
            unpacked = pickle.load(fh)
        return unpacked


class SerJSON(SerializationInterface):
    def write_to_file(self, filename, content):
        with open(filename, "w") as fj:
            jsonfile = {'content': content}
            json.dump(jsonfile, fj)

    def read_from_file(self, filename):
        with open(filename, "r") as fj:
            unpack = json.load(fj)
        return unpack['content']
