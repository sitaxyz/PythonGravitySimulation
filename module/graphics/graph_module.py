import matplotlib.pyplot as plt
import math

def create_graph2D(data):
    # Извлечение скоростей и времени из данных
    speed1 = [item[0] for item in data]
    speed2 = [item[1] for item in data]
    time = [item[2] for item in data]

    # Нахождение корня суммы квадратов скоростей
    root_sum_of_squares = [math.sqrt(speed1[i]**2 + speed2[i]**2) for i in range(len(data))]

    # Создание графика
    plt.plot(time, root_sum_of_squares, label='Скорость')
    plt.axis('equal')
    plt.xlabel('Время')
    plt.ylabel('Скорость')
    plt.title('Пример графика')
    plt.legend()

    # Отображение графика
    plt.show()

def create_graph3D(data):
    # Создание 3D графика
    x = [item[3] for item in data]
    y = [item[4] for item in data]
    t = [item[2] for item in data]
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x, y, t) # Построение траектории в 3D
    ax.axis('equal')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Time')

    # Отображение графика
    plt.show()

def create_graphs(data):
    create_graph2D(data)
    create_graph3D(data)