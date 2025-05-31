from abc import ABC, abstractmethod

class CarState(ABC):
    def __init__(self, car):
        self.car = car

    @abstractmethod
    def turn_on(self) -> None:
        pass

    @abstractmethod
    def turn_off(self) -> None:
        pass

    @abstractmethod
    def accelerate(self) -> None:
        pass

    @abstractmethod
    def brake(self) -> None:
        pass

class TurnedOn(CarState):
    def __init__(self, car):
        super().__init__(car)
        self.acceleration_count = 0  # Para rastrear sobrecalentamiento

    def turn_on(self) -> None:
        print("Ya estoy prendido")

    def turn_off(self) -> None:
        print("Apagándome")
        self.car.state = TurnedOff(self.car)
        # No consume gasolina al apagar

    def accelerate(self) -> None:
        print("Acelerando")
        self.car.used_gas += 10  # Consume 10 al acelerar estando encendido
        self.acceleration_count += 1
        
        # Sobrecalentamiento después de 5 aceleraciones consecutivas
        if self.acceleration_count >= 5:
            print("¡Motor sobrecalentado!")
            self.car.used_gas += 50  # Consume 50 adicionales al sobrecalentar
            self.car.state = OverHeat(self.car)

    def brake(self) -> None:
        print("Frenando")
        self.acceleration_count = 0  # Resetear contador al frenar
        # No consume gasolina al frenar

class TurnedOff(CarState):
    def turn_on(self) -> None:
        print("Prendiendo")
        self.car.used_gas += 30  # Consume 30 al encender un auto apagado
        self.car.state = TurnedOn(self.car)

    def turn_off(self) -> None:
        print("Ya estoy apagado")

    def accelerate(self) -> None:
        print("No puedo acelerar, estoy apagado")
        # No consume gasolina cuando está apagado

    def brake(self) -> None:
        print("No puedo frenar, estoy apagado")
        # No consume gasolina cuando está apagado

class OverHeat(CarState):
    def turn_on(self) -> None:
        print("No puedo prender el motor, estoy sobrecalentado")

    def turn_off(self) -> None:
        print("No puedo apagar el motor, estoy sobrecalentado")
        # No consume gasolina (ya está sobrecalentado)

    def accelerate(self) -> None:
        print("No puedo acelerar, estoy sobrecalentado")
        self.car.used_gas += 20  # Consume 20 al acelerar sobrecalentado

    def brake(self) -> None:
        print("No puedo frenar, estoy sobrecalentado")
        # No consume gasolina al frenar

    def cool_down(self) -> None:
        """Método para enfriar el motor y volver al estado apagado"""
        print("Motor enfriándose... Regresando a estado apagado")
        self.car.state = TurnedOff(self.car)

class Car:
    def __init__(self):
        self.used_gas = 0  # Nuevo campo para rastrear gasolina consumida
        self.state = TurnedOff(self)

    def turn_on(self) -> None:
        self.state.turn_on()

    def turn_off(self) -> None:
        self.state.turn_off()

    def accelerate(self) -> None:
        self.state.accelerate()

    def brake(self) -> None:
        self.state.brake()

    def cool_down(self) -> None:
        """Método para enfriar el motor si está sobrecalentado"""
        if isinstance(self.state, OverHeat):
            self.state.cool_down()
        else:
            print("El motor no está sobrecalentado")

    def get_gas_consumption(self) -> int:
        """Método para obtener el consumo total de gasolina"""
        return self.used_gas

    def reset_gas_consumption(self) -> None:
        """Método para resetear el contador de gasolina"""
        self.used_gas = 0
