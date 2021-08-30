from pyswip import Prolog

prolog = Prolog()
prolog.consult("rules_prolog/turista.pl")


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
        results.append(result['X'][0])
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
