media = 7
nota1 = float(input('Informe sua nota  '))
nota2 = float(input('Informe sua segunda nota '))
nota3 = float(input('Informe sua terceira nota '))
media = (nota1 + nota2 + nota3) / 3
repetente = True
if(media >= 7):
  print('Passou, sua nota é' ,media)
elif(media < 7 and repetente):
 print('Reprovado, sua nota é' ,media)
elif(media < 7):
  print('Não passou, sua nota é ' , media)
else:
  print("Não passou, sua nota é" ,media)