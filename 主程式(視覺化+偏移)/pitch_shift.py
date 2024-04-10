import librosa
import soundfile as sf


input_file = "C:/Users/mason/Desktop/作業/科技系/教育大數據專題製作/EDU-Data/output/audio.wav"
output_file = "C:/Users/mason/Desktop/作業/科技系/教育大數據專題製作/EDU-Data/output/output.wav"

# 读取.wav文件
wav_data, sr = librosa.load(input_file)
# 调整音高
shifted_wav_data = librosa.effects.pitch_shift(wav_data, sr=sr, n_steps=8,bins_per_octave=24)

# 将处理后的音频数据写入到output.wav文件中
sf.write(output_file, shifted_wav_data, sr)
