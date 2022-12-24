#╔═══════════════════════════════════════════════════════════════════════════════════════════════════════╗
#║  ___  ____  ____    __   ____  ____  ____     ____  _  _     ___  ____    __    ____  ___  ____  ____ ║
#║ / __)(  _ \( ___)  /__\ (_  _)( ___)(  _ \   (  _ \( \/ )   / __)(  _ \  /__\  ( ___)/ __)( ___)(_  _)║
#║( (__  )   / )__)  /(__)\  )(   )__)  )(_) )   ) _ < \  /   ( (__  )   / /(__)\  )__) \__ \ )__)   )(  ║
#║ \___)(_)\_)(____)(__)(__)(__) (____)(____/   (____/ (__)    \___)(_)\_)(__)(__)(__)  (___/(____) (__) ║
#╚═══════════════════════════════════════════════════════════════════════════════════════════════════════╝


#╔══════════════════════════════════════╗
#║                IMPORT                ║
#╚══════════════════════════════════════╝


import json
import os

# TELEGRAM
try:
    import telegram
except:
    os.system("pip install python-telegram-bot")

# FADE
try:
    import fade
except:
    os.system("pip install fade")

# PYSTYLE
try:
    from pystyle import Colors, Colorate
except:
    os.system("pip install pystyle")

# REQUEST, PRAW
try:
    import time, requests, praw, random 
except:
    os.system("pip install requests")
    os.system("pip install praw")

# ALIVE_PROCESS
try:
    from alive_progress import alive_bar
except:
    os.system("pip install alive_progress")

os.system("cls")

with open("config.json", 'r') as confg:
    config = json.load(confg)


class Spy:
    gris = "\033[1;30;1m"
    rouge = "\033[1;31;1m"
    vert = "\033[1;32;1m"
    jaune = "\033[1;33;1m"
    bleu = "\033[1;34;1m"
    violet = "\033[1;35;1m"
    yellow = "\033[1;36;1m"
    blanc = "\033[2;0;1m"

reddit = praw.Reddit(client_id=config["clientid"],
                     client_secret=config["clientsecret"],
                     user_agent="<console:HAPPY:1.0>",
                     username=config["pseudo"],
                     password=config["motdepasse"])

class RedditBot:
    def __init__(self, subcatego="NFTsMarketPlace", nbr_message=1000):
        self.__cooldown = 10
        self.__subcatego = subcatego
        self.__nbr_message = 240

        os.system("cls")
#╔══════════════════════════════════════╗
#║                START                 ║
#╚══════════════════════════════════════╝  
          
        category = {}
        os.system("cls")
#╔══════════════════════════════════════╗
#║             MESSAGE START            ║
#╚══════════════════════════════════════╝        
        bot = telegram.Bot(token='5974861797:AAG76oDYSVLhFEn3FUOSb6xS0uySJAdpXhw')

        bot.send_message(chat_id='-1001875291848', text=f'🟢 | Programme Lancé !')
        print(Colorate.Horizontal(Colors.red_to_yellow, """
      )\  )\  )`-.--. .-,.-.,-.         )\.-.     /`-.     .-./(     /`-.  
     (  \, /  ) ,-._( ) ,, ,. (       ,'     )  ,' _  \  ,'     )  ,' _  \ 
      ) \ (   \ `-._  \( |(  )/      (  .-, (  (  '-' ( (  .-, (  (  '-' ( 
     ( ( \ \   ) ,_(     ) \          ) '._\ )  ) ,_ .'  ) '._\ )  ) ,._.' 
      `.)/  ) (  \       \ (         (  ,   (  (  ' ) \ (  ,   (  (  '     
         '.(   ).'        )/          )/ ._.'   )/   )/  )/ ._.'   )/      
                                                                    """, ))

        print(Colorate.Horizontal(Colors.red_to_yellow, "                              (　-_･) ︻デ═一 ▸", )) 
                   
        self.__category = reddit.subreddit(subcatego).new(limit=nbr_message)

    def run(self):
        with open("config.json", 'r') as confg:
            config = json.load(confg)

        try:
            for submission in reddit.subreddit("all").hot(limit=1):
                submission.upvote()
        except:
            input(Colorate.Horizontal(Colors.red_to_yellow, "> Account information is invalid ! ",))
            return
        error = False
        start = True
        message = 0
#╔══════════════════════════════════════╗
#║                TEXTE                 ║
#╚══════════════════════════════════════╝        
        while start or (message != self.__nbr_message):
            with alive_bar(self.__nbr_message, title=f"{Spy.rouge}> Reddit Bot", bar='classic',spinner='waves') as bar:

                for submission in self.__category:
                    if message == self.__nbr_message:
                        start = False
                        break

                    success = {}

                    with open('post_list.txt', 'r') as populist:
                        allpost = populist.readline()

                    if submission in allpost.split():
                        message += 1
                        bar()
                        time.sleep(5)

                    else:
                        try:
                            submission.upvote()
                            submission.reply(
                                f"My Metamask Key > {config['metakey']} !"
                                f" {random.choice(config['phrase'])}")

                            with open("post_list.txt", 'a+') as fishier:
                                fishier.write(f"{submission}\n")
                            message += 1
                            bar()
                            time.sleep(random.randint(20,40))
                        except Exception as err:
                            with bar.pause():
                                    error = {}
#╔══════════════════════════════════════╗
#║                ERREUR                ║
#╚══════════════════════════════════════╝
                                    bot = telegram.Bot(token='5974861797:AAG76oDYSVLhFEn3FUOSb6xS0uySJAdpXhw')

                                    bot.send_message(chat_id='-1001875291848', text=f'''🔴 | Erreur!''')

                                    requests.post(config['webhook'], json=error)
                                    error = True

                                    os.system("cls")
                                    print(Spy.violet)
                                    cooldown = self.__cooldown
                                    self.__cooldown *= 10
                                    with alive_bar(cooldown, title="Cooldown - RateLimit", bar='classic',
                                                   spinner="waves", stats=True, elapsed=False,
                                                   monitor=False) as bar2:
                                        while cooldown > 0:
                                            time.sleep(1)
                                            cooldown -= 1
                                            bar2()


                                    os.system("cls")

                                    print(self.__confignumber)
                                    self.run()
            if not error:
                requests.post(config['webhook'], json=success)
#╔══════════════════════════════════════╗
#║                TERMINÉ               ║
#╚══════════════════════════════════════╝                
                bot = telegram.Bot(token='5974861797:AAG76oDYSVLhFEn3FUOSb6xS0uySJAdpXhw')

                bot.send_message(chat_id='-1001875291848', text=f'''❎ | Programme Terminé !''')
            else:
                print("Fini !")


try:
    os.system("cls")
except:
    os.system("clear")         
RedditBot().run()
