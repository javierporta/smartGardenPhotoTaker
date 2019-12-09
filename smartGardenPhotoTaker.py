from subprocess import call
import requests
from datetime import datetime
from time import sleep
import os

# obter imagem da camera
file_name = "capture.jpg"
print("a capturar imagem...")
#call(["fswebcam", file_name])
os.system('fswebcam -r 1280x720 --no-banner '+ file_name)
sleep(1)
print("ok")


# configurações do serviço Web (alterar para URL correta)
paramUrl = 'https://smart-garden-api.azurewebsites.net/api/Image'
paramAuth = 'bangladesh'
paramKey = 'image'
paramNow = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#paramData = {'auth':paramAuth, 'key':paramKey, 'date':paramNow}
paramFiles = {'image': open(file_name, 'rb')}
# enviar dados para o serviço Web
print("a enviar para o serviço Web...")
# nota: como se vai enviar uma imagem, o 'Content-Type' é automaticamente 'multipart/form-data'
r = requests.post(paramUrl, files=paramFiles)
# mostrar resultados
print(r)
print(r.text)
	
print("Fim do programa.")



