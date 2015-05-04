import os
import urllib 
import re 
while True:
           print ("""
           1. Usos Comunes
           2. Network
           3. Salir
                  """)
           usos= raw_input("Que Necesitas?>")
           if usos == "1":
                             while True:
                                        print ("""
                                        1. Calculadora
                                        2. Salir
                                        """)
                                        comunes= raw_input("Que Necesitas?> ")
                                        if comunes == "1":
                                            os.system('title Calculadora')
                                            while True:
                                        	os.system('cls')
                                            	print '''
                                            	Opciones:
                                            	1. Sumar.
                                        	2.  Restar.
                                        	3.  Multiplicar.
                                        	4.  Dividir.
                                        	5.  Salir.
                                                '''
                                                opc=input("Que opcion quiere?> ")
                                                if opc==1:
                                                    num1=input("Ingrese un numero > ")
                                                    num2=input("Ingrese otro numero > ")
                                                    print (num1 + num2)
                                                    os.system('pause>nul')
                                        	elif opc==2:
                                                    numi1=input("Ingrese un numero > ")
                                                    numi2=input("Ingrese otro numero > ")
                                                    print (numi1 - numi2)
                                                    os.system('pause>nul')
		
                                                elif opc==3:
                                                	numit1=input("Ingrese un numero > ")
                                                    	numit2=input("Ingrese otro numero > ")
                                                        print (numit1 * numit2)
                                                        os.system('pause>nul')
	
                                                elif opc==4:
                                                        numito1=input("Ingrese un numero > ")
                                                        numito2=input("Ingrese otro numero > ")
                                                        print (numito1 / numito2)
                                                        os.system('pause>nul')
		
                                                elif opc==5:
                                                        exit();
                                        elif comunes == "2":
                                                           break
           elif usos == "2":
                              while True:
                                        print ("""
                                        1. IP Externa
                                        2. SSH
                                        """)
                                        net= raw_input("Que Necesitas? = ")
                                        if net == "1":
                                            print "Buscando..."
                                            print "Utilizando Servidor: DynDNS"
                                            servidor= "http://checkip.dyndns.org/"
                                            request = urllib.urlopen(servidor).read()
                                            IPResul = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}.\d{1,3}", request)
                                            print "La IP de esta maquina es: ", IPResul
                                        elif net == "2":
                                              break       
           elif usos == "3":
                                break
                                                        
