a = input('enter your gender:')
a = a.lower()
b = input('enter your Marital status:')
b = b.lower()
c = int(input('enter your Family annual income:'))
if a == 'female':
    print('gender : eligible')
else:
    print('gender : not eligible')
if b == 'married':
    print('marital status : eligible')
else:
    print('marital status : not eligible')
if c < 450000:
    print('income : eligible')
else:
    print('income : not eligible')
if (a == 'female' and b == 'married' and c <= 450000):
    print(' congratulation you will eligible for getting Rs.5000 per month in magalir urimai thogai')
else:
    print(' you not eligible for magalir urimai thogai')
    
