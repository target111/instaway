import random, time


def sleep_random(duration: tuple) -> None:
    """
    sleep_random is designed to emulate a human user by pausing execution of the
    program (sleeping) for a random duration of time between `a` and `b` seconds.
    :param duration: tuple containing two floats: `a` is the minimum sleep duration while `b` is the maximum duration
    """
    a: float = 0
    b: float = 0
    try:
        a, b = duration
    except ValueError as e:
        print(e)
    sleep_time = random.uniform(a, b)
    print(f'Pausing execution flow for {sleep_time} seconds...')
    time.sleep(sleep_time)
