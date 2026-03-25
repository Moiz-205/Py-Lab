import time


def timer(sec: int, min: int, hr: int):
    if sec == 60:
        min += 1
        sec = 0
    elif min == 60:
        hr += 1
        min = 0
    elif hr == 24:
        hr = 0
        min = 0
        sec = 0
    return sec, min, hr

def clock() -> None:
    sec = 0
    min = 0
    hr = 0
    while True:
        print(f"\r{hr:02} : {min:02} : {sec:02}", end="", flush=True)
        time.sleep(1)
        sec += 1
        sec, min, hr = timer(sec, min, hr)


def main() -> None:
    print("\n==== Clock Timer ====")
    print(clock())


if __name__ == "__main__":
    main()
else:
    print("Error")
