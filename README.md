# api server

![api](api.img?raw=true "api")

build
``````
docker build -t apiproj:latest .
docker-compose up
``````

test
``````
curl -X 'GET'   'http://0.0.0.0:5057/test'

    {"hello":"world"}
``````

HOLDINGS task queued and run in a different process 
``````
curl -X 'POST'   'http://0.0.0.0:5057/tasks/holdings/run'

apiproj_worker_1  | 21:57:16 my_queue: Job OK (5fc525e9-5e99-4da5-8c92-145c7ab4fdf2)
apiproj_worker_1  | 21:57:16 Result is kept for 500 seconds
apiproj_worker_1  | 21:59:36 my_queue: worker.runTask('holdings run') (931c12a6-be87-45c8-9606-fde90ea4bc69)
apiproj_api_1     | ERROR:    Exception in ASGI application
apiproj_api_1     | Traceback (most recent call last):
apiproj_redis_1   | 1:M 09 Aug 2021 21:59:36.203 * 100 changes in 300 seconds. Saving...
apiproj_redis_1   | 1:M 09 Aug 2021 21:59:36.204 * Background saving started by pid 20
apiproj_redis_1   | 20:C 09 Aug 2021 21:59:36.211 * DB saved on disk
apiproj_redis_1   | 20:C 09 Aug 2021 21:59:36.211 * RDB: 0 MB of memory used by copy-on-write
apiproj_redis_1   | 1:M 09 Aug 2021 21:59:36.305 * Background saving terminated with success
apiproj_worker_1  |  
apiproj_worker_1  | task holdings run starting
apiproj_worker_1  |  
apiproj_worker_1  | task holdings run completed 
apiproj_worker_1  |  
apiproj_worker_1  | 21:59:41 my_queue: Job OK (931c12a6-be87-45c8-9606-fde90ea4bc69)
``````


CACHE task queued and run in a different process
``````
curl -X 'POST'   'http://0.0.0.0:5057/tasks/cache/run

apiproj_worker_1  | 22:05:37 my_queue: worker.runTask('cache upate') (7daa6463-d3d1-4b5d-8ed8-337a85850d6e)
apiproj_api_1     | INFO:     172.20.0.1:42976 - "POST /tasks/cache/update HTTP/1.1" 500 Internal Server Error
apiproj_api_1     | ERROR:    Exception in ASGI application
apiproj_api_1     | Traceback (most recent call last):
apiproj_worker_1  |  
apiproj_worker_1  | task cache upate starting
apiproj_worker_1  |  
apiproj_worker_1  | task cache upate completed 
apiproj_worker_1  |  
apiproj_worker_1  | 22:05:42 my_queue: Job OK (7daa6463-d3d1-4b5d-8ed8-337a85850d6e)
``````


deploy
``````
todo
``````
