#!/usr/bin/python3

import requests
import threading 
import argparse 
from sys import argv as argu  

HEADERS = {'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Language' : 'en-US,en;q=0.5',
           'Accept-Encoding' : 'gzip, deflate',
           'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)  Chrome/93.0.4577.63 Safari/537.36"
          }
NAME = None
OUTPUT = None

G = '\033[92m'  
Y = '\033[93m'  
B = '\033[94m'  
R = '\033[91m' 
W = '\033[0m'

COUNTER = 0

WEBSITES ={
1:'https://www.21buttons.com/buttoner/{name}',
2:'http://forum.3dnews.ru/member.php?username={name}',
3:'https://about.me/{name}',
4:'https://akniga.org/profile/{name}',
5:'https://allmylinks.com/{name}',
6:'https://www.alltrails.com/members/{name}',
7:'https://ameblo.jp/{name}',
8:'https://www.anime-planet.com/users/{name}',
9:'https://armorgames.com/user/{name}',
10:'https://asciinema.org/~{name}',
11:'https://audiojungle.net/user/{name}',
12:'https://pixabay.com/en/users/{name}/',
13:'https://bandcamp.com/{name}',
14:'https://www.behance.net/{name}',
15:'https://bentbox.co/{name}',
16:'https://www.biggerpockets.com/users/{name}',
17:'https://bitbucket.org/{name}/',
18:'https://www.bitchute.com/channel/{name}/',
19:'https://blip.fm/{name}',
20:'http://{name}.blogspot.com',
21:'http://api.bodybuilding.com/api-proxy/bbc/get?slug={name}',
22:'https://www.bookcrossing.com/mybookshelf/{name}',
23:'https://{name}.booth.pm/',
24:'https://www.buymeacoffee.com/{name}',
25:'https://www.buzzfeed.com/{name}',
26:'https://{name}.carbonmade.com/',
27:'https://career.habr.com/{name}',
28:'https://www.championat.com/user/{name}/',
29:'https://profile.cheezburger.com/{name}',
30:'https://www.chess.com/member/{name}',
31:'https://community.cloudflare.com/u/{name}',
32:'https://www.cnet.com/profiles/{name}/',
33:'https://www.codementor.io/@{name}',
34:'https://coderwall.com/{name}/',
35:'https://www.cracked.com/members/{name}',
36:'https://{name}.crevado.com/',
37:'https://www.dailymotion.com/{name}',
38:'https://dating.ru/{name}/',
39:'https://www.designspiration.com/{name}/',
40:'https://www.destructoid.com/?name={name}',
41:'https://dev.to/{name}',
42:'https://www.deviantart.com/{name}',
43:'https://devrant.com/users/{name}',
44:'https://www.diigo.com/interact_api/load_profile_info?name={name}',
45:'https://discuss.elastic.co/u/{name}',
46:'https://disqus.com/by/{name}/',
47:'https://hub.docker.com/v2/users/{name}/',
48:'https://dojoverse.com/members/{name}/',
49:'https://dribbble.com/{name}',
50:'https://www.duolingo.com/2017-06-30/users?username={name}&_=1628308619574',
51:'https://www.ebay.com/usr/{name}',
52:'https://echo.msk.ru/users/{name}/',
53:'https://ello.co/{name}',
54:'https://www.engadget.com/about/editors/{name}/',
55:'https://www.etsy.com/people/{name}',
56:'https://www.eyeem.com/u/{name}',
57:'https://f3.cool/{name}',
58:'https://www.fabswingers.com/profile/{name}',
59:'https://facenama.com/{name}',
60:'https://fancy.com/{name}',
61:'https://www.fanpop.com/fans/{name}',
62:'https://www.fatsecret.com/member/{name}',
63:'https://www.fiverr.com/{name}',
64:'https://www.flickr.com/photos/{name}/',
65:'https://flipboard.com/@{name}',
66:'https://www.fodors.com/community/profile/{name}/forum-activity',
67:'https://www.freelancer.com/u/{name}',
68:'https://freesound.org/people/{name}/',
69:'https://www.furaffinity.net/user/{name}',
70:'https://www.furiffic.com/{name}',
71:'https://gab.com/api/v1/account_by_username/{name}',
72:'https://www.gamespot.com/profile/{name}/',
73:'https://connect.garmin.com/modern/profile/{name}',
74:'https://www.geocaching.com/p/?u={name}',
75:'https://gitee.com/{name}',
76:'https://github.com/{name}',
77:'https://gitlab.com/{name}',
78:'http://en.gravatar.com/profiles/{name}.json',
79:'https://{name}.gumroad.com/',
80:'https://hackaday.io/{name}',
81:'https://news.ycombinator.com/user?id={name}',
82:'https://hackernoon.com/u/{name}',
83:'https://hackerone.com/{name}',
84:'https://hubski.com/user/{name}',
85:'https://ifttt.com/p/{name}',
86:'http://forum.igromania.ru/member.php?username={name}',
87:'https://support.ilovegrowingmarijuana.com/u/{name}',
88:'https://imageshack.com/user/{name}',
89:'https://api.imgur.com/account/v1/accounts/{name}?client_id=546c25a59c58ad7&include=trophies%2Cmedallions',
90:'https://{name}.insanejournal.com/profile',
91:'https://www.picuki.com/profile/{name}',
92:'https://www.instructables.com/member/{name}/',
93:'https://archive.org/search.php?query={name}',
94:'https://archive.org/details/@{name}',
95:'https://www.interpals.net/{name}',
96:'https://issuu.com/{name}',
97:'https://jsfiddle.net/user/{name}/',
98:'https://justfor.fans/{name}',
99:'https://keybase.io/{name}',
100:'https://www.kickstarter.com/profile/{name}',
101:'https://www.last.fm/user/{name}',
102:'https://www.librarything.com/profile/{name}',
103:'https://linktr.ee/{name}',
104:'https://www.linux.org.ru/people/{name}/profile',
105:'https://{name}.livejournal.com',
106:'https://lobste.rs/u/{name}',
107:'https://lovehomeporn.com/user/{name}',
108:'https://www.magix.info/us/users/profile/{name}/',
109:'https://www.mapmytracks.com/{name}',
110:'https://marshmallow-qa.com/{name}',
111:'https://mastodon.social/@{name}',
112:'https://www.meetme.com/{name}',
113:'https://social.technet.microsoft.com/profile/{name}/',
114:'https://mix.com/{name}/',
115:'http://api.mixlr.com/users/{name}',
116:'https://www.moddb.com/members/{name}',
117:'https://forums.moneysavingexpert.com/profile/{name}',
118:'https://muckrack.com/{name}',
119:'https://www.mumblit.com/{name}?ref=se',
120:'https://myanimelist.net/profile/{name}',
121:'https://www.myfitnesspal.com/user/{name}/status',
122:'https://blog.naver.com/{name}',
123:'https://{name}.newgrounds.com/',
124:'https://notabug.org/{name}',
125:'https://www.openstreetmap.org/user/{name}',
126:'https://orbys.net/{name}',
127:'https://pastebin.com/u/{name}',
128:'https://www.photoblog.com/{name}/',
129:'https://www.pinkbike.com/u/{name}/',
130:'https://playlists.net/members/{name}',
131:'https://www.plurk.com/{name}',
132:'https://pokemonshowdown.com/users/{name}',
133:'http://www.pokerstrategy.net/user/{name}/profile/',
134:'https://pollev.com/proxy/api/users/{name}',
135:'https://www.pornhub.com/users/{name}',
136:'https://poshmark.com/closet/{name}',
137:'https://www.producthunt.com/@{name}',
138:'https://promodj.com/{name}',
139:'https://www.redbubble.com/people/{name}/shop?ref=artist_title_name%2F',
140:'https://www.reddit.com/user/{name}',
141:'https://replit.com/@{name}',
142:'https://ruby.dating/en/users/{name}',
143:'https://rumble.com/user/{name}',
144:'https://scratch.mit.edu/users/{name}/',
145:'https://seneporno.com/user/{name}',
146:'https://www.seoclerks.com/user/{name}',
147:'https://{name}.myshopify.com',
148:'https://www.shutterstock.com/g/{name}',
149:'https://www.skypli.com/profile/{name}',
150:'https://{name}.skyrock.com/',
151:'https://slides.com/{name}',
152:'https://www.slideshare.net/{name}',
153:'https://smashrun.com/{name}/',
154:'https://{name}.smugmug.com',
155:'https://www.smule.com/{name}/',
156:'https://feelinsonice.appspot.com/web/deeplink/snapcode?username={name}&size=400&type=SVG',
157:'https://soundcloud.com/{name}',
158:'https://sourceforge.net/u/{name}/profile',
159:'https://speakerdeck.com/{name}/',
160:'https://steemit.com/@{name}',
161:'https://archive.storycorps.org/user/{name}/',
162:'https://suzuri.jp/{name}',
163:'https://tamtam.chat/{name}',
164:'https://www.taskrabbit.com/profile/{name}/about',
165:'https://user.teknik.io/{name}',
166:'https://t.me/{name}',
167:'http://www.tf2items.com/id/{name}/',
168:'https://themeforest.net/user/{name}',
169:'https://www.thetattooforum.com/members/{name}/',
170:'https://www.tiktok.com/@{name}?lang=en',
171:'https://tinder.com/@{name}',
172:'https://en.tm-ladder.com/{name}_rech.php',
173:'https://trakt.tv/users/{name}',
174:'https://passport.twitch.tv/usernames/{name}',
175:'https://shadowban.eu/.api/{name}',
176:'https://unsplash.com/@{name}',
177:'https://untappd.com/user/{name}/',
178:'http://www.ustream.tv/channel/{name}',
179:'https://vero.co/{name}',
180:'https://vimeo.com/{name}',
181:'https://www.vivino.com/users/{name}',
182:'https://vk.com/{name}',
183:'https://vsco.co/{name}/gallery',
184:'https://wanelo.co/{name}',
185:'https://weheartit.com/{name}',
186:'https://wimkin.com/{name}',
187:'https://www.wireclub.com/users/{name}',
188:'https://profiles.wordpress.org/{name}/',
189:'https://wordpress.org/support/users/{name}/',
190:'https://www.wowhead.com/user={name}',
191:'https://www.xboxgamertag.com/search/{name}',
192:'https://xhamster.com/users/{name}',
193:'https://www.zomato.com/{name}/foodjourney',
194:'https://instagram.com/{name}/',
195:'https://www.facebook.com/{name}',
196:'https://www.twitter.com/{name}',
197:'https://tryhackme.com/p/{name}',
198:'https://forum.hackthebox.eu/profile/{name}',
199:'https://youtube.com/{name}',
200:'https://myspace.com/{name}',
201:'https://open.spotify.com/user/{name}',
202:'https://trello.com/{name}',
203:'https://pornhub.com/users/{name}',
204:'https://www.xvideos.com/profiles/{name}',
205:'https://steamcommunity.com/id/{name}',
206:'https://www.npmjs.com/~{name}',
207:'https://www.cups.com/@{name}',
208:'https://independent.academia.edu/{name}',
209:'https://discussions.apple.com/profile/{name}',
210:'https://ask.fm/{name}',
211:'https://www.bandcamp.com/{name}',
212:'https://bitbucket.org/{name}',
213:'https://bodyspace.bodybuilding.com/{name}',
214:'https://www.cnet.com/profiles/{name}',
215:'https://www.cloob.com/name/{name}',
216:'https://www.codecademy.com/profiles/{name}',
217:'https://www.codechef.com/users/{name}',
218:'https://www.colourlovers.com/lover/{name}',
219:'https://www.cloob.com/name/{name}',
220:'https://www.colourlovers.com/lover/{name}',
221:'https://www.designspiration.net/{name}',
222:'https://www.discogs.com/user/{name}',
223:'https://disqus.com/{name}',
224:'https://hub.docker.com/u/{name}',
225:'https://www.duolingo.com/profile/{name}',
226:'https://euw.op.gg/summoner/userName={name}',
227:'https://f.cool/{name}',
228:'https://www.flickr.com/people/{name}',
229:'https://my.flightradar.com/{name}',
230:'https://flipboard.com/@{name}',
231:'https://fortnitetracker.com/profile/all/{name}',
232:'https://freesound.org/people/{name}',
233:'https://giphy.com/{name}',
234:'https://gitee.com/{name}',
235:'https://www.goodreads.com/{name}',
236:'http://en.gravatar.com/{name}',
237:'https://gurushots.com/{name}',
238:'https://hackaday.io/{name}',
239:'https://news.ycombinator.com/user?id={name}',
240:'https://hackerrank.com/{name}',
241:'https://www.house-mixes.com/profile/{name}',
242:'https://houzz.com/user/{name}',
243:'https://imgur.com/user/{name}',
244:'https://www.instructables.com/member/{name}',
245:'https://itch.io/profile/{name}',
246:'https://www.kongregate.com/accounts/{name}',
247:'https://launchpad.net/~{name}',
248:'https://leetcode.com/{name}',
249:'https://letterboxd.com/{name}',
250:'https://lichess.org/@/{name}',
251:'https://lolchess.gg/profile/na/{name}',
252:'https://www.memrise.com/user/{name}',
253:'https://www.mixcloud.com/{name}',
254:'https://opensource.com/users/{name}',
255:'https://otzovik.com/profile/{name}',
256:'https://forums.pcgamer.com/members/?username={name}',
257:'https://psnprofiles.com/{name}',
258:'https://www.patreon.com/{name}',
259:'https://www.periscope.tv/{name}',
260:'https://www.pinterest.com/{name}',
261:'https://www.producthunt.com/@{name}',
262:'http://promodj.com/{name}',
263:'https://pypi.org/user/{name}',
264:'https://quizlet.com/{name}',
265:'https://www.quora.com/profile/{name}',
266:'https://raidforums.com/User-{name}',
267:'https://rateyourmusic.com/~{name}',
268:'https://www.redbubble.com/people/{name}',
269:'https://repl.it/@{name}',
270:'https://www.reverbnation.com/{name}',
271:'https://www.roblox.com/user.aspx?username={name}',
272:'https://scratch.mit.edu/users/{name}',
273:'https://www.scribd.com/{name}',
274:'https://pikabu.ru/@{name}',
275:'https://osu.ppy.sh/users/{name}',
276:'https://www.npmjs.com/~{name}',
277:'https://note.com/{name}',
278:'https://www.nn.ru/{name}',
279:'https://www.nairaland.com/{name}',
280:'https://moikrug.ru/{name}',
281:'https://www.mercadolivre.com.br/perfil/{name}',
282:'https://mastodon.social/@{name}',
283:'https://forum.leasehackr.com/u/{name}',
284:'https://last.fm/user/{name}',
285:'https://kwork.ru/user/{name}',
286:'http://www.jeuxvideo.com/profil/{name}',
287:'https://www.hackster.io/{name}',
288:'https://www.geocaching.com/p/default.aspx?u={name}',
289:'https://www.fl.ru/users/{name}',
290:'https://www.fixya.com/users/{name}',
291:'https://www.drive.ru/users/{name}',
292:'https://www.babyblog.ru/user/info/{name}',
293:'http://www.authorstream.com/{name}',
294:'https://aminoapps.com/u/{name}',
295:'https://www.zhihu.com/people/{name}',
296:'https://youpic.com/photographer/{name}',
297:'https://www.younow.com/{name}',
298:'https://xboxgamertag.com/search/{name}',
299:'https://profiles.wordpress.org/{name}',
300:'https://community.windy.com/user/{name}',
301:'http://www.wikidot.com/user:info/{name}',
302:'https://ultimate-guitar.com/u/{name}',
303:'https://data.typeracer.com/pit/profile?user={name}',
304:'https://www.trakt.tv/users/{name}',
305:'https://www.tradingview.com/u/{name}',
306:'https://ch.tetr.io/u/{name}',
307:'https://steamcommunity.com/groups/{name}',
308:'https://scratch.mit.edu/users/{name}',
309:'https://www.scribd.com/{name}',
310:'https://slashdot.org/~{name}',
311:'https://www.sparkpeople.com/mypage.asp?id={name}',
312:'https://www.pexels.com/@{name}',
313:'https://www.9gag.com/u/{name}',
314:'https://asciinema.org/~{name}',
315:'https://ask.fedoraproject.org/u/{name}',
316:'https://ask.fm/{name}',
317:'https://discuss.atom.io/u/{name}/summary',
318:'https://audiojungle.net/user/{name}',
319:'https://www.avizo.cz/{name}/',
320:'https://www.bandcamp.com/{name}',
321:'https://www.bazar.cz/{name}/',
322:'https://www.behance.net/{name}',
323:'https://binarysearch.io/@/{name}',
324:'https://{name}.crevado.com',
325:'https://{name}.wordpress.com/',
326:'https://{name}.wix.com'
}

def val(x):
    if(OUTPUT != None):
        with open(OUTPUT,'a',encoding='utf-8') as f:
            f.write(f"{x} \n")



def parse_arg():
    parser = argparse.ArgumentParser(epilog='\tExample: \r\npython3 ' + argu[0] + " ")
    parser._optionals.title = "OPTIONS"
    parser.add_argument("-u",'--username' ,help="Username to search in web",required=True)
    parser.add_argument("-o",'--output' ,help="Name  of the output file ",default=None)
    parser.add_argument("-t",'--threads',help="to set thread value [default and recomended= 50] ",default=50)
    return parser.parse_args()


def do_it():
    while True:
        global COUNTER
        if COUNTER <=312:
            COUNTER = COUNTER+1
        else:
            break

        location = WEBSITES[COUNTER].format(name=NAME)
        try:
            response = requests.get(location, headers=HEADERS,timeout=150)
            if(response.status_code == 200 or response.status_code == 302):
                if (response.status_code == 200):
                    print(G+"[*] : "+location+W)
                elif (response.status_code == 302):
                    print(G+"[-] : "+location+W)
                val(location)
        
        except requests.exceptions.Timeout :
            pass
        except requests.exceptions.TooManyRedirects :
            pass
        except Exception :
             pass


def main():
    print('''
 ▄▄▄·  ▄▄ • ▄▄▄ . ▐ ▄ ▄▄▄▄▄        ▄ •▄ 
▐█ ▀█ ▐█ ▀ ▪▀▄.▀·•█▌▐█•██          █▌▄▌▪
▄█▀▀█ ▄█ ▀█▄▐▀▀▪▄▐█▐▐▌ ▐█.▪        ▐▀▀▄·
▐█ ▪▐▌▐█▄▪▐█▐█▄▄▌██▐█▌ ▐█▌·        ▐█.█▌
 ▀  ▀ ·▀▀▀▀  ▀▀▀ ▀▀ █▪ ▀▀▀         ·▀  ▀ 

-----Result may not be accurate always------
    ''')
    global NAME,OUTPUT
    arg=parse_arg()
    NAME = arg.username
    OUTPUT = arg.output
    tvalue =int(arg.threads)

    thread = []
    for i in range(tvalue):
        t = threading.Thread(target=do_it)
        t.daemon = True
        thread.append(t)

    for i in range(tvalue):
        thread[i].start()

    for i in range(tvalue):
        thread[i].join()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("[^]Keybord pressed Exiting")
        exit(0)
