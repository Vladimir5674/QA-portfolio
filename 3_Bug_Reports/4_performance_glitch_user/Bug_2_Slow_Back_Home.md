## Баг #2: Медленный переход на главную страницу после оформления заказа

**Серьезность**: Major  
**Приоритет**: High  
**Окружение**: Chrome 120, Windows 11  

### Шаги:
1. Оформите заказ как `performance_glitch_user`.
2. Нажмите "Back Home".

### Ожидаемый результат:
Переход на главную страницу за <100 мс.

### Фактический результат:
Задержка — **5888 мс**.

### Доказательства:
- **Лог производительности (DevTools)**:  
  ![Performance Log](../../5_Additional_Materials/Performance_glitch_user_logs/Bug_Slow_Page_Loade.json)
- **Снимок вкладки Performance**:  
  ![Performance Log](../../5_Additional_Materials/Performance_glitch_user_logs/back_home_performance.png)
- **Long Tasks**:  
  - Задача 1: 4817 мс (Scripting).  
  - Задача 2: 2 мс (Rendering).  

### Рекомендации:
- Проверить оптимизацию сетевых запросов.