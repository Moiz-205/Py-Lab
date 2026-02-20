import time


def time_inc(s: int, m: int, h: int):
    if s == 4:
        m += 1
        s = 0
    if m == 4:
        h += 1
        m = 0
    return s, m, h


def clock() -> None:
    s = 0
    m = 0
    h = 0
    while True:
        print(f"\r{h:02} : {m:02} : {s:02}", end="", flush=True)
        time.sleep(1)
        s += 1
        s, m, h = time_inc(s, m, h)


def main() -> None:
    print("\n==== Clock Timer ====")
    print(clock())


if __name__ == "__main__":
    main()
else:
    print("Error")
