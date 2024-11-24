import turtle

class Tree:
    """ Класс который используется для отрисовки фрактального дерева
    """

    def setup_turtle(self):
        """ Метод используемый для установки черепахи в нужном положении для старта рисования
        """

        turtle.left(90)
        turtle.backward(100)
        turtle.color("brown")

    def draw_wooden_stick(self, length):
        """ Метод используемый для отрисовки ветки путём рекурсии
        """

        if length > 5:
            turtle.forward(length)
            turtle.right(20)
            self.draw_wooden_stick(length - 15)
            turtle.left(40)
            self.draw_wooden_stick(length - 15)
            turtle.right(20)
            turtle.backward(length)
    
    def end_turtle(self):
        """ Метод используемый для того чтобы спрятать рисующий курсор и закончить все с этим связанные действия
        """

        turtle.hideturtle()
        turtle.done()

class Triangle:
    """ Класс который используется для отрисовки треугольника Серпинского (https://ru.wikipedia.org/wiki/Треугольник_Серпинского)
    """

    initial_cords = [[-200, -150], [0, 200], [200, -150]]

    def setup_turtle(self, cords):
        """ Метод используемый для установки черепахи в нужном положении для старта рисования
        """

        turtle.penup()

        turtle.goto(cords[0])

        turtle.pendown()

    def __draw_single_triangle(self, cords):
        """ Метод используемый для отрисовки одного треугольника
        """

        self.setup_turtle(cords)

        for cord in cords:
            turtle.goto(cord)

        turtle.goto(cords[0])

    def draw_serpinckiy_triangle(self, count, cords):
        """ Метод используемый для отрисовки треугольника Серпинского путём рекурсии
        """

        if count > 0:
            midcords = [
                [(cords[0][0] + cords[1][0]) / 2, (cords[0][1] + cords[1][1]) / 2],
                [(cords[1][0] + cords[2][0]) / 2, (cords[1][1] + cords[2][1]) / 2],
                [(cords[2][0] + cords[0][0]) / 2, (cords[2][1] + cords[0][1]) / 2]
            ]
            
            self.draw_serpinckiy_triangle(count - 1, [cords[0], midcords[0], midcords[2]])
            self.draw_serpinckiy_triangle(count - 1, [midcords[0], cords[1], midcords[1]])
            self.draw_serpinckiy_triangle(count - 1, [midcords[2], midcords[1], cords[2]])
        else:
            self.__draw_single_triangle(cords)

    def end_turtle(self):
        """ Метод используемый для того чтобы спрятать рисующий курсор и закончить все с этим связанные действия
        """

        turtle.hideturtle()
        turtle.done()

def main():
    # Выбор фрактального рисунка и обработка исключений
    try:
        fractal_paint_choice = int(input("Какой фрактальный рисунок вы хотите отрисовать? (1 - Дерево, 2 - Треугольник Серпинского): "))
    except:
        print("Ввод был осуществлён некорректно, нужно вводить только одно целочисленное число без лишних символов (1 или 2 в зависимости от ваших предпочтений)")
        input()
        return

    # Реализация дерева
    if fractal_paint_choice == 1:
        # Ввод значения длины фрактального дерева и обработка исключений
        try:
            tree_fractal_length = int(input("Введите целочисленное значение длинны фрактального дерева (от 0 до 100): "))
            if tree_fractal_length < 0:
                print("Ввод был осуществлён некорректно, введённое число меньше 0")
                input()
                return
            elif tree_fractal_length > 100:
                print("Ввод был осуществлён некорректно, введённое число больше 100")
                input()
                return
        except:
            print("Ввод был осуществлён некорректно, нужно вводить только одно целочисленное число без лишних символов")
            input()
            return
        
        # Инициализация класса Tree и последующий вызов всех методов с нужными параметрами
        tree = Tree()

        tree.setup_turtle()

        tree.draw_wooden_stick(25 + tree_fractal_length)

        tree.end_turtle()

    # Реализация Треугольника Серпинского
    elif fractal_paint_choice == 2:
        # Ввод значения количества треугольников Серпинского и обработка исключений
        try:
            triangle_fractal_count = int(input("Введите целочисленное значение количества треугольников Серпинского (от 0 до 5): "))
            if triangle_fractal_count < 0:
                print("Ввод был осуществлён некорректно, введённое число меньше 0")
                input()
                return
            elif triangle_fractal_count > 5:
                print("Ввод был осуществлён некорректно, введённое число больше 5")
                input()
                return
        except:
            print("Ввод был осуществлён некорректно, нужно вводить только одно целочисленное число без лишних символов")
            input()
            return

        # Инициализация класса Triangle и последующий вызов всех методов с нужными параметрами
        triangle = Triangle()

        triangle.setup_turtle(triangle.initial_cords)

        triangle.draw_serpinckiy_triangle(triangle_fractal_count, triangle.initial_cords)
        
        triangle.end_turtle()
     
    # Дополнительная обработка исключений выбора фрактального рисунка
    if fractal_paint_choice > 2 or fractal_paint_choice < 1:
        print("Ввод осуществлён некорректно, нужно вводить целочисленное число в заданном диапазоне")
        input()
        return

# Реализация функции Main
if __name__ == "__main__":
    main()