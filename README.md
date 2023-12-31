# Дистанционное выключение ПК со смартфона
**Приложение на Android создано в конструкторе приложений Mit App Inventor 2. Программа для компьютера написана на Python**<br>
<br>
> Передача команд происходит через MQTT Брокер HiveMq.<br>

Для использования приложения, заригистрируйтесь на сайте [www.hivemq.com](https://www.hivemq.com/), создайте логин и пароль для входа через WebClient<br>
#### Настройка приложения
Для настройки приложения, установите APK файл на свой смартфон из папки Android в репозитории.<br>
После установки, запустите приложение и перейдите во вкладку "Настройки". Введите свои логин и пароль и нажмите на кнопку "Сохранить". После сохранения, статус возле кнопки переподключения должен измениться на "Connected".
#### Настройка диспатчера
Для настройки диспатчера, создайте `.env` файл рядом с основным файлом скрипта и добавьте в него следующее содержание:<br>
```
USERNAME=Ваше имя пользователя HiveMq
PASSWORD=Ваш пароль HiveMq
BROKER=broker.hivemq.com
PORT=1883
```
> В Github Actions этого репозитория находится собранный код диспатчера под Windows/Linux. Если Вы хотите только установить программу без изменения её кода, можете взять эти собранные файлы. Если Вы изменили код диспатчера и хотите собрать его в .exe файл, то делать это нужно с помощью утилиты `pyinstaller`, выполнив следующую комманду `pyinstaller --onefile --windowed main.py`, перед этим установив все нужные модули из файла `requirements.txt`.

После создания `.env` файла, перенесите **ярлык** диспатчера в папку автозапуска (найти её можно выполнив Win+R, затем `shell:startup`). После перезагрузки компьютера, статус в приложении должен измениться на "В сети", если это произошло, значит связь настроена и ПК ожидает комманд, если нет, проверьте правильность введённых данных.
