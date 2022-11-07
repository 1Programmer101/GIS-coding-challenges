import random

all_songs_list = [['Good Vibrations ', 'California Girls ', "Wouldn't It Be Nice ", 'I Get Around ', 'Fun, Fun, Fun ',
                   "Surfin' USA ", 'I Can Hear Music ', 'Barbara Ann ', 'Help Me Rhonda ', 'Then I Kissed Her '],
                  ['Lucy In The Sky With Diamonds', "Sgt. Pepper's Lonely Hearts Club Band", 'The Fool On The Hill',
                   'I Am The Walrus', 'While My Guitar Gently Weeps', 'Magical Mystery Tour', 'Here Comes The Sun',
                   'Eight Days A Week', 'We Can Work It Out', "You've Got To Hide Your Love Away"],
                  ['Just A Shadow', 'Fields Of Fire', 'Where The Rose Is Sown', 'Steeltown', 'Flame Of The West',
                   'Chance', 'Come Back To Me', 'East Of Eden', 'In A Big Country', 'Wonderland'],
                  ['Touch Too Much', 'Shot Down In Flames', 'Girls Got Rhythm', "If You Want Blood (You've Got It)",
                   'Highway To Hell', 'Dirty Deeds Done Dirt Cheap', 'Problem Child', 'Let There Be Rock',
                   'Back In Black', ' Kicked In The Teeth'],
                  ['Black Lake Nidstang', 'Not Unlike The Waves', 'In The Shadow Of Our Pale Companion',
                   'Our Fortress is Burning... II', 'Limbs', 'Ghosts Of The Midwinter Falls', 'Falling Snow',
                   'The Hawthorne Passage', 'Into The Painted Grey', ' I Am The Wooden Doors'],
                  ["Martha's Harbour", 'Flowers In Our Hair', 'What Kind Of Fool', 'Wild Hearted Woman', 'Every Angel',
                   'She Moves Through The Fair', 'Gypsy Dance', 'In The Meadow', 'Road To Your Soul', ' Candytree'],
                  ['Move My Body', 'Real Time Status', 'Infiltrate 202', 'E-Vapor-8', 'Hypnotic St-8', 'Frequency',
                   'Activ-8', 'Brutal-8-E', 'Armageddon', " 8's Revenge"],
                  ['I Am The Law', 'Among The Living', 'Indians', 'One World', 'Armed And Dangerous', 'A.I.R.',
                   'Medusa', 'Metal Thrashing Mad', 'Caught In A Mosh', ' Efilnikufesin (N.F.L.)'],
                  ['We Will Rise', 'Bridge of Destiny', 'Burning Angel', 'Ravenous', 'Enemy Within', 'The Immortal',
                   'Dead Eyes See No Future', 'Dead Bury Their Dead', 'Pilgrim', ' Nemesis'],
                  ['Kathaarian Life Code', 'Natassja In Eternal Sleep', 'The Pagan Winter', 'Paragon Belial',
                   'In The Shadow Of The Horns', 'To Walk The Infernal Fields', 'I En Hall Med Flesk Og Mjod',
                   'A Blaze In The Northern Sky', 'Where Cold Winds Blow', ' Under A Funeral Moon']
                  ]
artists = ["The beach boys", 'THe beatles', 'Big country', 'AC/DC', 'Agalloch', 'All about eve', 'Altern 8', 'Anthrax', 'arch enemy', 'dark throne']
songs_until_played_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
songs_list = []

# with open('Script 1.txt') as text:
#     for line in text:
#         end = line.index(' - ')
#         start = 3
#         songs_list.append(line[start:end])
# print(songs_list)

n = int(input("How many songs to play:"))
print("-------------------------------------------------")
for x in range(n):
    artist_index = random.randint(0, 9)
    while songs_until_played_count[artist_index] != 0:
        artist_index = random.randint(0, 9)
    songs_until_played_count[artist_index] += 2
    for elem in range(10):
        if elem != artist_index:
            songs_until_played_count[elem] = songs_until_played_count[elem] -1
            if songs_until_played_count[elem] < 0:
                songs_until_played_count[elem] = 0
    song_index = random.randint(0, 9)
    song_played = all_songs_list[artist_index][song_index]
    artist = artists[artist_index]
    print(song_played, "by", artist)
