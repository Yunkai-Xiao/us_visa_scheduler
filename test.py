import pygame

def play_ring_sound(sound_file):
    # Initialize pygame mixer
    pygame.mixer.init()

    # Load the sound file
    ring_sound = pygame.mixer.Sound(sound_file)

    # Play the sound
    ring_sound.play()

    # Keep the script running until the sound is playing
    while pygame.mixer.get_busy():
        pygame.time.Clock().tick(10)

# Replace 'your_ring_sound_file.wav' with the path to your sound file
play_ring_sound('ring-sound.wav')
