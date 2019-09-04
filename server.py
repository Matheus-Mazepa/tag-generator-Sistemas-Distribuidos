import Pyro4

cont = 0

@Pyro4.expose
class HelloWorld(object):
  def say_hello(self, name):
    return "Hello {0}".format(name)

  def get_tag(self):
    global cont
    cont += 1
    return "Tag " + str(cont)

daemon = Pyro4.Daemon()
uri = daemon.register(HelloWorld)

print("Ready. Object uri =", uri)
daemon.requestLoop()

