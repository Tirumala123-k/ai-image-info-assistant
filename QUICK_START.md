# Quick Start Guide - Voice Coding Assistant

## Summary of Fixes

✅ **Infinite retry loop FIXED** - Now exits gracefully after 3 failed API attempts
✅ **Unicode emoji support FIXED** - Use `PYTHONIOENCODING=utf-8` environment variable
✅ **Invalid API key handling IMPROVED** - Clear error message telling you to check your API key
✅ **Missing dependencies FIXED** - Graceful fallback when speech_recognition unavailable

---

## How to Run (Windows)

### Step 1: Set Up Your API Key

Edit the `.env` file and replace the placeholder with your actual OpenAI API key:

```bash
OPENAI_API_KEY=sk-your-actual-key-here
```

Get your API key from: https://platform.openai.com/account/api-keys

### Step 2: Run with UTF-8 Encoding

#### Option A - Command Prompt
```bash
set PYTHONIOENCODING=utf-8
python main.py
```

#### Option B - PowerShell
```powershell
$env:PYTHONIOENCODING="utf-8"
python main.py
```

#### Option C - Run the API Server
```bash
set PYTHONIOENCODING=utf-8
python server.py
```

Then send requests to: `http://localhost:8000/api/ask`

---

## What Happens Now

1. **Voice Mode** (if microphone available)
   - Listens for your voice input
   - Falls back to text if speech not detected

2. **Text Mode**
   - Asks you to type your request
   - Processes with AI

3. **API Retry Logic**
   - Tries up to 3 times on API errors
   - Shows clear error message after failures
   - Doesn't hang in infinite loop anymore

---

## Example Requests

- "Create a Python calculator app"
- "Build a todo list app in React"
- "Create a weather app in my_workspace folder"
- "Write a snake game"
- "Analyze the performance of my code"

---

## Troubleshooting

### Issue: "Incorrect API key provided"
- ✓ Check that your `.env` file has the correct API key
- ✓ Key should start with `sk-`
- ✓ Make sure there are no extra spaces
- ✓ Get a new key from: https://platform.openai.com/account/api-keys

### Issue: Microphone not working
- ✓ Install PyAudio: `pip install PyAudio`
- ✓ Or use text mode instead (press Ctrl+C when asked for voice input)

### Issue: "No speech detected"
- ✓ Speak more clearly
- ✓ Reduce background noise
- ✓ Press Enter to fall back to text mode
- ✓ Close the app and use text mode directly

### Issue: Output has garbled characters
- ✓ Make sure to set: `PYTHONIOENCODING=utf-8`
- ✓ This enables emoji support on Windows

---

## Installation (if not done yet)

```bash
# Install all dependencies
pip install -r requirements.txt

# Copy example env (if not already done)
cp .env.example .env

# Edit .env and add your OpenAI API key
# Then run with UTF-8 support
set PYTHONIOENCODING=utf-8
python main.py
```

---

## Features

✨ **Voice-to-Code**: Speak your project requirements
🎙️ **Speech Recognition**: Automatic fallback to text mode
🤖 **AI-Powered**: Uses GPT-4o-mini by default (configurable)
📁 **Project Organization**: Auto-creates folders in `ai_projects/`
🛠️ **Multi-Tool Support**: Create, read, analyze, execute code
🔒 **Safe Commands**: Only safe system commands allowed
⏱️ **Graceful Errors**: No infinite loops, clear error messages

---

## The Fix Applied

The main issue was an **infinite retry loop** when API requests failed. The code would keep retrying the same failing request forever instead of moving on.

**What changed:**
- Added `max_retries = 3` to limit attempts
- Added `retry_count` to track failures
- On 3 failures, the loop breaks and asks for a new query
- Error messages now clearly indicate what went wrong

**Before Fix:**
```
API Error: ...
API Error: ...
API Error: ...
API Error: ...  [repeats forever]
```

**After Fix:**
```
API Error: ...
API Error: ...
API Error: ...
❌ Failed after 3 retries. Please check your API key and try again.
[Back to voice input prompt]
```

---

## Next Steps

1. ✅ Fix applied and tested
2. 🔑 Add your OpenAI API key to `.env`
3. ▶️ Run: `python main.py` (with UTF-8 encoding)
4. 🎤 Start speaking or typing requests!
