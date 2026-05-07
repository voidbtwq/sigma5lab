def is_palindrome(s: str) -> bool:
    """
    Проверяет, является ли строка палиндромом.
    Игнорирует регистр и пробелы.
    """
    # Шаг 1: убираем чувствительность к регистру
    # Шаг 2: удаляем все пробелы
    cleaned = s.lower().replace(" ", "")
    # Шаг 3: сравниваем с обратной строкой
    return cleaned == cleaned[::-1]

# Необязательный блок для ручного тестирования
if __name__ == "__main__":
    examples = ["А роза упала на лапу Азора", "Madam", "hello"]
    for ex in examples:
        print(f"'{ex}' -> {is_palindrome(ex)}")
