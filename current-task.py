# example of getting the current task
import asyncio
import time

# define a main coriutine
async def main():
    # report a message
    print(f'{time.ctime()} main coroutine started')
    # get the task
    task = asyncio.current_task()# report its details
    # report its details
    print(f'{time.ctime()}{task}')

# start the asyncio program
asyncio.run(main())

Fri Jul 14 08:48:10 2023 main coroutine started
Fri Jul 14 08:48:10 2023<Task pending name='Task-1' coro=<main() running at c:\Asyncio-1\current-task.py:12> cb=[_run_until_complete_cb() at C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.11_3.11.1264.0_x64__qbz5n2kfra8p0\Lib\asyncio\base_events.py:180]>
