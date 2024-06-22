# Instalacion de gcloud, al iniciar pedira logeo con tu cuenta gmail nnedzaio, instala la ultima version
#(New-Object Net.WebClient).DownloadFile("https://dl.google.com/dl/cloudsdk/channels/rapid/GoogleCloudSDKInstaller.exe", "$env:Temp\GoogleCloudSDKInstaller.exe")

#& $env:Temp\GoogleCloudSDKInstaller.exe
    
#descarga el archivo

gsutil -m cp -r gs://zaia-health-dev_pocs/etl/typeSideEffect C:\Developer_1.0\Proyecto_GCP\

