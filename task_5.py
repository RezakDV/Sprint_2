# Создание класса Results
class Results:
    # Инициализация атрирутов victories, draws, losses
    def __init__(self, victories, draws, losses):
        self.victories = victories
        self.draws = draws
        self.losses = losses

# Создание подкласса Football, который наследует от Results
class Football(Results):
    # Инициализация атрибутов victories, draws, losses из суперкласса Results
    def __init__(self, victories, draws, losses):
        super().__init__(victories, draws, losses)
    
    # Создание метода подсчета побед
    def number_of_wins(self):
        return f"Футбольных побед: {self.victories}"
    
    # Создание метода подсчета ничьих
    def number_of_draws(self):
        return f"Футбольных ничьих: {self.draws}"
    
    # Создание метода подсчета поражений
    def number_of_losses(self):
        return f"Футбольных поражений: {self.losses}"
    
    # Cоздание метода подсчета общего количества очков
    def total_points(self):
        points = 3 * self.victories + self.draws
        return f"Общее количество очков: {points}"
    
# Создание подкласса Hockey, который наследует от Results
class Hockey(Results):
    # Инициализация атрибутов victories, draws, losses из суперкласса Results
    def __init__(self, victories, draws, losses):
        super().__init__(victories, draws, losses)
    
    # Создание метода подсчета побед
    def number_of_wins(self):
        return f"Хоккейных побед: {self.victories}"
    
    # Создание метода подсчета ничьих
    def number_of_draws(self):
        return f"Хоккейных ничьих: {self.draws}"
    
    # Создание метода подсчета поражений
    def number_of_losses(self):
        return f"Хоккейных поражений: {self.losses}"
    
    # Cоздание метода подсчета общего количества очков
    def total_points(self):
        points = 2 * self.victories + self.draws
        return f"Общее количество очков: {points}"

# Создание объектов подклассов Football и Hockey    
football_team = Football(2, 2, 2)
hockey_team = Hockey(2, 2, 2)

# Вызов всех методов для каждого из объектов
for team in (football_team, hockey_team):
    print(team.number_of_wins())
    print(team.number_of_draws())
    print(team.number_of_losses())
    print(team.total_points())
