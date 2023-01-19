import time

def get_timestamp() -> str:
    return time.strftime('%Y-%m-%d_%H_%M_%S', time.localtime(time.time()))