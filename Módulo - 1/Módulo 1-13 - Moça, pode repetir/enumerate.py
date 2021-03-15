#função de nome enumerate
lista_nums = [100,200,300,400,500,600,700,800]
for idx, item in enumerate(lista_nums):
    lista_nums[idx] += 1000
print(lista_nums)