from time import sleep
import time
import sys
import os


os.system('clear')
print(f'{'Sorai - Nadin Amizah':^30}')
print('-'*30)
def print_lyrics():
    lines = [
        ('Kau dan aku saling membantu', 0.18),
        ('Membasuh hati yang pernah pilu', 0.18),    
        ('Mungkin akhirnya tak jadi satu', 0.20),
        ('Namun bersorai pernah bertemu', 0.18),    
    ]
    
    delays = [0.9, 1, 0.9, 5]
    
    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print('')
        
print_lyrics()
    