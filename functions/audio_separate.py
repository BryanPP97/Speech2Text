import os
import numpy as np
import librosa
from pyAudioAnalysis import audioSegmentation


def separar_audio_por_personas(carpeta_audio):
    #Carga el archivo de audio
    personas = {}
    for archivo_audio in os.listdir(carpeta_audio):
        if archivo_audio.endswith(".wav"):
            archivo_audio_path = os.path.join(carpeta_audio, archivo_audio)
            audio, sr = librosa.load(archivo_audio, sr=None)
    
            # Obtener los segmentos de habla usando pyAudioAnalysis
            segmentos_habla = audioSegmentation.speacker_diarization(audio, sr)
            
            #Separar el audio en segmentos individuales
            
            for i , segmentos in enumerate(segmentos_habla):
                inicio, fin = segmento[0], segmento[1]
                persona_id = segmento[2]
                if persona_id not in personas:
                    personas[persona_id] = []
                personas[persona_id].append(audio[inicio:fin])
    return personas