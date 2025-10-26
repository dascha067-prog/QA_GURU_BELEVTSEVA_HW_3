print("Привет, README!")

text = (
    "Lorem Ipsum — это текст-рыба, часто используемый в печати и веб-дизайне. "
    "Lorem Ipsum."
)
print(text)


def add(a: int, b: int) -> int:
    return a + b  # Возвращаем сумму двух чисел.


def greet(name: str) -> str:
    return f"Привет, {name}!"  # Возвращаем строку приветствия.


numbers = [1, 2, 3, 4, 5]

print(greet("мир"))
print(add(2, 2))
