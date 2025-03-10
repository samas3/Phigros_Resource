import atexit
from configparser import ConfigParser
import tkinter
import gameInformation
import getResource

path = tkinter.Entry()
path.insert(0, 'com.PigeonGames.Phigros.apk')
path.pack()

d = {
    "avatar": tkinter.BooleanVar(),
    "Chart": tkinter.BooleanVar(),
    "IllustrationBlur": tkinter.BooleanVar(),
    "IllustrationLowRes": tkinter.BooleanVar(),
    "Illustration": tkinter.BooleanVar(),
    "music": tkinter.BooleanVar(),
    "collection": tkinter.BooleanVar(),
    "tips": tkinter.BooleanVar(),
}

tkinter.Checkbutton(text="头像", variable=d["avatar"]).pack()
tkinter.Checkbutton(text="谱面", variable=d["Chart"]).pack()
tkinter.Checkbutton(text="曲绘(模糊)", variable=d["IllustrationBlur"]).pack()
tkinter.Checkbutton(text="曲绘(低质量)", variable=d["IllustrationLowRes"]).pack()
tkinter.Checkbutton(text="曲绘", variable=d["Illustration"]).pack()
tkinter.Checkbutton(text="音乐", variable=d["music"]).pack()
tkinter.Checkbutton(text="收集品", variable=d["collection"]).pack()
tkinter.Checkbutton(text="Tips", variable=d["tips"]).pack()

c = ConfigParser()
c.optionxform = str
c.read("config.ini", "utf8")

for key in c["TYPES"]:
    d[key].set(c["TYPES"].getboolean(key))

def exit_handle():
    for key in c["TYPES"]:
        c["TYPES"][key] = str(d[key].get())
    with open("config.ini", "w", encoding="utf8") as f:
        c.write(f)
atexit.register(exit_handle)

def callback():
    config = {
        "UPDATE": {
            "main_story": 0,
            "side_story": 0,
            "other_song": 0
        }
    }
    for key, value in d.items():
        config[key] = value.get()
    gameInformation.run(path.get(), config)
    if config['Chart'] or config['avatar'] or config['music'] or config['Illustration'] or config['IllustrationLowRes'] or config['IllustrationBlur']:
        getResource.run(path.get(), config)


tkinter.Button(text="执行", command = callback).pack()
tkinter.mainloop()
