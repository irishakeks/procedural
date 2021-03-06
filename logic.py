import math
import sys


container = None
parr_keys = ['height', 'width', 'length', 'density', 'temperature']
sphere_keys = ['radius', 'density', 'temperature']
tetr_keys = ['a', 'density', 'temperature']


def init():
    shapes_list = []
    container = {
        'shapes_list': shapes_list,
        'size': 0
    }
    return container


def inp(c, file_name):
    try:
        with open(file_name) as file:

            for line in file:
                input_shape(c, line, file.readline().split(" "))
                c['size'] += 1

            file.close()
        return c

    except OSError:
        print("Файл с данными не найден.")
        return None


def clear(c, file):
    with open(file, 'w') as output_file:
        output_file.write("Empty container " + str(c['size']))


def out(c, file_name):
    with open(file_name, "w") as output_file:
        output_file.write("Container's length = " + str(c['size']) + "\n")

        s = c['size']

        while c['size'] != 0:
            shape = c['shapes_list'].pop()
            output_file.write(str(s - c['size']) + " ")
            output_shape(output_file, shape)
            output_file.write("square: " + str(square(shape)) + "\n")
            c['size'] -= 1
    return True


def out_sphere(c, file_name):
    with open(file_name, "w") as output_file:
        output_file.write("Container's length = " + str(c['size']) + "\n")
        output_file.write("Only spheres" + "\n")
        s = c['size']

        while c['size'] != 0:

            shape = c['shapes_list'].pop()
            output_file.write(str(s - c['size']))

            if list(shape.keys()) == sphere_keys:
                output_sphere(output_file, shape)
                output_file.write("square: " + str(square(shape)) + "\n")
            else:
                output_file.write("\n")
            c['size'] -= 1

    return True


def output_shape(file, shape):
    if list(shape.keys()) == sphere_keys:
        output_sphere(file, shape)
    elif list(shape.keys()) == parr_keys:
        output_parr(file, shape)
    elif list(shape.keys()) == tetr_keys:
        output_tetr(file, shape)
    else:
        return False



def output_sphere(file, shape):
    file.write(": It's sphere: r = " + shape['radius'] + ", d = " + shape['density'].strip() +
               ", t = " + shape['temperature'] + " | ")


def output_parr(file, shape):
    file.write("It's parallelepiped: h = " + shape['height'] + ", "
                "w = " + shape['width'] + ", l = " + shape['length'] + ", "
                "d = " + shape['density'].strip() + ", t = " + shape['temperature']  + " | ")


def output_tetr(file, shape):
    file.write("It's tetrahedron: a = " + shape['a'] + ", d = " + shape['density'].strip() +
               ", t=" + shape['temperature'] + " | ")


def input_shape(c, shape_type, param):
    try:
        if int(shape_type) == 1:
            input_parr(c, param)
        elif int(shape_type) == 2:
            input_sphere(c, param)
        elif int(shape_type) == 3:
            input_tetrahedron(c, param)
    except ValueError:
        print("Ошибка в формате записи данных в файле. Неправильно указан тип фигуры")
        quit()



def input_parr(c, param):  # создаем функцию ввода параллелепипеда

    if len(param)!= 5:
        print("Неверное количество параметров параллелепипеда")
        quit()

    parr = {  # словарь с параметрами параллелепипеда
        'height': param[0],
        'width': param[1],
        'length': param[2],
        'density': param[3],
        'temperature': param[4].strip()
    }

    for par in parr:
        if not parr[par].isdigit or (int(parr[par]) <= 0):
            print("Введены неверные параметры параллелепипеда. "
                  "Все параметры должны быть неотрицательными числами больше 0!")
            quit()

    c['shapes_list'].append(parr)


def input_sphere(c, param):

    if len(param)!= 3:
        print("Неверное количество параметров сферы")
        quit()

    sphere = {
        'radius': param[0],
        'density': param[1],
        'temperature': param[2].strip()
    }

    for par in sphere:
        if not sphere[par].isdigit or (int(sphere[par]) <= 0):
            print("Введены неверные параметры сферы. "
                  "Все параметры должны быть неотрицательными числами больше 0!")
            quit()
    c['shapes_list'].append(sphere)


def input_tetrahedron(c, param):

    if len(param)!= 3:
        print("Неверное количество параметров тетраэдра")
        quit()

    param[1].strip()
    tetrahedron = {
        'a': param[0],
        'density': param[1],
        'temperature': param[2].strip()
    }

    for par in tetrahedron:
        if not tetrahedron[par].isdigit or (int(tetrahedron[par]) <= 0):
            print("Введены неверные параметры тетраэдра. "
                  "Все параметры должны быть неотрицательными числами больше 0!")
            quit()
    c['shapes_list'].append(tetrahedron)


def input_shapes(file_name):
    try:
        file = open(file_name)

    except OSError:
        return print("Файл с данными не найден.")

    for line in file:
        inp(container, line, file.readline().split(" "))


def square(shape):
    if list(shape.keys()) == sphere_keys:
        return square_sphere(shape)
    elif list(shape.keys()) == parr_keys:
        return square_parr(shape)
    else:
        return square_tetr(shape)


def square_sphere(shape):
    return 3.1415*4*int(shape['radius'])*int(shape['radius'])*int(shape['radius'])/3


def square_parr(shape):
    return (int(shape['width'])*int(shape['length']) +
            int(shape['length'])*int(shape['height']) + int(shape['width'])*int(shape['height']))*2


def square_tetr(shape):
    return math.sqrt(3)*int(shape['a'])


def compare(shape0, shape1):
    return square(shape0) < square(shape1)


def sort(c):
    c['shapes_list'].reverse()
    n = len(c['shapes_list'])
    for i in range(n):
        for j in range(0, n - i - 1):
            if compare(c['shapes_list'][j], c['shapes_list'][j+1]):
                c['shapes_list'][j], c['shapes_list'][j+1] = c['shapes_list'][j+1], c['shapes_list'][j]
    return c