# Тест-кейс 8: Проверка задержек для `performance_glitch_user`

## ID
TC-008

## Приоритет
Средний

## Тип теста
Производительность

## Окружение
- Браузер: Chrome 120
- ОС: Windows 11

## Предусловие
Пользователь `performance_glitch_user` авторизован.

## Шаги
1. Замерить время загрузки главной страницы.

## Ожидаемый результат
Загрузка занимает менее 3 секунд.

## Фактический результат
Загрузка занимает больше 3 секунд.

## Связанные баг-репорты
- [Баг #1: Долгая загрузка главной страницы для `performance_glitch_user`](../../3_Bug_Reports/4_performance_glitch_user/Bug_1_Slow_Page_Load_All_Items.md)
- [Баг #2: Долгая загрузка главной страницы для `performance_glitch_user`](../../3_Bug_Reports/4_performance_glitch_user/Bug_2_Slow_Back_Home.md)