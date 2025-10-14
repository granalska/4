def total_salary(path):
    try:
        with open(path, 'r') as file:
            total = 0   # загальна зп
            count = 0   # кількість прац
            workers = [("Alex Korp",3000),
                       ("Nikita Borisenko",2000),
                       ("Sitarama Raju",1000)]
            print("Прізвище Ім'я — Заробітна плата")

            for line in file:
                line = line.strip()  #підчищаємо пробіли
                if not line: 
                    continue

                parts = line.split(",") 
                if len(parts) != 2:
                    continue  #некорек дані пропускаємо

                name = parts[0].strip()
                salary_str = parts[1].strip()

                try:
                    salary = int(salary_str)
                except ValueError:
                    continue  #не числа пропускаємо

                #сепредня зп
                total += salary
                count += 1

                #првців у стовпчик
                print(f"{name} — {salary}")

        
            if count > 0:
                average = round(total / count, 2)
            else:
                average = 0

            print(f"Загальна зп: {total}")
            print(f"Середня зп: {average}")

            return total, average

    except FileNotFoundError:
        print("Файл не існує!")
        return None, None
    total_salary("workers.txt")