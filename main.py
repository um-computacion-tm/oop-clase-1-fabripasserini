from alumno import Alumno
from profesor import Profesor

profe_elio = Profesor("Elio", "elio@gmail.com")
profe_gabi = Profesor("Gabi", "gabi@gmail.com")

print("el nombre de un profe es:" + profe_elio.dame_tu_nombre())
print("El nombre de otro profe es" + profe_gabi.dame_tu_nombre())

alumno_juan = Alumno("juan")
alumno_maria = Alumno("maria")

alumno_juan.falta()
alumno_juan.falta()
alumno_juan.falta()
alumno_juan.falta()
alumno_juan.falta()


print("Inasistencias de Juan: " + str(alumno_juan.__inasistencia__))
print("Inasistencias de Maria: " + str(alumno_maria.__inasistencia__))
print("La condicion de Maria es: " +  alumno_maria.esta_libre())
print("La condicion de Juan es: " + alumno_juan.esta_libre())

alumno_maria.__dieta__ = "vegetariano"
print("Maria es: " + alumno_maria.__dieta__)
alumno_juan.es_vegano()
print("Juan es: " + alumno_juan.__dieta__)

alumno_juan.mentoria(profe_gabi)
print("El mentor de Juan es: " + alumno_juan.__mentor__.__nombre__)

alumno_maria.mentoria(profe_elio)
print("El mentor de Maria es: " + alumno_maria.__mentor__.__nombre__)


