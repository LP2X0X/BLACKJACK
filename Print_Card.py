def Card( rank, suit):
    if len(rank) < 2:
        print('┌─────────┐')
        print('│{}{}       │'.format(rank, suit))  # use two {} one for char, one for space or char
        print('│         │')
        print('│         │')
        print('│    {}    │'.format(suit))
        print('│         │')
        print('│         │')
        print('│       {}{}│'.format(rank, suit))
        print('└─────────┘')
    else: 
        print('┌─────────┐')
        print('│{}{}      │'.format(rank, suit))  # use two {} one for char, one for space or char
        print('│         │')
        print('│         │')
        print('│    {}    │'.format(suit))
        print('│         │')
        print('│         │')
        print('│      {}{}│'.format(rank, suit))
        print('└─────────┘')

def Face_Down_Card():
    print('''
┌─────────┐
│░░░░░░░░░│
│░░░░░░░░░│
│░░░░░░░░░│
│░░░░░░░░░│
│░░░░░░░░░│
│░░░░░░░░░│
│░░░░░░░░░│
└─────────┘
''')