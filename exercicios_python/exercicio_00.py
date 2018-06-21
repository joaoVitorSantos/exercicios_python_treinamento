# coding: utf-8

def preco_aluguel_carro(dias,km):
    ''' Recebe uma quantidade de dias que o carro foi alugado e a 
    quantidade de kilometros rodados, e retorna o valor a ser pago.
    1 dia: 60 reais mais R$ 0,15 por km rodado.
    Dica: use round() para arrendondar o resultado'''

    preco_dia = dias * 60
    preco_km = km * 0.15

    preco_total = preco_dia + preco_km

    return preco_total

def dias_para_segundos(dias,horas,minutos,segundos):
    ''' Recebe uma data em dias com horas,minutos,segundos, e retorna 
    a data em segundos'''

    minutos_convertidos = 60 * minutos
    horas_convertidas = 60 * 60 * horas
    dias_convertidos = 3600 * 24 * dias

    preco_total = dias_convertidos + horas_convertidas + minutos_convertidos + segundos

    return preco_total

def salario(dinheiro_horas,horas_mensais):
    ''' Recebe quanto ganha por hora e quantas horas trabalho ao mês,
    e retorna o salário líquido.
    Descontos:
    - INSS é 8% do salário bruto
    - IR é 11% do salário bruto
    - Sindicato é 5% do salário bruto'''

    bruto = dinheiro_horas * horas_mensais
    desconto_inss = 8/100 * bruto
    desconto_ir = 11/100 * bruto
    desconto_sindicato = 5/100 * bruto

    liquido = bruto - (desconto_inss + desconto_ir + desconto_sindicato)

    return liquido

# Área de testes: só mexa aqui se souber o que está fazendo!
acertos = 0
total = 0 

def test(obtido, esperado):
    global acertos, total
    total += 1
    if obtido != esperado:
        prefixo = ' Falhou.'
    else:
        prefixo = ' Passou.'
        acertos += 1
        print ('%s Esperado: %s \tObtido: %s' % (prefixo, repr(esperado), 
            repr(obtido)))

def main():

    print('Preco a pagar pelo aluguel do carro:')
    test(preco_aluguel_carro(10,100), 615.00)
    test(preco_aluguel_carro(13,133), 799.95)
    test(preco_aluguel_carro(1,0), 60.00)
    test(preco_aluguel_carro(3,79), 191.85)

    print('Dias,horas,minutos e segundos para segundos:')
    test(dias_para_segundos(0,0,0,1), 1)
    test(dias_para_segundos(0,0,1,0), 60)
    test(dias_para_segundos(0,0,1,1), 61)
    test(dias_para_segundos(0,1,0,0), 3600)
    test(dias_para_segundos(0,1,1,0), 3660)
    test(dias_para_segundos(0,1,1,1), 3661)
    test(dias_para_segundos(1,0,0,0), 86400)
    test(dias_para_segundos(0,23,59,59), 86399)
    test(dias_para_segundos(1,1,1,1), 90061)
    test(dias_para_segundos(10,20,59,1), 939541)

    print('Salário líquido:')
    test(salario(10,80), 608)
    test(salario(100,30), 2280)
    test(salario(2.5,300), 570)
    test(salario(5,120), 456)


if __name__ == '__main__':
    main()
    print("\n%d Testes, %d Ok, %d Falhas: Nota %.1f" %(total, acertos,
        total-acertos, float(acertos*10)/total))
    if total == acertos:
        print("Parabéns, seu programa rodou sem falhas!")