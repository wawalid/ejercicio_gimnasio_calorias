from abc import ABC, abstractmethod 

class Ejercicio(ABC):
    @abstractmethod
    def __init__(self, nombre, nivel_de_dificultad : int, calorias : int):
        pass

    @abstractmethod
    def calorias_quemadas(self):
        pass




class Cardio(Ejercicio):
    def __init__(self, nombre, nivel_de_dificultad: int, calorias: int, duracion):
        # super().__init__(nombre, nivel_de_dificultad, calorias)
        self.nombre = nombre
        self.nivel_de_dificultad = nivel_de_dificultad
        self.calorias = calorias
        self.duracion = duracion
        
    @property    
    def calorias_quemadas(self):
        return (self.duracion / 60) * self.calorias
    
    
    def __str__(self):
        return f"Ejercicio de cardio: {self.nombre}, dificultad: {self.nivel_de_dificultad}, calorias: {self.calorias}, duracion: {self.duracion}"

class Fuerza(Ejercicio):
    def __init__(self, nombre, nivel_de_dificultad: int, calorias: int, series, repeticiones, tiempo_tension, tiempo_descanso):
        self.nombre = nombre
        self.nivel_de_dificultad = nivel_de_dificultad
        self.calorias = calorias
        self.series = series
        self.repeticiones = repeticiones
        self.tiempo_tension = tiempo_tension
        self.tiempo_descanso = tiempo_descanso

    @property
    def calorias_quemadas(self):
        return self.series * self.repeticiones * self.tiempo_tension * self.tiempo_descanso
    
    def __str__(self):
        return f"Ejercicio de fuerza: {self.nombre}, dificultad: {self.nivel_de_dificultad}, calorias: {self.calorias}, series: {self.series}, repeticiones: {self.repeticiones}, tiempo en tension: {self.tiempo_tension}, descanso: {self.tiempo_descanso} "
        




class Cliente():
    def __init__(self, nombre, fecha_nacimiento, peso, condicion_fisica):
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento
        self.peso = peso
        self.condicion_fisica = condicion_fisica
        self.lista_ejercicios = []


    def asignar_entrenamiento(self, ejercicio):
            try:
                if self.condicion_fisica < ejercicio.nivel_de_dificultad:
                    raise ValueError("No se puede asignar al cliente un ejercicio superior a su nivel de condicion fisica.")
                else:
                    self.lista_ejercicios.append(ejercicio)
                    print(f"Perfe, ejercicio '{ejercicio.nombre}' añadido.") 
            except ValueError as e:
                print(e)

    def eliminar_entrenamiento(self, ejercicio):
        if not self.lista_ejercicios:
            return "Usuario sin ejercicios asignados"
        else:
            if ejercicio in self.lista_ejercicios:
                self.lista_ejercicios.remove(ejercicio)
                return f"Ejercicio '{ejercicio.nombre}' eliminado correctamente."
            else:
                return f"Ejercicio {ejercicio} no encontrado"

    def consultar_entrenamientos(self):
        resultados = f"Entrenamientos hechos por el cliente {self.nombre}: \n"
        for ejercicio in self.lista_ejercicios:
            resultados += f"- {ejercicio.nombre} \n" 
        return print(resultados)

    def calcular_entrenamiento(self):
        total_calorias = sum(ejercicio.calorias_quemadas for ejercicio in self.lista_ejercicios)
        return print(total_calorias)

    def __str__(self):
        return f"Cliente: {self.nombre}, fecha nacimineto: {self.fecha_nacimiento}, peso: {self.peso}, condicion fisica: {self.condicion_fisica}"
    
# correr = Cardio("correr", 3, 3, 3)
# walid = Cliente("walid", 210903, 70, 4)
# walid.asignar_entrenamiento(correr)
# walid.calcular_entrenamiento()

class Crossfitero(Cliente):
    def __init__(self, nombre, fecha_nacimiento, peso, condicion_fisica, nivel_intensidad, modalidad_entrenamiento):
        super().__init__(nombre, fecha_nacimiento, peso, condicion_fisica)
        self.nivel_intensidad = nivel_intensidad
        self.modalidad_entrenamiento = modalidad_entrenamiento

        

    def asignar_wod(self, ejercicio):
        self.wod = []
        self.wod.append(ejercicio)

    def agregar_ejercicio(self, ejercicio):
        ejercicios_cross = []
        ejercicios_cross.append(ejercicio)
        print("perfeperfe")

    
"""Se le podrán asignar ejercicios de fuerza y de cardio, pero la
diferencia entre ellos sólo podrá variar en 1 (es decir, si tiene 5 ejercicios de fuerza deberá tener 4, 5 o 6
ejercicios de cardio)."""

class Culturista(Cliente):
    def __init__(self, nombre, fecha_nacimiento, peso, condicion_fisica):
        super().__init__(nombre, fecha_nacimiento, peso, condicion_fisica)
        self.lista_ejercicios = []

    def asignar_rutina(self, rutina):
        self.lista_ejercicios = []
        self.lista_ejercicios.append(rutina)
        


class Ciclista(Cliente):
    def __init__(self, nombre, fecha_nacimiento, peso, condicion_fisica, tipo_bici, kilometraje):
        super().__init__(nombre, fecha_nacimiento, peso, condicion_fisica)
        self.tipo_bici = tipo_bici
        self.kilometraje = kilometraje

    def kilometros_anuales(self):
        pass



class Entrenador():
    def __init__(self, nombre):
        self.nombre = nombre
        self.lista_clientes = []


    def asignar_cliente(self,cliente):
        self.lista_clientes.append(cliente)
        return f"Cliente {cliente.nombre} asignado al entrenador {self.nombre}"


    def eliminar_cliente(self, cliente):
        if not self.lista_clientes:
            return "Usuario sin ejercicios asignados"
        else:
            if cliente in self.lista_ejercicios:
                self.lista_ejercicios.remove(cliente)
                return f"Clliente eliminado correctamente."
            else:
                return f"Cliente {cliente} no encontrado"
        

    def consultar_clientes(self):
        if not self.lista_clientes:
            return print("Entrenador sin clientes asignados")
        else:
            for cliente in self.lista_clientes:
                if cliente is not None:
                    print(cliente.nombre)




    def __str__(self):
        return f"Entrenador: {self.nombre}"





