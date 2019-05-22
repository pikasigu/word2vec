# %%
import datetime
import time


def main():
    for count in range(0, 10):
        print_current_time()
        time.sleep(1)


def print_current_time():
    print(datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S'))


if __name__ == '__main__':
    main()
