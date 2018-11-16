import time
from single_requests import get_player_info
from serialization import interval_dumper
import logging

INTERVAL = 10

def main_loop():
    dumper = interval_dumper()
    logging.info("玩家信息获取系统 Alpha v0.0.2")
    logging.info("author: liubai01")
    while True:
        ret = get_player_info()
        if ret:
            logging.info("成功获取玩家信息: 长度[{}], 在线人数：[{}]".format(
                len(str(ret)), ret['currentcount'])
            )
            dumper.dump(ret)
        else:
            logging.info("获取玩家信息失败")
        logging.info("等待{}秒至下一次获取".format(INTERVAL))
        time.sleep(INTERVAL)
