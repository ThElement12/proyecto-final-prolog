from pyswip import Prolog
from rules_prolog.reglas import *


def main_prueba():
    prolog = Prolog()
    prolog.consult("rules_prolog/turista.pl")

    print(restaurante_presupuesto(5000, "bavaro", "medio", "rapida", "50"))
    print(todas_las_actividades(5000))
    print(buscar_disco_presupuesto("centro_santiago", 5000,"excelente","elevado")[0])
    print(cines_peliculas("centro_santiago", "terror"))
    print(sucursales("boca_marina")[0])
    print(cine_sucursales("palacio_del_cine")[0])
    print(restauranteimp("concierto_ricardo_montaner", 4000, 10))


if __name__ == "__main__":
    main_prueba()
