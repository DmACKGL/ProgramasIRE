import pxssh
import urllib 
import re 
while True:
           print ("""
           1. Usos Comunes
           2. Network
           3. Salir
           """)
           True= raw_input("Que Necesitas? = ")
           if True == "1":
                             while True:
                                        print ("""
                                        1. Calculadora
                                        2. Salir
                                        """)
                                        True= raw_input("Que Necesitas? = ")
                                        if True == "1":
                                               while True:
                                                         print ("""
                                                         1. Suma
                                                         2. Resta
                                                         3. Multiplicacion
                                                         4. Divicion
                                                         5. Salir
                                                         """)
                                                         True= raw_input("Que Necesitas? = ")
                                                         if True == "1":
                                                                            print ("")
                                                         elif True == "5":
                                                                            break
                                        elif True == "2":
                                                           break
           elif True == "2":
                              while True:
                                        print ("""
                                        1. IP Externa
                                        2. SSH
                                        """)
                                        True= raw_input("Que Necesitas? = ")
                                        if True == "1":
                                            print "Buscando..."
                                            print "Utilizando Servidor: DynDNS"
                                            servidor= "http://checkip.dyndns.org/"
                                            request = urllib.urlopen(servidor).read()
                                            IPResul = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}.\d{1,3}", request)
                                            print "La IP de esta maquina es: ", IPResul
                                        elif True == "2":
                                              s = pxssh.pxssh()
					      if not s.login ('localhost', 'root', '13251325CD'):
						    print "ERROR al conectar con gastly."
						    print str(s)
					      else:
						    print "Conectado..."
						    s.sendline ('htop')
						    s.prompt()         
           elif True == "3":
                                break
                                                        
