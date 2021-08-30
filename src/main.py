from pyswip import Prolog
from rules_prolog.reglas import *

def main_prueba():


    print(restaurante_presupuesto(5000, "bavaro", "medio", "rapida", "50"))
    print(todas_las_actividades(5000))
    print(buscar_disco_presupuesto("centro_santiago", 5000,"excelente","elevado")[0])
    print(cines_peliculas("centro_santiago", "terror"))
    print(sucursales("boca_marina")[0])
    print(cine_sucursales("palacio_del_cine")[0])
    print(restauranteimp("concierto_ricardo_montaner", 4000, 10))


    #REGISTRAR
    registrar_restaurante("boca_marina","centro_santiago", 400, 2, 22)
    registrar_actividad("concierto_ricardo_montaner", 600, "alli")
    registrar_discoteca("discoteca1", "centro_santiago", 2, 100)


if __name__ == "__main__":
    main_prueba()
