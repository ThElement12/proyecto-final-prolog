from pyswip import Prolog


def main_prueba():
    prolog = Prolog()
    prolog.consult("rules_prolog/turista.pl")

    query = "restaurantePresupuesto(5000, bavaro, medio, rapida, 50, X)"
    q2 = prolog.query(query)

    for result in q2:
        print(result)


if __name__ == "__main__":
    main_prueba()
