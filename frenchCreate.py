import genanki
from gtts import gTTS
import csv
import os
from pydub import AudioSegment
from pydub.playback import play
import subprocess
import json

# Prompt user for input file name
user_input = input("Enter your input: ")

# Read words from csv file
filename = user_input
words = []
with open(filename, newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in reader:
        for word in row:
            # Remove any special characters not used in French
            word = ''.join(c for c in word if c.isalpha() or c.isspace())
            words.append(word.strip())

print(words)
# Define Anki model and deck
my_model = genanki.Model(
    1380120064,
    'FrenchDeck',
    fields=[
        {'name': 'Question'},
        {'name': 'Answer'}
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': '{{Question}}',
            'afmt': '{{FrontSide}}<br>{{Answer}}',
        },
    ])

my_deck = genanki.Deck(
    2059400191,
    'los1n')

# Generate audio files and create Anki notes
audio_paths = []
for i, word in enumerate(words):
    # Generate audio using gTTS
    clean_word = "".join(c for c in word if c.isalpha() or c.isspace()) # Remove special characters
    audio = gTTS(text=clean_word, lang='fr')
    audio_path = '/Users/lolhomie/Documents/audio/'+clean_word+'.mp3'
    audio.save(audio_path)
    audio_paths.append(audio_path)
    
    # Load audio file using pydub
    audio_segment = AudioSegment.from_file(audio_path, format='mp3')

    # Add the audio as an attachment to the note
    my_note = genanki.Note(
        model=my_model,
        fields=[word + "[sound:" + audio_paths[i] + "]", "[sound:" + audio_paths[i] + "]"]
    )
    my_deck.add_note(my_note)

# Create Anki package and write to file
my_package = genanki.Package(my_deck)
my_package.write_to_file('/Users/lolhomie/Documents/crappy3.apkg')

# Prompt user to open Anki and start testing
user_input = ''
while user_input != 'y':
    user_input = input('Are you ready to open Anki? (type y): ')
    
if user_input == 'y':
    subprocess.call(['open', '/Users/lolhomie/Documents/crappy3.apkg'])
    subprocess.call(['python3', 'pytest2.py',  str(words)])
