
class Car:
    def __init__(self, serial_number):
        self.is_running = False
        self.serial_number = serial_number

    def sound(self):
        print("bip-bip")

    def engine_turn_on(self):
        if self.is_running == True:
            print("Машина уже заведена!!!")
        else:
            print("Vruuuuum")
            self.is_running = True

    def engine_turn_off(self):
        if self.is_running == False:
            print("Машина еще не заведена!!!")
        else:
            print("Пых-пых-пых...")
            self.is_running = False

    def __str__(self):
        return (f"Состояние машины ({self.serial_number}):"
                f"\n\tСостояние двигателя: {self.is_running}\n")


commands_info = """
Введите команду:
    1 - Завести машину
    2 - Остановить машину
    0 - Завершить работу
Ввод: """

def main():
    car = Car(serial_number="VR-001")
    commands = {
        "1": car.engine_turn_on,
        "2": car.engine_turn_off,
        "0": "exit",
    }
    while True:
        print(str(car))

        choice = input(commands_info)
        result = commands.get(choice)
        if result == "exit":
            break
        elif result is not None:
            result()
        # else:
        #     continue

main()