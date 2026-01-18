import sys
import wikipedia
import pyttsx3

try:
    import speech_recognition as sr
except ImportError:
    sr = None


# ----------------------------
# Initialize Speech Recognizer
# ----------------------------
r = sr.Recognizer() if sr else None

mic_available = False
if sr:
    try:
        sr.Microphone()
        mic_available = True
        print("🎤 Microphone available. You can use voice input.")
    except Exception:
        print("🔇 Microphone not available. Using text mode.")
else:
    print("🔇 speech_recognition not installed. Using text mode.")


# ----------------------------
# Voice Input Function
# ----------------------------
def get_voice_input():
    if not sr:
        return input("Type your query: ")

    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=1)
            print("🎤 Listening... (speak now)")
            audio = r.listen(source, timeout=10, phrase_time_limit=10)
            print("🔄 Processing speech...")
            text = r.recognize_google(audio)
            print(f"📝 You said: {text}")
            return text

    except sr.UnknownValueError:
        print("❓ Could not understand speech.")
        return input("Type your query: ")

    except sr.WaitTimeoutError:
        print("⏰ Timeout. Switching to text input.")
        return input("Type your query: ")

    except Exception as e:
        print(f"❌ Voice error: {e}")
        return input("Type your query: ")


# ----------------------------
# Smart Wikipedia Response
# ----------------------------
def smart_response(query):
    q = query.lower()

    if "exit" in q or "quit" in q:
        print("👋 Exiting assistant.")
        sys.exit(0)

    try:
        wikipedia.set_lang("en")
        return wikipedia.summary(query, sentences=2)

    except wikipedia.exceptions.DisambiguationError as e:
        return f"Your query is ambiguous. Try one of these: {e.options[:3]}"

    except wikipedia.exceptions.PageError:
        return "Sorry, I could not find information on that topic."

    except Exception:
        return "Sorry, something went wrong while fetching information."


# ----------------------------
# Text-to-Speech
# ----------------------------
def speak(text):
    try:
        engine = pyttsx3.init()
        engine.setProperty("rate", 170)
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"❌ TTS error: {e}")


# ----------------------------
# Main Loop
# ----------------------------
print("\n🎙️ Voice Assistant Started (say 'exit' to quit)\n")

while True:
    if mic_available:
        print("=" * 50)
        user_query = get_voice_input()
    else:
        user_query = input("Type your query: ")

    print("🧠 Searching...")
    answer = smart_response(user_query)

    print("🤖", answer)
    speak(answer)
