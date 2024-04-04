import librosa
import soundfile as sf


input_file = "EDU-Data/output/audio.wav"
output_file = "output.wav"

# 读取.wav文件
wav_data, sr = librosa.load(input_file)
# 调整音高
shifted_wav_data = librosa.effects.pitch_shift(wav_data, sr=sr, n_steps=12)

# 将处理后的音频数据写入到output.wav文件中
sf.write(output_file, shifted_wav_data, sr)
