<img src="logo_bot.png" width="100" height="100">

# Полезная информация
Нас развалит ВК окончательно 1 ноября. Библиотека прекратила свое существование и разработку. Мы мигрировали в ТамТам, за нас не переживайте.

# VK Teams Bot API для Python
![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)

### [<img src="logo_msg.png" width="16"> Спецификация API VK Teams](https://teams.vk.com/botapi/)

## Начало использования
* Создайте своего бота, отправив команду _/newbot_ в _Metabot_ и следуя инструкциям.
    >Внимание: бот может ответить только после того, как пользователь добавил его в свой список контактов, или если пользователь первым начал диалог.
* Вы можете настроить домен, на котором размещен ваш сервер VK Teams. При создании экземпляра класса Bot добавьте адрес вашего домена.
* Пример использования фреймворка можно увидеть в _example/test_bot.py_.

## Установка
Установка из исходников:
```bash
git clone https://github.com/alex3ysmirnov/vkteams.git
cd vkteams
python setup.py install
```
Установка с PyPi:
```bash
pip install --upgrade vkteams
```
