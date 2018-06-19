import speech_recognition as sr
import pyttsx
from retrieval_ans import ai_response

### RECOGNIZER ###
# Recognizer recognises speech

def initialise_recognizer():
    # New instance as r
    r = sr.Recognizer()
    return r

def initialise_mic():
    # Open MIC
    mic = sr.Microphone()
    return mic

# Set responses
response = {
    "success" : True,
    "error"  : None,
}
    
def recognize_speech_from_mic(r,audio):
    try:
        response = (r.recognize_google(audio))

    except LookupError:
        response["success"] = False
        response["error"] = "Google audio API unavailable"

    except sr.UnknownValueError:
        response["error"] = "Unable to recognize speech"

    return response

def mic_listen(mic,r):
    with mic as source:
        # mic will wait for 0.3 sec before it will listen
        r.adjust_for_ambient_noise(source, duration = 0.3)
        audio = r.listen(source)
    return audio

def start_conversation():
    r = initialise_recognizer()
    mic = initialise_mic()
    engine = pyttsx.init()
    engine.say("Good morning! Ask me anything")
    engine.runAndWait()
    ans = continue_conversation(mic,r,engine)
    return ans

def continue_conversation(mic,r,engine):
    print("say something")
    audio = mic_listen(mic,r)
    myresponse = recognize_speech_from_mic(r,audio)
    ans = ai_response(myresponse)
    print(ans)
    repeat_response(engine,myresponse,ans)
    return ans

def repeat_response(engine,myresponse,ans):
    engine.say((myresponse,"So the answer to this is",ans))
    engine.runAndWait()



