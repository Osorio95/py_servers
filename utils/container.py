import sys
import docker

def get_docker_client():
    try:
        # Intenta crear un cliente de Docker desde el entorno
        docker_client = docker.from_env()

        # Verifica si el cliente se creó correctamente
        if docker_client.ping():
            print("El daemon de Docker está en funcionamiento.")
            return docker_client
        else:
            print("El daemon de Docker no está en ejecución o no se pudo verificar correctamente.")
            sys.exit(1)  # Interrumpir la ejecución de Python
    except docker.errors.DockerException:
        print("No se pudo crear el cliente de Docker. Asegúrate de que Docker esté instalado y en ejecución.")
        sys.exit(1)  # Interrumpir la ejecución de Python
