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
sectores(la_vega, [centro_la_vega]).
sectores(samana, [las_galeras,las_terrenas]).

%1.D sectores-actividades
actividades(centro_santo_domingo, [discoteca1, discoteca2, restaurante1, restaurante2, restaurante3, cine1, cine2, teatro1]).
actividades(boca_chica, [discoteca1, restaurante1, restaurante2]).
actividades(centro_santiago, [discoteca1, discoteca3, discoteca2, restaurante1, restaurante2, restaurante3, cine1, cine2, teatro1]).
actividades(sosua,[discoteca1, discoteca2, restaurante1, restaurante2]).
actividades(punta_cana,[discoteca1,discoteca2, restaurante1, restaurante2]).
actividades(centro_la_vega,[discoteca1, discoteca2, restaurante1, 
restaurante2, restaurante3]).
actividades(las_galeras, [discoteca1, restaurante1, restaurante2]).
actividades(las_terrenas, [discoteca2, restaurante2, restaurante3]).
%1.F provincias-vecinas
provincias_vecinas(santiago, la_vega).
provincias_vecinas(santo_domingo,samana).
provincias_vecinas(la_vega, samana).
%2 tipocomida restaurantes
tipocomida(restaurante1, [criolla, rapida, gourmet]).
tipocomida(restaurante2, [gourmet, casera]).
tipocomida(restaurante3, [criolla]).
%3 Rango de precio (economico, medio, elevado)
rango_precio(0, 599, economico).
rango_precio(600,1199, medio).
rango_precio(1200,2400, elevado).
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
eventos_importantes(concierto1, boca_chica).
eventos_importantes(concierto2, sosua).
eventos_importantes(carnaval, centro_la_vega).
%8 cine-peliculas
cine(cine1, [pelicula1, pelicula2, pelicula3]).
cine(cine2, [pelicula2,pelicula4, pelicula1]).
%8 A genero-pelicula
genero(pelicula1, terror).
genero(pelicula2, drama).
genero(pelicula3, ficcion).
genero(pelicula4, humor).

%9 puntuacion-actividades
puntuacion(discoteca1, mala).
puntuacion(discoteca2, excelente).
puntuacion(restaurante1, regular).
puntuacion(restaurante2, regular).
puntuacion(restaurante3, excelente).
puntuacion(cine1, excelente).
puntuacion(cine2, regular).
puntuacion(teatro1, mala).

%10 precioTodo 
precio(concierto1, 600).
precio(concierto2,1300).
precio(carnaval, 0).
precio(discoteca1, 500).
precio(discoteca2, 1200).
precio(restaurante1, 1250).
precio(restaurante2, 700).
precio(restaurante3, 200).
precio(cine1, 250).
precio(cine2, 300).
precio(teatro1, 200).

