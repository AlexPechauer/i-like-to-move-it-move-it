import subprocess
from daemon import Daemon
import sys, time
import os



class Mouse(Daemon):
  # def __init__(self):

  def run(self):
    self.dir_path = os.path.dirname(os.path.realpath(__file__))
    self.python_bin = self.dir_path + "/mickey/bin/python3"
    self.script_file = self.dir_path + "/mickey.py"
    self.mover = subprocess.Popen([self.python_bin, self.script_file])
    while True:
      time.sleep(1)

  def quit(self):
    self.mover.kill()

if __name__ == "__main__":
  daemon = Mouse()
  if len(sys.argv) == 2:
    if 'start' == sys.argv[1]:
      daemon.start()
    elif 'stop' == sys.argv[1]:
      daemon.stop()
    elif 'restart' == sys.argv[1]:
      daemon.restart()
    else:
      print("Unknown command")
      sys.exit(2)
    sys.exit(0)
  else:
    print("usage: %s start|stop|restart" % sys.argv[0])
    sys.exit(2)