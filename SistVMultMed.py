import datetime

class Medicamento:
    def __init__(self):
        self.__nombre = "" 
        self.__dosis = 0 
    
    def verNombre(self):
        return self.__nombre 
    def verDosis(self):
        return self.__dosis 
    
    def asignarNombre(self,med):
        self.__nombre = med 
    def asignarDosis(self,med):
        self.__dosis = med 
        
class Mascota:
    
    def __init__(self):
        self.__nombre= " "
        self.__historia=0
        self.__tipo=" "
        self.__peso=" "
        self.__fecha_ingreso=" "
        self.__lista_medicamentos=[]
        
    def verNombre(self):
        return self.__nombre
    def verHistoria(self):
        return self.__historia
    def verTipo(self):
        return self.__tipo
    def verPeso(self):
        return self.__peso
    def verFecha(self):
        return self.__fecha_ingreso
    def verLista_Medicamentos(self):
        return self.__lista_medicamentos 
            
    def asignarNombre(self,n):
        self.__nombre=n
    def asignarHistoria(self,nh):
        self.__historia=nh
    def asignarTipo(self,t):
        self.__tipo=t
    def asignarPeso(self,p):
        self.__peso=p
    def asignarFecha(self,f):
        self.__fecha_ingreso=f
    def asignarLista_Medicamentos(self,n):
        self.__lista_medicamentos = n 
    
class sistemaV:
    def __init__(self):
        self.__lista_felinos = []
        self.__lista_caninos = []
    
    def verificarExiste(self,historia):
        return historia in self.__lista_felinos or historia in self.__lista_caninos
        
    def verNumeroMascotas(self):
        return len(self.__lista_felinos) + len(self.__lista_caninos) 
    
    def ingresarMascota(self,mascota):
        tipo=mascota.verTipo()
        historia=mascota.verHistoria()
        if tipo == "felino":
            self.__lista_felinos.append(mascota)
        elif tipo == "canino":  
            self.__lista_caninos.append(mascota)
        else:   
            print("Tipo de mascota no válido.")
            return False 
   

    def verFechaIngreso(self,historia):
        if historia in self.__lista_felinos:
            return self.__felinos[historia].verFecha()
        elif historia in self.__lista_caninos:
            return self.__lista_caninos[historia].verFecha()
        return None

    def verMedicamento(self,historia):
        if historia in self.__lista_felinos:
            return self.__felinos[historia].verLista_Medicamentos()
        elif historia in self.__lista_caninos:
            return self.__lista_caninos[historia].verListaMedicamentos()
        return None
    
    def eliminarMascota(self, historia):
        for felino in self.__lista_felinos:
            if felino.verHistoria() == historia:
                self.__lista_felinos.remove(felino)
                return True
        for canino in self.__lista_caninos:
            if canino.verHistoria() == historia:
                self.__lista_caninos.remove(canino)
                return True
        
            

def main():
    servicio_hospitalario = sistemaV()
    # sistma=sistemaV()
    while True:
        menu=int(input('''\nIngrese una opción: 
                       \n1- Ingresar una mascota 
                       \n2- Ver fecha de ingreso 
                       \n3- Ver número de mascotas en el servicio 
                       \n4- Ver medicamentos que se están administrando
                       \n5- Eliminar mascota 
                       \n6- Eliminar Medicamento
                       \n7- Salir
                       \nUsted ingresó la opción: ''' ))
        if menu==1: # Ingresar una mascota 
            if servicio_hospitalario.verNumeroMascotas() >= 10:
                print("No hay espacio ...") 
                continue
            historia=int(input("Ingrese la historia clínica de la mascota: "))
            #   verificacion=servicio_hospitalario.verDatosPaciente(historia)
            if servicio_hospitalario.verificarExiste(historia) == False:
                nombre=input("Ingrese el nombre de la mascota: ")
                tipo=input("Ingrese el tipo de mascota (felino o canino): ")
                peso=int(input("Ingrese el peso de la mascota: "))
                fecha= ''
                while True:
                    fecha=input("Ingrese la fecha de ingreso (dia/mes/año): ")
                    try:
                        fecha_valida= datetime.strptime(fecha, "%d/%m/%Y")
                    except ValueError:
                        print('Invalido')

            nm = int(input("Ingrese cantidad de medicamentos: "))
            lista_med = []

            for i in range(0, nm):
                repetido = False
                for m in lista_med:
                    if m.verNombre() == nombre:
                        repetido = True
                        break
                if repetido:
                    print('El medicamento ya fue ingresado')
                    continue
                nombre_medicamentos = input("Ingrese el nombre del medicamento: ")
                dosis = int(input("Ingrese la dosis: "))
                medicamento = Medicamento()
                medicamento.asignarNombre(nombre_medicamentos)
                medicamento.asignarDosis(dosis)
                lista_med.append(medicamento)

            mas = Mascota()
            mas.asignarNombre(nombre)
            mas.asignarHistoria(historia)
            mas.asignarPeso(peso)
            mas.asignarTipo(tipo)
            mas.asignarFecha(fecha)
            mas.asignarLista_Medicamentos(lista_med)
            servicio_hospitalario.ingresarMascota(mas)

        elif menu == 2:  # Ver fecha de ingreso
            q = int(input("Ingrese la historia clínica de la mascota: "))
            fecha = servicio_hospitalario.verFechaIngreso(q)
            if fecha is not None:
                print("La fecha de ingreso de la mascota es: " + fecha)
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")

        elif menu == 3:  # Ver número de mascotas en el servicio
            numero = servicio_hospitalario.verNumeroMascotas()
            print("El número de pacientes en el sistema es: " + str(numero))

        elif menu == 4:  # Ver medicamentos que se están administrando
            q = int(input("Ingrese la historia clínica de la mascota: "))
            medicamento = servicio_hospitalario.verMedicamento(q)
            if medicamento is not None:
                print("Los medicamentos suministrados son: ")
                for m in medicamento:
                    print(f"\n- {m.verNombre()}")
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")

        elif menu == 5:  # Eliminar mascota
            q = int(input("Ingrese la historia clínica de la mascota: "))
            resultado_operacion = servicio_hospitalario.eliminarMascota(q)
            if resultado_operacion:
                print("Mascota eliminada del sistema con éxito")
            else:
                print("No se ha podido eliminar la mascota")

        elif menu == 6:
            q = int(input('Ingrese la historia clinica de la mascota: '))
            medicamento = servicio_hospitalario.verMedicamento(q)
            if medicamento is not None:
                print('Los medicamentos son: ')
                for me in medicamento:
                    print(f' {me.verNombre()}')
                nombre_medicamento = input('Ingrese el nombre del medicament0:')
                for me in medicamento:
                    if me.verNombre() == nombre_medicamento:
                        medicamento.remove(me)
                        print(f'Medicamento {nombre_medicamento} eliminado.')
                        break
                else:
                    print(f'El medicamento {nombre_medicamento} no esta')
            else:
                print('La historia clinica no existe')
 
        elif menu == 7:
            print("Usted ha salido del sistema de servicio de hospitalización...")
            break

        else:
            print("Usted ingresó una opción no válida, inténtelo nuevamente...")

if __name__=='__main__':
    main()





            

                

