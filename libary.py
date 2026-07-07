import json

file = "libary.json"

def load_data():
    data = {}
    try:
        with open(file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print("[!] Файл не знайдено.")

    return data

def save_data(data):
    try:
        with open(file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"[!] Помилка при збереженні даних: {e}")

def all(data):
    if not data:
        print("[!] Книг немає.")
        return
    
    for eid, info in data.items():
        print(f" ID: ➜  {eid}")
        print(f" Назва: ➜  {info['title']}")
        print(f" Автор: ➜  {info['author']}")
        print(f" Рік видання: ➜  {info['year']}")
        print(f" Жанр: ➜  {info['genre']}")
        print(f" Прочитано: ➜ {info.get('status', 'Ні')}")
        print(" ──────────────────────────────")
        input("\nНатисніть Enter, щоб продовжити.")

def add(data):
    name = input(" Назва книги ➜  ")
    author = input(" Автор ➜  ")

    while True:
        year = input(" Рік видання ➜  ")
        if not year.isdigit():
            print("[!] Помилка: Рік має складатися тільки з цифр!")
            continue
        year_int = int(year)
        if year_int > 2026 or year_int < 1400:
            print("[!] Помилка: Рік має бути від 1400 до 2026!")
            continue
        break
    
    genre = input(" Жанр ➜  ")


    if data:
        next_id = str(max(int(k) for k in data.keys()) + 1)
    else:
        next_id = "1"

    data[next_id] = {
        "title": name,
        "author": author,
        "year": year,
        "genre": genre,
        "status": "Ні"
    }

    save_data(data)
    print(" ──────────────────────────────")
    print(" [!] Книгу успішно додано.")
    print(" ──────────────────────────────")

def search(data):
    if not data:
        print("[!] Немає книг для пошуку.")
        return
    
    author_input = input("Введіть ім'я автора для пошуку ➜  ")

    if not author_input:
        print("[!] Запит не може бути порожнім!")
        return
    
    results = []

    for book_id, info in data.items():
        book_author = info.get('author', '')
        if author_input in book_author:
            results.append((book_id, info))
    if not results:
        print("[!] Книг цього автора не знайдено.")
    else:
        print("\n ╭──────────────────────────────╮")
        print(" │       Результати пошуку      │")
        print(" ╰──────────────────────────────╯")
        
        for book_id, info in results:
            print(f" ID: {book_id}")
            print(f" Назва: {info.get('title')}")
            print(f" Автор: {info.get('author')}")
            print(" ──────────────────────────────")

def delete(data):
    if not data:
        print("[!] Книг немає.")
        return
    while True:
        eid = input("Введіть ID книги для видалення ➜  ")

        if eid in data:
            break
        else:
            print(" [!] Такого ID не існує. Спробуйте ще раз.")
            print(" ──────────────────────────────")


    conf = input(f"Ви впевнені що хочете видалити книгу N{eid} (так/ні) ➜ ")

    if conf == "так":
        try:
            if eid in data:
                del data[eid]
                save_data(data)
                print(" ──────────────────────────────")
                print(" [!] Книгу успішно видалено.")
            else:
                print(" ──────────────────────────────")
                print(" [!] Книгу не знайдено")
        except Exception as e:
            print(f"Виникла помилка! {e}")
    else:
        print(" [!] Видалення скасовано.")

def stats(data):
    total = len(data)
    print("\n ╭──────────────────────────────╮")
    print(" │          Статистика          │")
    print(" ╰──────────────────────────────╯")
    print(f" Кількість книг у базі ➜  {total}")
    print(" ──────────────────────────────")
    input("\nНатисніть Enter, щоб повернутися.")

def readb(data):
    if not data:
        print("[!] Книг немає.")
        return
    
    eid = input("Введіть ID книги, яку ви прочитали ➜  ")

    if eid in data:
        if data[eid].get("status") == "Так":
            print(f"[!] Книга {data[eid]['title']} вже була позначена як прочитана раніше!")
            input("Натисніть Enter, щоб повернутися в меню...")
            return
        data[eid]["status"] = "Так"
        save_data(data)

        print(" ──────────────────────────────")
        print(f"Книгу \"{data[eid]['title']}\" позначено як прочитану!")
        print(" ──────────────────────────────")
        input("Натисніть Enter, щоб повернутися.")
    else:
        print("[!] Книгу з таким ID не знайдено.")
libary = load_data()

while True:
    print("╭────────────────────────────────╮")
    print("│        Бібліотека книг         │")
    print("╰────────────────────────────────╯")
    print(" ────────────────────────────────")
    print("  [1] ➜  Додати книгу")
    print("  [2] ➜  Переглянути всі книги")
    print("  [3] ➜  Видалити книгу")
    print("  [4] ➜  Знайти книгу за автором")
    print("  [5] ➜  Статистика")
    print("  [6] ➜  Позначити книгу як прочитану")
    print("  [7] ➜  Вийти")
    print(" ────────────────────────────────")
    
    choice = input(" Виберіть пункт меню ➜  ")

    if choice == "1":
        print("\n ╭──────────────────────────────╮")
        print(" │       Додавання книги        │")
        print(" ╰──────────────────────────────╯")
        add(libary)
        
    elif choice == "2":
        print("\n ╭──────────────────────────────╮")
        print(" │       Перегляд усіх книг     │")
        print(" ╰──────────────────────────────╯")
        all(libary)
        
    elif choice == "3":
        print("\n ╭──────────────────────────────╮")
        print(" │       Видалення книги        │")
        print(" ╰──────────────────────────────╯")
        delete(libary)

    elif choice == "4":
        print("\n ╭──────────────────────────────╮")
        print(" │       Пошук книг за автором  │")
        print(" ╰──────────────────────────────╯")
        search(libary)

    elif choice == "5":
        print("\n ╭──────────────────────────────╮")
        print(" │        Статистика            │")
        print(" ╰──────────────────────────────╯")
        stats(libary)

    elif choice == "6":
        print("\n ╭──────────────────────────────╮")
        print(" │       Позначення книги        │")
        print(" ╰──────────────────────────────╯")
        readb(libary) 
        
    elif choice == "7":
        print("\n ╭──────────────────────────────╮")
        print(" │  Програма завершує роботу.   │")
        print(" ╰──────────────────────────────╯")
        break
        
    else:
        print("\n [!] Некоректний вибір.")