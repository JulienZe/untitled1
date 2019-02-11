import random
from retrying import retry

import random
from retrying import retry
import time


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


# test_wait_random()


# 6、wait_exponential_multiplier-间隔时间倍数增加，wait_exponential_max-最大间隔时间
@retry(wait_exponential_multiplier=1000, wait_exponential_max=10000)
def test_wait_exponential():
    print("test %d" % int(time()))
    raise Exception


# test_wait_exponential()


# 7、retry_on_exception：指定异常类型，指定的异常类型会重试，不指定的类型，会直接异常退出，wrap_exception参数设置为True，则其他类型异常，或包裹在RetryError中，会看到RetryError和程序抛的Exception error
def retry_if_io_error(exception):
    print("---------------------------")
    return isinstance(exception, FileNotFoundError)


@retry(retry_on_exception=retry_if_io_error)
def this_maybe_has_error():
    try:
        print("test")
        with open("aa.txt", 'r') as f:
            f.readlines()
    except FileNotFoundError as e:
        raise FileNotFoundError


this_maybe_has_error()


# 此时会重复调用this_maybe_has_error()


def retry_if_io_error(exception):
    print("---------------------------")
    return isinstance(exception, FileNotFoundError)


@retry(retry_on_exception=retry_if_io_error, wrap_exception=True)
def test_retry_error():
    print("Retry forever with no wait if an FileNotFoundError occurs, raise any other errors wrapped in RetryError")
    raise Exception('a')


test_retry_error()
# 只会调用一次即结束
