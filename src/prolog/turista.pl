%1.provincias
provincia(santiago).
provincia(santo_domingo).
provincia(puerto_plata).
provincia(higuey).
provincia(la_vega).
provincia(samana).
%1.A sectores-playas
playas(boca_chica,[boca_chica]).
playas(sosua, [sosua, cabarete, alicia]).
playas(bavaro, [bavaro]).
playas(punta_cana,[punta_cana,arena_blanca]).
playas(las_terrenas, [las_terrenas]).
playas(las_galeras, [las_galeras]).
%1.B provincias-sectores
sectores(santo_domingo, [boca_chica, centro_santo_domingo]).
sectores(santiago, [centro_santiago]).
sectores(puerto_plata, [sosua]).
sectores(higuey,[bavaro, punta_cana]).

%1.D sectores-actividades
restaurante(restaurante1,boca_chica, 400, baja).
restaurante(restaurante2,centro_santo_domingo, 500, normal).
restaurante(restaurante3,centro_santiago, 1000, normal).
restaurante(restaurante4,centro_santiago, 1400, alta).
restaurante(restaurante5,sosua, 100, normal).
restaurante(restaurante6,bavaro, 200, baja).
restaurante(restaurante6,bavaro, 900, alta).
restaurante(restaurante6,bavaro, 700, normal).
restaurante(restaurante7,punta_cana, 250, normal).
restaurante(restaurante7,punta_cana, 400, alta).

discoteca(discoteca1,centro_santo_domingo, 100, baja).
discoteca(discoteca2,centro_santiago, 500, normal).
discoteca(discoteca3,centro_santiago, 500, alta).
discoteca(discoteca4,sosua, 1200, alta).
discoteca(discoteca5,bavaro, 1200, baja).
discoteca(discoteca6,punta_cana, 1200, alta).
discoteca(discoteca7, centro_santiago, 1400, alta).
discoteca(discoteca8,punta_cana, 1200, alta).

cine(cine1, centro_santiago, 500, normal).
cine(cine2,centro_santiago, 250, alta).
cine(cine3,centro_santiago, 250, alta).
cine(cine4,centro_santo_domingo, 400, baja).
cine(cine5,centro_santo_domingo, 300, alta).
cine(cine6,centro_santo_domingo, 300, normal).
cine(cine7,punta_cana, 250, alta).

%2 tipocomida restaurantes
tipocomida(restaurante1, criolla).
tipocomida(restaurante2, casera).
tipocomida(restaurante3, casera).
tipocomida(restaurante4, gourmet).
tipocomida(restaurante5, buffet).
tipocomida(restaurante6, criolla).
tipocomida(restaurante7, rapida).

%3 Rango de precio (economico, medio, elevado)
rango_precio(Precio, economico):- Precio =< 599.
rango_precio(Precio, medio):- Precio >= 600, Precio =< 1199.
rango_precio(Precio, elevado):- Precio >= 1200.
%4 playas
playa(boca_chica).
playa(sosua).
playa(cabarete). 
playa(alicia).
playa(bavaro).
playa(punta_cana).
playa(arena_blanca).
playa(las_terrenas).
playa(las_galeras).
%5 sectores turisticos
sector(boca_chica).
sector(sosua).
sector(bavaro).
sector(punta_cana).
sector(las_terrenas).
sector(las_galeras).
%6 eventos, sector
eventos_importantes(concierto1, 600, boca_chica).
eventos_importantes(concierto2, 1300, sosua).
eventos_importantes(carnaval, 0,centro_la_vega).
%8 cine-peliculas
cine(cine1, centro_santiago, [pelicula1, pelicula2, pelicula3, pelicula4]).
cine(cine2, centro_santo_domingo, [pelicula2,pelicula4, pelicula1]).
cine(cine3, centro_santo_domingo, [pelicula1, pelicula2, pelicula3, pelicula4]).
cine(cine4, centro_santiago, [pelicula2,pelicula4, pelicula1]).
cine(cine5, bavaro, [pelicula1, pelicula2, pelicula3]).
cine(cine6, sosua, [pelicula2,pelicula4, pelicula1]).
cine(cine7, centro_santiago,[pelicula2,pelicula4, pelicula1]).
%8 A genero-pelicula
genero(pelicula1, terror).
genero(pelicula2, drama).
genero(pelicula3, ficcion).
genero(pelicula4, humor).

%reglas generales
buscarEnLista([], _):-fail.
buscarEnLista([Cabeza|_], CasoABuscar):- CasoABuscar =:= Cabeza, !.
buscarEnLista([_|Cola], CasoABuscar):-buscarEnLista(Cola, CasoABuscar).
%reglas restaurante


%restaurantesPorPrecio(Restaurante, CalPrecio):-precio(Restaurante, Precio),
%restaurante_presupuesto(Presupuesto, TipoComida, Ubicacion).


%Peliculas del genero deseado
buscarPeliculaPorGenero([], _):- fail.
buscarPeliculaPorGenero([Cabeza|_], Genero ):- genero(Cabeza, Genero), !.
buscarPeliculaPorGenero([_|Cola], Genero):- buscarPeliculaPorGenero(Cola, Genero).

cinesPelicula(Lugar, Genero, Cines):- findall(Cine, (cine(Cine, Lugar, Peliculas), buscarPeliculaPorGenero(Peliculas, Genero)), Cines).



%Bares discotecas de precio elevado

buscarDiscoPresupuesto(Lugar, Presupuesto, Puntuacion, CalPrecio, Discotecas):-findall(Disco, (
    discoteca(Disco, Lugar, Precio, Puntuacion), rango_precio(Precio, CalPrecio), Precio =< Presupuesto), Discotecas).

%discotecaPornormalPrecio([Cabeza|_], Puntuacion, Precio, Discotecas):- 

%getDiscoteca(Precio, Puntuacion, Ciudad, Discotecas):-actividades(Ciudad,Discos_ciudad, _,_,_).


