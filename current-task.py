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