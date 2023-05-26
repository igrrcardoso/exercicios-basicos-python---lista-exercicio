while True:
    
    cm_ou_m = input('você quer converter "cm" ou "m" ?')


    if cm_ou_m == "cm":
   
        cm_to_m = int(input('digite quantos "cm" quer converter em "metros": '))
        cm_para_metros = cm_to_m / 100
        print(f'{cm_to_m} centimetros em metros é = {cm_para_metros}')
        
   


    elif cm_ou_m == "m":
        metros_para_centimetros = int(input('digite quantos "metros" quer converter em "cm": '))
        conversão_m_cm = metros_para_centimetros * 100
        print(f'{metros_para_centimetros} metros em centimetros é = {conversão_m_cm}')


