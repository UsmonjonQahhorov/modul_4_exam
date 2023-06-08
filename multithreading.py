import httpx
import threading
import redis
from datetime import timedelta


def thread(name):
    connection = redis.Redis(host="localhost", port=6379, decode_responses=True)
    response = httpx.get(f"https://{name}")
    data = response.content
    connection.set(name=name, value=data, ex=timedelta(seconds=60))


thread1 = threading.Thread(target=thread, args=('kun.uz',))
thread2 = threading.Thread(target=thread, args=("daryo.uz",))
thread3 = threading.Thread(target=thread, args=("qalampir.uz",))
thread4 = threading.Thread(target=thread, args=("google.com",))
thread5 = threading.Thread(target=thread, args=("wikipedia.org",))

thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()
thread5.join()



"""====================#tekshirish===================================="""
# connection = redis.Redis(host="localhost", port=6379, decode_responses=True)
# print(connection.get('kun.uz'))
