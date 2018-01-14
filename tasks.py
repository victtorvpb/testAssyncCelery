from celery import Celery
from random import randint

app = Celery('test', broker='amqp://guest:guest@localhost//')
app.conf.task_routes = {'tasks.hello':  {'queue': 'hello'}}


@app.task
def hello(i):
    import time
    time.sleep(randint(0,30))
    print(i)
    return 'hello world'