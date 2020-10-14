#这段代码没有找到线程池的模块，ThreadPoolExecutor这个模块似乎没有，只有看到了下面那个

import time
import threading
import PriorityThreadPoolExecutor

def moyu_time(name, delay, counter):
  while counter:
    time.sleep(delay)
    print("%s 开始摸鱼 %s" % (name, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
    counter -= 1


if __name__ == '__main__':
  pool = ThreadPoolExecutor(20)
  for i in range(1,5):
    pool.submit(moyu_time('xiaoshuaib'+str(i),1,3))