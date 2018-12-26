import schedule
import time
from app import index


def main():
    schedule.every().day.at('09:00').do(index)
    while True:
        schedule.run_pending()
        time.sleep(60)


if __name__ == '__main__':
    main()
