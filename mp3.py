import mp3play
filename = r'C:\Users\administrator\Desktop\y.mp3'
mp3 = mp3play.load(filename)
mp3.play()
import time
time.sleep(min(30, mp3.seconds()))
mp3.stop()
