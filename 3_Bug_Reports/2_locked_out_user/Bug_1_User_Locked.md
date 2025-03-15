## Баг #1: Пользователь locked_out_user не может войти

**Серьезность**: Critical  
**Приоритет**: High  
**Окружение**: Edge 125, Windows 10  

### Шаги:
1. Введите логин `locked_out_user`, пароль `secret_sauce`.
2. Нажмите Login.

### Ожидаемый результат:
Успешный вход.

### Фактический результат:
Сообщение: **Epic sadface: Sorry, this user has been locked out**.