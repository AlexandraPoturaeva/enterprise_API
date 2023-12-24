# enterprise_API

Данный сервис выполнен в качестве учебного проекта по изучению Django REST framework.

## Описание

В организации существует множество подразделений.
Подразделение может быть частью другого подразделения.
В каждом подразделении могут быть различные должности.
Каждый сотрудник организации может занимать несколько должностей.
Сотрудники имеют определенный набор прав, в зависимости от их должностей.

## Задача

Cоздать REST-api для управления структурой компании и правами сотрудников.

## Технологии

[![Python](https://img.shields.io/badge/Python-464641?style=flat-square&logo=Python)](https://www.python.org/)
[![Django REST framework](https://img.shields.io/badge/Django+DRF-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![Docker](https://img.shields.io/badge/Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)

## Запуск проекта локально

Клонировать репозиторий: 

```
git clone https://github.com/AlexandraPoturaeva/enterprise_API.git
```
Перейти в корень проекта:

```
cd .../enterprise_API
```

Создать и активировать виртуальное окружение

Windows:

```
python -m venv venv
venv\Scripts\activate
```
Linux:

```
python -m venv venv
source venv\Scripts\activate
```

Установить зависимости из файла requirements.txt

```
pip install -r requirements.txt
```

При необходимости создать и применить миграции:

```
python manage.py makemigrations
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

## Запуск проекта в Docker

Выполнить в командной строке: 

```
docker pull ghcr.io/alexandrapoturaeva/enterprise_api:release
```

Запустить контейнер: 

```
docker run -p 8001:8000 ghcr.io/alexandrapoturaeva/enterprise_api:release
```

## Тестирование проекта на удалённом сервере

Проект доступен по адресу http://apoturaeva.site:8003/swagger/