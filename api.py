from fastapi import FastAPI
from pydantic import BaseModel
from redis import Redis
from rq import Queue

from worker import runTask


app = FastAPI()
redis_conn = Redis(host='apiproj_redis', port=6379, db=0)
q = Queue('my_queue', connection=redis_conn)


# Request body class
class Task(BaseModel):
    owner: str
    description: str = None


@app.get('/holdings',
         responses={
             200: {
                 "content": {"application/csv": {}},
                 "description": "Return CSV or JSON",
             }
         }
         )
def get_the_holdings_file():
    """
    download the holdings file. that's what PMs do.  csv, json formats, gzip
    """
    return None


@app.post('/tasks/holdings/run', status_code=201)
def run_the_holdings_task():
    """
    start the holdings file creation task.  Consumes the datamart odbc datasource and the local cache.
    """
    job = q.enqueue(
        runTask,
        'holdings run'
    )
    return {'job': job}


@app.post('/tasks/cache/update', status_code=201)
def run_the_cache_update_task():
    """
    update cache task
    """
    job = q.enqueue(
        runTask,
        'cache update'
    )
    return {'job': job}


@app.get('/tasks/holdings')
def get_the_status_of_the_holdings_task():
    """
    get the status of the holdings task
    """
    return None


@app.get('/tasks/cache')
def get_the_status_of_the_cache():
    """
    get the status of the cache
    """
    return None


@app.get('/queue')
def get_the_status_of_the_task_queue():
    """
    get the status of the task queue
    """
    return None


@app.get('/test')
def test():
    """Test"""
    return {'hello': 'world'}

#
# @app.post('/tasks/{task_name}', status_code=201)
# def addTask(task_name: str):
#     """
#     Adds tasks to worker queue.
#     Expects body as dictionary matching the Group class.
#     """
#     if task_name not in ('task1', 'task2'):
#         raise HTTPException(
#             status_code=404, detail='task not found'
#         )
#     job = q.enqueue(
#         runTask,
#         task_name
#     )
#     return {'job': job}
#
#
