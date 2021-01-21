print('cars available')
print('tesla,bmw,mercedes ')
car_choosen = input ('pls type your intreset in options: ')
while car_choosen.lower != mercedes:
  if car_choosen.lower =='tesla':
    price_tag = (500000)
    print('what is yourbugdet in figures: ')
    amount = int(input())
    if amount > price_tag:
      print('sorry were are not intrested')
      break
    else:
      print('pls secure registration and continue')
      break
  elif car_choosen.lower == 'bmw':
    price = (800000)
    print('what yur planned budget')
    bmw = int(input(''))
    if bmw > price:
      print('were wasting our time here')
      break
    else:
      print('nice just a few things left')
      break
else:
  print('pls your price range in numbers')
  to_pay = (700000)
  mercedes = int(input())
