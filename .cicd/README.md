# full automation

Вся магия находится в директории [.cicd](../.cicd)
- [site.yml](site.yml) – единая точка входа;
- [files](files) – все статические файлы, которые копируются как есть;
- [task](tasks) – все задачи для разворачивания простейшего проекта на Django;
- [templates](templates) – все шаблоны конфигураций;


Перед запуском задать значение переменной `run_site_secret_key` (default: `run_site_secret_key: "$up3RseCR37"`). Для генерации можно использовать вот такую команду (запускать в Linux):

```bash
date +%s | sha256sum | base64 | head -c 64 ; echo
```

## Полный запуск делается следующим образом
Заполнить файл [inventory.ini](inventory.ini) по аналогии с текущей записью.
```ini
# имя группы хостов
[troyka]
# имя хоста (для себя лично выбираем)
skyhost-vds-22211

# переменные для группы
[troyka:vars]
# хост подключения
ansible_host=193.187.174.202
# пользователь для подключения
ansible_user=root
# путь до интерпретатора python
ansible_python_interpreter=/usr/bin/python3

[all:children]
troyka
```
Установить себе локально [Ansible](https://docs.ansible.com).

> **Важно!** Запуск ansible возможен только на Linux системе.

Склонировать данный репозиторий:
```bash
git clone https://github.com/Linkor-35/django-photo.git
```
Перейти в директорию с автоматизацией и запустить ansible-playbook:
```bash
# переход в директорию с ansible
cd django-photo/.cicd
# установка зависимосте  ansible
ansible-galaxy install -r requirements.yml
# кладем мастер-пароль от секретов
echo "secret" > .vault_pass
# запускаем мастер-плейбук с указанием мастер-пароля
ansible-playbook site.yml --vault-password-file=./.vault_pass
```
Дождаться завершения работы или алерта в [канал](https://t.me/joinchat/UPrS7rPVm9vkMfha).

## Работа с секретами
Хранение секретов реализовано через `ansible-vault`. Подробнее о работе смотреть [документацию](https://docs.ansible.com/ansible/latest/user_guide/vault.html).

Склонировать репозиторий:
```bash
git clone https://github.com/Linkor-35/django-photo.git
```

Переходим в директорию с `ansible`:
```bash
cd django-photo/.cicd
```
Кладем пароль в специальный файл:
```bash
# кладем мастер-пароль от секретов
echo "secret" > .vault_pass
```
Расшифровать файл с секретами:
```bash
ansible-vault decrypt secrets.yml
Decryption successful
```
После расшифровки можно открыть в любом текстовом редакторе и поправить/заменить значения. По завершении редактирования и перед откравкой изменений в репозиторий **ОБЯЗАТЕЛЬНО** зашифровать файл с секретами.

Зашифровать файл с секретами:
```bash
ansible-vault encrypt secrets.yml
Encryption successful
```
## Example
В качестве примера смотреть вот тут: [asciinema](https://asciinema.org/a/P3nWbd1q7Fsp0JkRwItzVv2cZ).

