# full automation

Вся магия находится в директории [.cicd](../.cicd)
- [site.yml](site.yml) - единая точка входа

Перед запуском задать значение переменной `run_site_secret_key` (default: `run_site_secret_key: "$up3RseCR37"`). Для генерации можно использовать вот такую команду (запускать в Linux):

```bash
date +%s | sha256sum | base64 | head -c 64 ; echo
```
