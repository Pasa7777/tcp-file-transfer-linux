Это приложение передает файлы по протоколу tcp

**Установка**

1. Клонируйте этот репозиторий
2. Зарегистрируйтесь в ngrok

https://ngrok.com
![alt text](https://raw.githubusercontent.com/Pasa7777/tcp-file-transfer/main/ngrok_photo.jpg)
3. Во время приема файлов вставьте с сайта команду регистрации ngrok
Пример : 

ngrok config add-authtoken XXXXXXXXXXXXXXXXXXXX

**Внимание!**
Во время приема файлв с одной стороны откроется окно ngrok.
В нем надо передать собеседнику ваш IP. Он находится во вкладке Forwarding

![image](https://github.com/Pasa7777/tcp-file-transfer/assets/106025935/fc2b02d0-5a4a-46ee-91fc-efa123bd692d)

Отправитель должен написать это IP без tcp:// 

Оригинал передатчика:

https://github.com/thelaycon/tcp-file-transfer
