import json

FilePath ='/Users/darika/Desktop/project/data.json'
IdFilePath ='/Users/darika/Desktop/project/id.txt'


def getData():
    with open(FilePath) as file:
        return json.load(file)

# print(getData())



def saves(data):
    with open(FilePath, 'w') as file:
        json.dump(data,file)


#------------------------------------------------------
def listing():
    data = getData()
    return f'Добро Пожаловать в наш магазин!В наличии имеются данные модели: {data}'
# print(listing())


def retrieve():
    data =getData()
    try:
        id  = int(input('Введите id товара: '))
        product =list(filter(lambda i:id ==i['id'],data))
        return f'Вот товар который вы искали {product[0]}'
    except :
        return 'Несуществующий id товара'

# print(retrieve())


def id():
    with open(IdFilePath,'r') as file:
        id = int(file.read())
        id +=1
    with open(IdFilePath,'w') as file:
        file.write(str(id))
        return id


def create():
    data =getData()
    try:
        product ={
            'id': id(),
            'brand': input('Введите марку продукта: '),
            'title': input('Введите модель продукта: '),
            'year' : int(input('Ведите год выпуска продукта: ')),
            'description' :input('Введите описание товара: '),
            'price' : round(float(input('Введите цену товара:')),2)
        }
    except:
        return 'Неверные данные'
    data.append(product)
    saves(data)
    return 'Новый товар успешно создан!'

# print(create())

def update():
    data =getData()
    try:
        id = int(input('Введите id продукта: '))
        product =list(filter(lambda x: x['id'] == id ,data))[0]
        print(f'Товар для обновления: {product["title"]}')
    except:
        return 'Неверный id!'
    index = data.index(product)
    choice =input('Что вы хотите изменить?(1-brand,2-title,3-year,4-description,5-price): ')
    if choice.strip() =='2':
        data[index]['title'] =input('Введите новую модель: ')

    elif choice.strip() =='1':
        data[index]['brand'] =input('Введите новый бренд товара: ')

    elif choice.strip() =='3':
        data[index]['year'] = input('Введите измененный год выпуска: ')
    

    elif choice.strip() =='5':
        try:
            data[index]['price'] =round(float(input('Введите новую цену: ')),2)
        except:
            return 'Неверное значение для цены'

    elif choice.strip() =='4':
        data[index]['description'] =input('Введите новое описание: ')

    else:
        return 'Неверное значение для обновления!'
    saves(data)

    return 'Товар обновлен!'

# print(update())

def delete():
    data =getData()
    try:
        id = int(input('Введите id продукта: '))
        product =list(filter(lambda x: x['id'] == id , data))[0]
        print(f'Товар для удаления: {product["title"]}')
    except:
        return 'Неверный id!'
    choice =input('Удалить этот товар(yes/no)?')
    if choice.lower().strip() !='yes':
        return 'Товар не удален!'
    data.remove(product)
    saves(data)
    return 'Товар успешно удален!'
