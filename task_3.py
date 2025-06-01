# Создание класса PointsForPlace
class PointsForPlace:
    # Атрибуты класса не инициализируются, метод не взаимодействует с ними, поэтому можно использовать @staticmethod
    @staticmethod
    def get_points_for_place(place):
        # Переменная points инициализируется локально для предотвращения изменений из других методов
        points = 0
        if place > 100:
            return (f'Баллы начисляются только первым 100 участникам') 
        elif place < 1:
            return(f'Спортсмен не может занять нулевое или отрицательное место') 
        else:
            points = 101 - place
            return int(points)
        
# Создание класса PointsForMeters            
class PointsForMeters:
    # Атрибуты класса не инициализируются, метод не взаимодействует с ними, поэтому можно использовать @staticmethod
    @staticmethod
    def get_points_for_meters(meters):
        # Переменная points инициализируется локально для предотвращения изменений из других методов
        points = 0
        if meters < 0:
            return(f'Количество метров не может быть отрицательным') 
        else:
            points = meters * 0.5
            return int(points)

# Создание класса TotalPoints, который наследуется от классов PointsForPlace и PointsForMeters        
class TotalPoints(PointsForPlace, PointsForMeters):
    # Атрибуты класса не инициализируются, метод не взаимодействует с ними, поэтому можно использовать @staticmethod
    @staticmethod
    def get_total_points(place, meters):
        # Методы get_points_for_place и get_points_for_meters могут возвращать строки - необходима проверка на тип возвращаемого значения
        if isinstance(TotalPoints.get_points_for_place(place), str) or isinstance(TotalPoints.get_points_for_meters(meters), str):  
            return f"{TotalPoints.get_points_for_place(place)}\n{TotalPoints.get_points_for_meters(meters)}"
        else:
            total = TotalPoints.get_points_for_place(place) + TotalPoints.get_points_for_meters(meters)
            return total
            
points_for_place = PointsForPlace()
print(points_for_place.get_points_for_place(10))

points_for_meters = PointsForMeters()
print(points_for_meters.get_points_for_meters(10))

total_points = TotalPoints()
print(total_points.get_points_for_place(10))
print(total_points.get_points_for_meters(10))
print(total_points.get_total_points(100, 10))