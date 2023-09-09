import subprocess

# Указываем команду для запуска сервера Django
command = "python manage.py runserver 0.0.0.0:8000"

# Запускаем сервер Django с помощью subprocess
try:
    subprocess.run(command, shell=True, check=True)
except subprocess.CalledProcessError as e:
    print(f"Произошла ошибка при запуске сервера: {e}")
