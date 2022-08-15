from pyannote.audio import Pipeline
import json
import torch
'''import ffmpeg

# for f in os.listdir("C:/Users/Илья/Documents/project"):
# 	print(f)

#m4a_file = 'Recording.m4a'
#wav_filename = 'audio_for_dia.wav'
from pydub import AudioSegment

AudioSegment.converter  = "C:/Users/Илья/Downloads/ffmpeg-snapshot/ffmpeg"
track = AudioSegment.from_mp3('034.mp3')
# track = AudioSegment.from_mp3(m4a_file)
#file_handle = track.export(wav_filename, format='wav')'''


class Diarization:

  def __init__(self, aud):
    self.audio = aud
    self.diarization = None

  def predict(self):
    pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization")
    self.diarization = pipeline(self.audio)

  def file(self):
    d = {'speakers': []}
    for turn, _, speaker in self.diarization.itertracks(yield_label=True):
      d['speakers'].append(
        {'speaker': speaker,
         'start': f"{turn.start:.1f}s",
         'stop': f"{turn.end:.1f}s"})

    with open('outfile.json', 'w+') as f:
      f.write(json.dumps(d))

    with open('outfile.json') as f:
      return f.read()