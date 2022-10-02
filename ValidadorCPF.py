cpf = '16899535009'

def soma_digito(cpf, range_):
    soma = 0
    acumulador = 0

    for index in range(range_, 1, -1):
        soma += int(cpf[acumulador]) * index

        acumulador += 1

    digito = 11 - (soma % 11)
    if range_ == 10:
        return 0 if digito > 9 else digito
    else:
        return digito

primeiro_digito = soma_digito(cpf[:-2], 10)
segundo_digito = soma_digito(f'{cpf[:-2]}{primeiro_digito}', 11)

novo_cpf = f'{cpf[:-2]}{primeiro_digito}{segundo_digito}'

if cpf == novo_cpf:
    print('CPF Válido!')
else:
    print('CPF inválido!')