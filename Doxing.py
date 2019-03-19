#coded by Jey Zeta
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

\033[1;31m                                ____            _
\033[1;31m                               |  _ \  _____  _(_)_ __   __ _
\033[1;37m                               | | | |/ _ \ \/ / | '_ \ / _` |
\033[1;37m                               | |_| | (_) >  <| | | | | (_| |
\033[1;31m                               |____/ \___/_/\_\_|_| |_|\__, |
\033[1;31m                                                        |___/

					  \033[1;31mHacking Live\033[1;m
			  \033[1;34mHecho por:\033[1;m Victor Bancayan & Kelvin Parra
  				       \033[1;35mVersion: Beta 1.0
				       \033[1;31m Modificado APPIF Para Panamá\033[1;m
  				      
"""
	print '''
\033[1;32m 1. Pipl 	 \033[1;32m 7. Registro            \033[1;32m 13. Censo           \033[1;32m19. Sanciones   \033[1;32m 25. Direccion
\033[1;32m 2. Verificate	 	 \033[1;32m 8. Aviso Operaciones         \033[1;32m 14. Ubicar Vechiculo    \033[1;32m   20. Sat 	 \033[1;32m 26. SkypeIp
\033[1;32m 3. Registro Electoral    	 \033[1;32m 9. Datos Abiertos       \033[1;32m  15. BuscarDatos  \033[1;32m   21. Runt  	 \033[1;32m 27. Multas
\033[1;32m 4. IMEI    \033[1;32m 10. Cepadem       \033[1;32m 16. Certificados   \033[1;32m 22. Libreta \033[1;32m     28. Username
\033[1;32m 5. Ruc       	\033[1;32m 11. ExifData       \033[1;32m 17. Licencia  	 \033[1;32m23. StalkScan  \033[1;32m  29. About
\033[1;32m 6. Tinfoleak   \033[1;32m 12. SPA   \033[1;32m 18. Curp          \033[1;32m  24. Colegiados  \033[1;32m 30. Exit

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
		webbrowser.open('https://wsp.registraduria.gov.co/censo/_censoResultado.php')
		menu()
	elif d == "14":
		webbrowser.open('https://311web.innovacion.gob.pa/Pages/VehicleLicenseSearch.aspx')
		menu()
	elif d == "15":
		webbrowser.open('http://buscardatos.com/')
		menu()
	elif d == "16":
		webbrowser.open('http://certificados.sena.edu.co/')
		menu()
	elif d == "17":
		webbrowser.open('http://www.licencia.com.pa/historial/historial.jsf')
		menu()
	elif d == "18":
		webbrowser.open('https://consultas.curp.gob.mx/')
		menu()
	elif d == "19":
		webbrowser.open('https://consulta.simit.org.co/Simit/index.html')
		menu()
	elif d == "20":
		webbrowser.open('https://www.sat.gob.pe/Websitev9')
		menu()
	elif d == "21":
		webbrowser.open('https://www.runt.com.co/consultaCiudadana/#/consultaPersona')
		menu()
	elif d == "22":
		webbrowser.open('https://www.libretamilitar.mil.co/Modules/Consult/MilitarySituation')
		menu()
	elif d == "23":
		webbrowser.open('https://stalkscan.com/')
		menu()
	elif d == "24":
		webbrowser.open('http://www.cipica.com/buscolegiado/buscolegiado.php')
		menu()
	elif d == "25":
		webbrowser.open('http://www.midis.gob.pe/padron/')
		menu()
	elif d == "26":
		webbrowser.open('http://mostwantedhf.info/')
		menu()
	elif d == "27":
		webbrowser.open('http://aplicaciones007.jne.gob.pe/multas/')
		menu()
	elif d == "28":
		webbrowser.open('https://namechk.com/')
		menu()
	elif d == "29":
		webbrowser.open('https://www.facebook.com/HackingEnVivo/')
		menu()
	elif d == "30":
		sys.exit()

menu()
