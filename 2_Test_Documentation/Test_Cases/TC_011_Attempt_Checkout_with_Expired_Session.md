# Тест-кейс 12: Попытка оформить заказ с истекшей сессией

## ID
TC-012

## Приоритет
Средний

## Тип теста
Функциональный

## Окружение
- Браузер: Chrome 120
- ОС: Windows 11

## Предусловие
Пользователь авторизован, и в корзине есть товар.

## Тестовые данные
- Имя: "John".
- Фамилия: "Doe".
- Почтовый индекс: "12345".

## Шаги
1. Перейти в корзину.
2. Нажать кнопку "Checkout".
3. Дождаться истечения сессии (например, подождать 30 минут).
4. Заполнить форму:
   - Ввести имя.
   - Ввести фамилию.
   - Ввести почтовый индекс.
5. Нажать кнопку "Continue".

## Ожидаемый результат
Отображается сообщение об ошибке: "Your session has expired. Please log in again."

## Фактический результат
(Заполняется во время тестирования)

## Связанные баг-репорты
- Нет