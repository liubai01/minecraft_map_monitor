import pickle
import time
import os
import logging

DEFAULT_INTERVAL = 300

def save(obj, path):
    with open(path, "wb") as f:
        ret = pickle.dump(obj, f)
    return ret

def load(path):
    with open(path, "rb") as f:
        ret = pickle.load(f)
    return ret

class interval_dumper():

    def __init__(self, interval=DEFAULT_INTERVAL, prefix="foglake", to_path=r"./database"):
        self.last_save_time = time.time()
        self.cache = []
        self.prefix = prefix
        self.to_path = to_path

    @property
    def get_save_path(self):
        filename = self.prefix + "_" + str(int(time.time()))
        return os.path.join(self.to_path, filename)

    def dump(self, obj):
        self.cache.append(obj)
        if time.time() - self.last_save_time >= DEFAULT_INTERVAL:
            to_path = self.get_save_path
            logging.info("持久化{}调信息至{}".format(len(self.cache), to_path))
            save(self.cache, to_path)
            logging.info("持久化信息完成！")
            self.cache = []
            self.last_save_time = time.time()
