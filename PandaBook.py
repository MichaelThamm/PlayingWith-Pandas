def quest():
    print('Hello travelling panda I am Po, an elder panda, who protects these bamboo forests. '
          'If you need help getting around, let me know first')
    name = input('What is your name young panda so I can add you to my list of travellers: ')

    print(f'\nWell {name}, it is nice to meet you.')
    answer = input('Would you like help getting through the forest? (Y/N)')

    if answer == 'Y':
        print('\nHere is a legend for traversing the forest: ')
        print(legend, end="\n\n")
        print(
            'Stay on the path and look for coins along the way. Eventually you will find the exit, where I will be waiting for you!')
    else:
        print('Okay, you little shit ... get to stepping')


legend = {'entrance': '()',
          'bamboo': '||',
          'path': '.',
          'coin': '*',
          'exit': '$'}

ready = input('Open YourMission.txt in the root directory and give it a read once you have done so type DONE: ')

if ready == 'DONE' or ready == 'done':
    quest()
else:
    print('Maybe next time')
