# Repository for test call assyn with Celery

## Run project

 1. Install the requirements
	> `pip install -r  requirements.txt`
 2. Run docker rabbitmq or install the [rabbitmq](https://www.rabbitmq.com/download.html)
	 > `docker run -d --hostname rabbitmq --name rabbitmq -p 15672:15672  -p 5672:5672 -e RABBITMQ_DEFAULT_USER=guest -e RABBITMQ_DEFAULT_PASS=guest rabbitmq:3-management`
3. Start the Celery
	>  `celery -A tasks worker -c <number concurrents> -P eventlet -Q celery,hello --loglevel=info --hostname=localtasks`

4. Execute the project
	> python run.py


