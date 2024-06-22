import subprocess

# Ejecutar el comando desde Python
subprocess.call(["gsutil", "-m", "cp", "-r", "gs://zaia-health-dev_pocs/etl/typeSideEffect", "C:\Developer_1.0\Proyecto_GCP\\"], shell=True)



