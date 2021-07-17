init python:

    show_window_trans = MoveTransition(0.25,
                                       enter_factory=MoveIn((None, 
                                       1.0, None, 0.0)))

    hide_window_trans = MoveTransition(0.25,
                                       leave_factory=MoveOut((None, 
                                       1.0, None, 0.0)))

    def hide_window():
        store._window_during_transitions = False
        narrator("", interact=False)
        renpy.with_statement(None)
        renpy.with_statement(hide_window_trans)

    def show_window():
        narrator("", interact=False)
        renpy.with_statement(show_window_trans)
        store._window_during_transitions = True

default sayoriWalk = False

# This is a copy of definitions.rpy from DDLC.
# Use this as a starting point if you would like to override with your own.

# Explanation for Definitions
# This section defines stuff for the game: sprite poses for the girls, music, and backgrounds
# If you plan on adding new content, pop them over down there and mimic the appropriate lines!


######### ##     ##  #######  ########   #######  ######### ########## ########## ########    #########
##        ##     ## ##     ## ##     ## ##     ## ##            ##     ##         ##      ##  ##
##        ##     ## ##     ## ##     ## ##     ## ##            ##     ##         ##      ##  ##
##        ######### ######### ########  ######### ##            ##     #######    ########    #########
##        ##     ## ##     ## ##   ##   ##     ## ##            ##     ##         ##    ##           ## 
##        ##     ## ##     ## ##    ##  ##     ## ##            ##     ##         ##     ##          ##
######### ##     ## ##     ## ##     ## ##     ## #########     ##     ########## ##      ##  #########


define narrator = Character(ctc="ctc", ctc_position="fixed")
define mc = DynamicCharacter('player', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define s = DynamicCharacter('s_name', image='sayori', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define m = DynamicCharacter('m_name', image='monika', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define n = DynamicCharacter('n_name', image='natsuki', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define y = DynamicCharacter('y_name', image='yuri', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define j = DynamicCharacter('j_name', image='josh', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define rus = DynamicCharacter('rus_name', image='russel', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define l = DynamicCharacter('l_name', image='lawson', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define r = DynamicCharacter('r_name', image='rivera', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define g = DynamicCharacter('g_name', image='griffin', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define speaker = DynamicCharacter('speaker_name', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define teacher = DynamicCharacter('teacher_name', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define respect_wamen = DynamicCharacter('respect_wamen_name', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define principal = DynamicCharacter('principal_name', image='principal', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define anon = DynamicCharacter('anon_name', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define man = DynamicCharacter('man_name', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define scientist = DynamicCharacter('scientist_name', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define subone = DynamicCharacter('subone_name', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define ny = Character('Nat & Yuri', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define girl1 = DynamicCharacter('girl1_name', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define girl2 = DynamicCharacter('girl2_name', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define girl3 = DynamicCharacter('girl3_name', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define matt = Character('Matt', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define my = Character('Matt & Nats', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define e = Character('Everyone', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")

#define matt = Character('matt_name', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
#default matt_name = "Matt"

default s_name = "Sayori"
default m_name = "Monika"
default n_name = "Natsuki"
default y_name = "Yuri"
default j_name = "Josh"
default rus_name = "Russel"
default l_name = "Dr. Lawson"
default r_name = "Dr. Rivera"
default g_name = "Dr. Griffin"
default anon_name = "???"
default speaker_name = "Speaker"
default teacher_name = "Teacher"
default respect_wamen_name = "Woman"
default principal_name = "Principal"
default man_name = "Man"
default scientist_name = "Scientist"
default subone_name = "Subject One"
default girl1_name = "Girl 1"
default girl2_name = "Girl 2"
default girl3_name = "Girl 3"
default e_name = "Everyone"

define persistent.demo = False
define persistent.steam = False
define config.developer = False #Change this flag to True to enable dev tools

python early:
    import singleton
    me = singleton.SingleInstance()

init python:
    config.keymap['game_menu'].remove('mouseup_3')
    config.keymap['hide_windows'].append('mouseup_3')
    config.keymap['self_voicing'] = []
    config.keymap['clipboard_voicing'] = []
    config.keymap['toggle_skip'] = []
    renpy.music.register_channel("music_poem", mixer="music", tight=True)
    def get_pos(channel='music'):
        pos = renpy.music.get_pos(channel=channel)
        if pos: return pos
        return 0
    def delete_all_saves():
        for savegame in renpy.list_saved_games(fast=True):
            renpy.unlink_save(savegame)
    def delete_character(name):
        if persistent.do_not_delete: return
        import os
        try: os.remove(config.basedir + "/characters/" + name + ".chr")
        except: pass
    def pause(time=None):
        if not time:
            renpy.ui.saybehavior(afm=" ")
            renpy.ui.interact(mouse='pause', type='pause', roll_forward=None)
            return
        if time <= 0: return
        renpy.pause(time)


  ######   ##      ## ########   ########## ##########
##      ## ##      ## ##      ##     ##     ##      ##
##      ## ##      ## ##      ##     ##     ##      ##
########## ##      ## ##      ##     ##     ##      ##
##      ## ##      ## ##      ##     ##     ##      ##
##      ## ##      ## ##      ##     ##     ##      ##
##      ## ########## ########   ########## ##########


define audio.t1 = "<loop 22.073>bgm/1.ogg"  #Main theme (title)


define audio.t2 = "<loop 4.499>bgm/2.ogg"   #Sayori theme
define audio.t2g = "bgm/2g.ogg"
define audio.t2g2 = "<from 4.499 loop 4.499>bgm/2.ogg"
define audio.t2g3 = "<loop 4.492>bgm/2g2.ogg"
define audio.t3 = "<loop 4.618>bgm/3.ogg"   #Main theme (in-game)
define audio.t3g = "<to 15.255>bgm/3g.ogg"
define audio.t3g2 = "<from 15.255 loop 4.618>bgm/3.ogg"
define audio.t3g3 = "<loop 4.618>bgm/3g2.ogg"
define audio.t3m = "<loop 4.618>bgm/3.ogg"
define audio.t4 = "<loop 19.451>bgm/4.ogg"  #Poem minigame
define audio.t4g = "<loop 1.000>bgm/4g.ogg"

define audio.t5 = "<loop 4.444>bgm/5.ogg"   #Sharing poems...... 'Okay Everyone~!'
#Hey Mod team, our themes aren't defined here in the original script.
#Did some reading around and there was this + "_character" reference elsewhere.
#Anyhow, I'll try 'defining' them and see if it works!

define audio.tmonika = "<loop 4.444>bgm/5_monika.ogg" #I'm the only one with pianos x3
define audio.tsayori = "<loop 4.444>bgm/5_sayori.ogg" #Hxppy Thoughts with Ukelele & Snapping~!
define audio.tnatsuki = "<loop 4.444>bgm/5_natsuki.ogg" #Was it always cute on purpose?
define audio.tyuri = "<loop 4.444>bgm/5_yuri.ogg" #Fancy harps and instruments!

#Yeah, Monika... that should be good.
#So, take it from her and if you want to define music, make sure it exists in the appropriate folder
#Define its "audio.name" and see how it goes! (this should always be .ogg too, I think)

define audio.t5b = "<loop 4.444>bgm/5.ogg"
define audio.t5c = "<loop 4.444>bgm/5.ogg"
define audio.t6 = "<loop 10.893>bgm/6.ogg"  #Yuri/Natsuki theme
define audio.t6g = "<loop 10.893>bgm/6g.ogg"
define audio.t6r = "<to 39.817 loop 0>bgm/6r.ogg"
define audio.t6s = "<loop 43.572>bgm/6s.ogg"
define audio.t7 = "<loop 2.291>bgm/7.ogg"   #Causing trouble
define audio.t7a = "<loop 4.316 to 12.453>bgm/7.ogg"
define audio.t7g = "<loop 31.880>bgm/7g.ogg"
define audio.t8 = "<loop 9.938>bgm/8.ogg"   #Trouble resolved
define audio.t9 = "<loop 3.172>bgm/9.ogg"   #Emotional
define audio.t9g = "<loop 1.532>bgm/9g.ogg" #207% speed
define audio.t10 = "<loop 5.861>bgm/10.ogg"   #Confession
define audio.t10y = "<loop 0>bgm/10-yuri.ogg"
define audio.td = "<loop 36.782>bgm/d.ogg"


define audio.m1 = "<loop 0>bgm/m1.ogg" #Monika and her spaceroom music
define audio.mend = "<loop 6.424>bgm/monika-end.ogg" #Monika music post-deletion

define audio.ghostmenu = "<loop 0>bgm/ghostmenu.ogg"
define audio.g1 = "<loop 0>bgm/g1.ogg"
define audio.g2 = "<loop 0>bgm/g2.ogg"
define audio.hb = "<loop 0>bgm/heartbeat.ogg"

define audio.closet_open = "sfx/closet-open.ogg"
define audio.closet_close = "sfx/closet-close.ogg"
define audio.page_turn = "sfx/pageflip.ogg"
define audio.fall = "sfx/fall.ogg"
define audio.fall2 = "sfx/fall2.ogg"
define audio.knockx3 = "mod_assets/knock_3_times.mp3"

# Custom Music
define audio.lab_music = "mod_assets/lab_music.mp3"
define audio.auditorium_music = "mod_assets/auditorium_music.mp3"
define audio.b1 = "mod_assets/prob_not_needed/burp1.ogg"
define audio.b2 = "mod_assets/prob_not_needed/burp2.ogg"
define audio.b3 = "mod_assets/prob_not_needed/burp3.ogg"

########   ##########   ##########
##      ## ##           ##
##      ## ##           ##
########   ##   #####   ##########
##      ## ##      ##           ##
##      ## ##      ##           ##
########   ##########   ##########

# Backgrounds
image black = "#000000"
image dark = "#000000e4"
image darkred = "#110000c8"
image white = "#ffffff"
image splash = "bg/splash.png"
image end:
    truecenter
    "gui/end.png"
image bg residential_day = "bg/residential.png"
image bg class_day = "bg/class.png"
image bg corridor = "bg/corridor.png"
image bg club_day = "bg/club.png"
image bg club_day2:
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg/club-skill.png"
image bg closet = "bg/closet.png"
image bg bedroom = "bg/bedroom.png"
image bg sayori_bedroom = "bg/sayori_bedroom.png"
image bg house = "bg/house.png"
image bg kitchen = "bg/kitchen.png"

# mod assets
# NEW BGS
image bg livingroom_a = "mod_assets/livingroom.png"
image bg livingroom_b = "mod_assets/livingroom_dusk.png"
image bg hallway_1:
    "mod_assets/NewBGs/hallway_a.png"
    zoom 1.25 xzoom 1.26
image bg gym:
    "mod_assets/NewBGs/gym.png"
    zoom 1.25 xzoom 1.26
image bg park_day:
    "mod_assets/NewBGs/park_a.png"
    zoom 1.25 xzoom 1.26
image bg park_night:
    "mod_assets/NewBGs/park_b.png"
    zoom 1.25 xzoom 1.26
image bg park_dark:
    "mod_assets/NewBGs/park_c.png"
    zoom 1.25 xzoom 1.26
image bg park_evening:
    "mod_assets/NewBGs/park_d.png"
    zoom 1.25 xzoom 1.26
image bg entrance_day:
    "mod_assets/NewBGs/door_a.png"
    zoom 1.25 xzoom 1.26
image bg entrance_evening:
    "mod_assets/NewBGs/door_b.png"
    zoom 1.25 xzoom 1.26
image bg entrance_night:
    "mod_assets/NewBGs/door_c.png"
    zoom 1.25 xzoom 1.26
image bg entrance_dark:
    "mod_assets/NewBGs/door_d.png"
    zoom 1.25 xzoom 1.26
image bg class_real = "mod_assets/NewBGs/class_real.jpg"
image bg building:
    "mod_assets/NewBGs/building.jpg"
    zoom .45
image bg hallway_2:
    "mod_assets/NewBGs/hallway_b.jpg"
    zoom .35
image bg bedroom1 = "mod_assets/NewBGs/bedroom_real.png"
# Demo BGS
image bg auditorium = "mod_assets/auditorium.png"
image bg auditorium2 = "mod_assets/auditorium2.jpg"
image bg auditorium3 = "mod_assets/auditorium3.jpg"
image bg dark_bedroom = "mod_assets/dark_bedroom.png"

image bg outside_lab:
    "mod_assets/outside_lab.png"
    zoom 1.75 xzoom 1.5
image bg lab:
    "mod_assets/inside_lab.png"
image bg class_thing:
    "mod_assets/class_thing.png"
    zoom 2 xzoom 1.25
image bg hallway_thing:
    "mod_assets/hallway_thing.png"
    zoom 2 xzoom 1.25
image bg lawson_office:
    "mod_assets/lawson_office.png"
    zoom 2 xzoom 1.25
image tbc1 = "mod_assets/tbc1.png"
image tbc2 = "mod_assets/tbc2.png"
image bg p_office:
    "mod_assets/p_office.png"
    zoom 1.25
image bg residential_night:
    "mod_assets/residential_night.png"
image bg cafeteria:
    "mod_assets/cafeteria_blur.png"
    zoom .25 xzoom 1.30
image bg credits1 = "mod_assets/credits1.png"
image bg credits2 = "mod_assets/credits2.png"
image bg credits3 = "mod_assets/credits3.png"

image bg notebook = "bg/notebook.png"
image bg notebook-glitch = "bg/notebook-glitch.png"

image bg glitch = LiveTile("bg/glitch.jpg")

image glitch_color:
    ytile 3
    zoom 2.5
    parallel:
        "bg/glitch-red.png"
        0.1
        "bg/glitch-green.png"
        0.1
        "bg/glitch-blue.png"
        0.1
        repeat
    parallel:
        yoffset 720
        linear 0.5 yoffset 0
        repeat
    parallel:
        choice:
            xoffset 0
        choice:
            xoffset 10
        choice:
            xoffset 20
        choice:
            xoffset 35
        choice:
            xoffset -10
        choice:
            xoffset -20
        choice:
            xoffset -30
        0.01
        repeat
    parallel:
        alpha 0.6
        linear 0.15 alpha 0.1
        0.2
        alpha 0.6
        linear 0.15 alpha 0.1
        0.2
        alpha 0.7
        linear 0.45 alpha 0
        #1.0
        #linear 1.0 alpha 0.0

image glitch_color2:
    ytile 3
    zoom 2.5
    parallel:
        "bg/glitch-red.png"
        0.1
        "bg/glitch-green.png"
        0.1
        "bg/glitch-blue.png"
        0.1
        repeat
    parallel:
        yoffset 720
        linear 0.5 yoffset 0
        repeat
    parallel:
        choice:
            xoffset 0
        choice:
            xoffset 10
        choice:
            xoffset 20
        choice:
            xoffset 35
        choice:
            xoffset -10
        choice:
            xoffset -20
        choice:
            xoffset -30
        0.01
        repeat
    parallel:
        alpha 0.7
        linear 0.45 alpha 0
        #1.0
        #linear 1.0 alpha 0.0


########## ########   ########   ########## ########## ########## ##########
##         ##      ## ##      ##     ##         ##     ##         ##
##         ##      ## ##      ##     ##         ##     ##         ##
########## ########   ########       ##         ##     #######    ##########
        ## ##         ##    ##       ##         ##     ##                 ##
        ## ##         ##     ##      ##         ##     ##                 ##
########## ##         ##      ## ##########     ##     ########## ##########


# Left, right, head

# MC/Matt (This guy is now me. I need some way to create this dumb skits to show my pain.) (They were made by u/-Chipz-, AKA Childish-N.)
image matt 1a = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/1l.png", (0, 0), "mod_assets/MCSpritesRed/1r.png", (0, 0), "mod_assets/MCSpritesRed/a.png")
image matt 1b = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/1l.png", (0, 0), "mod_assets/MCSpritesRed/1r.png", (0, 0), "mod_assets/MCSpritesRed/b.png")
image matt 1c = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/1l.png", (0, 0), "mod_assets/MCSpritesRed/1r.png", (0, 0), "mod_assets/MCSpritesRed/c.png")
image matt 1d = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/1l.png", (0, 0), "mod_assets/MCSpritesRed/1r.png", (0, 0), "mod_assets/MCSpritesRed/d.png")
image matt 1e = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/1l.png", (0, 0), "mod_assets/MCSpritesRed/1r.png", (0, 0), "mod_assets/MCSpritesRed/e.png")
image matt 1f = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/1l.png", (0, 0), "mod_assets/MCSpritesRed/1r.png", (0, 0), "mod_assets/MCSpritesRed/f.png")
image matt 1g = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/1l.png", (0, 0), "mod_assets/MCSpritesRed/1r.png", (0, 0), "mod_assets/MCSpritesRed/g.png")
image matt 1h = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/1l.png", (0, 0), "mod_assets/MCSpritesRed/1r.png", (0, 0), "mod_assets/MCSpritesRed/h.png")
image matt 1i = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/1l.png", (0, 0), "mod_assets/MCSpritesRed/1r.png", (0, 0), "mod_assets/MCSpritesRed/i.png")
image matt 1j = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/1l.png", (0, 0), "mod_assets/MCSpritesRed/1r.png", (0, 0), "mod_assets/MCSpritesRed/j.png")
image matt 1k = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/1l.png", (0, 0), "mod_assets/MCSpritesRed/1r.png", (0, 0), "mod_assets/MCSpritesRed/k.png")
image matt 1l = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/1l.png", (0, 0), "mod_assets/MCSpritesRed/1r.png", (0, 0), "mod_assets/MCSpritesRed/l.png")
image matt 1m = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/1l.png", (0, 0), "mod_assets/MCSpritesRed/1r.png", (0, 0), "mod_assets/MCSpritesRed/m.png")
image matt 1n = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/1l.png", (0, 0), "mod_assets/MCSpritesRed/1r.png", (0, 0), "mod_assets/MCSpritesRed/n.png")
image matt 1o = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/1l.png", (0, 0), "mod_assets/MCSpritesRed/1r.png", (0, 0), "mod_assets/MCSpritesRed/o.png")
image matt 1p = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/1l.png", (0, 0), "mod_assets/MCSpritesRed/1r.png", (0, 0), "mod_assets/MCSpritesRed/p.png")
image matt 1q = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/1l.png", (0, 0), "mod_assets/MCSpritesRed/1r.png", (0, 0), "mod_assets/MCSpritesRed/q.png")
image matt 1r = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/1l.png", (0, 0), "mod_assets/MCSpritesRed/1r.png", (0, 0), "mod_assets/MCSpritesRed/r.png")
image matt 1s = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/1l.png", (0, 0), "mod_assets/MCSpritesRed/1r.png", (0, 0), "mod_assets/MCSpritesRed/s.png")
image matt 1t = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/1l.png", (0, 0), "mod_assets/MCSpritesRed/1r.png", (0, 0), "mod_assets/MCSpritesRed/t.png")
image matt 1u = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/1l.png", (0, 0), "mod_assets/MCSpritesRed/1r.png", (0, 0), "mod_assets/MCSpritesRed/u.png")
image matt 1v = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/1l.png", (0, 0), "mod_assets/MCSpritesRed/1r.png", (0, 0), "mod_assets/MCSpritesRed/v.png")
image matt 1w = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/1l.png", (0, 0), "mod_assets/MCSpritesRed/1r.png", (0, 0), "mod_assets/MCSpritesRed/w.png")
image matt 1x = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/1l.png", (0, 0), "mod_assets/MCSpritesRed/1r.png", (0, 0), "mod_assets/MCSpritesRed/x.png")
image matt 1y = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/1l.png", (0, 0), "mod_assets/MCSpritesRed/1r.png", (0, 0), "mod_assets/MCSpritesRed/y.png")
image matt 1z = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/1l.png", (0, 0), "mod_assets/MCSpritesRed/1r.png", (0, 0), "mod_assets/MCSpritesRed/z.png")

image matt 2a = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/2l.png", (0, 0), "mod_assets/MCSpritesRed/1r.png", (0, 0), "mod_assets/MCSpritesRed/a.png")
image matt 2b = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/2l.png", (0, 0), "mod_assets/MCSpritesRed/1r.png", (0, 0), "mod_assets/MCSpritesRed/b.png")
image matt 2c = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/2l.png", (0, 0), "mod_assets/MCSpritesRed/1r.png", (0, 0), "mod_assets/MCSpritesRed/c.png")
image matt 2d = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/2l.png", (0, 0), "mod_assets/MCSpritesRed/1r.png", (0, 0), "mod_assets/MCSpritesRed/d.png")
image matt 2e = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/2l.png", (0, 0), "mod_assets/MCSpritesRed/1r.png", (0, 0), "mod_assets/MCSpritesRed/e.png")
image matt 2f = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/2l.png", (0, 0), "mod_assets/MCSpritesRed/1r.png", (0, 0), "mod_assets/MCSpritesRed/f.png")
image matt 2g = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/2l.png", (0, 0), "mod_assets/MCSpritesRed/1r.png", (0, 0), "mod_assets/MCSpritesRed/g.png")
image matt 2h = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/2l.png", (0, 0), "mod_assets/MCSpritesRed/1r.png", (0, 0), "mod_assets/MCSpritesRed/h.png")
image matt 2i = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/2l.png", (0, 0), "mod_assets/MCSpritesRed/1r.png", (0, 0), "mod_assets/MCSpritesRed/i.png")
image matt 2j = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/2l.png", (0, 0), "mod_assets/MCSpritesRed/1r.png", (0, 0), "mod_assets/MCSpritesRed/j.png")
image matt 2k = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/2l.png", (0, 0), "mod_assets/MCSpritesRed/1r.png", (0, 0), "mod_assets/MCSpritesRed/k.png")
image matt 2l = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/2l.png", (0, 0), "mod_assets/MCSpritesRed/1r.png", (0, 0), "mod_assets/MCSpritesRed/l.png")
image matt 2m = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/2l.png", (0, 0), "mod_assets/MCSpritesRed/1r.png", (0, 0), "mod_assets/MCSpritesRed/m.png")
image matt 2n = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/2l.png", (0, 0), "mod_assets/MCSpritesRed/1r.png", (0, 0), "mod_assets/MCSpritesRed/n.png")
image matt 2o = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/2l.png", (0, 0), "mod_assets/MCSpritesRed/1r.png", (0, 0), "mod_assets/MCSpritesRed/o.png")
image matt 2p = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/2l.png", (0, 0), "mod_assets/MCSpritesRed/1r.png", (0, 0), "mod_assets/MCSpritesRed/p.png")
image matt 2q = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/2l.png", (0, 0), "mod_assets/MCSpritesRed/1r.png", (0, 0), "mod_assets/MCSpritesRed/q.png")
image matt 2r = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/2l.png", (0, 0), "mod_assets/MCSpritesRed/1r.png", (0, 0), "mod_assets/MCSpritesRed/r.png")
image matt 2s = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/2l.png", (0, 0), "mod_assets/MCSpritesRed/1r.png", (0, 0), "mod_assets/MCSpritesRed/s.png")
image matt 2t = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/2l.png", (0, 0), "mod_assets/MCSpritesRed/1r.png", (0, 0), "mod_assets/MCSpritesRed/t.png")
image matt 2u = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/2l.png", (0, 0), "mod_assets/MCSpritesRed/1r.png", (0, 0), "mod_assets/MCSpritesRed/u.png")
image matt 2v = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/2l.png", (0, 0), "mod_assets/MCSpritesRed/1r.png", (0, 0), "mod_assets/MCSpritesRed/v.png")
image matt 2w = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/2l.png", (0, 0), "mod_assets/MCSpritesRed/1r.png", (0, 0), "mod_assets/MCSpritesRed/w.png")
image matt 2x = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/2l.png", (0, 0), "mod_assets/MCSpritesRed/1r.png", (0, 0), "mod_assets/MCSpritesRed/x.png")
image matt 2y = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/2l.png", (0, 0), "mod_assets/MCSpritesRed/1r.png", (0, 0), "mod_assets/MCSpritesRed/y.png")
image matt 2z = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/2l.png", (0, 0), "mod_assets/MCSpritesRed/1r.png", (0, 0), "mod_assets/MCSpritesRed/z.png")

image matt 3a = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/1l.png", (0, 0), "mod_assets/MCSpritesRed/2r.png", (0, 0), "mod_assets/MCSpritesRed/a.png")
image matt 3b = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/1l.png", (0, 0), "mod_assets/MCSpritesRed/2r.png", (0, 0), "mod_assets/MCSpritesRed/b.png")
image matt 3c = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/1l.png", (0, 0), "mod_assets/MCSpritesRed/2r.png", (0, 0), "mod_assets/MCSpritesRed/c.png")
image matt 3d = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/1l.png", (0, 0), "mod_assets/MCSpritesRed/2r.png", (0, 0), "mod_assets/MCSpritesRed/d.png")
image matt 3e = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/1l.png", (0, 0), "mod_assets/MCSpritesRed/2r.png", (0, 0), "mod_assets/MCSpritesRed/e.png")
image matt 3f = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/1l.png", (0, 0), "mod_assets/MCSpritesRed/2r.png", (0, 0), "mod_assets/MCSpritesRed/f.png")
image matt 3g = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/1l.png", (0, 0), "mod_assets/MCSpritesRed/2r.png", (0, 0), "mod_assets/MCSpritesRed/g.png")
image matt 3h = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/1l.png", (0, 0), "mod_assets/MCSpritesRed/2r.png", (0, 0), "mod_assets/MCSpritesRed/h.png")
image matt 3i = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/1l.png", (0, 0), "mod_assets/MCSpritesRed/2r.png", (0, 0), "mod_assets/MCSpritesRed/i.png")
image matt 3j = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/1l.png", (0, 0), "mod_assets/MCSpritesRed/2r.png", (0, 0), "mod_assets/MCSpritesRed/j.png")
image matt 3k = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/1l.png", (0, 0), "mod_assets/MCSpritesRed/2r.png", (0, 0), "mod_assets/MCSpritesRed/k.png")
image matt 3l = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/1l.png", (0, 0), "mod_assets/MCSpritesRed/2r.png", (0, 0), "mod_assets/MCSpritesRed/l.png")
image matt 3m = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/1l.png", (0, 0), "mod_assets/MCSpritesRed/2r.png", (0, 0), "mod_assets/MCSpritesRed/m.png")
image matt 3n = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/1l.png", (0, 0), "mod_assets/MCSpritesRed/2r.png", (0, 0), "mod_assets/MCSpritesRed/n.png")
image matt 3o = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/1l.png", (0, 0), "mod_assets/MCSpritesRed/2r.png", (0, 0), "mod_assets/MCSpritesRed/o.png")
image matt 3p = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/1l.png", (0, 0), "mod_assets/MCSpritesRed/2r.png", (0, 0), "mod_assets/MCSpritesRed/p.png")
image matt 3q = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/1l.png", (0, 0), "mod_assets/MCSpritesRed/2r.png", (0, 0), "mod_assets/MCSpritesRed/q.png")
image matt 3r = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/1l.png", (0, 0), "mod_assets/MCSpritesRed/2r.png", (0, 0), "mod_assets/MCSpritesRed/r.png")
image matt 3s = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/1l.png", (0, 0), "mod_assets/MCSpritesRed/2r.png", (0, 0), "mod_assets/MCSpritesRed/s.png")
image matt 3t = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/1l.png", (0, 0), "mod_assets/MCSpritesRed/2r.png", (0, 0), "mod_assets/MCSpritesRed/t.png")
image matt 3u = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/1l.png", (0, 0), "mod_assets/MCSpritesRed/2r.png", (0, 0), "mod_assets/MCSpritesRed/u.png")
image matt 3v = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/1l.png", (0, 0), "mod_assets/MCSpritesRed/2r.png", (0, 0), "mod_assets/MCSpritesRed/v.png")
image matt 3w = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/1l.png", (0, 0), "mod_assets/MCSpritesRed/2r.png", (0, 0), "mod_assets/MCSpritesRed/w.png")
image matt 3x = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/1l.png", (0, 0), "mod_assets/MCSpritesRed/2r.png", (0, 0), "mod_assets/MCSpritesRed/x.png")
image matt 3y = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/1l.png", (0, 0), "mod_assets/MCSpritesRed/2r.png", (0, 0), "mod_assets/MCSpritesRed/y.png")
image matt 3z = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/1l.png", (0, 0), "mod_assets/MCSpritesRed/2r.png", (0, 0), "mod_assets/MCSpritesRed/z.png")

image matt 4a = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/2l.png", (0, 0), "mod_assets/MCSpritesRed/2r.png", (0, 0), "mod_assets/MCSpritesRed/a.png")
image matt 4b = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/2l.png", (0, 0), "mod_assets/MCSpritesRed/2r.png", (0, 0), "mod_assets/MCSpritesRed/b.png")
image matt 4c = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/2l.png", (0, 0), "mod_assets/MCSpritesRed/2r.png", (0, 0), "mod_assets/MCSpritesRed/c.png")
image matt 4d = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/2l.png", (0, 0), "mod_assets/MCSpritesRed/2r.png", (0, 0), "mod_assets/MCSpritesRed/d.png")
image matt 4e = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/2l.png", (0, 0), "mod_assets/MCSpritesRed/2r.png", (0, 0), "mod_assets/MCSpritesRed/e.png")
image matt 4f = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/2l.png", (0, 0), "mod_assets/MCSpritesRed/2r.png", (0, 0), "mod_assets/MCSpritesRed/f.png")
image matt 4g = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/2l.png", (0, 0), "mod_assets/MCSpritesRed/2r.png", (0, 0), "mod_assets/MCSpritesRed/g.png")
image matt 4h = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/2l.png", (0, 0), "mod_assets/MCSpritesRed/2r.png", (0, 0), "mod_assets/MCSpritesRed/h.png")
image matt 4i = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/2l.png", (0, 0), "mod_assets/MCSpritesRed/2r.png", (0, 0), "mod_assets/MCSpritesRed/i.png")
image matt 4j = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/2l.png", (0, 0), "mod_assets/MCSpritesRed/2r.png", (0, 0), "mod_assets/MCSpritesRed/j.png")
image matt 4k = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/2l.png", (0, 0), "mod_assets/MCSpritesRed/2r.png", (0, 0), "mod_assets/MCSpritesRed/k.png")
image matt 4l = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/2l.png", (0, 0), "mod_assets/MCSpritesRed/2r.png", (0, 0), "mod_assets/MCSpritesRed/l.png")
image matt 4m = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/2l.png", (0, 0), "mod_assets/MCSpritesRed/2r.png", (0, 0), "mod_assets/MCSpritesRed/m.png")
image matt 4n = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/2l.png", (0, 0), "mod_assets/MCSpritesRed/2r.png", (0, 0), "mod_assets/MCSpritesRed/n.png")
image matt 4o = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/2l.png", (0, 0), "mod_assets/MCSpritesRed/2r.png", (0, 0), "mod_assets/MCSpritesRed/o.png")
image matt 4p = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/2l.png", (0, 0), "mod_assets/MCSpritesRed/2r.png", (0, 0), "mod_assets/MCSpritesRed/p.png")
image matt 4q = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/2l.png", (0, 0), "mod_assets/MCSpritesRed/2r.png", (0, 0), "mod_assets/MCSpritesRed/q.png")
image matt 4r = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/2l.png", (0, 0), "mod_assets/MCSpritesRed/2r.png", (0, 0), "mod_assets/MCSpritesRed/r.png")
image matt 4s = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/2l.png", (0, 0), "mod_assets/MCSpritesRed/2r.png", (0, 0), "mod_assets/MCSpritesRed/s.png")
image matt 4t = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/2l.png", (0, 0), "mod_assets/MCSpritesRed/2r.png", (0, 0), "mod_assets/MCSpritesRed/t.png")
image matt 4u = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/2l.png", (0, 0), "mod_assets/MCSpritesRed/2r.png", (0, 0), "mod_assets/MCSpritesRed/u.png")
image matt 4v = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/2l.png", (0, 0), "mod_assets/MCSpritesRed/2r.png", (0, 0), "mod_assets/MCSpritesRed/v.png")
image matt 4w = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/2l.png", (0, 0), "mod_assets/MCSpritesRed/2r.png", (0, 0), "mod_assets/MCSpritesRed/w.png")
image matt 4x = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/2l.png", (0, 0), "mod_assets/MCSpritesRed/2r.png", (0, 0), "mod_assets/MCSpritesRed/x.png")
image matt 4y = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/2l.png", (0, 0), "mod_assets/MCSpritesRed/2r.png", (0, 0), "mod_assets/MCSpritesRed/y.png")
image matt 4z = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/2l.png", (0, 0), "mod_assets/MCSpritesRed/2r.png", (0, 0), "mod_assets/MCSpritesRed/z.png")

image matt 5a = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/3.png", (0, 0), "mod_assets/MCSpritesRed/a.png")
image matt 5b = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/3.png", (0, 0), "mod_assets/MCSpritesRed/b.png")
image matt 5c = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/3.png", (0, 0), "mod_assets/MCSpritesRed/c.png")
image matt 5d = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/3.png", (0, 0), "mod_assets/MCSpritesRed/d.png")
image matt 5e = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/3.png", (0, 0), "mod_assets/MCSpritesRed/e.png")
image matt 5f = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/3.png", (0, 0), "mod_assets/MCSpritesRed/f.png")
image matt 5g = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/3.png", (0, 0), "mod_assets/MCSpritesRed/g.png")
image matt 5h = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/3.png", (0, 0), "mod_assets/MCSpritesRed/h.png")
image matt 5i = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/3.png", (0, 0), "mod_assets/MCSpritesRed/i.png")
image matt 5j = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/3.png", (0, 0), "mod_assets/MCSpritesRed/j.png")
image matt 5k = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/3.png", (0, 0), "mod_assets/MCSpritesRed/k.png")
image matt 5l = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/3.png", (0, 0), "mod_assets/MCSpritesRed/l.png")
image matt 5m = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/3.png", (0, 0), "mod_assets/MCSpritesRed/m.png")
image matt 5n = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/3.png", (0, 0), "mod_assets/MCSpritesRed/n.png")
image matt 5o = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/3.png", (0, 0),  "mod_assets/MCSpritesRed/o.png")
image matt 5p = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/3.png", (0, 0),  "mod_assets/MCSpritesRed/p.png")
image matt 5q = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/3.png", (0, 0), "mod_assets/MCSpritesRed/q.png")
image matt 5r = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/3.png", (0, 0), "mod_assets/MCSpritesRed/r.png")
image matt 5s = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/3.png", (0, 0), "mod_assets/MCSpritesRed/s.png")
image matt 5t = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/3.png", (0, 0), "mod_assets/MCSpritesRed/t.png")
image matt 5u = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/3.png", (0, 0), "mod_assets/MCSpritesRed/u.png")
image matt 5v = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/3.png", (0, 0), "mod_assets/MCSpritesRed/v.png")
image matt 5w = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/3.png", (0, 0), "mod_assets/MCSpritesRed/w.png")
image matt 5x = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/3.png", (0, 0), "mod_assets/MCSpritesRed/x.png")
image matt 5y = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/3.png", (0, 0), "mod_assets/MCSpritesRed/y.png")
image matt 5z = im.Composite((960, 960), (0, 0), "mod_assets/MCSpritesRed/3.png", (0, 0), "mod_assets/MCSpritesRed/z.png")

# Dr. Griffin (casual dadsuki)

image griffin 1a = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/1l.png", (0, 0), "mod_assets/GriffinSprites/1r.png", (0, 0), "mod_assets/GriffinSprites/a.png")
image griffin 1a2 = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/1l.png", (0, 0), "mod_assets/GriffinSprites/1r.png", (0, 0), "mod_assets/GriffinSprites/a2.png")
image griffin 1a3 = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/1l.png", (0, 0), "mod_assets/GriffinSprites/1r.png", (0, 0), "mod_assets/GriffinSprites/a3.png")
image griffin 1b = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/1l.png", (0, 0), "mod_assets/GriffinSprites/1r.png", (0, 0), "mod_assets/GriffinSprites/b.png")
image griffin 1c = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/1l.png", (0, 0), "mod_assets/GriffinSprites/1r.png", (0, 0), "mod_assets/GriffinSprites/c.png")
image griffin 1d = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/1l.png", (0, 0), "mod_assets/GriffinSprites/1r.png", (0, 0), "mod_assets/GriffinSprites/d.png")
image griffin 1e = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/1l.png", (0, 0), "mod_assets/GriffinSprites/1r.png", (0, 0), "mod_assets/GriffinSprites/e.png")
image griffin 1f = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/1l.png", (0, 0), "mod_assets/GriffinSprites/1r.png", (0, 0), "mod_assets/GriffinSprites/f.png")
image griffin 1g = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/1l.png", (0, 0), "mod_assets/GriffinSprites/1r.png", (0, 0), "mod_assets/GriffinSprites/g.png")
image griffin 1h = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/1l.png", (0, 0), "mod_assets/GriffinSprites/1r.png", (0, 0), "mod_assets/GriffinSprites/h.png")
image griffin 1i = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/1l.png", (0, 0), "mod_assets/GriffinSprites/1r.png", (0, 0), "mod_assets/GriffinSprites/i.png")
image griffin 1j = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/1l.png", (0, 0), "mod_assets/GriffinSprites/1r.png", (0, 0), "mod_assets/GriffinSprites/j.png")
image griffin 1k = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/1l.png", (0, 0), "mod_assets/GriffinSprites/1r.png", (0, 0), "mod_assets/GriffinSprites/k.png")
image griffin 1l = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/1l.png", (0, 0), "mod_assets/GriffinSprites/1r.png", (0, 0), "mod_assets/GriffinSprites/l.png")
image griffin 1m = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/1l.png", (0, 0), "mod_assets/GriffinSprites/1r.png", (0, 0), "mod_assets/GriffinSprites/m.png")
image griffin 1n = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/1l.png", (0, 0), "mod_assets/GriffinSprites/1r.png", (0, 0), "mod_assets/GriffinSprites/n.png")
image griffin 1o = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/1l.png", (0, 0), "mod_assets/GriffinSprites/1r.png", (0, 0), "mod_assets/GriffinSprites/o.png")
image griffin 1p = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/1l.png", (0, 0), "mod_assets/GriffinSprites/1r.png", (0, 0), "mod_assets/GriffinSprites/p.png")
image griffin 1q = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/1l.png", (0, 0), "mod_assets/GriffinSprites/1r.png", (0, 0), "mod_assets/GriffinSprites/q.png")
image griffin 1r = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/1l.png", (0, 0), "mod_assets/GriffinSprites/1r.png", (0, 0), "mod_assets/GriffinSprites/r.png")
image griffin 1s = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/1l.png", (0, 0), "mod_assets/GriffinSprites/1r.png", (0, 0), "mod_assets/GriffinSprites/s.png")
image griffin 1t = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/1l.png", (0, 0), "mod_assets/GriffinSprites/1r.png", (0, 0), "mod_assets/GriffinSprites/t.png")
image griffin 1u = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/1l.png", (0, 0), "mod_assets/GriffinSprites/1r.png", (0, 0), "mod_assets/GriffinSprites/u.png")
image griffin 1v = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/1l.png", (0, 0), "mod_assets/GriffinSprites/1r.png", (0, 0), "mod_assets/GriffinSprites/v.png")

image griffin 2a = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/2l.png", (0, 0), "mod_assets/GriffinSprites/1r.png", (0, 0), "mod_assets/GriffinSprites/a.png")
image griffin 2a2 = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/2l.png", (0, 0), "mod_assets/GriffinSprites/1r.png", (0, 0), "mod_assets/GriffinSprites/a2.png")
image griffin 2a3 = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/2l.png", (0, 0), "mod_assets/GriffinSprites/1r.png", (0, 0), "mod_assets/GriffinSprites/a3.png")
image griffin 2b = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/2l.png", (0, 0), "mod_assets/GriffinSprites/1r.png", (0, 0), "mod_assets/GriffinSprites/b.png")
image griffin 2c = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/2l.png", (0, 0), "mod_assets/GriffinSprites/1r.png", (0, 0), "mod_assets/GriffinSprites/c.png")
image griffin 2d = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/2l.png", (0, 0), "mod_assets/GriffinSprites/1r.png", (0, 0), "mod_assets/GriffinSprites/d.png")
image griffin 2e = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/2l.png", (0, 0), "mod_assets/GriffinSprites/1r.png", (0, 0), "mod_assets/GriffinSprites/e.png")
image griffin 2f = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/2l.png", (0, 0), "mod_assets/GriffinSprites/1r.png", (0, 0), "mod_assets/GriffinSprites/f.png")
image griffin 2g = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/2l.png", (0, 0), "mod_assets/GriffinSprites/1r.png", (0, 0), "mod_assets/GriffinSprites/g.png")
image griffin 2h = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/2l.png", (0, 0), "mod_assets/GriffinSprites/1r.png", (0, 0), "mod_assets/GriffinSprites/h.png")
image griffin 2i = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/2l.png", (0, 0), "mod_assets/GriffinSprites/1r.png", (0, 0), "mod_assets/GriffinSprites/i.png")
image griffin 2j = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/2l.png", (0, 0), "mod_assets/GriffinSprites/1r.png", (0, 0), "mod_assets/GriffinSprites/j.png")
image griffin 2k = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/2l.png", (0, 0), "mod_assets/GriffinSprites/1r.png", (0, 0), "mod_assets/GriffinSprites/k.png")
image griffin 2l = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/2l.png", (0, 0), "mod_assets/GriffinSprites/1r.png", (0, 0), "mod_assets/GriffinSprites/l.png")
image griffin 2m = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/2l.png", (0, 0), "mod_assets/GriffinSprites/1r.png", (0, 0), "mod_assets/GriffinSprites/m.png")
image griffin 2n = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/2l.png", (0, 0), "mod_assets/GriffinSprites/1r.png", (0, 0), "mod_assets/GriffinSprites/n.png")
image griffin 2o = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/2l.png", (0, 0), "mod_assets/GriffinSprites/1r.png", (0, 0), "mod_assets/GriffinSprites/o.png")
image griffin 2p = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/2l.png", (0, 0), "mod_assets/GriffinSprites/1r.png", (0, 0), "mod_assets/GriffinSprites/p.png")
image griffin 2q = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/2l.png", (0, 0), "mod_assets/GriffinSprites/1r.png", (0, 0), "mod_assets/GriffinSprites/q.png")
image griffin 2r = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/2l.png", (0, 0), "mod_assets/GriffinSprites/1r.png", (0, 0), "mod_assets/GriffinSprites/r.png")
image griffin 2s = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/2l.png", (0, 0), "mod_assets/GriffinSprites/1r.png", (0, 0), "mod_assets/GriffinSprites/s.png")
image griffin 2t = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/2l.png", (0, 0), "mod_assets/GriffinSprites/1r.png", (0, 0), "mod_assets/GriffinSprites/t.png")
image griffin 2u = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/2l.png", (0, 0), "mod_assets/GriffinSprites/1r.png", (0, 0), "mod_assets/GriffinSprites/u.png")
image griffin 2v = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/2l.png", (0, 0), "mod_assets/GriffinSprites/1r.png", (0, 0), "mod_assets/GriffinSprites/v.png")

image griffin 3a = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/1l.png", (0, 0), "mod_assets/GriffinSprites/2r.png", (0, 0), "mod_assets/GriffinSprites/a.png")
image griffin 3a2 = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/1l.png", (0, 0), "mod_assets/GriffinSprites/2r.png", (0, 0), "mod_assets/GriffinSprites/a2.png")
image griffin 3a3 = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/1l.png", (0, 0), "mod_assets/GriffinSprites/2r.png", (0, 0), "mod_assets/GriffinSprites/a3.png")
image griffin 3b = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/1l.png", (0, 0), "mod_assets/GriffinSprites/2r.png", (0, 0), "mod_assets/GriffinSprites/b.png")
image griffin 3c = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/1l.png", (0, 0), "mod_assets/GriffinSprites/2r.png", (0, 0), "mod_assets/GriffinSprites/c.png")
image griffin 3d = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/1l.png", (0, 0), "mod_assets/GriffinSprites/2r.png", (0, 0), "mod_assets/GriffinSprites/d.png")
image griffin 3e = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/1l.png", (0, 0), "mod_assets/GriffinSprites/2r.png", (0, 0), "mod_assets/GriffinSprites/e.png")
image griffin 3f = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/1l.png", (0, 0), "mod_assets/GriffinSprites/2r.png", (0, 0), "mod_assets/GriffinSprites/f.png")
image griffin 3g = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/1l.png", (0, 0), "mod_assets/GriffinSprites/2r.png", (0, 0), "mod_assets/GriffinSprites/g.png")
image griffin 3h = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/1l.png", (0, 0), "mod_assets/GriffinSprites/2r.png", (0, 0), "mod_assets/GriffinSprites/h.png")
image griffin 3i = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/1l.png", (0, 0), "mod_assets/GriffinSprites/2r.png", (0, 0), "mod_assets/GriffinSprites/i.png")
image griffin 3j = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/1l.png", (0, 0), "mod_assets/GriffinSprites/2r.png", (0, 0), "mod_assets/GriffinSprites/j.png")
image griffin 3k = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/1l.png", (0, 0), "mod_assets/GriffinSprites/2r.png", (0, 0), "mod_assets/GriffinSprites/k.png")
image griffin 3l = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/1l.png", (0, 0), "mod_assets/GriffinSprites/2r.png", (0, 0), "mod_assets/GriffinSprites/l.png")
image griffin 3m = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/1l.png", (0, 0), "mod_assets/GriffinSprites/2r.png", (0, 0), "mod_assets/GriffinSprites/m.png")
image griffin 3n = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/1l.png", (0, 0), "mod_assets/GriffinSprites/2r.png", (0, 0), "mod_assets/GriffinSprites/n.png")
image griffin 3o = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/1l.png", (0, 0), "mod_assets/GriffinSprites/2r.png", (0, 0), "mod_assets/GriffinSprites/o.png")
image griffin 3p = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/1l.png", (0, 0), "mod_assets/GriffinSprites/2r.png", (0, 0), "mod_assets/GriffinSprites/p.png")
image griffin 3q = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/1l.png", (0, 0), "mod_assets/GriffinSprites/2r.png", (0, 0), "mod_assets/GriffinSprites/q.png")
image griffin 3r = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/1l.png", (0, 0), "mod_assets/GriffinSprites/2r.png", (0, 0), "mod_assets/GriffinSprites/r.png")
image griffin 3s = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/1l.png", (0, 0), "mod_assets/GriffinSprites/2r.png", (0, 0), "mod_assets/GriffinSprites/s.png")
image griffin 3t = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/1l.png", (0, 0), "mod_assets/GriffinSprites/2r.png", (0, 0), "mod_assets/GriffinSprites/t.png")
image griffin 3u = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/1l.png", (0, 0), "mod_assets/GriffinSprites/2r.png", (0, 0), "mod_assets/GriffinSprites/u.png")
image griffin 3v = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/1l.png", (0, 0), "mod_assets/GriffinSprites/2r.png", (0, 0), "mod_assets/GriffinSprites/v.png")

image griffin 4a = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/2l.png", (0, 0), "mod_assets/GriffinSprites/2r.png", (0, 0), "mod_assets/GriffinSprites/a.png")
image griffin 4a2 = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/2l.png", (0, 0), "mod_assets/GriffinSprites/2r.png", (0, 0), "mod_assets/GriffinSprites/a2.png")
image griffin 4a3 = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/2l.png", (0, 0), "mod_assets/GriffinSprites/2r.png", (0, 0), "mod_assets/GriffinSprites/a3.png")
image griffin 4b = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/2l.png", (0, 0), "mod_assets/GriffinSprites/2r.png", (0, 0), "mod_assets/GriffinSprites/b.png")
image griffin 4c = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/2l.png", (0, 0), "mod_assets/GriffinSprites/2r.png", (0, 0), "mod_assets/GriffinSprites/c.png")
image griffin 4d = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/2l.png", (0, 0), "mod_assets/GriffinSprites/2r.png", (0, 0), "mod_assets/GriffinSprites/d.png")
image griffin 4e = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/2l.png", (0, 0), "mod_assets/GriffinSprites/2r.png", (0, 0), "mod_assets/GriffinSprites/e.png")
image griffin 4f = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/2l.png", (0, 0), "mod_assets/GriffinSprites/2r.png", (0, 0), "mod_assets/GriffinSprites/f.png")
image griffin 4g = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/2l.png", (0, 0), "mod_assets/GriffinSprites/2r.png", (0, 0), "mod_assets/GriffinSprites/g.png")
image griffin 4h = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/2l.png", (0, 0), "mod_assets/GriffinSprites/2r.png", (0, 0), "mod_assets/GriffinSprites/h.png")
image griffin 4i = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/2l.png", (0, 0), "mod_assets/GriffinSprites/2r.png", (0, 0), "mod_assets/GriffinSprites/i.png")
image griffin 4j = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/2l.png", (0, 0), "mod_assets/GriffinSprites/2r.png", (0, 0), "mod_assets/GriffinSprites/j.png")
image griffin 4k = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/2l.png", (0, 0), "mod_assets/GriffinSprites/2r.png", (0, 0), "mod_assets/GriffinSprites/k.png")
image griffin 4l = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/2l.png", (0, 0), "mod_assets/GriffinSprites/2r.png", (0, 0), "mod_assets/GriffinSprites/l.png")
image griffin 4m = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/2l.png", (0, 0), "mod_assets/GriffinSprites/2r.png", (0, 0), "mod_assets/GriffinSprites/m.png")
image griffin 4n = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/2l.png", (0, 0), "mod_assets/GriffinSprites/2r.png", (0, 0), "mod_assets/GriffinSprites/n.png")
image griffin 4o = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/2l.png", (0, 0), "mod_assets/GriffinSprites/2r.png", (0, 0), "mod_assets/GriffinSprites/o.png")
image griffin 4p = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/2l.png", (0, 0), "mod_assets/GriffinSprites/2r.png", (0, 0), "mod_assets/GriffinSprites/p.png")
image griffin 4q = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/2l.png", (0, 0), "mod_assets/GriffinSprites/2r.png", (0, 0), "mod_assets/GriffinSprites/q.png")
image griffin 4r = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/2l.png", (0, 0), "mod_assets/GriffinSprites/2r.png", (0, 0), "mod_assets/GriffinSprites/r.png")
image griffin 4s = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/2l.png", (0, 0), "mod_assets/GriffinSprites/2r.png", (0, 0), "mod_assets/GriffinSprites/s.png")
image griffin 4t = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/2l.png", (0, 0), "mod_assets/GriffinSprites/2r.png", (0, 0), "mod_assets/GriffinSprites/t.png")
image griffin 4u = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/2l.png", (0, 0), "mod_assets/GriffinSprites/2r.png", (0, 0), "mod_assets/GriffinSprites/u.png")
image griffin 4v = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/2l.png", (0, 0), "mod_assets/GriffinSprites/2r.png", (0, 0), "mod_assets/GriffinSprites/v.png")

image griffin 5a = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/3.png", (0, 0), "mod_assets/GriffinSprites/a.png")
image griffin 5a2 = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/3.png", (0, 0), "mod_assets/GriffinSprites/a2.png")
image griffin 5a3 = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/3.png", (0, 0), "mod_assets/GriffinSprites/a3.png")
image griffin 5b = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/3.png", (0, 0), "mod_assets/GriffinSprites/b.png")
image griffin 5c = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/3.png", (0, 0), "mod_assets/GriffinSprites/c.png")
image griffin 5d = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/3.png", (0, 0), "mod_assets/GriffinSprites/d.png")
image griffin 5e = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/3.png", (0, 0), "mod_assets/GriffinSprites/e.png")
image griffin 5f = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/3.png", (0, 0), "mod_assets/GriffinSprites/f.png")
image griffin 5g = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/3.png", (0, 0), "mod_assets/GriffinSprites/g.png")
image griffin 5h = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/3.png", (0, 0), "mod_assets/GriffinSprites/h.png")
image griffin 5i = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/3.png", (0, 0), "mod_assets/GriffinSprites/i.png")
image griffin 5j = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/3.png", (0, 0), "mod_assets/GriffinSprites/j.png")
image griffin 5k = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/3.png", (0, 0), "mod_assets/GriffinSprites/k.png")
image griffin 5l = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/3.png", (0, 0), "mod_assets/GriffinSprites/l.png")
image griffin 5m = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/3.png", (0, 0), "mod_assets/GriffinSprites/m.png")
image griffin 5n = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/3.png", (0, 0), "mod_assets/GriffinSprites/n.png")
image griffin 5o = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/3.png", (0, 0), "mod_assets/GriffinSprites/o.png")
image griffin 5p = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/3.png", (0, 0), "mod_assets/GriffinSprites/p.png")
image griffin 5q = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/3.png", (0, 0), "mod_assets/GriffinSprites/q.png")
image griffin 5r = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/3.png", (0, 0), "mod_assets/GriffinSprites/r.png")
image griffin 5s = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/3.png", (0, 0), "mod_assets/GriffinSprites/s.png")
image griffin 5t = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/3.png", (0, 0), "mod_assets/GriffinSprites/t.png")
image griffin 5u = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/3.png", (0, 0), "mod_assets/GriffinSprites/u.png")
image griffin 5v = im.Composite((960, 960), (0, 0), "mod_assets/GriffinSprites/3.png", (0, 0), "mod_assets/GriffinSprites/v.png")


# RESPECT WAMEN (casual)
image principal ca:
    "mod_assets/wamen/ca.png"
    zoom 0.65
    yoffset 50
image principal cb:
    "mod_assets/wamen/cb.png"
    zoom 0.65
    yoffset 50
image principal cc:
    "mod_assets/wamen/cc.png"
    zoom 0.65
    yoffset 50
image principal cd:
    "mod_assets/wamen/cd.png"
    zoom 0.65
    yoffset 50
image principal ce:
    "mod_assets/wamen/ce.png"
    zoom 0.65
    yoffset 50
image principal cf:
    "mod_assets/wamen/cf.png"
    zoom 0.65
    yoffset 50
image principal cg:
    "mod_assets/wamen/cg.png"
    zoom 0.65
    yoffset 50
image principal ch:
    "mod_assets/wamen/ch.png"
    zoom 0.65
    yoffset 50
image principal ci:
    "mod_assets/wamen/ci.png"
    zoom 0.65
    yoffset 50
image principal cj:
    "mod_assets/wamen/cj.png"
    zoom 0.65
    yoffset 50
image principal ck:
    "mod_assets/wamen/ck.png"
    zoom 0.65
    yoffset 50
image principal cl:
    "mod_assets/wamen/cl.png"
    zoom 0.65
    yoffset 50
# winter (school)
image principal wa:
    "mod_assets/wamen/wa.png"
    zoom 0.65
    yoffset 50
image principal wb:
    "mod_assets/wamen/wb.png"
    zoom 0.65
    yoffset 50
image principal wc:
    "mod_assets/wamen/wc.png"
    zoom 0.65
    yoffset 50
image principal wd:
    "mod_assets/wamen/wd.png"
    zoom 0.65
    yoffset 50
image principal we:
    "mod_assets/wamen/we.png"
    zoom 0.65
    yoffset 50
image principal wf:
    "mod_assets/wamen/wf.png"
    zoom 0.65
    yoffset 50
image principal wg:
    "mod_assets/wamen/wg.png"
    zoom 0.65
    yoffset 50
image principal wh:
    "mod_assets/wamen/wh.png"
    zoom 0.65
    yoffset 50
image principal wi:
    "mod_assets/wamen/wi.png"
    zoom 0.65
    yoffset 50
image principal wj:
    "mod_assets/wamen/wj.png"
    zoom 0.65
    yoffset 50
image principal wk:
    "mod_assets/wamen/wk.png"
    zoom 0.65
    yoffset 50
image principal wl:
    "mod_assets/wamen/wl.png"
    zoom 0.65
    yoffset 50


# Dr. Lawson (glasses guy)
image lawson a = "mod_assets/DrLTrans/a.png"
image lawson b = "mod_assets/DrLTrans/b.png"
image lawson c = "mod_assets/DrLTrans/c.png"
image lawson d = "mod_assets/DrLTrans/d.png"
image lawson e = "mod_assets/DrLTrans/e.png"
image lawson f = "mod_assets/DrLTrans/f.png"
image lawson g = "mod_assets/DrLTrans/g.png"
image lawson h = "mod_assets/DrLTrans/h.png"
image lawson i = "mod_assets/DrLTrans/i.png"
image lawson j = "mod_assets/DrLTrans/j.png"
image lawson k = "mod_assets/DrLTrans/k.png"
image lawson l = "mod_assets/DrLTrans/l.png"
image lawson m = "mod_assets/DrLTrans/m.png"
image lawson n = "mod_assets/DrLTrans/n.png"
image lawson o = "mod_assets/DrLTrans/o.png"
image lawson p = "mod_assets/DrLTrans/p.png"
image lawson q = "mod_assets/DrLTrans/q.png"
image lawson r = "mod_assets/DrLTrans/r.png"
image lawson s = "mod_assets/DrLTrans/s.png"
image lawson t = "mod_assets/DrLTrans/t.png"
image lawson u = "mod_assets/DrLTrans/u.png"
image lawson v = "mod_assets/DrLTrans/v.png"




# Russel (kieran)
image russel a:
    "mod_assets/kieran/a.png"
    zoom 0.70 yoffset 150
image russel b:
    "mod_assets/kieran/b.png"
    zoom 0.70 yoffset 150
image russel c:
    "mod_assets/kieran/c.png"
    zoom 0.70 yoffset 150
image russel d:
    "mod_assets/kieran/d.png"
    zoom 0.70 yoffset 150
image russel e:
    "mod_assets/kieran/e.png"
    zoom 0.70 yoffset 150
image russel f:
    "mod_assets/kieran/f.png"
    zoom 0.70 yoffset 150
image russel g:
    "mod_assets/kieran/g.png"
    zoom 0.70 yoffset 150
image russel h:
    "mod_assets/kieran/h.png"
    zoom 0.70 yoffset 150
image russel i:
    "mod_assets/kieran/i.png"
    zoom 0.70 yoffset 150
image russel j:
    "mod_assets/kieran/j.png"
    zoom 0.70 yoffset 150
image russel k:
    "mod_assets/kieran/k.png"
    zoom 0.70 yoffset 150
image russel l:
    "mod_assets/kieran/l.png"
    zoom 0.70 yoffset 150



#  (shounen)
image josh a:
    "mod_assets/shounen/a.png"
    zoom 0.75 xoffset 50 yoffset 50
image josh b:
    "mod_assets/shounen/b.png"
    zoom 0.75 xoffset 50 yoffset 50
image josh c:
    "mod_assets/shounen/c.png"
    zoom 0.75 xoffset 50 yoffset 50
image josh d:
    "mod_assets/shounen/d.png"
    zoom 0.75 xoffset 50 yoffset 50
image josh e:
    "mod_assets/shounen/e.png"
    zoom 0.75 xoffset 50 yoffset 50
image josh f:
    "mod_assets/shounen/f.png"
    zoom 0.75 xoffset 50 yoffset 50
image josh g:
    "mod_assets/shounen/g.png"
    zoom 0.75 xoffset 50 yoffset 50
image josh h:
    "mod_assets/shounen/h.png"
    zoom 0.75 xoffset 50 yoffset 50
image josh i:
    "mod_assets/shounen/i.png"
    zoom 0.75 xoffset 50 yoffset 50





# Dr. Rivera (formal dadsuki) there's none yet
# image rivera 1a = im.Composite((960, 960), (0, 0), "rivera/1l.png", (0, 0), "rivera/1r.png", (0, 0), "rivera/a.png")

##### As of right now, I am missing sprites for Dr. Rivera.
##### Hopefully they should be available before the full release.
##### Also, no peeking!

##### meep is the best mod programmer in the entire universe


# Sayori
image sayori 1 = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/a.png")
image sayori 1a = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/a.png")
image sayori 1b = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/b.png")
image sayori 1c = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/c.png")
image sayori 1d = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/d.png")
image sayori 1e = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/e.png")
image sayori 1f = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/f.png")
image sayori 1g = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/g.png")
image sayori 1h = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/h.png")
image sayori 1i = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/i.png")
image sayori 1j = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/j.png")
image sayori 1k = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/k.png")
image sayori 1l = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/l.png")
image sayori 1m = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/m.png")
image sayori 1n = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/n.png")
image sayori 1o = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/o.png")
image sayori 1p = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/p.png")
image sayori 1q = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/q.png")
image sayori 1r = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/r.png")
image sayori 1s = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/s.png")
image sayori 1t = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/t.png")
image sayori 1u = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/u.png")
image sayori 1v = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/v.png")
image sayori 1w = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/w.png")
image sayori 1x = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/x.png")
image sayori 1y = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/y.png")

image sayori 2 = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/a.png")
image sayori 2a = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/a.png")
image sayori 2b = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/b.png")
image sayori 2c = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/c.png")
image sayori 2d = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/d.png")
image sayori 2e = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/e.png")
image sayori 2f = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/f.png")
image sayori 2g = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/g.png")
image sayori 2h = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/h.png")
image sayori 2i = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/i.png")
image sayori 2j = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/j.png")
image sayori 2k = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/k.png")
image sayori 2l = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/l.png")
image sayori 2m = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/m.png")
image sayori 2n = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/n.png")
image sayori 2o = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/o.png")
image sayori 2p = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/p.png")
image sayori 2q = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/q.png")
image sayori 2r = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/r.png")
image sayori 2s = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/s.png")
image sayori 2t = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/t.png")
image sayori 2u = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/u.png")
image sayori 2v = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/v.png")
image sayori 2w = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/w.png")
image sayori 2x = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/x.png")
image sayori 2y = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/y.png")

image sayori 3 = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/a.png")
image sayori 3a = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/a.png")
image sayori 3b = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/b.png")
image sayori 3c = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/c.png")
image sayori 3d = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/d.png")
image sayori 3e = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/e.png")
image sayori 3f = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/f.png")
image sayori 3g = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/g.png")
image sayori 3h = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/h.png")
image sayori 3i = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/i.png")
image sayori 3j = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/j.png")
image sayori 3k = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/k.png")
image sayori 3l = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/l.png")
image sayori 3m = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/m.png")
image sayori 3n = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/n.png")
image sayori 3o = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/o.png")
image sayori 3p = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/p.png")
image sayori 3q = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/q.png")
image sayori 3r = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/r.png")
image sayori 3s = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/s.png")
image sayori 3t = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/t.png")
image sayori 3u = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/u.png")
image sayori 3v = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/v.png")
image sayori 3w = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/w.png")
image sayori 3x = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/x.png")
image sayori 3y = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/y.png")

image sayori 4 = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/a.png")
image sayori 4a = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/a.png")
image sayori 4b = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/b.png")
image sayori 4c = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/c.png")
image sayori 4d = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/d.png")
image sayori 4e = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/e.png")
image sayori 4f = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/f.png")
image sayori 4g = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/g.png")
image sayori 4h = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/h.png")
image sayori 4i = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/i.png")
image sayori 4j = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/j.png")
image sayori 4k = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/k.png")
image sayori 4l = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/l.png")
image sayori 4m = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/m.png")
image sayori 4n = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/n.png")
image sayori 4o = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/o.png")
image sayori 4p = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/p.png")
image sayori 4q = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/q.png")
image sayori 4r = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/r.png")
image sayori 4s = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/s.png")
image sayori 4t = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/t.png")
image sayori 4u = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/u.png")
image sayori 4v = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/v.png")
image sayori 4w = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/w.png")
image sayori 4x = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/x.png")
image sayori 4y = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/y.png")

image sayori 5 = im.Composite((960, 960), (0, 0), "sayori/3a.png")
image sayori 5a = im.Composite((960, 960), (0, 0), "sayori/3a.png")
image sayori 5b = im.Composite((960, 960), (0, 0), "sayori/3b.png")
image sayori 5c = im.Composite((960, 960), (0, 0), "sayori/3c.png")
image sayori 5d = im.Composite((960, 960), (0, 0), "sayori/3d.png")

image sayori 1ba = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/a.png")
image sayori 1bb = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/b.png")
image sayori 1bc = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/c.png")
image sayori 1bd = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/d.png")
image sayori 1be = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/e.png")
image sayori 1bf = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/f.png")
image sayori 1bg = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/g.png")
image sayori 1bh = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/h.png")
image sayori 1bi = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/i.png")
image sayori 1bj = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/j.png")
image sayori 1bk = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/k.png")
image sayori 1bl = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/l.png")
image sayori 1bm = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/m.png")
image sayori 1bn = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/n.png")
image sayori 1bo = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/o.png")
image sayori 1bp = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/p.png")
image sayori 1bq = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/q.png")
image sayori 1br = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/r.png")
image sayori 1bs = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/s.png")
image sayori 1bt = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/t.png")
image sayori 1bu = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/u.png")
image sayori 1bv = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/v.png")
image sayori 1bw = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/w.png")
image sayori 1bx = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/x.png")
image sayori 1by = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/y.png")

image sayori 2ba = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/a.png")
image sayori 2bb = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/b.png")
image sayori 2bc = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/c.png")
image sayori 2bd = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/d.png")
image sayori 2be = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/e.png")
image sayori 2bf = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/f.png")
image sayori 2bg = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/g.png")
image sayori 2bh = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/h.png")
image sayori 2bi = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/i.png")
image sayori 2bj = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/j.png")
image sayori 2bk = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/k.png")
image sayori 2bl = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/l.png")
image sayori 2bm = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/m.png")
image sayori 2bn = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/n.png")
image sayori 2bo = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/o.png")
image sayori 2bp = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/p.png")
image sayori 2bq = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/q.png")
image sayori 2br = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/r.png")
image sayori 2bs = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/s.png")
image sayori 2bt = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/t.png")
image sayori 2bu = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/u.png")
image sayori 2bv = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/v.png")
image sayori 2bw = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/w.png")
image sayori 2bx = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/x.png")
image sayori 2by = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/y.png")

image sayori 3ba = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/a.png")
image sayori 3bb = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/b.png")
image sayori 3bc = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/c.png")
image sayori 3bd = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/d.png")
image sayori 3be = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/e.png")
image sayori 3bf = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/f.png")
image sayori 3bg = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/g.png")
image sayori 3bh = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/h.png")
image sayori 3bi = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/i.png")
image sayori 3bj = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/j.png")
image sayori 3bk = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/k.png")
image sayori 3bl = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/l.png")
image sayori 3bm = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/m.png")
image sayori 3bn = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/n.png")
image sayori 3bo = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/o.png")
image sayori 3bp = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/p.png")
image sayori 3bq = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/q.png")
image sayori 3br = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/r.png")
image sayori 3bs = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/s.png")
image sayori 3bt = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/t.png")
image sayori 3bu = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/u.png")
image sayori 3bv = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/v.png")
image sayori 3bw = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/w.png")
image sayori 3bx = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/x.png")
image sayori 3by = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/y.png")

image sayori 4ba = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/a.png")
image sayori 4bb = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/b.png")
image sayori 4bc = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/c.png")
image sayori 4bd = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/d.png")
image sayori 4be = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/e.png")
image sayori 4bf = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/f.png")
image sayori 4bg = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/g.png")
image sayori 4bh = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/h.png")
image sayori 4bi = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/i.png")
image sayori 4bj = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/j.png")
image sayori 4bk = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/k.png")
image sayori 4bl = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/l.png")
image sayori 4bm = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/m.png")
image sayori 4bn = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/n.png")
image sayori 4bo = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/o.png")
image sayori 4bp = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/p.png")
image sayori 4bq = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/q.png")
image sayori 4br = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/r.png")
image sayori 4bs = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/s.png")
image sayori 4bt = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/t.png")
image sayori 4bu = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/u.png")
image sayori 4bv = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/v.png")
image sayori 4bw = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/w.png")
image sayori 4bx = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/x.png")
image sayori 4by = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/y.png")

image sayori glitch:
    "sayori/glitch1.png"
    pause 0.01666
    "sayori/glitch2.png"
    pause 0.01666
    repeat




# Natsuki
image natsuki 11 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/1t.png")
image natsuki 1a = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/a.png")
image natsuki 1b = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/b.png")
image natsuki 1c = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/c.png")
image natsuki 1d = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/d.png")
image natsuki 1e = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/e.png")
image natsuki 1f = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/f.png")
image natsuki 1g = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/g.png")
image natsuki 1h = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/h.png")
image natsuki 1i = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/i.png")
image natsuki 1j = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/j.png")
image natsuki 1k = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/k.png")
image natsuki 1l = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/l.png")
image natsuki 1m = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/m.png")
image natsuki 1n = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/n.png")
image natsuki 1o = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/o.png")
image natsuki 1p = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/p.png")
image natsuki 1q = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/q.png")
image natsuki 1r = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/r.png")
image natsuki 1s = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/s.png")
image natsuki 1t = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/t.png")
image natsuki 1u = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/u.png")
image natsuki 1v = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/v.png")
image natsuki 1w = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/w.png")
image natsuki 1x = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/x.png")
image natsuki 1y = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/y.png")
image natsuki 1z = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/z.png")

image natsuki 21 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/1t.png")
image natsuki 2a = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/a.png")
image natsuki 2b = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/b.png")
image natsuki 2c = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/c.png")
image natsuki 2d = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/d.png")
image natsuki 2e = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/e.png")
image natsuki 2f = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/f.png")
image natsuki 2g = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/g.png")
image natsuki 2h = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/h.png")
image natsuki 2i = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/i.png")
image natsuki 2j = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/j.png")
image natsuki 2k = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/k.png")
image natsuki 2l = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/l.png")
image natsuki 2m = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/m.png")
image natsuki 2n = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/n.png")
image natsuki 2o = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/o.png")
image natsuki 2p = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/p.png")
image natsuki 2q = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/q.png")
image natsuki 2r = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/r.png")
image natsuki 2s = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/s.png")
image natsuki 2t = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/t.png")
image natsuki 2u = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/u.png")
image natsuki 2v = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/v.png")
image natsuki 2w = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/w.png")
image natsuki 2x = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/x.png")
image natsuki 2y = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/y.png")
image natsuki 2z = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/z.png")

image natsuki 31 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/1t.png")
image natsuki 3a = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/a.png")
image natsuki 3b = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/b.png")
image natsuki 3c = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/c.png")
image natsuki 3d = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/d.png")
image natsuki 3e = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/e.png")
image natsuki 3f = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/f.png")
image natsuki 3g = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/g.png")
image natsuki 3h = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/h.png")
image natsuki 3i = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/i.png")
image natsuki 3j = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/j.png")
image natsuki 3k = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/k.png")
image natsuki 3l = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/l.png")
image natsuki 3m = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/m.png")
image natsuki 3n = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/n.png")
image natsuki 3o = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/o.png")
image natsuki 3p = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/p.png")
image natsuki 3q = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/q.png")
image natsuki 3r = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/r.png")
image natsuki 3s = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/s.png")
image natsuki 3t = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/t.png")
image natsuki 3u = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/u.png")
image natsuki 3v = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/v.png")
image natsuki 3w = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/w.png")
image natsuki 3x = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/x.png")
image natsuki 3y = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/y.png")
image natsuki 3z = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/z.png")

image natsuki 41 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/1t.png")
image natsuki 4a = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/a.png")
image natsuki 4b = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/b.png")
image natsuki 4c = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/c.png")
image natsuki 4d = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/d.png")
image natsuki 4e = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/e.png")
image natsuki 4f = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/f.png")
image natsuki 4g = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/g.png")
image natsuki 4h = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/h.png")
image natsuki 4i = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/i.png")
image natsuki 4j = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/j.png")
image natsuki 4k = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/k.png")
image natsuki 4l = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/l.png")
image natsuki 4m = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/m.png")
image natsuki 4n = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/n.png")
image natsuki 4o = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/o.png")
image natsuki 4p = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/p.png")
image natsuki 4q = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/q.png")
image natsuki 4r = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/r.png")
image natsuki 4s = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/s.png")
image natsuki 4t = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/t.png")
image natsuki 4u = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/u.png")
image natsuki 4v = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/v.png")
image natsuki 4w = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/w.png")
image natsuki 4x = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/x.png")
image natsuki 4y = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/y.png")
image natsuki 4z = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/z.png")

image natsuki 12 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2t.png")
image natsuki 12a = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2ta.png")
image natsuki 12b = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2tb.png")
image natsuki 12c = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2tc.png")
image natsuki 12d = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2td.png")
image natsuki 12e = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2te.png")
image natsuki 12f = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2tf.png")
image natsuki 12g = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2tg.png")
image natsuki 12h = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2th.png")
image natsuki 12i = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2ti.png")

image natsuki 42 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2t.png")
image natsuki 42a = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2ta.png")
image natsuki 42b = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2tb.png")
image natsuki 42c = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2tc.png")
image natsuki 42d = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2td.png")
image natsuki 42e = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2te.png")
image natsuki 42f = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2tf.png")
image natsuki 42g = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2tg.png")
image natsuki 42h = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2th.png")
image natsuki 42i = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2ti.png")

image natsuki 51 = im.Composite((960, 960), (18, 22), "natsuki/1t.png", (0, 0), "natsuki/3.png")
image natsuki 5a = im.Composite((960, 960), (18, 22), "natsuki/a.png", (0, 0), "natsuki/3.png")
image natsuki 5b = im.Composite((960, 960), (18, 22), "natsuki/b.png", (0, 0), "natsuki/3.png")
image natsuki 5c = im.Composite((960, 960), (18, 22), "natsuki/c.png", (0, 0), "natsuki/3.png")
image natsuki 5d = im.Composite((960, 960), (18, 22), "natsuki/d.png", (0, 0), "natsuki/3.png")
image natsuki 5e = im.Composite((960, 960), (18, 22), "natsuki/e.png", (0, 0), "natsuki/3.png")
image natsuki 5f = im.Composite((960, 960), (18, 22), "natsuki/f.png", (0, 0), "natsuki/3.png")
image natsuki 5g = im.Composite((960, 960), (18, 22), "natsuki/g.png", (0, 0), "natsuki/3.png")
image natsuki 5h = im.Composite((960, 960), (18, 22), "natsuki/h.png", (0, 0), "natsuki/3.png")
image natsuki 5i = im.Composite((960, 960), (18, 22), "natsuki/i.png", (0, 0), "natsuki/3.png")
image natsuki 5j = im.Composite((960, 960), (18, 22), "natsuki/j.png", (0, 0), "natsuki/3.png")
image natsuki 5k = im.Composite((960, 960), (18, 22), "natsuki/k.png", (0, 0), "natsuki/3.png")
image natsuki 5l = im.Composite((960, 960), (18, 22), "natsuki/l.png", (0, 0), "natsuki/3.png")
image natsuki 5m = im.Composite((960, 960), (18, 22), "natsuki/m.png", (0, 0), "natsuki/3.png")
image natsuki 5n = im.Composite((960, 960), (18, 22), "natsuki/n.png", (0, 0), "natsuki/3.png")
image natsuki 5o = im.Composite((960, 960), (18, 22), "natsuki/o.png", (0, 0), "natsuki/3.png")
image natsuki 5p = im.Composite((960, 960), (18, 22), "natsuki/p.png", (0, 0), "natsuki/3.png")
image natsuki 5q = im.Composite((960, 960), (18, 22), "natsuki/q.png", (0, 0), "natsuki/3.png")
image natsuki 5r = im.Composite((960, 960), (18, 22), "natsuki/r.png", (0, 0), "natsuki/3.png")
image natsuki 5s = im.Composite((960, 960), (18, 22), "natsuki/s.png", (0, 0), "natsuki/3.png")
image natsuki 5t = im.Composite((960, 960), (18, 22), "natsuki/t.png", (0, 0), "natsuki/3.png")
image natsuki 5u = im.Composite((960, 960), (18, 22), "natsuki/u.png", (0, 0), "natsuki/3.png")
image natsuki 5v = im.Composite((960, 960), (18, 22), "natsuki/v.png", (0, 0), "natsuki/3.png")
image natsuki 5w = im.Composite((960, 960), (18, 22), "natsuki/w.png", (0, 0), "natsuki/3.png")
image natsuki 5x = im.Composite((960, 960), (18, 22), "natsuki/x.png", (0, 0), "natsuki/3.png")
image natsuki 5y = im.Composite((960, 960), (18, 22), "natsuki/y.png", (0, 0), "natsuki/3.png")
image natsuki 5z = im.Composite((960, 960), (18, 22), "natsuki/z.png", (0, 0), "natsuki/3.png")
#image natsuki 52 = im.Composite((960, 960), (0, 0), "natsuki/3.png", (0, 0), "natsuki/4t.png")

image natsuki 1ba = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/a.png")
image natsuki 1bb = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/b.png")
image natsuki 1bc = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/c.png")
image natsuki 1bd = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/d.png")
image natsuki 1be = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/e.png")
image natsuki 1bf = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/f.png")
image natsuki 1bg = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/g.png")
image natsuki 1bh = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/h.png")
image natsuki 1bi = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/i.png")
image natsuki 1bj = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/j.png")
image natsuki 1bk = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/k.png")
image natsuki 1bl = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/l.png")
image natsuki 1bm = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/m.png")
image natsuki 1bn = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/n.png")
image natsuki 1bo = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/o.png")
image natsuki 1bp = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/p.png")
image natsuki 1bq = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/q.png")
image natsuki 1br = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/r.png")
image natsuki 1bs = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/s.png")
image natsuki 1bt = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/t.png")
image natsuki 1bu = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/u.png")
image natsuki 1bv = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/v.png")
image natsuki 1bw = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/w.png")
image natsuki 1bx = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/x.png")
image natsuki 1by = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/y.png")
image natsuki 1bz = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/z.png")

image natsuki 2ba = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/a.png")
image natsuki 2bb = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/b.png")
image natsuki 2bc = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/c.png")
image natsuki 2bd = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/d.png")
image natsuki 2be = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/e.png")
image natsuki 2bf = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/f.png")
image natsuki 2bg = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/g.png")
image natsuki 2bh = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/h.png")
image natsuki 2bi = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/i.png")
image natsuki 2bj = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/j.png")
image natsuki 2bk = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/k.png")
image natsuki 2bl = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/l.png")
image natsuki 2bm = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/m.png")
image natsuki 2bn = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/n.png")
image natsuki 2bo = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/o.png")
image natsuki 2bp = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/p.png")
image natsuki 2bq = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/q.png")
image natsuki 2br = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/r.png")
image natsuki 2bs = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/s.png")
image natsuki 2bt = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/t.png")
image natsuki 2bu = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/u.png")
image natsuki 2bv = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/v.png")
image natsuki 2bw = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/w.png")
image natsuki 2bx = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/x.png")
image natsuki 2by = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/y.png")
image natsuki 2bz = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/z.png")

image natsuki 3ba = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/a.png")
image natsuki 3bb = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/b.png")
image natsuki 3bc = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/c.png")
image natsuki 3bd = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/d.png")
image natsuki 3be = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/e.png")
image natsuki 3bf = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/f.png")
image natsuki 3bg = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/g.png")
image natsuki 3bh = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/h.png")
image natsuki 3bi = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/i.png")
image natsuki 3bj = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/j.png")
image natsuki 3bk = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/k.png")
image natsuki 3bl = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/l.png")
image natsuki 3bm = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/m.png")
image natsuki 3bn = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/n.png")
image natsuki 3bo = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/o.png")
image natsuki 3bp = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/p.png")
image natsuki 3bq = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/q.png")
image natsuki 3br = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/r.png")
image natsuki 3bs = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/s.png")
image natsuki 3bt = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/t.png")
image natsuki 3bu = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/u.png")
image natsuki 3bv = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/v.png")
image natsuki 3bw = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/w.png")
image natsuki 3bx = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/x.png")
image natsuki 3by = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/y.png")
image natsuki 3bz = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/z.png")

image natsuki 4ba = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/a.png")
image natsuki 4bb = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/b.png")
image natsuki 4bc = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/c.png")
image natsuki 4bd = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/d.png")
image natsuki 4be = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/e.png")
image natsuki 4bf = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/f.png")
image natsuki 4bg = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/g.png")
image natsuki 4bh = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/h.png")
image natsuki 4bi = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/i.png")
image natsuki 4bj = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/j.png")
image natsuki 4bk = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/k.png")
image natsuki 4bl = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/l.png")
image natsuki 4bm = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/m.png")
image natsuki 4bn = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/n.png")
image natsuki 4bo = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/o.png")
image natsuki 4bp = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/p.png")
image natsuki 4bq = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/q.png")
image natsuki 4br = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/r.png")
image natsuki 4bs = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/s.png")
image natsuki 4bt = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/t.png")
image natsuki 4bu = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/u.png")
image natsuki 4bv = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/v.png")
image natsuki 4bw = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/w.png")
image natsuki 4bx = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/x.png")
image natsuki 4by = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/y.png")
image natsuki 4bz = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/z.png")

image natsuki 12ba = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2bta.png")
image natsuki 12bb = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2btb.png")
image natsuki 12bc = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2btc.png")
image natsuki 12bd = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2btd.png")
image natsuki 12be = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2bte.png")
image natsuki 12bf = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2btf.png")
image natsuki 12bg = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2btg.png")
image natsuki 12bh = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2bth.png")
image natsuki 12bi = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2bti.png")

image natsuki 42ba = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2bta.png")
image natsuki 42bb = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2btb.png")
image natsuki 42bc = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2btc.png")
image natsuki 42bd = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2btd.png")
image natsuki 42be = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2bte.png")
image natsuki 42bf = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2btf.png")
image natsuki 42bg = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2btg.png")
image natsuki 42bh = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2bth.png")
image natsuki 42bi = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2bti.png")

image natsuki 5ba = im.Composite((960, 960), (18, 22), "natsuki/a.png", (0, 0), "natsuki/3b.png")
image natsuki 5bb = im.Composite((960, 960), (18, 22), "natsuki/b.png", (0, 0), "natsuki/3b.png")
image natsuki 5bc = im.Composite((960, 960), (18, 22), "natsuki/c.png", (0, 0), "natsuki/3b.png")
image natsuki 5bd = im.Composite((960, 960), (18, 22), "natsuki/d.png", (0, 0), "natsuki/3b.png")
image natsuki 5be = im.Composite((960, 960), (18, 22), "natsuki/e.png", (0, 0), "natsuki/3b.png")
image natsuki 5bf = im.Composite((960, 960), (18, 22), "natsuki/f.png", (0, 0), "natsuki/3b.png")
image natsuki 5bg = im.Composite((960, 960), (18, 22), "natsuki/g.png", (0, 0), "natsuki/3b.png")
image natsuki 5bh = im.Composite((960, 960), (18, 22), "natsuki/h.png", (0, 0), "natsuki/3b.png")
image natsuki 5bi = im.Composite((960, 960), (18, 22), "natsuki/i.png", (0, 0), "natsuki/3b.png")
image natsuki 5bj = im.Composite((960, 960), (18, 22), "natsuki/j.png", (0, 0), "natsuki/3b.png")
image natsuki 5bk = im.Composite((960, 960), (18, 22), "natsuki/k.png", (0, 0), "natsuki/3b.png")
image natsuki 5bl = im.Composite((960, 960), (18, 22), "natsuki/l.png", (0, 0), "natsuki/3b.png")
image natsuki 5bm = im.Composite((960, 960), (18, 22), "natsuki/m.png", (0, 0), "natsuki/3b.png")
image natsuki 5bn = im.Composite((960, 960), (18, 22), "natsuki/n.png", (0, 0), "natsuki/3b.png")
image natsuki 5bo = im.Composite((960, 960), (18, 22), "natsuki/o.png", (0, 0), "natsuki/3b.png")
image natsuki 5bp = im.Composite((960, 960), (18, 22), "natsuki/p.png", (0, 0), "natsuki/3b.png")
image natsuki 5bq = im.Composite((960, 960), (18, 22), "natsuki/q.png", (0, 0), "natsuki/3b.png")
image natsuki 5br = im.Composite((960, 960), (18, 22), "natsuki/r.png", (0, 0), "natsuki/3b.png")
image natsuki 5bs = im.Composite((960, 960), (18, 22), "natsuki/s.png", (0, 0), "natsuki/3b.png")
image natsuki 5bt = im.Composite((960, 960), (18, 22), "natsuki/t.png", (0, 0), "natsuki/3b.png")
image natsuki 5bu = im.Composite((960, 960), (18, 22), "natsuki/u.png", (0, 0), "natsuki/3b.png")
image natsuki 5bv = im.Composite((960, 960), (18, 22), "natsuki/v.png", (0, 0), "natsuki/3b.png")
image natsuki 5bw = im.Composite((960, 960), (18, 22), "natsuki/w.png", (0, 0), "natsuki/3b.png")
image natsuki 5bx = im.Composite((960, 960), (18, 22), "natsuki/x.png", (0, 0), "natsuki/3b.png")
image natsuki 5by = im.Composite((960, 960), (18, 22), "natsuki/y.png", (0, 0), "natsuki/3b.png")
image natsuki 5bz = im.Composite((960, 960), (18, 22), "natsuki/z.png", (0, 0), "natsuki/3b.png")

# Natsuki legacy
image natsuki 1 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/1t.png")
image natsuki 2 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/1t.png")
image natsuki 3 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/1t.png")
image natsuki 4 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/1t.png")
image natsuki 5 = im.Composite((960, 960), (18, 22), "natsuki/1t.png", (0, 0), "natsuki/3.png")

image natsuki mouth = LiveComposite((960, 960), (0, 0), "natsuki/0.png", (390, 340), "n_rects_mouth", (480, 334), "n_rects_mouth")

image n_rects_mouth:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    size (20, 25)

image n_moving_mouth:
    "images/natsuki/mouth.png"
    pos (615, 305)
    xanchor 0.5 yanchor 0.5
    parallel:
        choice:
            ease 0.10 yzoom 0.2
        choice:
            ease 0.05 yzoom 0.2
        choice:
            ease 0.075 yzoom 0.2
        pass
        choice:
            0.02
        choice:
            0.04
        choice:
            0.06
        choice:
            0.08
        pass
        choice:
            ease 0.10 yzoom 1
        choice:
            ease 0.05 yzoom 1
        choice:
            ease 0.075 yzoom 1
        pass
        choice:
            0.02
        choice:
            0.04
        choice:
            0.06
        choice:
            0.08
        repeat
    parallel:
        choice:
            0.2
        choice:
            0.4
        choice:
            0.6
        ease 0.2 xzoom 0.4
        ease 0.2 xzoom 0.8
        repeat

image natsuki_ghost_blood:
    "#00000000"
    "natsuki/ghost_blood.png" with ImageDissolve("images/menu/wipedown.png", 80.0, ramplen=4, alpha=True)
    pos (620,320) zoom 0.80

image natsuki ghost_base:
    "natsuki/ghost1.png"
image natsuki ghost1:
    "natsuki 11"
    "natsuki ghost_base" with Dissolve(20.0, alpha=True)
image natsuki ghost2 = Image("natsuki/ghost2.png")
image natsuki ghost3 = Image("natsuki/ghost3.png")
image natsuki ghost4:
    "natsuki ghost3"
    parallel:
        easeout 0.25 zoom 4.5 yoffset 1200
    parallel:
        ease 0.025 xoffset -20
        ease 0.025 xoffset 20
        repeat
    0.25
    "black"
image natsuki glitch1:
    "natsuki/glitch1.png"
    zoom 1.25
    block:
        yoffset 300 xoffset 100 ytile 2
        linear 0.15 yoffset 200
        repeat
    time 0.75
    yoffset 0 zoom 1 xoffset 0 ytile 1
    "natsuki 4e"

image natsuki scream = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/scream.png")
image natsuki vomit = "natsuki/vomit.png"

image n_blackeyes = "images/natsuki/blackeyes.png"
image n_eye = "images/natsuki/eye.png"






# Yuri
image yuri 1 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/a.png")
image yuri 2 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/a.png")
image yuri 3 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/a.png")
image yuri 4 = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/a2.png")

image yuri 1a = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/a.png")
image yuri 1b = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/b.png")
image yuri 1c = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/c.png")
image yuri 1d = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/d.png")
image yuri 1e = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/e.png")
image yuri 1f = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/f.png")
image yuri 1g = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/g.png")
image yuri 1h = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/h.png")
image yuri 1i = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/i.png")
image yuri 1j = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/j.png")
image yuri 1k = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/k.png")
image yuri 1l = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/l.png")
image yuri 1m = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/m.png")
image yuri 1n = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/n.png")
image yuri 1o = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/o.png")
image yuri 1p = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/p.png")
image yuri 1q = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/q.png")
image yuri 1r = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/r.png")
image yuri 1s = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/s.png")
image yuri 1t = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/t.png")
image yuri 1u = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/u.png")
image yuri 1v = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/v.png")
image yuri 1w = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/w.png")

image yuri 1y1 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y1.png")
image yuri 1y2 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y2.png")
image yuri 1y3 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y3.png")
image yuri 1y4 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y4.png")
image yuri 1y5 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y5.png")
image yuri 1y6 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y6.png")
image yuri 1y7 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y7.png")

image yuri 2a = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/a.png")
image yuri 2b = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/b.png")
image yuri 2c = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/c.png")
image yuri 2d = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/d.png")
image yuri 2e = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/e.png")
image yuri 2f = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/f.png")
image yuri 2g = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/g.png")
image yuri 2h = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/h.png")
image yuri 2i = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/i.png")
image yuri 2j = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/j.png")
image yuri 2k = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/k.png")
image yuri 2l = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/l.png")
image yuri 2m = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/m.png")
image yuri 2n = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/n.png")
image yuri 2o = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/o.png")
image yuri 2p = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/p.png")
image yuri 2q = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/q.png")
image yuri 2r = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/r.png")
image yuri 2s = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/s.png")
image yuri 2t = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/t.png")
image yuri 2u = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/u.png")
image yuri 2v = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/v.png")
image yuri 2w = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/w.png")

image yuri 2y1 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y1.png")
image yuri 2y2 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y2.png")
image yuri 2y3 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y3.png")
image yuri 2y4 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y4.png")
image yuri 2y5 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y5.png")
image yuri 2y6 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y6.png")
image yuri 2y7 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y7.png")

image yuri 3a = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/a.png")
image yuri 3b = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/b.png")
image yuri 3c = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/c.png")
image yuri 3d = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/d.png")
image yuri 3e = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/e.png")
image yuri 3f = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/f.png")
image yuri 3g = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/g.png")
image yuri 3h = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/h.png")
image yuri 3i = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/i.png")
image yuri 3j = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/j.png")
image yuri 3k = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/k.png")
image yuri 3l = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/l.png")
image yuri 3m = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/m.png")
image yuri 3n = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/n.png")
image yuri 3o = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/o.png")
image yuri 3p = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/p.png")
image yuri 3q = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/q.png")
image yuri 3r = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/r.png")
image yuri 3s = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/s.png")
image yuri 3t = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/t.png")
image yuri 3u = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/u.png")
image yuri 3v = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/v.png")
image yuri 3w = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/w.png")

image yuri 3y1 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y1.png")
image yuri 3y2 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y2.png")
image yuri 3y3 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y3.png")
image yuri 3y4 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y4.png")
image yuri 3y5 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y5.png")
image yuri 3y6 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y6.png")
image yuri 3y7 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y7.png")

image yuri 4a = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/a2.png")
image yuri 4b = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/b2.png")
image yuri 4c = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/c2.png")
image yuri 4d = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/d2.png")
image yuri 4e = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/e2.png")

image yuri 1ba = im.Composite((960, 960), (0, 0), "yuri/a.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bb = im.Composite((960, 960), (0, 0), "yuri/b.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bc = im.Composite((960, 960), (0, 0), "yuri/c.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bd = im.Composite((960, 960), (0, 0), "yuri/d.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1be = im.Composite((960, 960), (0, 0), "yuri/e.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bf = im.Composite((960, 960), (0, 0), "yuri/f.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bg = im.Composite((960, 960), (0, 0), "yuri/g.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bh = im.Composite((960, 960), (0, 0), "yuri/h.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bi = im.Composite((960, 960), (0, 0), "yuri/i.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bj = im.Composite((960, 960), (0, 0), "yuri/j.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bk = im.Composite((960, 960), (0, 0), "yuri/k.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bl = im.Composite((960, 960), (0, 0), "yuri/l.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bm = im.Composite((960, 960), (0, 0), "yuri/m.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bn = im.Composite((960, 960), (0, 0), "yuri/n.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bo = im.Composite((960, 960), (0, 0), "yuri/o.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bp = im.Composite((960, 960), (0, 0), "yuri/p.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bq = im.Composite((960, 960), (0, 0), "yuri/q.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1br = im.Composite((960, 960), (0, 0), "yuri/r.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bs = im.Composite((960, 960), (0, 0), "yuri/s.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bt = im.Composite((960, 960), (0, 0), "yuri/t.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bu = im.Composite((960, 960), (0, 0), "yuri/u.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bv = im.Composite((960, 960), (0, 0), "yuri/v.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bw = im.Composite((960, 960), (0, 0), "yuri/w.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")

image yuri 2ba = im.Composite((960, 960), (0, 0), "yuri/a.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bb = im.Composite((960, 960), (0, 0), "yuri/b.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bc = im.Composite((960, 960), (0, 0), "yuri/c.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bd = im.Composite((960, 960), (0, 0), "yuri/d.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2be = im.Composite((960, 960), (0, 0), "yuri/e.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bf = im.Composite((960, 960), (0, 0), "yuri/f.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bg = im.Composite((960, 960), (0, 0), "yuri/g.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bh = im.Composite((960, 960), (0, 0), "yuri/h.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bi = im.Composite((960, 960), (0, 0), "yuri/i.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bj = im.Composite((960, 960), (0, 0), "yuri/j.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bk = im.Composite((960, 960), (0, 0), "yuri/k.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bl = im.Composite((960, 960), (0, 0), "yuri/l.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bm = im.Composite((960, 960), (0, 0), "yuri/m.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bn = im.Composite((960, 960), (0, 0), "yuri/n.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bo = im.Composite((960, 960), (0, 0), "yuri/o.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bp = im.Composite((960, 960), (0, 0), "yuri/p.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bq = im.Composite((960, 960), (0, 0), "yuri/q.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2br = im.Composite((960, 960), (0, 0), "yuri/r.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bs = im.Composite((960, 960), (0, 0), "yuri/s.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bt = im.Composite((960, 960), (0, 0), "yuri/t.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bu = im.Composite((960, 960), (0, 0), "yuri/u.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bv = im.Composite((960, 960), (0, 0), "yuri/v.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bw = im.Composite((960, 960), (0, 0), "yuri/w.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")

image yuri 3ba = im.Composite((960, 960), (0, 0), "yuri/a.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bb = im.Composite((960, 960), (0, 0), "yuri/b.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bc = im.Composite((960, 960), (0, 0), "yuri/c.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bd = im.Composite((960, 960), (0, 0), "yuri/d.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3be = im.Composite((960, 960), (0, 0), "yuri/e.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bf = im.Composite((960, 960), (0, 0), "yuri/f.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bg = im.Composite((960, 960), (0, 0), "yuri/g.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bh = im.Composite((960, 960), (0, 0), "yuri/h.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bi = im.Composite((960, 960), (0, 0), "yuri/i.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bj = im.Composite((960, 960), (0, 0), "yuri/j.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bk = im.Composite((960, 960), (0, 0), "yuri/k.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bl = im.Composite((960, 960), (0, 0), "yuri/l.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bm = im.Composite((960, 960), (0, 0), "yuri/m.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bn = im.Composite((960, 960), (0, 0), "yuri/n.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bo = im.Composite((960, 960), (0, 0), "yuri/o.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bp = im.Composite((960, 960), (0, 0), "yuri/p.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bq = im.Composite((960, 960), (0, 0), "yuri/q.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3br = im.Composite((960, 960), (0, 0), "yuri/r.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bs = im.Composite((960, 960), (0, 0), "yuri/s.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bt = im.Composite((960, 960), (0, 0), "yuri/t.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bu = im.Composite((960, 960), (0, 0), "yuri/u.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bv = im.Composite((960, 960), (0, 0), "yuri/v.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bw = im.Composite((960, 960), (0, 0), "yuri/w.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")

image yuri 4ba = im.Composite((960, 960), (0, 0), "yuri/a2.png", (0, 0), "yuri/3b.png")
image yuri 4bb = im.Composite((960, 960), (0, 0), "yuri/b2.png", (0, 0), "yuri/3b.png")
image yuri 4bc = im.Composite((960, 960), (0, 0), "yuri/c2.png", (0, 0), "yuri/3b.png")
image yuri 4bd = im.Composite((960, 960), (0, 0), "yuri/d2.png", (0, 0), "yuri/3b.png")
image yuri 4be = im.Composite((960, 960), (0, 0), "yuri/e2.png", (0, 0), "yuri/3b.png")

image y_glitch_head:
    "images/yuri/za.png"
    0.15
    "images/yuri/zb.png"
    0.15
    "images/yuri/zc.png"
    0.15
    "images/yuri/zd.png"
    0.15
    repeat

image yuri stab_1 = "yuri/stab/1.png"
image yuri stab_2 = "yuri/stab/2.png"
image yuri stab_3 = "yuri/stab/3.png"
image yuri stab_4 = "yuri/stab/4.png"
image yuri stab_5 = "yuri/stab/5.png"
image yuri stab_6 = LiveComposite((960,960), (0, 0), "yuri/stab/6-mask.png", (0, 0), "yuri stab_6_eyes", (0, 0), "yuri/stab/6.png")

image yuri stab_6_eyes:
    "yuri/stab/6-eyes.png"
    subpixel True
    parallel:
        choice:
            xoffset 0.5
        choice:
            xoffset 0
        choice:
            xoffset -0.5
        0.2
        repeat
    parallel:
        choice:
            yoffset 0.5
        choice:
            yoffset 0
        choice:
            yoffset -0.5
        0.2
        repeat
    parallel:
        2.05
        easeout 1.0 yoffset -15
        linear 10 yoffset -15


image yuri oneeye = LiveComposite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/oneeye.png", (0, 0), "yuri oneeye2")
image yuri oneeye2:
    "yuri/oneeye2.png"
    subpixel True
    pause 5.0
    linear 60 xoffset -50 yoffset 20

image yuri glitch:
    "yuri/glitch1.png"
    pause 0.1
    "yuri/glitch2.png"
    pause 0.1
    "yuri/glitch3.png"
    pause 0.1
    "yuri/glitch4.png"
    pause 0.1
    "yuri/glitch5.png"
    pause 0.1
    repeat
image yuri glitch2:
    "yuri/0a.png"
    pause 0.1
    "yuri/0b.png"
    pause 0.5
    "yuri/0a.png"
    pause 0.3
    "yuri/0b.png"
    pause 0.3
    "yuri 1"

image yuri eyes = LiveComposite((1280, 720), (0, 0), "yuri/eyes1.png", (0, 0), "yuripupils")

image yuri eyes_base = "yuri/eyes1.png"

image yuripupils:
    "yuri/eyes2.png"
    yuripupils_move

image yuri cuts = "yuri/cuts.png"

image yuri dragon:
    "yuri 3"
    0.25
    parallel:
        "yuri/dragon1.png"
        0.01
        "yuri/dragon2.png"
        0.01
        repeat
    parallel:
        0.01
        choice:
            xoffset -1
            xoffset -2
            xoffset -5
            xoffset -6
            xoffset -9
            xoffset -10
        0.01
        xoffset 0
        repeat
    time 0.55
    xoffset 0
    "yuri 3"





#------------------------------------------------Our beloved Monika only has her school uniform here, but that can change!

# Just Monika
image monika 1 = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/a.png")
image monika 2 = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/a.png")
image monika 3 = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/a.png")
image monika 4 = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/a.png")
image monika 5 = im.Composite((960, 960), (0, 0), "monika/3a.png")

image monika 1a = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/a.png")
image monika 1b = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/b.png")
image monika 1c = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/c.png")
image monika 1d = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/d.png")
image monika 1e = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/e.png")
image monika 1f = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/f.png")
image monika 1g = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/g.png")
image monika 1h = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/h.png")
image monika 1i = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/i.png")
image monika 1j = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/j.png")
image monika 1k = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/k.png")
image monika 1l = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/l.png")
image monika 1m = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/m.png")
image monika 1n = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/n.png")
image monika 1o = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/o.png")
image monika 1p = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/p.png")
image monika 1q = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/q.png")
image monika 1r = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/r.png")

image monika 2a = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/a.png")
image monika 2b = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/b.png")
image monika 2c = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/c.png")
image monika 2d = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/d.png")
image monika 2e = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/e.png")
image monika 2f = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/f.png")
image monika 2g = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/g.png")
image monika 2h = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/h.png")
image monika 2i = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/i.png")
image monika 2j = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/j.png")
image monika 2k = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/k.png")
image monika 2l = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/l.png")
image monika 2m = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/m.png")
image monika 2n = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/n.png")
image monika 2o = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/o.png")
image monika 2p = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/p.png")
image monika 2q = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/q.png")
image monika 2r = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/r.png")

image monika 3a = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/a.png")
image monika 3b = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/b.png")
image monika 3c = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/c.png")
image monika 3d = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/d.png")
image monika 3e = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/e.png")
image monika 3f = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/f.png")
image monika 3g = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/g.png")
image monika 3h = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/h.png")
image monika 3i = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/i.png")
image monika 3j = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/j.png")
image monika 3k = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/k.png")
image monika 3l = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/l.png")
image monika 3m = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/m.png")
image monika 3n = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/n.png")
image monika 3o = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/o.png")
image monika 3p = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/p.png")
image monika 3q = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/q.png")
image monika 3r = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/r.png")

image monika 4a = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/a.png")
image monika 4b = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/b.png")
image monika 4c = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/c.png")
image monika 4d = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/d.png")
image monika 4e = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/e.png")
image monika 4f = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/f.png")
image monika 4g = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/g.png")
image monika 4h = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/h.png")
image monika 4i = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/i.png")
image monika 4j = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/j.png")
image monika 4k = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/k.png")
image monika 4l = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/l.png")
image monika 4m = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/m.png")
image monika 4n = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/n.png")
image monika 4o = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/o.png")
image monika 4p = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/p.png")
image monika 4q = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/q.png")
image monika 4r = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/r.png")

# custom bending expression, then custom Monika outfit, tucked and untucked

image monika 6a = im.Composite((960, 960), (0, 0), "mod_assets/mcas/ca.png")
image monika 6b = im.Composite((960, 960), (0, 0), "mod_assets/mcas/cb.png")
image monika 6c = im.Composite((960, 960), (0, 0), "mod_assets/mcas/cc.png")
image monika 6d = im.Composite((960, 960), (0, 0), "mod_assets/mcas/cd.png")
image monika 6e = im.Composite((960, 960), (0, 0), "mod_assets/mcas/ce.png")

image monika 7a = im.Composite((960, 960), (0, 0), "mod_assets/mcas/ua.png")
image monika 7b = im.Composite((960, 960), (0, 0), "mod_assets/mcas/ub.png")
image monika 7c = im.Composite((960, 960), (0, 0), "mod_assets/mcas/uc.png")
image monika 7d = im.Composite((960, 960), (0, 0), "mod_assets/mcas/ud.png")
image monika 7e = im.Composite((960, 960), (0, 0), "mod_assets/mcas/ue.png")

image monika 5a = im.Composite((960, 960), (0, 0), "monika/3a.png")
image monika 5b = im.Composite((960, 960), (0, 0), "monika/3b.png")
image monika 5c = im.Composite((960, 960), (0, 0), "mod_assets/mcas/3c.png")
image monika 5d = im.Composite((960, 960), (0, 0), "mod_assets/mcas/3d.png")
image monika 5e = im.Composite((960, 960), (0, 0), "mod_assets/mcas/3e.png")

# The better custom Monika outfits
image monika 1ba = im.Composite((960, 960), (0, 0), "mod_assets/mcas/3l.png", (0, 0), "mod_assets/mcas/3r.png", (0, 0), "monika/a.png")
image monika 1bb = im.Composite((960, 960), (0, 0), "mod_assets/mcas/3l.png", (0, 0), "mod_assets/mcas/3r.png", (0, 0), "monika/b.png")
image monika 1bc = im.Composite((960, 960), (0, 0), "mod_assets/mcas/3l.png", (0, 0), "mod_assets/mcas/3r.png", (0, 0), "monika/c.png")
image monika 1bd = im.Composite((960, 960), (0, 0), "mod_assets/mcas/3l.png", (0, 0), "mod_assets/mcas/3r.png", (0, 0), "monika/d.png")
image monika 1be = im.Composite((960, 960), (0, 0), "mod_assets/mcas/3l.png", (0, 0), "mod_assets/mcas/3r.png", (0, 0), "monika/e.png")
image monika 1bf = im.Composite((960, 960), (0, 0), "mod_assets/mcas/3l.png", (0, 0), "mod_assets/mcas/3r.png", (0, 0), "monika/f.png")
image monika 1bg = im.Composite((960, 960), (0, 0), "mod_assets/mcas/3l.png", (0, 0), "mod_assets/mcas/3r.png", (0, 0), "monika/g.png")
image monika 1bh = im.Composite((960, 960), (0, 0), "mod_assets/mcas/3l.png", (0, 0), "mod_assets/mcas/3r.png", (0, 0), "monika/h.png")
image monika 1bi = im.Composite((960, 960), (0, 0), "mod_assets/mcas/3l.png", (0, 0), "mod_assets/mcas/3r.png", (0, 0), "monika/i.png")
image monika 1bj = im.Composite((960, 960), (0, 0), "mod_assets/mcas/3l.png", (0, 0), "mod_assets/mcas/3r.png", (0, 0), "monika/j.png")
image monika 1bk = im.Composite((960, 960), (0, 0), "mod_assets/mcas/3l.png", (0, 0), "mod_assets/mcas/3r.png", (0, 0), "monika/k.png")
image monika 1bl = im.Composite((960, 960), (0, 0), "mod_assets/mcas/3l.png", (0, 0), "mod_assets/mcas/3r.png", (0, 0), "monika/l.png")
image monika 1bm = im.Composite((960, 960), (0, 0), "mod_assets/mcas/3l.png", (0, 0), "mod_assets/mcas/3r.png", (0, 0), "monika/m.png")
image monika 1bn = im.Composite((960, 960), (0, 0), "mod_assets/mcas/3l.png", (0, 0), "mod_assets/mcas/3r.png", (0, 0), "monika/n.png")
image monika 1bo = im.Composite((960, 960), (0, 0), "mod_assets/mcas/3l.png", (0, 0), "mod_assets/mcas/3r.png", (0, 0), "monika/o.png")
image monika 1bp = im.Composite((960, 960), (0, 0), "mod_assets/mcas/3l.png", (0, 0), "mod_assets/mcas/3r.png", (0, 0), "monika/p.png")
image monika 1bq = im.Composite((960, 960), (0, 0), "mod_assets/mcas/3l.png", (0, 0), "mod_assets/mcas/3r.png", (0, 0), "monika/q.png")
image monika 1br = im.Composite((960, 960), (0, 0), "mod_assets/mcas/3l.png", (0, 0), "mod_assets/mcas/3r.png", (0, 0), "monika/r.png")

image monika 2ba = im.Composite((960, 960), (0, 0), "mod_assets/mcas/3l.png", (0, 0), "mod_assets/mcas/4r.png", (0, 0), "monika/a.png")
image monika 2bb = im.Composite((960, 960), (0, 0), "mod_assets/mcas/3l.png", (0, 0), "mod_assets/mcas/4r.png", (0, 0), "monika/b.png")
image monika 2bc = im.Composite((960, 960), (0, 0), "mod_assets/mcas/3l.png", (0, 0), "mod_assets/mcas/4r.png", (0, 0), "monika/c.png")
image monika 2bd = im.Composite((960, 960), (0, 0), "mod_assets/mcas/3l.png", (0, 0), "mod_assets/mcas/4r.png", (0, 0), "monika/d.png")
image monika 2be = im.Composite((960, 960), (0, 0), "mod_assets/mcas/3l.png", (0, 0), "mod_assets/mcas/4r.png", (0, 0), "monika/e.png")
image monika 2bf = im.Composite((960, 960), (0, 0), "mod_assets/mcas/3l.png", (0, 0), "mod_assets/mcas/4r.png", (0, 0), "monika/f.png")
image monika 2bg = im.Composite((960, 960), (0, 0), "mod_assets/mcas/3l.png", (0, 0), "mod_assets/mcas/4r.png", (0, 0), "monika/g.png")
image monika 2bh = im.Composite((960, 960), (0, 0), "mod_assets/mcas/3l.png", (0, 0), "mod_assets/mcas/4r.png", (0, 0), "monika/h.png")
image monika 2bi = im.Composite((960, 960), (0, 0), "mod_assets/mcas/3l.png", (0, 0), "mod_assets/mcas/4r.png", (0, 0), "monika/i.png")
image monika 2bj = im.Composite((960, 960), (0, 0), "mod_assets/mcas/3l.png", (0, 0), "mod_assets/mcas/4r.png", (0, 0), "monika/j.png")
image monika 2bk = im.Composite((960, 960), (0, 0), "mod_assets/mcas/3l.png", (0, 0), "mod_assets/mcas/4r.png", (0, 0), "monika/k.png")
image monika 2bl = im.Composite((960, 960), (0, 0), "mod_assets/mcas/3l.png", (0, 0), "mod_assets/mcas/4r.png", (0, 0), "monika/l.png")
image monika 2bm = im.Composite((960, 960), (0, 0), "mod_assets/mcas/3l.png", (0, 0), "mod_assets/mcas/4r.png", (0, 0), "monika/m.png")
image monika 2bn = im.Composite((960, 960), (0, 0), "mod_assets/mcas/3l.png", (0, 0), "mod_assets/mcas/4r.png", (0, 0), "monika/n.png")
image monika 2bo = im.Composite((960, 960), (0, 0), "mod_assets/mcas/3l.png", (0, 0), "mod_assets/mcas/4r.png", (0, 0), "monika/o.png")
image monika 2bp = im.Composite((960, 960), (0, 0), "mod_assets/mcas/3l.png", (0, 0), "mod_assets/mcas/4r.png", (0, 0), "monika/p.png")
image monika 2bq = im.Composite((960, 960), (0, 0), "mod_assets/mcas/3l.png", (0, 0), "mod_assets/mcas/4r.png", (0, 0), "monika/q.png")
image monika 2br = im.Composite((960, 960), (0, 0), "mod_assets/mcas/3l.png", (0, 0), "mod_assets/mcas/4r.png", (0, 0), "monika/r.png")

image monika 3ba = im.Composite((960, 960), (0, 0), "mod_assets/mcas/4l.png", (0, 0), "mod_assets/mcas/3r.png", (0, 0), "monika/a.png")
image monika 3bb = im.Composite((960, 960), (0, 0), "mod_assets/mcas/4l.png", (0, 0), "mod_assets/mcas/3r.png", (0, 0), "monika/b.png")
image monika 3bc = im.Composite((960, 960), (0, 0), "mod_assets/mcas/4l.png", (0, 0), "mod_assets/mcas/3r.png", (0, 0), "monika/c.png")
image monika 3bd = im.Composite((960, 960), (0, 0), "mod_assets/mcas/4l.png", (0, 0), "mod_assets/mcas/3r.png", (0, 0), "monika/d.png")
image monika 3be = im.Composite((960, 960), (0, 0), "mod_assets/mcas/4l.png", (0, 0), "mod_assets/mcas/3r.png", (0, 0), "monika/e.png")
image monika 3bf = im.Composite((960, 960), (0, 0), "mod_assets/mcas/4l.png", (0, 0), "mod_assets/mcas/3r.png", (0, 0), "monika/f.png")
image monika 3bg = im.Composite((960, 960), (0, 0), "mod_assets/mcas/4l.png", (0, 0), "mod_assets/mcas/3r.png", (0, 0), "monika/g.png")
image monika 3bh = im.Composite((960, 960), (0, 0), "mod_assets/mcas/4l.png", (0, 0), "mod_assets/mcas/3r.png", (0, 0), "monika/h.png")
image monika 3bi = im.Composite((960, 960), (0, 0), "mod_assets/mcas/4l.png", (0, 0), "mod_assets/mcas/3r.png", (0, 0), "monika/i.png")
image monika 3bj = im.Composite((960, 960), (0, 0), "mod_assets/mcas/4l.png", (0, 0), "mod_assets/mcas/3r.png", (0, 0), "monika/j.png")
image monika 3bk = im.Composite((960, 960), (0, 0), "mod_assets/mcas/4l.png", (0, 0), "mod_assets/mcas/3r.png", (0, 0), "monika/k.png")
image monika 3bl = im.Composite((960, 960), (0, 0), "mod_assets/mcas/4l.png", (0, 0), "mod_assets/mcas/3r.png", (0, 0), "monika/l.png")
image monika 3bm = im.Composite((960, 960), (0, 0), "mod_assets/mcas/4l.png", (0, 0), "mod_assets/mcas/3r.png", (0, 0), "monika/m.png")
image monika 3bn = im.Composite((960, 960), (0, 0), "mod_assets/mcas/4l.png", (0, 0), "mod_assets/mcas/3r.png", (0, 0), "monika/n.png")
image monika 3bo = im.Composite((960, 960), (0, 0), "mod_assets/mcas/4l.png", (0, 0), "mod_assets/mcas/3r.png", (0, 0), "monika/o.png")
image monika 3bp = im.Composite((960, 960), (0, 0), "mod_assets/mcas/4l.png", (0, 0), "mod_assets/mcas/3r.png", (0, 0), "monika/p.png")
image monika 3bq = im.Composite((960, 960), (0, 0), "mod_assets/mcas/4l.png", (0, 0), "mod_assets/mcas/3r.png", (0, 0), "monika/q.png")
image monika 3br = im.Composite((960, 960), (0, 0), "mod_assets/mcas/4l.png", (0, 0), "mod_assets/mcas/3r.png", (0, 0), "monika/r.png")

image monika 4ba = im.Composite((960, 960), (0, 0), "mod_assets/mcas/4l.png", (0, 0), "mod_assets/mcas/4r.png", (0, 0), "monika/a.png")
image monika 4bb = im.Composite((960, 960), (0, 0), "mod_assets/mcas/4l.png", (0, 0), "mod_assets/mcas/4r.png", (0, 0), "monika/b.png")
image monika 4bc = im.Composite((960, 960), (0, 0), "mod_assets/mcas/4l.png", (0, 0), "mod_assets/mcas/4r.png", (0, 0), "monika/c.png")
image monika 4bd = im.Composite((960, 960), (0, 0), "mod_assets/mcas/4l.png", (0, 0), "mod_assets/mcas/4r.png", (0, 0), "monika/d.png")
image monika 4be = im.Composite((960, 960), (0, 0), "mod_assets/mcas/4l.png", (0, 0), "mod_assets/mcas/4r.png", (0, 0), "monika/e.png")
image monika 4bf = im.Composite((960, 960), (0, 0), "mod_assets/mcas/4l.png", (0, 0), "mod_assets/mcas/4r.png", (0, 0), "monika/f.png")
image monika 4bg = im.Composite((960, 960), (0, 0), "mod_assets/mcas/4l.png", (0, 0), "mod_assets/mcas/4r.png", (0, 0), "monika/g.png")
image monika 4bh = im.Composite((960, 960), (0, 0), "mod_assets/mcas/4l.png", (0, 0), "mod_assets/mcas/4r.png", (0, 0), "monika/h.png")
image monika 4bi = im.Composite((960, 960), (0, 0), "mod_assets/mcas/4l.png", (0, 0), "mod_assets/mcas/4r.png", (0, 0), "monika/i.png")
image monika 4bj = im.Composite((960, 960), (0, 0), "mod_assets/mcas/4l.png", (0, 0), "mod_assets/mcas/4r.png", (0, 0), "monika/j.png")
image monika 4bk = im.Composite((960, 960), (0, 0), "mod_assets/mcas/4l.png", (0, 0), "mod_assets/mcas/4r.png", (0, 0), "monika/k.png")
image monika 4bl = im.Composite((960, 960), (0, 0), "mod_assets/mcas/4l.png", (0, 0), "mod_assets/mcas/4r.png", (0, 0), "monika/l.png")
image monika 4bm = im.Composite((960, 960), (0, 0), "mod_assets/mcas/4l.png", (0, 0), "mod_assets/mcas/4r.png", (0, 0), "monika/m.png")
image monika 4bn = im.Composite((960, 960), (0, 0), "mod_assets/mcas/4l.png", (0, 0), "mod_assets/mcas/4r.png", (0, 0), "monika/n.png")
image monika 4bo = im.Composite((960, 960), (0, 0), "mod_assets/mcas/4l.png", (0, 0), "mod_assets/mcas/4r.png", (0, 0), "monika/o.png")
image monika 4bp = im.Composite((960, 960), (0, 0), "mod_assets/mcas/4l.png", (0, 0), "mod_assets/mcas/4r.png", (0, 0), "monika/p.png")
image monika 4bq = im.Composite((960, 960), (0, 0), "mod_assets/mcas/4l.png", (0, 0), "mod_assets/mcas/4r.png", (0, 0), "monika/q.png")
image monika 4br = im.Composite((960, 960), (0, 0), "mod_assets/mcas/4l.png", (0, 0), "mod_assets/mcas/4r.png", (0, 0), "monika/r.png")

image monika 5ba = im.Composite((960, 960), (0, 0), "mod_assets/mcas/5a.png")
image monika 5bb = im.Composite((960, 960), (0, 0), "mod_assets/mcas/5b.png")
image monika 5bc = im.Composite((960, 960), (0, 0), "mod_assets/mcas/5c.png")
image monika 5bd = im.Composite((960, 960), (0, 0), "mod_assets/mcas/5d.png")
image monika 5be = im.Composite((960, 960), (0, 0), "mod_assets/mcas/5e.png")


image monika g1:
    "monika/g1.png"
    xoffset 35 yoffset 55
    parallel:
        zoom 1.00
        linear 0.10 zoom 1.03
        repeat
    parallel:
        xoffset 35
        0.20
        xoffset 0
        0.05
        xoffset -10
        0.05
        xoffset 0
        0.05
        xoffset -80
        0.05
        repeat
    time 1.25
    xoffset 0 yoffset 0 zoom 1.00
    "monika 3"

image monika g2:
    block:
        choice:
            "monika/g2.png"
        choice:
            "monika/g3.png"
        choice:
            "monika/g4.png"
    block:
        choice:
            pause 0.05
        choice:
            pause 0.1
        choice:
            pause 0.15
        choice:
            pause 0.2
    repeat


define _dismiss_pause = config.developer

###### Persistent Variables ######
# These values are automatically loaded/saved on game start and exit.
# These exist across all saves

default persistent.playername = ""
default player = persistent.playername
default persistent.playthrough = 0
default persistent.yuri_kill = 0
default persistent.seen_eyes = None
default persistent.seen_sticker = None
default persistent.ghost_menu = None
default persistent.seen_ghost_menu = None
default seen_eyes_this_chapter = False
default persistent.anticheat = 0
default persistent.clear = [False, False, False, False, False, False, False, False, False, False]
default persistent.special_poems = None
default persistent.clearall = None
default persistent.menu_bg_m = None
default persistent.first_load = None

###### Other global variables ######
# It's good practice to define global variables here, just so you know what you can call later

default in_sayori_kill = None
default in_yuri_kill = None
default anticheat = 0
define config.mouse = None
default allow_skipping = True
default basedir = config.basedir
default chapter = 0
default currentpos = 0
default faint_effect = None


# Instantiating variables for poem appeal. This is how much each character likes the poem for each day.
# -1 = Dislike, 0 = Neutral, 1 = Like
default n_poemappeal = [0, 0, 0]
default s_poemappeal = [0, 0, 0]
default y_poemappeal = [0, 0, 0]
default m_poemappeal = [0, 0, 0]

# The last winner of the poem minigame.
default poemwinner = ['sayori', 'sayori', 'sayori']

# Keeping track of who read your poem when you're showing it to each of the girls.
default s_readpoem = False
default n_readpoem = False
default y_readpoem = False
default m_readpoem = False

# Used in poemresponse_start because it's easier than checking true/false on everyone's read state.
default poemsread = 0

# The main appeal points. Whoever likes your poem the most gets an appeal point for that chapter.
# Appeal points are used to keep track of which exclusive scene to show each chapter.
default n_appeal = 0
default s_appeal = 0
default y_appeal = 0
default m_appeal = 0

# We keep track of whether we watched Natsuki's and sayori's second exclusive scenes
# to decide whether to play them in chapter 3.
default n_exclusivewatched = False
default y_exclusivewatched = False

# Yuri runs away after the first exclusive scene of playthrough 2.
default y_gave = False
default y_ranaway = False

# We choose who to side with in chapter 1.
default ch1_choice = "sayori"

# If we choose to help Sayori in ch3, some of the dialogue changes.
default help_sayori = None
default help_monika = None

# We choose who to spend time with in chapter 4.
default ch4_scene = "yuri"
default ch4_name = "Yuri"
default sayori_confess = True

# We read Natsuki's confession poem in chapter 23.
default natsuki_23 = None
