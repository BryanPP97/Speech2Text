import os
import numpy as np
import librosa
from pyAudioAnalysis import audioSegmentation

def separar_audio_por_personas(archivo_audio):
    #Carga el archivo de audio
    audio, sr = librosa.load(archivo_audio, sr=None)
    
    # Obtener los segmentos de habla usando pyAudioAnalysis
    segmentos_habla = audioSegmentation.speacker_diarization(audio, sr)
    
    #Separar el audio en segmentos individuales
    personas = {}
    for i , segmentos in enumerate(segmentos_habla):
        inicio, fin = segmento[0], segmento[1]
        persona_id = segmento[2]
        if persona_id not in personas:
            personas[persona_id] = []
        personas[persona_id].append(audio[inicio:fin])
    return personas