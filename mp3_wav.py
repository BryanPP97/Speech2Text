import os
from pydub import AudioSegment

def convertir_mp3_a_wav(mp3_file, wav_file):
    # Cargar el archivo MP3
    audio = AudioSegment.from_mp3(mp3_file)

    # Guardar el archivo en formato WAV
    audio.export(wav_file, format="wav")

# Ruta de la carpeta que contiene los archivos MP3
carpeta_mp3 = "C:/Users/Javier Peña/Documents/BRYAN/GRABACIONES_HSBC"

# Obtener la lista de archivos MP3 en la carpeta
archivos_mp3 = [archivo for archivo in os.listdir(carpeta_mp3) if archivo.endswith(".mp3")]

# Contador para el número consecutivo
contador = 1

# Iterar sobre la lista de archivos MP3
for mp3_file in archivos_mp3:
    # Ruta completa del archivo MP3
    mp3_path = os.path.join(carpeta_mp3, mp3_file)

    # Nombre del archivo WAV de salida con el número consecutivo
    wav_file = f"grabacion_{contador}.wav"

    # Ruta completa del archivo WAV de salida
    wav_path = os.path.join(carpeta_mp3, wav_file)

    # Llamar a la función para convertir el archivo
    convertir_mp3_a_wav(mp3_path, wav_path)

    # Incrementar el contador
    contador += 1