# Voice Coding Assistant - Setup Guide

## Critical Fixes Applied

### 1. **Infinite Retry Loop Fixed** ✅
**Problem**: When the API returned an error (like invalid API key), the code would retry infinitely without breaking out of the loop.

**Solution**: 
- Added a maximum retry count of 3 attempts
- After 3 failed API calls, the program breaks and asks for a new query
- Changed `continue` to `break` on JSON parsing errors
- Better error messages indicating when to check your API key

### 2. **API Key Setup Required** ⚠️

## Setup Instructions

### Step 1: Get an OpenAI API Key

1. Go to [OpenAI Platform](https://platform.openai.com/account/api-keys)
2. Sign in or create an account
3. Click "Create new secret key"
4. Copy the key (it will start with `sk-`)

### Step 2: Update Your .env File

Edit the `.env` file in the project directory:

```bash
# Current (INVALID):
OPENAI_API_KEY=your_openai_api_key_here

# Change to your actual key:
OPENAI_API_KEY=sk-your-actual-key-here-1234567890
```

**Important**: 
- Make sure to paste your actual API key
- Do not share your API key publicly
- The key should start with `sk-`
- It should be at least 48 characters long

### Step 3: Run the Application

#### Option 1: Windows Command Prompt
```bash
set PYTHONIOENCODING=utf-8
python main.py
```

#### Option 2: PowerShell
```powershell
$env:PYTHONIOENCODING="utf-8"
python main.py
```

#### Option 3: Run the API Server
```bash
set PYTHONIOENCODING=utf-8
python server.py
```

Then access the API at `http://localhost:8000`

## How to Use

### Voice Mode
1. The program will ask you to speak
2. Say your request clearly
3. The AI will respond with spoken output

### Text Mode
1. If voice input fails, it automatically switches to text mode
2. Type your request and press Enter
3. The AI will process and respond

### Example Requests
- "Create a Python calculator app"
- "Build a todo list app"
- "Create a web calculator in my_apps folder"
- "Analyze the main.py file"

## Troubleshooting

### Issue: "Incorrect API key provided"
**Solution**: 
- Check that your API key in `.env` is correct
- Make sure it starts with `sk-`
- Verify you copied the entire key
- Try generating a new key on openai.com

### Issue: "No speech detected"
**Solution**: 
- Ensure your microphone is connected and working
- Check that PyAudio is installed: `pip install PyAudio`
- The app will fall back to text mode automatically
- Or press Ctrl+C to switch to text mode

### Issue: "Could not understand speech"
**Solution**:
- Speak more clearly
- Reduce background noise
- Try using text mode instead
- Press Ctrl+C to switch to text mode

### Issue: App keeps retrying with API error
**Solution** (FIXED):
- The app now retries max 3 times then breaks
- Check your API key in the `.env` file
- Make sure it's a valid OpenAI API key

## Features

✅ Voice-to-Code conversion with speech recognition
✅ Text-to-Speech responses with OpenAI's TTS
✅ Smart project organization in `ai_projects/`
✅ File creation, reading, and analysis tools
✅ Command execution with safety checks
✅ Rate limiting to prevent abuse
✅ Fallback to text-only mode if audio unavailable
✅ Graceful error handling with retry limits

## Requirements

- Python 3.8+
- Valid OpenAI API key
- Microphone (optional - works in text mode too)
- All packages from `requirements.txt`

## Environment Setup

```bash
# Install dependencies
pip install -r requirements.txt

# Set up environment (copy example to .env)
cp .env.example .env

# Edit .env with your API key
# Then run with UTF-8 encoding
set PYTHONIOENCODING=utf-8
python main.py
```

## Notes

- The app supports models: `gpt-4o-mini`, `gpt-4o`, `gpt-3.5-turbo`
- Default model is `gpt-4o-mini` for cost efficiency
- Projects are organized automatically in `ai_projects/` folder
- Custom location support: mention a folder name in your request
- All generated code follows best practices and includes error handling
