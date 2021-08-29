:-dynamic provincia/1.
:-dynamic playa/1.
:-dynamic sector_playas/2.
:-dynamic restaurante/5.
:-dynamic discoteca/4.
:-dynamic cine/4.
:-dynamic cine_pelicula/2.
:-dynamic sector/1.
:-dynamic sectores_provincia/2.
:-dynamic eventos_importantes/3.
:-dynamic eventos_culturales/3.
:-dynamic genero/2.
:-dynamic tipocomida/2.

%1.provincias
provincia(santiago).
provincia(santo_domingo).
provincia(puerto_plata).
provincia(higuey).
provincia(la_vega).
provincia(samana).
%1.A playas por sector
sector_playas(boca_chica,[boca_chica]).
sector_playas(sosua, [sosua, cabarete, alicia]).
sector_playas(bavaro, [bavaro]).
sector_playas(punta_cana,[punta_cana,arena_blanca]).
sector_playas(las_terrenas, [las_terrenas]).
sector_playas(las_galeras, [las_galeras]).
%1.B sectores por provincia
sectores_provincia(santo_domingo, [boca_chica, centro_santo_domingo]).
sectores_provincia(santiago, [centro_santiago]).
sectores_provincia(puerto_plata, [sosua]).
sectores_provincia(higuey,[bavaro, punta_cana]).

%1.D sectores_provincia-actividades
%restaurante (nombre, lugar, precio, calificacion, hora de cierre)
restaurante(restaurante1,boca_chica, 400, 2, 22).
restaurante(restaurante1,centro_santo_domingo, 400, 5, 23).
restaurante(restaurante2,centro_santo_domingo, 500, 4, 20).
restaurante(restaurante3,centro_santiago, 1000, 7, 16).
restaurante(restaurante4,centro_santiago, 1400, 9, 0).
restaurante(restaurante5,sosua, 100, 5, 23).
restaurante(restaurante6,bavaro, 200, 3, 14).
restaurante(restaurante7,bavaro, 900, 10, 18).
restaurante(restaurante8,sosua, 700, 6, 12).
restaurante(restaurante9,punta_cana, 250, 6, 3).
restaurante(restaurante10,punta_cana, 400, 8, 5).

discoteca(discoteca1,centro_santo_domingo, 100, 1).
discoteca(discoteca2,centro_santiago, 500, 7).
discoteca(discoteca3,centro_santiago, 500, 8).
discoteca(discoteca4,sosua, 1200, 9).
discoteca(discoteca5,bavaro, 1200, 1).
discoteca(discoteca6,punta_cana, 1200, 10).
discoteca(discoteca7, centro_santiago, 1400, 10).
discoteca(discoteca8,punta_cana, 1200, 8).

cine(cine1, centro_santiago, 500, 5).
cine(cine2,centro_santiago, 250, 9).
cine(cine3,centro_santiago, 250, 8).
cine(cine4,centro_santo_domingo, 400, 1).
cine(cine5,centro_santo_domingo, 300, 8).
cine(cine6,centro_santo_domingo, 300, 6).
cine(cine7,punta_cana, 250, 9).

%2 tipocomida restaurantes
tipocomida(restaurante1, criolla).
tipocomida(restaurante2, casera).
tipocomida(restaurante3, casera).
tipocomida(restaurante4, gourmet).
tipocomida(restaurante5, buffet).
tipocomida(restaurante6, criolla).
tipocomida(restaurante7, rapida).
tipocomida(restaurante8, buffet).
tipocomida(restaurante9, criolla).
tipocomida(restaurante10, gourmet).

%3 Rango de precio (economico, medio, elevado)
rango_precio(Precio, economico):- Precio =< 599.
rango_precio(Precio, medio):- Precio >= 600, Precio =< 1199.
rango_precio(Precio, elevado):- Precio >= 1200.

%3.1 Rango calificacion(mala, regular, buena)
rango_calificacion(Calificacion, mala):- Calificacion =< 4.
rango_calificacion(Calificacion, regular):- Calificacion >= 5, Calificacion =< 7.
rango_calificacion(Calificacion, excelente):- Calificacion >= 8, Calificacion =< 10.


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

%6 eventos_culturales secto
eventos_culturales(obra_teatro1, 1500, centro_santiago).
eventos_culturales(obra_teatro2, 1300, sosua).
eventos_culturales(carnaval, 0,centro_la_vega).

%7 eventos, sector
eventos_importantes(concierto1, 600, boca_chica).
eventos_importantes(concierto2, 1300, sosua).
eventos_importantes(concierto_juan_luis_guerra, 600, boca_chica).
eventos_importantes(noche_jazz, 1300, centro_santiago).
%8 cine-peliculas
cine_pelicula(cine1, [pelicula1, pelicula2, pelicula3, pelicula4]).
cine_pelicula(cine2,  [pelicula2,pelicula4, pelicula1]).
cine_pelicula(cine3,  [pelicula1, pelicula2, pelicula3, pelicula4]).
cine_pelicula(cine4,  [pelicula2,pelicula4, pelicula1]).
cine_pelicula(cine5,  [pelicula1, pelicula2, pelicula3]).
cine_pelicula(cine6,  [pelicula2,pelicula4, pelicula1]).
cine_pelicula(cine7, [pelicula2,pelicula4, pelicula1]).
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

%Con el presupuesto que tenemos para el día ¿Hay algún sitio donde podríamos comer en 
%X, que sea Y y sirvan comida Z y nos quede el W% 
%del mismo disponible para otras actividades del día?

restaurantePresupuesto(Presupuesto, Ciudad, NivelEconomico, TipoComida, Porcentaje, Restaurante):-restaurante(Restaurante, Ciudad, Costo, _, _),
rango_precio(Costo, NivelEconomico), tipocomida(Restaurante, TipoComida),Presupuesto * (Porcentaje / 100) >= Costo.


%Actividades culturales con X cantidad de dinero (nombre y lugar)

actividadPorPresupuesto(Presupuesto, Actividad, Lugar):- eventos_culturales(Actividad, Costo, Lugar), Costo =< Presupuesto.
todasLasActividades(Presupuesto, Lista):-findall((X,Y), actividadPorPresupuesto(Presupuesto, X, Y), Lista).

%Peliculas del genero deseado
buscarPeliculaPorGenero([], _):- fail.
buscarPeliculaPorGenero([Cabeza|_], Genero ):- genero(Cabeza, Genero), !.
buscarPeliculaPorGenero([_|Cola], Genero):- buscarPeliculaPorGenero(Cola, Genero).

cinesPelicula(Lugar, Genero, Cines):- findall(Cine, (cine_pelicula(Cine, Peliculas), cine(Cine,Lugar,_,_), buscarPeliculaPorGenero(Peliculas, Genero)), Cines).

%Bares discotecas de precio elevado
buscarDiscoPresupuesto(Lugar, Presupuesto, Puntuacion, CalPrecio, Discotecas):-findall(Disco, (
    discoteca(Disco, Lugar, Precio, NumeroPuntuacion), rango_calificacion(NumeroPuntuacion, Puntuacion), rango_precio(Precio, CalPrecio), Precio =< Presupuesto), Discotecas).


% extra 1 , El visitante ha escuchado acerca de un restaurante en
% especifico y le gustaria saber si el mismo tiene diversas surcursales

sucursales(Nombre, Resultado):- bagof(Sector,restaurante(Nombre,Sector,_,_,_),Resultado).

% extra 2 , El visitante ha escuchado acerca de un cine en
% especifico y le gustaria saber si el mismo tiene diversas surcursales

cine_sucursales(Nombre, Resultado):- bagof(Sector,cine(Nombre,Sector,_,_),Resultado).

% extra 3 Buscar un restaurante que quede cerca de algun evento
% importante

restauranteimp(Evento,Presupuesto,Hora_restaurante, Restaurante):- eventos_importantes(Evento,Precio,Lugar)
,restaurante(Restaurante,Lugar,Preciob,_,Hora_cierre),Hora_restaurante<Hora_cierre
,Calculo is Precio+Preciob,Presupuesto>=Calculo.


