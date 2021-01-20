Tesla_model_3 = '200,000 Dollars'
mercedes = '500,000 Dollars'
Bmw_m_1450 = '1,000,000,000 Dollars'
command = input('>Username: ')
print ('input car brand youy prefer')
while :

    cars_available = input('>Tesla ,Bmw ,mercedes ')
    if cars_available.lower == 'Tesla':
         price_tag = int(input('>pls what amount are you budgeted '))
       if price_tag > 500000:
          print ('>Not eligible')
        else:
           print('>Continue pls')
          break
     elif cars_available.lower == 'bmw':
          if price_tag > 500000:
          print ('>Not eligible')
        else:
           print('>Continue pls')
          break
    elif cars_available.lower == 'mercedes':
          if price_tag > 500000:
          print ('>Not eligible')
        else:
           print('>Continue pls')
          break
         