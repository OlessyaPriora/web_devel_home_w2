Web development: домашние задание 2 (Python)

Разработать систему регистрации пользователя, используя Pydantic для валидации входных данных, обработки вложенных структур и сериализации. Система должна обрабатывать данные в формате JSON.


Задачи:
    1.Создать классы моделей данных с помощью Pydantic для пользователя и его адреса.
    2.Реализовать функцию, которая принимает JSON строку, десериализует её в объекты Pydantic, валидирует данные,
      и в случае успеха сериализует объект обратно в JSON и возвращает его.
    3.Добавить кастомный валидатор для проверки соответствия возраста и статуса занятости пользователя.
    4.Написать несколько примеров JSON строк для проверки различных сценариев валидации: успешные регистрации и случаи, когда валидация не проходит
      (например возраст не соответствует статусу занятости).


Модели:
Address: Должен содержать следующие поля:
city: строка, минимум 2 символа.
street: строка, минимум 3 символа.
house_number: число, должно быть положительным.
User: Должен содержать следующие поля:
name: строка, должна быть только из букв, минимум 2 символа.
age: число, должно быть между 0 и 120.
email: строка, должна соответствовать формату email.
is_employed: булево значение, статус занятости пользователя.
address: вложенная модель адреса.

