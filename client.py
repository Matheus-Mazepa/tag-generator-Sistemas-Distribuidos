import Pyro4

uri = input("URI Object? ").strip()

hello_world = Pyro4.Proxy(uri)
flag = "s"
while flag.lower() == "s":
    print(hello_world.get_tag())
    flag = raw_input("Deseja continuar criando etiquetas? S/N ").strip()


