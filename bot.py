from twitchio.ext import commands
import vlc
                  

# with open('tokens.txt', "r", encoding="utf-8") as f:
#     for line in f:
#         exec(line)

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


class Player():

    def __init__(self, soundLocation):

        self.soundLocation = soundLocation

    def play_sound(self, sound):
        sound = self.soundLocation+"/"+sound#+".wav"
        vlc.MediaPlayer(sound).play()


class Bot(commands.Bot):

    def __init__(self):
        super().__init__(irc_token=IRC_TOKEN, 
                         prefix='!',
                         client_id= CLIENT_ID,
                         nick = BOT_NICK,
                         initial_channels=INITIAL_CHANELS
                         )
        self.player = Player(SOUND_LOCATION)
        self.soundList = SOUND_LIST
        self.MUSIC_ANSWER = MUSIC_ANSWER
        self.SOUND_COMMAND = SOUND_COMMAND
        self.SOUND_COMMAND2 = SOUND_COMMAND2


    async def event_ready(self):
        print(f'Ready | {self.nick}')


    @commands.command(name=MUSIC_COMMAND)
    async def music(self, ctx):
        await ctx.send(self.MUSIC_ANSWER)


    @commands.command(name=LIST_COMMAND)
    async def my_command(self, ctx):
        await ctx.send('List is :')
        for key in self.soundList:   
            await ctx.send(f'{key} -> {self.soundList[key][:-4]}')


    @commands.command(name=SOUND_COMMAND)
    async def play(self, ctx):
        num = int(ctx.message.content[len(self.SOUND_COMMAND)+2:])
        sound = self.soundList[num]
        print(f"Playing {sound}")
        self.player.play_sound(sound)


    @commands.command(name=MUSIC_COMMAND2)
    async def music2(self, ctx):
        await ctx.send(self.MUSIC_ANSWER)


    @commands.command(name=LIST_COMMAND2)
    async def my_command2(self, ctx):
        await ctx.send('List is :')
        for key in self.soundList:   
            await ctx.send(f'{key} -> {self.soundList[key][:-4]}')


    @commands.command(name=SOUND_COMMAND2)
    async def play2(self, ctx):
        num = int(ctx.message.content[len(self.SOUND_COMMAND2)+2:])
        sound = self.soundList[num]
        print(f"Playing {sound}")
        self.player.play_sound(sound)

bot = Bot()
bot.run()
