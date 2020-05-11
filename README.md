# Simple-sound-bar-python-twitch-bot-using-twitchio-and-vlc
Simple sound bar python twitch bot. You can add sounds so your spectators play them on stream, using chat commands


IRC_TOKEN = "YOUR_IRC_TOKEN" # You can get this here https://twitchapps.com/tmi/ 
                         # (logit through your bot account or from your own if you want your account to be a bot)
                         # Example IRC_TOKEN='oauth:sdwa8d0adsaddwadwadw98d6awdn'

CLIENT_ID = "YOUR_CLIENT_ID" #You get this here https://dev.twitch.tv/console/apps register an app and copy app client id
                           # Example CLIENT_ID='t9tvmegddnwajkda78dagmttufu7wk'

BOT_NICK = "YOUR_BOT_NICK"  # Your bots account nickname(or your if you use your acc as bot)

INITIAL_CHANELS = ['YOUR_INITIAL_CHANEL1', 'YOUR_INITIAL_CHANEL2',] # Nicknames of chanels where bot will work

SOUND_LOCATION = "C:/Users/111/Documents/twitch_bot/sounds"

SOUND_COMMAND = "sound" # You need to write !sound 1 or !sound № to play such sound
SOUND_COMMAND2 = "звук"
LIST_COMMAND = "list" # Commant to display list of all sounds !list
LIST_COMMAND2 = "список"
MUSIC_COMMAND = "music" # Commant to display music message !music
MUSIC_COMMAND2 = "музыка"
MUSIC_ANSWER = "Play your music on stream free by this link :" # Message that displays after !music command


SOUND_LIST={1:"Sound Name.wav", # Number of sound(!sound {number}) : Name of sound file in sound location
            2:"Another Sound Name.mp3",
            3:"One More Sound Name.mp3",
            4:"It Can Be Ethernal Sound Name",
            }