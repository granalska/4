def get_cats_info(path):
    cats_info = []  #інф про кітів
    
    try:
        with open(path, 'r') as file: 
            
            for line in file:
                line = line.strip() #зачистка
                if not line:
                    continue

                parts = line.split(",")
                if len(parts)!= 3:
                    print(f'Некоректні дані: {line}')
                    continue
                    
                cat_id = parts[0].strip()
                name = parts[1].strip()
                age_str = parts[2].strip()
                #вік кітів у число
                try: 
                    age = int(age_str)
                except ValueError:
                    print(f"Некоректний вік '{age_str}' кіта '{name}'")
                    continue
                #додаємо інф про кота у список
                cats_info.append({ "ID": cat_id,"name": name,"age": age})
        #верніть кіта
        return cats_info

    except FileNotFoundError:
        print(f"Файл '{path}' не знайдено")
        return [] 
#виклик киць
cats_info = get_cats_info("6/cats_info.txt")
for cat in cats_info:
 print(cats_info)