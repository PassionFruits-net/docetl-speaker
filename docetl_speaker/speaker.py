import tts_wrapper
import pydub

def render_conversation(responses, voices = None, speaker_key = "speaker", text_key = "text"):
    if voices is None:
        speakers = set(response[speaker_key] for response in responses)
        voices = {speaker: voice
                  for speaker, voice in
                  zip(speakers, tts_wrapper.get_voices().keys())}

    for response in responses:
        yield tts_wrapper.render(response[text_key], voices[response[speaker_key]])


def append_audios(audios):
    output = pydub.AudioSegment.empty()
    for audio in audios:
        output.append(audio)
    return output
