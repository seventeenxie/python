from multiprocessing import Process
import  os
import  time

def test(arg):

     print(arg+'is running')
     time.sleep(3)
if __name__ == '__main__':
   print('father is running %s'%os.getpid())
   p= Process(target=test,args=("ffffff",))

   p.start()

   print("end")
