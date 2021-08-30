from pyswip import Prolog
import pyswip


prolog = Prolog()
prolog.consult("turista.pl")


def restaurante_presupuesto(presupuesto, ciudad, nivelEconomico, tipoComida, porcentaje):
    query = f"restaurantePresupuesto({presupuesto}, {ciudad}, {nivelEconomico}, {tipoComida}, {porcentaje}, X)"
    q2 = prolog.query(query)
    result = []
    for resultado in q2:
        result.append(resultado['X'])
    return result




def todas_las_actividades(presupuesto):
    query = f"actividadPorPresupuesto({presupuesto}, X, Y)"
    q2 = prolog.query(query)
    results = []
    for result in q2:
        results.append((result['X'], result['Y']))
    return results


def buscar_disco_presupuesto(ciudad, presupuesto, puntuacion, precio):
    query = f"buscarDiscoPresupuesto({ciudad}, {presupuesto},{puntuacion},{precio}, X)"
    q2 = prolog.query(query)
    results = []
    for result in q2:
        results.append(result['X'])
    return results


def cines_peliculas(lugar, genero):
    query = f"cinesPelicula({lugar},{genero}, X)"
    q2 = prolog.query(query)
    results = []
    for result in q2:
        results.append(result['X'])
    return results


def sucursales(nombre):
    query = f"sucursales({nombre}, X)"
    q2 = prolog.query(query)
    results = []
    for result in q2:
        results = results + result['X']

    return results


def cine_sucursales(nombre):
    query = f"cine_sucursales({nombre}, X)"
    q2 = prolog.query(query)
    results = []
    for result in q2:
        results = results + result['X']

    return results


def restauranteimp(nombre, presupuesto,hora):
    query = f"restauranteimp({nombre}, {presupuesto},{hora}, X)."
    q2 = prolog.query(query)
    results = []
    for result in q2:
        results.append(result['X'])

    return results

##REGISTRAR


def registrar_restaurante(nombre, ciudad, precio, calificacion, hora):
    prolog.assertz(f"restaurante({nombre},{ciudad}, {precio}, {calificacion}, {hora})")
    q2 = prolog.query(f"restaurante({nombre}, X, _,_,_)")

    print("DEBUG RESTAURANTES CON ESE NOMBRE: ")
    for results in q2:
        print(results['X'])


def registrar_actividad(nombre, precio, lugar):
    prolog.assertz(f"eventos_importantes({nombre}, {precio}, {lugar})")
    q2 = prolog.query(f"eventos_importantes({nombre},_,X)")

    print("DEBUG EVENTOS IMPORTANTES CON ESE NOMBRE: ")
    for results in q2:
        print(results['X'])


def registrar_discoteca(nombre, ciudad, calificacion, precio):
    prolog.assertz(f"discoteca({nombre},{ciudad}, {precio}, {calificacion})")
    q2 = prolog.query(f"discoteca({nombre}, X, _,_)")

    print("DEBUG DISCOTECA CON ESE NOMBRE: ")
    for results in q2:
        print(results['X'])
