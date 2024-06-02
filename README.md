# Text To Speech in Python

![TTS Image](tts-logo.png)

This repository contains two scripts that:
1. Takes user input via microphone
2. Translates the same using Google Translate
3. Uses a TTS to speak translated text in English

**Python Environment**: python 3

## Installation Steps

### For Mac

Install the dependencies required for our python packages. 

Follow [this link](https://brew.sh/) to install homebrew as the package manager or simply run the following in your command line/bash:

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Mac should now come with Python 3 installed by default. To check, simply run:

```
which python3
```

If this returns a path then congratulations 🎉 you have python3 installed. If not, follow [this link](https://docs.brew.sh/Homebrew-and-Python) to install python3 using homebrew. Also ensure to set pip.

Next install the depedencies [mpg321](https://formulae.brew.sh/formula/mpg321) and [portaudio](https://formulae.brew.sh/formula/portaudio).

mgp321 allows us to run mp3 files in command line and port audio is for audio I/O management.

```
python -m pip install --upgrade pip setuptools wheel
brew install mpg321
brew install portaudio
```

### Cloning the repository

Download the ZIP file from Github or clone using git clone command in the local directory. 

### Install the requirements

Run the following command in your project directory:

```
pip install -r requirements.txt
```

### Using Python Offline TTS

**Link to TTS Project**: https://github.com/nateshmbhat/pyttsx3

As this is an offline TTS we can simply run it from the command line.

```
$ python3 tts.py

(.env) ➜  tts-test git:(master) ✗ python tts.py
Listening...
Translated Text: My house is in Mumbai city
Sentiment: Sentiment(polarity=0.0, subjectivity=0.0)
==================================================
Listening...
```

### Using Amazon Polly TTS

You will need to set up an AWS account and get the credentials (Access Key and Secret Key to run this project). 

After getting the credential create a .env file in your local directory and add the credentials. The file can look something like this:

```
WS_ACCESS_KEY="YOUR_ACCESS_KEY"
AWS_SECRET="YOUR_SECRET_KEY"
```
Save the above file. 

Next we run the file similar to the local TTS:

```
$ python3 ttspolly.py

(.env) ➜  tts-test git:(master) ✗ python ttspolly.py
Listening...
High Performance MPEG 1.0/2.0/2.5 Audio Player for Layer 1, 2, and 3.
Version 0.3.2-1 (2012/03/25). Written and copyrights by Joe Drew,
now maintained by Nanakos Chrysostomos and others.
Uses code from various people. See 'README' for more!
THIS SOFTWARE COMES WITH ABSOLUTELY NO WARRANTY! USE AT YOUR OWN RISK!

Playing MPEG stream from output.mp3 ...
MPEG 2.0 layer III, 48 kbit/s, 22050 Hz mono
                                                                            
[0:01] Decoding of output.mp3 finished.
Translated Text: My house is in Mumbai city
Sentiment: Sentiment(polarity=0.0, subjectivity=0.0)
==================================================
Listening...
```

For AWS an output.mp3 file will be created in your local directory. 
