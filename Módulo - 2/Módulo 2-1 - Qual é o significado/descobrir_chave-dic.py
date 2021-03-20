def verifica_chave(dicionario, chave):
   if dicionario == {}:
      return False
   else:
      for cada in dicionario.keys():
         if cada == chave:
             return True
         else:
            return False
      
      
        
chave =  'a'
dic = {"a": 1, "b": 2, "c": 2}
print(verifica_chave(dic, chave))