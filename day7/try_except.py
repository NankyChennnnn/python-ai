# Author: bibberzz
# Created: 2026/6/1 14:19
# Project: day7
# File: try_except.py
# Description:

def divide(a, b):
    try:
        result = a / b
        print(result)
    except ZeroDivisionError:
        print("除0异常")
    else:
        print("没有异常")
        return 0
    finally:
        print("try-except结束必执行")


divide(10, 2)
divide(10, 0)


def divide2(a, b):
    try:
        result = a / b
        print(result)
    except Exception as e:
        print(f'divide2 error: {e}')
        print(e.__traceback__.tb_lineno)
        print(e.__traceback__.tb_frame.f_globals['__file__'])
    else:
        print("没有异常")
        return 0
    finally:
        print("try-except结束必执行")


divide2(10, 2)
divide2(10, 0)
