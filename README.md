## Структура проекта

sauce-demo-testing/
├── 1_Test_Documentation/
├── 2_Automation/
├── 3_Reports/
├── README.md
└── requirements.txt


## Технологии
- Ручное тестирование: Test Cases, Bug Reports
- Автоматизация: Python + Selenium/Playwright, Postman
- Отчетность: Allure, Markdown

## Как запустить
1. Установите зависимости: `pip install -r requirements.txt`
2. Для UI-тестов: `pytest 2_Automation/Web_UI/`
3. Отчет Allure: `allure serve 3_Reports/Allure_Report/`