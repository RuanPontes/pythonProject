import emoji
import math



print(emoji.emojize('''\nBem Vindo ao programa calculadora em python :computer:
nessa versão será possivel calcular :arrow_down::arrow_down:
\n+ \n- \nx \n◺
^ \n√x ''',language='alias'))

a=input('\nDeseja fazer qual calculo? \n\nadição + \nsubtração - \nmutiplicação x \nhipotenusa ◺ \npotenciação ^ \nraiz quadrada √x \nDigite aqui:').strip().lower()

if a == 'adição':
   s1=int(input('\nDigite o primeiro número da adição: '))
   s2=int(input('Digite o segundo número da adição: '))
   print('\nO resultado da adição é {}'.format(s1+s2))

if a == 'subtração':
    r1=int(input('\nDigite o primeiro número da subtração: '))
    r2=int(input('Digite o segundo número da subtração: '))
    print('\nO resultado da subtração foi {}'.format(r1-r2))

if a == 'divisão':
    d1=int(input('\nDigite o primeiro número da divisão: '))
    d2=int(input('Digite o segundo número da divsão: '))
    print('\nO resultado da divisão é igual a {}'.format(d1//d2))

if a == 'multiplicação':
    m1=int(input('\nDigite o primeiro número da multiplicação: '))
    m2=int(input('Digite o segundo número da multiplicação: '))
    print('\nO resultado da multiplicação foi {}'.format(m1*m2))

if a == 'hipotenusa':
    h1=int(input('\nDigite o angulo do cateto adjacente: '))
    h2=int(input('\nDigite o angulo do cateto oposto: '))
    print('\nO resultado da hipotenusa é {:.2f}'.format(math.hypot(h1,h2)))

if a == 'potenciação':
    p1=int(input('\nDigite o primeiro número: '))
    p2=int(input('Digite o segundo número: '))
    print('\nO resultado da potenciação foi {:.2f}'.format(p1**p2))

if a == 'raiz quadrada':
    q1=int(input('\nDigite o número: '))
    print('O resultado é {:.2f}'.format(math.sqrt(q1)))

print(emoji.emojize('\nObrigado por utilizar o programa :registered: '))