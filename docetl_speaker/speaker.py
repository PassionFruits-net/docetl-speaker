import tts_wrapper
import pydub

def render_conversation(responses, voices = None, speaker_key = "speaker", text_key = "text"):
    if voices is None:
        speakers = set(response.get(speaker_key, "default") for response in responses)
        voices = {speaker: voice
                  for speaker, voice in
                  zip(speakers, tts_wrapper.get_voices().keys())}

    default_voice = voices.get("default", None)
    
    for response in responses:
        yield tts_wrapper.render(response[text_key], voices.get(response.get(speaker_key, "default"), default_voice))


def append_audios(audios):
    output = pydub.AudioSegment.empty()
    for audio in audios:
        output.append(audio)
    return output
