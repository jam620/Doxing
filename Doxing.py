#coded by Jey Zeta
#Usar python 2.7
# coding: utf8
import sys, os, webbrowser, platform, subprocess

import webbrowser

def __limpiar():
	if os.name == 'nt':
            os.system('cls')
	else:
            os.system('clear')
def menu():
	__limpiar()

	print """
\033[1;31m                                  
\033[1;31m
\033[1;31m              
\033[1;31m              +';;+               
\033[1;31m             ''';;;+              
\033[1;31m            +''+++';#             
\033[1;31m           .'''';;;+;`            
\033[1;31m           ''''';;;;'+            
\033[1;31m          ,+'''';;;;;'            
\033[1;31m          +''  ';:  ;+'           
\033[1;31m          '''  .;  .;'+           
\033[1;31m          '''''';;;;;;+           
\033[1;31m          '''''';;;;;;`           
\033[1;31m          .''''';;;;;'            
\033[1;31m           +'''';;;;;             
\033[1;31m            +''';;;;`             
\033[1;31m         :+''''';;;;;'+           
\033[1;31m        +''''''';;';;;;;#         
\033[1;31m       ''''''''';';;;;;;;+        
\033[1;31m      +''''''''':;;;;;;;;;+       
\033[1;31m      '''''''''';'''''''';;       
\033[1;31m     +'''''''''';;;;;;;;+;;;      
\033[1;31m     '''+''''''';;;;;;;;#;;;      
\033[1;31m    #'''#''''''';;;;;;;;';;;,     
\033[1;31m    ''''+''''''':;;;;;;;;;;;'     
\033[1;31m   ;'''''''''''':;;;;;;;;';;;.    
\033[1;31m   +'''+'''''''':;;;;;;+++;;;#    
\033[1;31m   ''''''''''''':;;;;;;+;;;;;+    
\033[1;31m   '''''++'''''':;;;;;;'+;;;;#    
\033[1;31m   +'''+'+'''''':;;;;;;;;;;;;     
\033[1;31m    .+'#'+'''''';''''''';''+      
\033[1;31m        ;''''''':;;;;;;;+         
\033[1;31m       .:::::::::::::::          
					  \033[1;31mHacking Live\033[1;m
			  \033[1;34mHecho por:\033[1;m Victor Bancayan & Kelvin Parra
  				       \033[1;35mVersion: Beta 1.0
				 \033[1;31m Modificado Dojo Panama\033[1;m
  				      
"""
	print '''

1. Pipl         7. Registro             13. Censo               19. Fake Name           25. NICpa
2. Verificate   8. Aviso Operaciones    14. Ubicar Vechiculo    20. Wayback Machine     26. SkypeIp
3. RE           9. Datos Abiertos       15. Tarjeta PV          21. Whois               27. Pwned
4. IMEI         10. Cepadem             16. Reverse IP          22. DNS                 28. Username
5. RUC          11. ExifData            17. Licencia            23. StalkScan           29. Dojo
6. Tinfoleak    12. SPA                 18. Avatar              24. Findsubdomain       30. Exit

		'''
	d = raw_input("\033[1;30m Doxing > ")

	if d == "1":
		webbrowser.open('https://pipl.com/')

		menu()
	elif d == "2":
		webbrowser.open('http://verificate.pa/')
		menu()
	elif d == "3":
		webbrowser.open('http://www.rere.pa/ReReApp/ConsultarDireccionActual.aspx')
		menu()
	elif d == "4":
		webbrowser.open('https://www.doctorsim.com/pa-es/chequear-celular-imei/')
		menu()
	elif d == "5":
		webbrowser.open('https://etax2.mef.gob.pa/etax2web/Login.aspx')
		menu()
	elif d == "6":
		webbrowser.open('https://tinfoleak.com/')
		menu()
	elif d == "7":
		webbrowser.open('https://registro-publico.gob.pa/')
		menu()
	elif d == "8":
		webbrowser.open('https://panamaemprende.gob.pa/login')
		menu()
	elif d == "9":
		webbrowser.open('https://www.datosabiertos.gob.pa/')
		menu()
	elif d == "10":
		webbrowser.open('https://formulario-cepadem.mef.gob.pa/register')
		menu()
	elif d == "11":
		webbrowser.open('http://exifdata.com')
		menu()
	elif d == "12":
		webbrowser.open('https://spa.sistemapenalacusatorio.gob.pa/')
		menu()
	elif d == "13":
		webbrowser.open('http://www.contraloria.gob.pa/INEC/Sistema/Default.aspx')
		menu()
	elif d == "14":
		webbrowser.open('https://311web.innovacion.gob.pa/Pages/VehicleLicenseSearch.aspx')
		menu()
	elif d == "15":
		webbrowser.open('https://www.tarjeta.com.pa/consultatpv/')
		menu()
	elif d == "16":
		webbrowser.open('https://viewdns.info/reverseip/')
		menu()
	elif d == "17":
		webbrowser.open('http://www.licencia.com.pa/historial/historial.jsf')
		menu()
	elif d == "18":
		webbrowser.open('https://faceapp.com/')
		menu()
	elif d == "19":
		webbrowser.open('https://www.fakenamegenerator.com/')
		menu()
	elif d == "20":
		webbrowser.open('https://archive.org/web/')
		menu()
	elif d == "21":
		webbrowser.open('http://whois.domaintools.com/')
		menu()
	elif d == "22":
		webbrowser.open('https://dnsdumpster.com/')
		menu()
	elif d == "23":
		webbrowser.open('https://stalkscan.com/')
		menu()
	elif d == "24":
		webbrowser.open('https://findsubdomains.com/')
		menu()
	elif d == "25":
		webbrowser.open('http://www.nic.pa/')
		menu()
	elif d == "26":
		webbrowser.open('http://mostwantedhf.info/')
		menu()
	elif d == "27":
		webbrowser.open('https://haveibeenpwned.com/')
		menu()
	elif d == "28":
		webbrowser.open('https://namechk.com/')
		menu()
	elif d == "29":
		webbrowser.open('https://comunidaddojo.online/')
		menu()
	elif d == "30":
		sys.exit()

menu()
