# RoyalFilms
Para poder utilizar el codigo, descargar los archivos, y editarlos mediante un software como "Visual Studio Code", para luego crear un entorno virtual "flask", el paso a paso para activar flask es:
1. Abrir una terminal cmd

2. copiar y pegar las siguientes lineas (presionar la tecla "Enter" despues de pegar cada una):
py -m venv env
env\Scripts\activate
pip install flask

3. dentro del cmd escribimos el comando:
cd ..
para poder salir de la carpeta env

4. escribimos en el cmd (presionar la tecla "Enter" despues de pegar cada una):
cd Royal Films
set FLASK_APP=main.py

Luego de esto solo debemos ejecutar el codigo desde el "main.py"

NOTA: si al ejecutar el codigo desde el main.py, abrir "Powershell" como administrador y escribir la siguiente linea:
Set-ExecutionPolicy -Scope Currentuser unrestricted
Presionar la tecla "enter", y luego la tecla "S" cuando se pida para aceptar el cambio
