import random
from retrying import retry

import random
from retrying import retry


@retry
def have_a_try():
    if random.randint(0, 10) != 5:
        raise Exception("It's not 5!")
    print('Its 5!')


@retry
def never_give_up_never_surrender():
    print("Retry forever ignoring Exceptions, don't wait between retries")


# have_a_try()

# never_give_up_never_surrender()

@retry(stop_max_attempt_number=7)
def stop_after_7_attempts():
    print("Stopping after 7 attempts")


stop_after_7_attempts()


# 1、只使用@retry，则会一直不停运行
@retry()
def test_retry():
    try:
        1 / 0
    except Exception as e:
        print(e)
        raise e


# test_retry()


# 2,使用stop_max_attempt_number最大运行次数
@retry(stop_max_attempt_number=3)
def test_stop_max_attempt_number():
    try:
        1 / 0
    except Exception as e:
        print(e)
        raise e


# test_stop_max_attempt_number()


# 3、stop_max_delay 设置失败重试的最大时间, 单位毫秒，超出时间，则停止重试
@retry(stop_max_delay=1000)
def test_stop_max_delay():
    try:
        # sleep(2)
        print("test")
        1 / 0
    except Exception as e:
        print(e)
        raise e


# test_stop_max_delay()


# 4、wait_fixed 设置失败重试的间隔时间

@retry(wait_fixed=1000)
def test_wait_fixed():
    try:
        print("test")
        1 / 0
    except Exception as e:
        print(e)
        raise e


# test_wait_fixed()


# 5、wait_random_min, wait_random_max 设置失败重试随机性间隔时间

@retry(wait_random_min=1000, wait_random_max=10000)
def test_wait_random():
    try:
        print("test")
        1 / 0
    except Exception as e:
        print(e)
        raise e


test_wait_random()
