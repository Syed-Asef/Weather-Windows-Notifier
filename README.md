# Weather Windows Notifier

A python script which generates a weather report notification on windows. You are able to set this on task scheduler to fit your preferred time/event for the notification to generate.

![Alt text](image.png)

## Requirements

You'll need the following to be able to run this:
- `winotify`
- `requests`
- `python 3.6+`

To install the libraries run:
 ```bash
pip3 install winotify
```
Replace winotify with requests as well.
## Usage
Before setting the script to run on task scheduler please change the following variables to match your location (on both the .py and .pyw files).
```python
#Change these variables to match your location
latitude = 
longitude = 
```

To make the script run on a set basis (such as when logging in):
1. Open task scheduler and right click on "Task Scheduler Library"
2. Click on Create Task
3. On the General tab, add a name of your choice
4. On the Triggers tab, click on New... and configure task to run on your liking
5. On the Actions tab, click on New... then Browse... find the following exe under `C:\Users\USERNAME\AppData\Local\Microsoft\WindowsApps\pythonw3.11.exe` (REPLACE THE USERNAME) and select it. The exe name and location may vary depending on the version and installation location. In the Add Arguements box put weather.pyw and in the Start In box put the folder path containing the script.