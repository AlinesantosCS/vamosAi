'''
Crie uma função chamada complete_series que recebe uma lista de números inteiros não negativos como parâmetro e retorna uma nova lista com a sequência completa dos números.

Dica: As sequências devem sempre começar em 0 e terminar com o maior valor da lista.

Se os números da sequência não estiverem em ordem, você deverá ordená-los, mas se houver valores repetidos, você terá que retornar somente o valor zero no array.
'''

def complete_series(seq): 
  
  sem_repeticao = set(seq)
  if len(seq) > len(sem_repeticao):
    return[0]
  
  maior_numero = max(seq)
  return list(range(maior_numero + 1))