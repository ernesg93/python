# import imageio

# filenames = ['team-pic1.png', 'team-pic2.png']
# images = [ ]

# for filename in filenames:
#   images.append(imageio.imread(filename))

# imageio.mimsave('team.gif', images, duration = 0.5)

dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
              'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
              'sign', 'the', 'to', 'uncertain']


palabras_frase = input().split()
corrector = True

for palabra in palabras_frase:
    if palabra not in dictionary:
        print(palabra)
        corrector = False


if corrector:
    print('OK')