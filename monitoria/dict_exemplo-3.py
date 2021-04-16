# Requisicao para api fictícia sobre covid
# Requisitamos o número de infectados do dia 01/03/2021 a 07/03/2021 por Estado
resultado = [
    {
        "data": "01/03/2021",
        "estado": "RJ",
        "numero_infectados": 10_000
    },
    {
        "data": "01/03/2021",
        "estado": "MG",
        "numero_infectados": 5_000
    },
    {
        "data": "01/03/2021",
        "estado": "PR",
        "numero_infectados": 2_000
    },
    # ...
]

# Outra forma
resultado = [
    {
        "01/03/2021": [
            {
                "estado": "RJ",
                "numero_infectados": 10_000
            },
            {
                "estado": "MG",
                "numero_infectados": 5_000
            },
            {
                "estado": "PR",
                "numero_infectados": 2_000
            },
        ]
    },
    {
        "02/03/2021": [
            {
                "estado": "RJ",
                "numero_infectados": 8_000
            },
            {
                "estado": "MG",
                "numero_infectados": 4_000
            },
            {
                "estado": "PR",
                "numero_infectados": 1_000
            },
        ]
    },
    # ...
]

