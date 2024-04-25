# 2. Interseção de Conjuntos:
# Crie dois conjuntos com seus hobbies e os hobbies de um amigo.
# Encontre os hobbies em comum entre vocês e imprima-os.

meus_hobbies = {'correr', 'ir praia', 'andar moto'}
hobbies_amigo = {'jogar bola', 'andar moto', 'viajar'}
hobbies_comum = meus_hobbies.intersection(hobbies_amigo) #comando "intersection" encontra o hobbies comum nos dois conjuntos.
print("hobbies_comum:", hobbies_comum)