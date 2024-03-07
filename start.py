import os
import ngrok
print("Вы желаете получить [1] или отправить [2] файл")
command = int(input())
# print("Вы желаете использовать шифрование? (y/n)")
# cryptography = input()

def priem():
    header = 1024
    port = 20000
    print("Введите кол-во данных, которые будут передаваться за 1 раз (в байтах) без пробелов: ")
    buffer_size = int(input())
    print("Введите токен ngrok")
    authtoken =input()
    ngrok.set_auth_token(authtoken)
    listener = ngrok.forward(20000, proto="tcp")
    print(f"Ваш ip - {listener.url()}")
    os.system(f"python tcp.py server --port {port} --buff {buffer_size} --header {header}")

def otpravka():
    ip = input("Введите IP принимателя (без двоеточия и цифр после него и без tcp://): ")
    port = input("Введите порт сервера (как раз эти цифры после двоеточия): ")
    print("Введите путь файла, который вы хотите отправить или его название, если он находится в папке с приложением.\n"
          "Если путь к файлу имеет пробелы, то необходимо поставить вот такие \"\" кавычки: ")
    path = input()
    os.system(f"python tcp.py client --ip {ip} --port {port} --path {path}")
def error():
    print("Вы ввели неправильное значение!")
    input("Нажмите Enter для завершения")
    exit()

if command not in [1, 2]:
    error()

if command == 1:
    priem()

if command == 2:
    otpravka()
