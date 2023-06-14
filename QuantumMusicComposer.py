import numpy as np

class QuantumNote:
    def __init__(self, frequency):
        self.frequency = frequency

    def play(self):
        print("Playing note with frequency:", self.frequency)

class QuantumMusicComposer:
    def __init__(self, scale):
        self.scale = scale

    def compose_song(self, duration):
        song = []

        for _ in range(duration):
            random_index = np.random.randint(len(self.scale))
            frequency = self.scale[random_index]
            note = QuantumNote(frequency)
            song.append(note)

        return song

def main():
    # Define a major scale in Hz
    major_scale = [261.63, 293.66, 329.63, 349.23, 392.00, 440.00, 493.88]

    # Create a QuantumMusicComposer with the major scale
    composer = QuantumMusicComposer(major_scale)

    # Compose a song with a duration of 5 notes
    song = composer.compose_song(5)

    # Play each note in the song
    for note in song:
        note.play()

if __name__ == "__main__":
    main()
