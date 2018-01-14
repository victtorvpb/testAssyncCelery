from tasks import hello

if __name__ == '__main__':
    for i in range(10000):
        hello.apply_async(args=(i,))