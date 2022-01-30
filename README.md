#  FakeUser

##### A simple Python script to fake a periodic keypress to prevent screensaver/screen-sleep/auto-lock on a desktop computer. 

Since 13 March, 2020, I've been in a permanent 'Work From Home' status because of the COVID-19 situation. Although I'm fortunate and grateful that my employer gives me that flexibilty, I've discovered a problem. In my home office, I have several machines that I interact with on a regular basis throughout the day. I'm the only one here (so lonely... 😉); local security is not a concern. I wanted to find a way to prevent screen sleep and the subsequent auto-lock occurring every time I spent more than 10 minutes working with another machine in the group. I _didn't_ want to disable the screen-sleep/auto-lock, though. I wanted a way to _temporarily_ overrride the configured settings. 

A quick Google search revealed the 'pynput' library and what it can do, so I whipped together a little thing that I could spin up in a terminal window, minimize it, and the screen would simply never sleep while it was running. Another goal I had was for it to be as unintrusive as possible while running, even if I was actively using the desktop being kept awake/active. Every 7 minutes or so (semi-randomised), it will simply press the CTRL key and release it. That's it. I can theoretically see the potential for an unexpected keystroke making it through (I imagine it would not be a good thing to leave running while playing a game) - In practice, I stop the script running when I'm using the system, but if I forget, it's not caused any drama (so far). Finally, I have it printing to the console where it's running with some stats (last keypress, total keypresses).

This script is dependent on the 'pynput' library, as mentioned, which can be easily installed via pip (pip3). pynput will need 'evdev', which pip will build/install on the fly, as long as python3-dev has been installed. Installing python3-dev will vary, depending on your OS (using brew, apt, yum, etc.), and is beyond the scope of this document. 

While it does work on Linux, Windows, _and_ MacOS (as long as Python3 is available), I did catch some caveats that are worth noting...

* Linux - actually, here, it "just works", really. Aside from having to install python3-dev on my test machine, it presented no significant issues.
* Windows - Python3 must be the native Windows executable; WSL isn't enough - the dependency on kernel headers for evdev to build are a showstopper. Also, the shebang at the top of the script is meaningless in Windows - run it with 'python fakeuser.py' in a cmd window.
* MacOS - Terminal.app will have to be granted permission, in the Security & Privacy System Preferences (under Accessibility). On the first run, MacOS did throw up a dialog announcing this, but note that it will either let you 'deny' access or simply open the relevant preference pane - you still have to unlock/authenticate and click the tick-box. Until that's done, the script will run, but do nothing.*

I do note, with some amusement, that this readme is roughly five times the length of the script itself. That's okay - this entire repo is pretty gratuitous.

2022-01-30: I note (again) with some amusement (again), that my Windows machines have begun _freaking out_ about fakeuser.py. Apparently, the use of pynput is triggering Windows Defender 'cos it can be used to build a keylogger, and [MS has a couple things to say about that](https://www.microsoft.com/en-us/wdsi/threats/malware-encyclopedia-description?name=HackTool%3aSH%2fPythonKeylogger.B&threatid=2147810695) - it's pretty clear from my code that nothing sketchy is happening, so un-quarantining the file is safe enough to do. Fun!
