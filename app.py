import pandas as pd
import streamlit as st
rowdy_total = 0
polite_total = 0
social_total = 0
watching_total = 0
playing_total = 0
pot_total = 0
alc_total = 0
lust_total = 0
crafting_total = 0
reading_total = 0
emo_total = 0
intellect_total = 0
body_total = 0
bake_total = 0
loser_total = 0

st.set_page_config(page_title='WWLID?')
st.title('What Should I do Tonight?')
st.header('Deciscions are hard, I got u bro')
st.subheader('Yes, this is essentially a big kid tigerbeat')


name_st = st.text_input("what's ur name?")
age_st = st.selectbox('how old are you?', ['15-17', '18-24', '25+'])
if age_st == '15-17' :
    polite_total += 10
    school_choice = st.radio('have u done ur homework?', ['yeah', 'no'])
    if school_choice == 'no' :
        rod = st.subheader('do your fucking homework, punk')
if age_st != '15-17' :
    parent_check = st.radio('are you responsible for another lifeform over 15?', ['yeah', 'no'])
    if parent_check == 'yeah' :
        polite_total += 10
        kiddo = st.radio('they good on their own?', ['yeah', 'no'])
        if kiddo == 'no' :
            kidzbop = st.subheader('get them to take the quiz')
    if parent_check == 'no':
        rowdy_total += 10
house = st.selectbox('Whats ur current living situation?', ['living with family', 'I live with roommates <3', 'I live with roommates </3', 'I live alone'])
if house == 'living with family' :
    polite_total += 10
    rowdy_total -= 10
    social_total += 3
if house == 'I live with roommates <3' :
    rowdy_total += 5
    social_total += 10
if house == 'I live with roommates </3' :
    rowdy_total += 5
    social_total += 3
if house == 'I live alone' :
    rowdy_total += 10

depression = st.selectbox('are you in a depressive episode?', ['yes', 'no'])
if depression == 'no' :
    body_total += 5
    emo_total += 5
    lust_total += 5
if depression == 'yes' :
    body_total -= 5
    emo_total -= 10

emo = st.select_slider(
    'How tired are you emotionally', ['I am a husk', 'decently so', 'a bit', 'not at all'])
if emo == 'I am a husk' :
    emo_total -= 10
if emo == 'decently so' :
    emo_total -= 5
if emo == 'a bit' :
    emo_total += 5
if emo == 'not at all' :
    emo_total += 10

brain = st.select_slider('how intellectually tired are you', ['smooth brain', 'worn down', 'Not too bad' ,'i could debate a redditor'])
if brain == 'smooth brain' :
    intellect_total -= 10
if brain == 'worn down' :
    intellect_total -= 5
if brain == 'not too bad' :
    intellect_total += 5
if brain == 'i could debate a redditor' :
    intellect_total += 10
body = st.select_slider('how tired are you physically',[ 'coma ready', 'want nap', 'been sittin all day', 'trackstar'])
if body == 'coma ready' :
    body_total -= 10
if body == 'want nap' :
    body_total -= 5
if body == 'been sittin all day' :
    body_total += 5
if body == 'trackstar' :
    body_total += 10

drink = st.radio('Do you drink?', ['yeah', 'socially', 'no'])
if drink == 'yeah':
    rowdy_total += 7
    alc_total += 10
if drink == 'socially' :
    rowdy_total += 5
    alc_total += 5
    social_total += 5
if drink == 'no' :
    rowdy_total -= 7
    alc_total == 0
smoke = st.radio('You smoke kush?', ['yes, but please. do not call it that.', 'no', 'socially', 'wake and bake'])
if smoke == 'no' :
    rowdy_total -= 5
    pot_total == 0
if smoke == 'socially' :
    rowdy_total += 5
    pot_total += 5
    social_total += 3
if smoke == 'yes, but please. do not call it that.' :
    rowdy_total += 7
    pot_total += 7
if smoke == 'wake and bake' :
    rowdy_total += 10
    pot_total += 10

sin = st.radio('Do you sin? carnally?', ['i am no freak', 'on all fours, as often as I can'])
if sin == 'i am no freak':
    rowdy_total -= 5
    lust_total -= 15
    polite_total += 10
if sin == 'on all fours as often as I can' :
    rowdy_total += 10
    lust_total += 10

craft = st.radio('Did u pick up a pandemic craft hobby?', ['no', 'I already knew how', 'yeah :D'])
if craft == 'no' :
    crafting_total == 0
if craft == 'I already knew how' :
    crafting_total += 10
    intellect_total += 5
if craft == 'yeah :D' :
    crafting_total += 10
    intellect_total += 5

bake = st.radio('Which of the following best describes your inclination towards baking', ['not really my thing', 'in theory i like it, reality not so much', 'fun from time to time', 'it soothes me'])
if bake == 'not really my thing' :
    bake_total -= 10
if bake == 'in theory i like it, reality not so much' :
    bake_total -= 5
if bake == 'from time to time' :
    bake_total += 5
if bake == 'it soothes me' :
    bake_total += 10

books = st.number_input('how many books have you read in the last year?', 0, None)
if books >= 3 :
    reading_total += 5
    intellect_total += 5
if books >= 7 :
    reading_total += 10
    intellect_total += 10

fic = st.radio('how much fanfic have you read in the last year?', ['none wtf', 'a few just for the memories or beacuse a friend sent them', 'at least once a month', 'too much to comfortably count'])
if fic == 'none wtf' :
    loser_total -= 10
    lust_total -= 5
    reading_total -= 1
if fic == 'a few just for the memories or beacuase a friend sent them' :
    loser_total += 3
    reading_total += 5
    social_total += 5
if fic == 'at least once a month' :
    loser_total += 5
    lust_total += 5
    reading_total += 5
    emo_total += 5
if fic == 'too much to comfortably count' :
    loser_total += 10
    lust_total += 10
    emo_total += 5
    reading_total += 10

weeb = st.radio('do you use discord?', ['yeah', 'no'])
if weeb == 'yeah' :
    social_total += 5
    loser_total += 3
    online = st.radio('do you have online friends?', ['some of my best friends are online friends', 'yeah a few', 'no'])
    if online == 'some of my best friends are online friends' :
        loser_total += 5
        social_total += 5
    if online == 'yeah a few' :
        loser_total += 3
        social_total += 3
gamer = st.selectbox('Thoughts on games?', ['yeah, im a gamer(but in a lame self-aware way)', 'I like board games, but thats kinda it', 'I have a switch/steam account/ console and a few games I like', 'I like some online games to pass the time but i dont have a console or anything', 'games are a waste of time'])
if gamer == 'yeah, im a gamer(but in a lame self-aware way)' :
    loser_total += 5
    playing_total += 10
if gamer == 'I like board games, but thats kinda it' :
    social_total += 5
    playing_total -= 5
if gamer == 'games are a waste of time' :
    playing_total -= 10
if gamer == 'I have a switch/steam account/ console and a few games I like' :
    playing_total += 10
if gamer == 'I like some online games to pass the time but i dont have a console or anything' :
    playing_total += 5

watch_one = st.radio('pick one', ['youtube', 'movies', 'TV', 'nah'])
if watch_one == 'movies' :
    watching_total += 5
if watch_one == 'TV' :
    watching_total += 10
fucking = st.selectbox('what are you putting on in the background during a hookup?', ['some netflix, let them pick', 'a playlist of my own creation', 'a show i have already seen', 'cowards put something on, we fuck in silence', 'I do not be fucking'])
if fucking == 'some netflix, let them pick' :
    rowdy_total += 5
    lust_total += 3
    watching_total += 5
if fucking == 'a playlist of my own creation' :
    rowdy_total += 5
    loser_total += 1
    lust_total += 5
if fucking == 'a show i have already seen' :
    rowdy_total += 5
    watching_total += 3
    social_total -= 1
    lust_total += 3
if fucking == 'cowards put something on, we fuck in silence' :
    rowdy_total += 5
    social_total -= 5
    lust_total += 5
if fucking == 'I do not be fucking' :
    loser_total += 3

plans = st.selectbox('What do you have going on tomorrow', ['I have work/school', 'I have another all day commitment', 'I have something to do in the afternoon', 'I am free all day'])
if plans == 'I have work/school' :
    rowdy_total -= 10
    alc_total -= 10
    pot_total -= 1
if plans == 'I have another all day commitment' :
    rowdy_total -= 10
    alc_total -= 10
if plans == 'I have something to do in the afternoon' :
    rowdy_total += 5
if plans == 'I am free all day' :
    rowdy_total += 8

if age_st == '15-17' :
    rowdy_total = 0
    lust_total = 0
    alc_total = 0

nunya = st.radio('do you work for my school/ are my parent or family member?' , ['yeah', 'no'])
if nunya == 'yeah' :
    lust_total = 0
    rowdy_total = 0

high_craft = pot_total + crafting_total + intellect_total
st.write(high_craft)
high_tetris = pot_total + playing_total + intellect_total
st.write(high_tetris)
high_friend_game = pot_total + playing_total + social_total
st.write(high_friend_game)
high_bake = pot_total + body_total + bake_total
st.write(high_bake)
high_watch_memories = pot_total + emo_total + watching_total
st.write(high_watch_memories)
high_watch_doc = pot_total + intellect_total + watching_total
st.write(high_watch_doc)
drink_friends = alc_total + social_total + body_total
st.write(drink_friends)
new_kink = lust_total + body_total + rowdy_total
st.write(new_kink)
read_new_book = reading_total + intellect_total + emo_total
st.write(read_new_book)
read_old_fic = reading_total + loser_total + emo_total
st.write(read_old_fic)
read_smut_newkink = reading_total + lust_total + loser_total
st.write(read_smut_newkink)
doc_tetris_videoessay = watching_total + intellect_total + polite_total
st.write(doc_tetris_videoessay)
watch_memories = watching_total + emo_total + loser_total
st.write(watch_memories)
play_mindgame = playing_total + intellect_total + loser_total
st.write(play_mindgame)
play_social = playing_total + social_total + loser_total
st.write(play_social)
play_sims_rpg = playing_total + emo_total + loser_total
st.write(play_sims_rpg)
bake_friends = bake_total + social_total + intellect_total
st.write(bake_friends)
craft_chill = crafting_total + intellect_total + body_total
st.write(craft_chill)


top1 = high_craft
top12 ='get high and craft'
truth = 'CRAFT TIME. Whatever it is you do, polymer clay, crochet, knit, friendship bracelets, small wood carvings, jewellery, collage, whatever take some time and get into it. Getting high can bring an emphasis on the fun sensory elements of crafting and give some exceedingly chill vibes. I like to throw on a video essay or podcast, or listen to music and sometimes even facetime a friend but do whatever add to the chill atmosphere. Tonight we craft and chill, tomorrow who knows, that’s future you’s problem.'
vibe = './craft.jpg'
if high_tetris > top1 :
    top1 = high_tetris
    top12 ='get high and play tetris'
    truth = 'What you really need is to turn your brain off. No more thinky, you’ve done enough in fact, tonight it’s time to polish your brain smooth and float away from reality. Get a little stoned, in whatever way you prefer(smoke, edible, whatever), put on a podcast, video essay, documentary, stand up comedy special, whatever long form not primarily visual content you prefer and open up tetris.com/play-tetris and turn your brain off.  I’m sure you’ll find that the audio experience plus the burst of intellectual and motor stimulation tetris provides in combination with a gentle high can bring a special kind of peace. Enjoy the journey my friend. My current high score is 355,260 if you beat it while stoned feel free to send a screenshot of your score and a recommendation with what you were listening at datemyfriendrebecca@gmail.com for bragging rights from yours truly.'
    vibe = './tetris.png'
if high_bake > top1 :
    top1 = high_bake
    top12 ='get high and bake'
    truth = 'It is time to heal <3 or something <3 . Baking can be a great way to do something that even if it doesn’t feel stressful can be fulfilling and bring a sense of accomplishment since you have made something. Getting a little stoned and making a simple recipe like banana bread, brownies, peanut butter cookies, squash bread or challah can lead to a chill night in that will even bring you some treats for tomorrow. Maybe you can bring them into work or school or for friends or family, or just keep them for yourself. If you are up for it I recommend talking to a friend on the phone or over discord(or video call) and goof off with a friend as you do for some extra serotonin. Bonus points if you blast music and dance around your kitchen as you clean up.'
    vibe = './bake.jpg'
if high_watch_memories > top1 :
    top1 = high_watch_memories
    top12 = 'get high and watch something from your youth'
    truth = 'Whats up loser it’s time to reminisce. Get a little high, a bit elevated if you will, and turn on a show or movie from an old fandom you used to be really into. Revisit something from years ago, I’m talking at least four, and see it with fresh eyes. It can give a sense of nostalgia and a maybe the tiniest bit of healing, I reccomend texting commentary to a friend or live tweeting the experience, which is the modern age fun version of annotating. But do remember to be nice to your past self, and your current one. And also soon you should probably wash your bong/pipe.'
    vibe = './reminisce.jpg'
if high_watch_doc > top1 :
    top1 = high_watch_doc
    top12 = 'get high and watch a doc'
    truth = 'You would be surprised at the peace a little bit of non stressful visual brain stimulation can bring. Watch a nature documentary for pretty colors and birds, bonus points if you get ot hear the soothing sounds of David Attenborough’s narration. If nature documentaries aren’t your thing no worries, there are lots of free documentaries on youtube(I recommend the one on Francis Bacon if your up to it) or even documentaries with recreation elements like the college admissions scandal one. If you are feeling a little more energetic documentaries like [insert ben rec here] are always a good time.'
    vibe ='./Weed_Netflix.jpg'
if high_friend_game > top1 :
    top1 = high_friend_game
    vibe = './high_gaymer.jpg'
    top12 = 'get high and play a game with your friends'
    truth = 'Get in discord and gather some of those losers because it’s time to game. And get high. Weather is be a game like Valorant or Overwatch or something more chill like JackBox, Smash Bros or dare I say even amogus and have a goofy little night with the pals. Friends not free? No problem, you can play one of those games online with strangers, or tune into a twitch streamer and play your own game to have a chill experience. Hats off to you bro.'
if drink_friends > top1 :
    top1 = drink_friends
    top12 ='drink with your friends'
    truth = 'This one requires some pals but can really be worth it, and tailored specifically to you and your friend/friends. If you have a roommate or a friend over you can do something cheesy like each try out a new cocktail and have the other person try and guess what is in it with a blind fold on, or play a drinking game with a movie. Even more fun can be coming up with your own drinking game, or modifying a board or video game to involve drinking for some added competitiveness, just make sure it’s something you both have a fair shot of winning.'
    vibe = './drunk_friends.jpg'
if new_kink > top1 :
    top1 = new_kink
    top12 = 'see if ur strong enough to not develop a new kink'
    truth = 'Listen. Sometimes in life you need to show a little courage, and take a risk. Take a kink you’ve heard people talk about but never /got/ and give it an honest shot. Whatever your poison is(written, video, pictures ect.) set aside some time and a open mind and see what the result it. I am praying for your strength tho. '
    vibe = './barbie_oops.jpg'
if read_new_book > top1 :
    top1 = read_new_book
    top12 ='read a book you have been meaning to get to'
    truth = 'I know your ‘to be read’ list is a disaster. You know it’s a disaster. Now do something about it. Get in some comfy clothes, make yourself a cup of tea or hot chocolate, get in your favorite reading spot and get after it. Is there a book you have been meaning to start? Go for it. Do you have a book you’re halfway through but lost the motivation to actually finish? Then don’t finish it now, and don’t feel guilty about it, you can go back to it later, but for now read a book you can more easily get into. You got this <3 .'
    vibe = './read_new.jpg'
if read_old_fic > top1 :
    top1 = read_old_fic
    top12 = 'read a fic from your yesteryears'
    truth = 'We were all messy once, and honestly most of us still are. Weather you are still reading fic every day or haven’t touched the stuff in years, think of a fic you used to be obsessed with, reading it all in one weekend or always waiting for update and track it down and give it a quick reread. Try and find something from at least three years ago, longer if you’ve got it and revisit it. Live text a friend from the fandom if you still have one or just laugh to yourself about and see if it lives up to all the hype you had at the time. But remember to be kind to present and past you however. '
    vibe = './BIG EYES.jfif'
if read_smut_newkink > top1 :
    top1 = read_smut_newkink
    top12 ='read some smut and see if ur strong enough to not develop a new kink'
    truth = 'Are you horny? Are you a loser? Are you feeling brave? Now is your chance to prove it, take a smut trope you have never read and really give it a shot, sort by that tag and find a fic that is well loved or seems fun and give it a fair shot. I believe in you, or don’t, whatever answer you need to be true. '
    vibe = './barbie_oops'
if doc_tetris_videoessay > top1 :
    top1 = doc_tetris_videoessay
    top12 = 'watch a doc and play tetris u bigbrain intellectual'
    truth = 'What you really need is to turn your brain off. No more thinky, you’ve done enough in fact, tonight it’s time to polish your brain smooth and float away from reality. Put on a podcast, video essay, documentary, stand up comedy special, whatever long form not primarily visual content you prefer and open up tetris.com/play-tetris and turn your brain off.  I’m sure you’ll find that the audio experience plus the burst of intellectual and motor stimulation tetris provides a special kind of peace. Enjoy the journey my friend. My current high score is 355,260 if you beat it feel free to send a screenshot of your score and a recommendation with what you were listening at datemyfriendrebecca@gmail.com for bragging rights from yours truly.'
    vibe = './tetris.png'
if watch_memories > top1 :
    top1 = watch_memories
    top12 ='watch something from your memories loser'
    truth = 'Ahhh the past, the cringy lovable past, it’s time to reminisce. Relace and turn on a show or movie from an old fandom you used to be really into. Revisit something from years ago, I’m talking at least four, and see it with fresh eyes. It can give a sense of nostalgia and a maybe the tiniest bit of healing, I recommend texting commentary to a friend or live tweeting the experience, which is the modern age fun version of annotating. But do remember to be nice to your past self, and your current one.'
    vibe = './reminisce.jpg'
if play_mindgame > top1 :
    top1 = play_mindgame
    top12 = 'play a little mindgame loser'
    truth = 'Oh look at you, so based and red pilled and not like other gaymers, it’s time to flex that muscle. Play a game that actually requires some thinking, an escape room game, a puzzle game, or a game like geo guessr that flexes one particular brain muscle. Show off all that knowledge and prowess and play a game that just shows off how much of an intellectual you are. '
    vibe = './socialist kithe.jpg'
if play_social > top1 :
    top1 = play_social
    top12 = 'play a game with your loser friends loser'
    truth = 'Get into the discord server, get into the channel of your choice, and round up those dorks for a game night. Weather it be a game like Overwatch, or Valorant or a game like Jackbox, Mario Kart, or dare I say even amogus and just goof off together. Get some social interaction and unlock the specific type of serotonin a low stakes competitive environment can provide. 07 to you gaymer.'
if play_sims_rpg > top1 :
    top1 = play_sims_rpg
    top12 = 'play some loser game loser'
    truth = 'Hey dork are you ready for some escapism? Get too into the Sims character creation and designing the house and then make those little virtual dolls have some fun.  Or if it’s more your style play a role playing game, weather that be an online game like A Dark Room, or something like Fire Emblem, Stardew Valley, Undertale and Final Fantasy. Listen to a soundtrack, put on some comfy clothes, and get going, it’s time for an adventure. '
    vibe = './take_this.png'
if bake_friends > top1 :
    top1 = bake_friends
    top12 = 'bake'
    truth = 'It is time to heal <3 or something <3 . Baking can be a great way to do something that even if it doesn’t feel stressful can be fulfilling and bring a sense of accomplishment since you have made something. Making a simple recipe like banana bread, brownies, peanut butter cookies, squash bread or challah with friends in person or over discord can lead to a chill night in that will even bring you some treats for tomorrow. Maybe you can bring them into work or school or for friends or family, or just keep them for yourself and your pals. Make some treats and goof off with a friend as you do for some extra serotonin. Bonus points if you blast music and dance around your kitchen as you clean up.'
    vibe = './bake.jpg'
if craft_chill > top1 :
    top1 = craft_chill
    vibe = './craft.jpg'
    top12 ='craft and chill'
    truth = 'CRAFT TIME. Whatever it is you do, polymer clay, crochet, knit, friendship bracelets, small wood carvings, jewellery, collage, whatever take some time and get into it. I like to throw on a video essay or podcast, or listen to music and sometimes even facetime a friend but do whatever add to the chill atmosphere. Tonight we craft and chill, tomorrow who knows, that’s future you’s problem. '

answer = st.header(top12)
destiny = st.subheader(truth)
if high_friend_game is top1  :
    video_file = open('im_gaymer.mp4','rb')
    gaymer = video_file.read()
    st.video(video_file)

img = st.image(vibe)
