def prueba():
    return """select nombre
              from jugador jug join temporada tempo on (jug.id = tempo.id_jugador)
              where tempo.id = 70"""
  
  # def consulta():
#     return """consulta escrita en sql"""

