# Resolution: 1920x1080
# OS used: Windows, tested on Linux, game layout is a bit distorted, bossKeyImage is distorted
# Photos of game in different OS are in the same folder
from tkinter import *
from random import randint
from tkinter import messagebox


class Game:
    def __init__(self):
        # Make root window
        self.root = Tk()
        self.root.title("Infinite Tower")
        self.root.geometry("1920x1080")
        self.containerWidth = 550

        # Make Boss Key Frame
        self.bossKeyFrame = Frame(self.root)
        self.bossKeyFrame.place(in_=self.root, anchor=CENTER, relx=0.5, rely=0.5, relwidth=1, relheight=1)
        self.fakeImg = PhotoImage(file="gameAssets/gameMisc/bossKeyImg.png")
        self.fakeScreen = Label(self.bossKeyFrame, image=self.fakeImg)
        self.fakeScreen.place(in_=self.bossKeyFrame, anchor=CENTER, relx=0.5, rely=0.5, relwidth=1, relheight=1)
        self.bossKeyOn = False

        # Make Main Menu Container
        self.mainFrame = Frame(self.root, width=1920, height=1080)
        self.mainFrame.place(in_=self.root, anchor=CENTER, relwidth=1, relheight=1, relx=0.5, rely=0.5)
        self.mainBg = PhotoImage(file="gameAssets/mainMenuBg.png")
        self.bgLabel = Label(self.mainFrame, image=self.mainBg)
        self.bgLabel.place(in_=self.mainFrame, anchor=CENTER, relx=0.5, rely=0.5, relwidth=1, relheight=1)
        self.gameTitle = Label(self.mainFrame, text="Infinite Tower", font=("Times New Roman", 50))
        self.gameTitle.place(in_=self.mainFrame, anchor=CENTER, relx=0.5, rely=0.1)
        self.container = Frame(self.mainFrame, width=self.containerWidth, height=600, bg="SteelBlue", relief=SOLID, border=5)
        self.container.place(in_=self.mainFrame, anchor=CENTER, relx=0.5, rely=0.55)

        # Make Game Container
        self.gameFrame = Frame(self.root, width=1920, height=1080, background="Black")
        self.gameFrame.place(in_=self.root, anchor=CENTER, relwidth=1, relheight=1, relx=0.5, rely=0.5)
        self.keyBinds = ["<Up>", "<Left>", "<Down>", "<Right>", "q", "w", "e", "r", "t", "a", "s", "d", "p", "b", "c"]

        # Make Dialog boxes
        self.drainLabel = Label(self.gameFrame, text="Drain")
        self.slowLabel = Label(self.gameFrame, text="Slow")
        self.hasteLabel = Label(self.gameFrame, text="Haste")
        self.silenceLabel = Label(self.gameFrame, text="Silence")
        self.demiLabel = Label(self.gameFrame, text="Demi")
        self.weakenLabel = Label(self.gameFrame, text="Weaken")
        self.drainLabel.place(in_=self.gameFrame, anchor=CENTER, relx=0.5, rely=0.075)
        self.slowLabel.place(in_=self.gameFrame, anchor=CENTER, relx=0.5, rely=0.075)
        self.hasteLabel.place(in_=self.gameFrame, anchor=CENTER, relx=0.5, rely=0.075)
        self.silenceLabel.place(in_=self.gameFrame, anchor=CENTER, relx=0.5, rely=0.075)
        self.demiLabel.place(in_=self.gameFrame, anchor=CENTER, relx=0.5, rely=0.075)
        self.weakenLabel.place(in_=self.gameFrame, anchor=CENTER, relx=0.5, rely=0.075)

        # Make the sub pages
        self.makeTutorialPage()
        self.makeMainMenuPage()
        self.makeLoadPage()
        self.makeLeaderboardPage()
        self.makeOptionsPage()
        self.makeCreditsPage()

        # Bring up the first page
        self.mainFrame.lift()
        self.mainMenuPage.lift()

        # Message
        messagebox.showinfo("Recommended Settings", "If you are on a laptop, please turn on full performance mode for a better experience")
        self.root.focus_force()

    def makeMainMenuPage(self):
        # Main Menu Page Frame
        self.mainMenuPage = Frame(self.container, width=self.containerWidth, height=600, bg="SteelBlue")
        self.mainMenuPage.place(in_=self.container, anchor=CENTER, relx=0.5, rely=0.5, relwidth=1, relheight=1)

        # Main Menu Page Buttons
        startButton = Button(self.mainMenuPage, text="Start Game", relief=SOLID, border=2, font=("Times New Roman", 25), width=20, command=self.resetTutorial)
        loadButton = Button(self.mainMenuPage, text="Load Game", relief=SOLID, border=2, font=("Times New Roman", 25), width=20, command=self.LoadGameButton)
        leaderboardButton = Button(self.mainMenuPage, text="Leaderboard", relief=SOLID, border=2, font=("Times New Roman", 25), width=20, command=self.LeaderboardPageButton)
        optionsButton = Button(self.mainMenuPage, text="Key Bind Options", relief=SOLID, border=2, font=("Times New Roman", 25), width=20, command=self.OptionsPageButton)
        creditsButton = Button(self.mainMenuPage, text="Credits", relief=SOLID, border=2, font=("Times New Roman", 25), width=20, command=self.CreditsPageButton)
        startButton.place(in_=self.mainMenuPage, anchor=CENTER, relx=0.5, rely=0.16)
        loadButton.place(in_=self.mainMenuPage, anchor=CENTER, relx=0.5, rely=0.33)
        leaderboardButton.place(in_=self.mainMenuPage, anchor=CENTER, relx=0.5, rely=0.5)
        optionsButton.place(in_=self.mainMenuPage, anchor=CENTER, relx=0.5, rely=0.66)
        creditsButton.place(in_=self.mainMenuPage, anchor=CENTER, relx=0.5, rely=0.83)

    def resetTutorial(self):
        self.storyFrame.lift()
        self.tutorialCont.lift()

    def makeLoadPage(self):
        # Load Game Page
        self.loadPage = Frame(self.container, width=self.containerWidth, height=600, bg="SteelBlue")
        self.loadPage.place(in_=self.container, anchor=CENTER, relx=0.5, rely=0.5, relwidth=1, relheight=1)
        loadPageLabel = Label(self.loadPage, text="Load Game", font=("Times New Roman", 30), width=20, relief=SOLID, border=2)
        loadPageLabel.place(in_=self.loadPage, anchor=CENTER, relx=0.5, rely=0.1)

        # Load Game Buttons
        self.loadButtonFrame = Frame(self.loadPage, width=400, height=400, relief=SOLID, border=5, bg="White")
        self.loadButtonFrame.place(in_=self.loadPage, anchor=CENTER, relx=0.5, rely=0.52)
        self.makeLoadSlot1("saveMemory1.txt", 0.275, "Slot1: \n")
        self.makeLoadSlot2("saveMemory2.txt", 0.7, "Slot2: \n")

        # Back Button
        lpBackButton = Button(self.loadPage, text="Back", font=("Times New Roman", 20), relief=SOLID, border=2, width=10, command=self.BackButton)
        lpBackButton.place(in_=self.loadPage, anchor=CENTER, relx=0.5, rely=0.92)

    def makeLoadSlot1(self, filename, yloc, slot):
        # Get data from save file
        loadText = StringVar()
        loadFile = open(filename, "r+")
        self.loadData1 = loadFile.readlines()
        for i in range(len(self.loadData1)):
            if "\n" in self.loadData1[i]:
                self.loadData1[i] = self.loadData1[i].strip("\n")
            self.loadData1[i] = self.loadData1[i].split(":")

        # Display saved game results
        if len(self.loadData1) == 0:
            loadText.set(slot + "No game data found")
            load1Button = Button(self.loadButtonFrame, textvariable=loadText, font=("Times New Roman", 15), relief=SOLID, border=2, width=10)
            load1Button.place(in_=self.loadButtonFrame, anchor=CENTER, relx=0.5, rely=yloc, relwidth=0.75, relheight=0.35)
        else:
            loadText.set(slot + "Last floor reacher: " + self.loadData1[0][0] + " " + self.loadData1[0][1])
            load1Button = Button(self.loadButtonFrame, textvariable=loadText, font=("Times New Roman", 15), relief=SOLID, border=2, width=10, command=self.LoadSavedGame1)
            load1Button.place(in_=self.loadButtonFrame, anchor=CENTER, relx=0.5, rely=yloc, relwidth=0.75, relheight=0.35)

    def LoadSavedGame1(self):
        # Load Slot 1
        keyBind = self.loadData1[8][1]
        keyBind = keyBind.replace("[", "")
        keyBind = keyBind.replace("]", "")
        keyBind = keyBind.replace("\'", "")
        keyBind = keyBind.split(",")
        self.StartGame(int(self.loadData1[0][1]), int(self.loadData1[1][1]), int(self.loadData1[2][1]), int(self.loadData1[3][1]), int(self.loadData1[4][1]), int(self.loadData1[5][1]), int(self.loadData1[6][1]), int(self.loadData1[7][1]), 1, keyBind)

    def makeLoadSlot2(self, filename, yloc, slot):
        # Get data from save file
        loadText = StringVar()
        loadFile = open(filename, "r+")
        self.loadData2 = loadFile.readlines()
        for i in range(len(self.loadData2)):
            if "\n" in self.loadData2[i]:
                self.loadData2[i] = self.loadData2[i].strip("\n")
            self.loadData2[i] = self.loadData2[i].split(":")

        # Display saved game results
        if len(self.loadData2) == 0:
            loadText.set(slot + "No game data found")
            load1Button = Button(self.loadButtonFrame, textvariable=loadText, font=("Times New Roman", 15), relief=SOLID, border=2, width=10)
            load1Button.place(in_=self.loadButtonFrame, anchor=CENTER, relx=0.5, rely=yloc, relwidth=0.75, relheight=0.35)
        else:
            loadText.set(slot + "Last floor reacher: " + self.loadData2[0][0] + " " + self.loadData2[0][1])
            load1Button = Button(self.loadButtonFrame, textvariable=loadText, font=("Times New Roman", 15), relief=SOLID, border=2, width=10, command=self.LoadSavedGame2)
            load1Button.place(in_=self.loadButtonFrame, anchor=CENTER, relx=0.5, rely=yloc, relwidth=0.75, relheight=0.35)

    def LoadSavedGame2(self):
        # Load Slot 2
        keyBind = self.loadData2[8][1]
        keyBind = keyBind.replace("[", "")
        keyBind = keyBind.replace("]", "")
        keyBind = keyBind.replace("\'", "")
        keyBind = keyBind.split(",")
        self.StartGame(int(self.loadData2[0][1]), int(self.loadData2[1][1]), int(self.loadData2[2][1]), int(self.loadData2[3][1]), int(self.loadData2[4][1]), int(self.loadData2[5][1]), int(self.loadData2[6][1]), int(self.loadData2[7][1]), 1, keyBind)

    def makeLeaderboardPage(self):
        # Make Leaderboard Page
        self.leaderboardPage = Frame(self.container, width=self.containerWidth, height=600, bg="SteelBlue")
        self.leaderboardPage.place(in_=self.container, anchor=CENTER, relx=0.5, rely=0.5, relwidth=1, relheight=1)
        leaderboardPageLabel = Label(self.leaderboardPage, text="Leaderboard", font=("Times New Roman", 30), width=20, relief=SOLID, border=2)
        leaderboardPageLabel.place(in_=self.leaderboardPage, anchor=CENTER, relx=0.5, rely=0.1)

        # Make a container
        leaderboardFrame = Frame(self.leaderboardPage, width=400, height=400, relief=SOLID, border=5, bg="White")
        leaderboardFrame.place(in_=self.leaderboardPage, anchor=CENTER, relx=0.5, rely=0.52)

        # Load leaderboard data from file
        self.playerStr = StringVar()
        self.scoreStr = StringVar()
        self.loadLeaderboard()

        playersLabel = Label(leaderboardFrame, textvariable=self.playerStr, font=("Times New Roman", 19), anchor=NW, padx=30, pady=20)
        playersLabel.place(in_=leaderboardFrame, anchor=NW, relx=0, rely=0, relwidth=0.75, relheight=1)
        playersLabel = Label(leaderboardFrame, textvariable=self.scoreStr, font=("Times New Roman", 19), anchor=NE, padx=30, pady=20)
        playersLabel.place(in_=leaderboardFrame, anchor=NE, relx=1, rely=0, relwidth=0.25, relheight=1)

        # Button button
        lbpBackButton = Button(self.leaderboardPage, text="Back", font=("Times New Roman", 20), relief=SOLID, border=2, width=10, command=self.BackButton)
        lbpBackButton.place(in_=self.leaderboardPage, anchor=CENTER, relx=0.5, rely=0.92)

    def loadLeaderboard(self):
        # Get data from file
        self.players = ""
        self.scores = ""
        leaderboardFile = open("leaderboardInfo.txt", "r+")
        leaderboardInfo = leaderboardFile.readlines()
        leaderboardFile.close()

        # Process data
        for i in range(len(leaderboardInfo)):
            if "\n" in leaderboardInfo[i]:
                leaderboardInfo[i] = leaderboardInfo[i].strip("\n")
            leaderboardInfo[i] = leaderboardInfo[i].split("-")
            self.players += str(leaderboardInfo[i][0]) + "\n"
            self.scores += str(leaderboardInfo[i][1]) + "\n"

        # Display on leaderboard
        self.playerStr.set(self.players)
        self.scoreStr.set(self.scores)

    def makeOptionsPage(self):
        # Make Options Page
        self.optionsPage = Frame(self.container, width=self.containerWidth, height=600, bg="SteelBlue")
        self.optionsPage.place(in_=self.container, anchor=CENTER, relx=0.5, rely=0.5, relwidth=1, relheight=1)
        optionsPageLabel = Label(self.optionsPage, text="Key Bind Options", font=("Times New Roman", 30), width=20, relief=SOLID, border=2)
        optionsPageLabel.place(in_=self.optionsPage, anchor=CENTER, relx=0.5, rely=0.1)

        # Make a container
        optionsFrame = Frame(self.optionsPage, width=400, height=400, relief=SOLID, border=5, bg="White")
        optionsFrame.place(in_=self.optionsPage, anchor=CENTER, relx=0.5, rely=0.52)

        # Keys Bindings Settings
        moveUpKeyLabel = Label(optionsFrame, text="Move Up:", font=("Times New Roman", 12))
        self.moveUpKeyEn = Entry(optionsFrame, font=("Times New Roman", 12), relief=SOLID, justify=CENTER)
        self.moveUpKeyEn.insert(0, "<Up>")
        moveUpKeyLabel.place(in_=optionsFrame, anchor=W, relx=0.1, rely=0.125, relwidth=0.2, relheight=0.1)
        self.moveUpKeyEn.place(in_=optionsFrame, anchor=W, relx=0.3, rely=0.125, relwidth=0.15, relheight=0.1)

        moveDownKeyLabel = Label(optionsFrame, text="Move Down:", font=("Times New Roman", 12))
        self.moveDownKeyEn = Entry(optionsFrame, font=("Times New Roman", 12), relief=SOLID, justify=CENTER)
        self.moveDownKeyEn.insert(0, "<Down>")
        moveDownKeyLabel.place(in_=optionsFrame, anchor=W, relx=0.1, rely=0.225, relwidth=0.2, relheight=0.1)
        self.moveDownKeyEn.place(in_=optionsFrame, anchor=W, relx=0.3, rely=0.225, relwidth=0.15, relheight=0.1)

        moveLeftKeyLabel = Label(optionsFrame, text="Move Left:", font=("Times New Roman", 12))
        self.moveLeftKeyEn = Entry(optionsFrame, font=("Times New Roman", 12), relief=SOLID, justify=CENTER)
        self.moveLeftKeyEn.insert(0, "<Left>")
        moveLeftKeyLabel.place(in_=optionsFrame, anchor=W, relx=0.1, rely=0.325, relwidth=0.2, relheight=0.1)
        self.moveLeftKeyEn.place(in_=optionsFrame, anchor=W, relx=0.3, rely=0.325, relwidth=0.15, relheight=0.1)

        moveRightKeyLabel = Label(optionsFrame, text="Move Right:", font=("Times New Roman", 12))
        self.moveRightKeyEn = Entry(optionsFrame, font=("Times New Roman", 12), relief=SOLID, justify=CENTER)
        self.moveRightKeyEn.insert(0, "<Right>")
        moveRightKeyLabel.place(in_=optionsFrame, anchor=W, relx=0.1, rely=0.425, relwidth=0.2, relheight=0.1)
        self.moveRightKeyEn.place(in_=optionsFrame, anchor=W, relx=0.3, rely=0.425, relwidth=0.15, relheight=0.1)

        attack1Label = Label(optionsFrame, text="Orb", font=("Times New Roman", 12))
        self.attack1En = Entry(optionsFrame, text="q", font=("Times New Roman", 12), relief=SOLID, justify=CENTER)
        self.attack1En.insert(0, "q")
        attack1Label.place(in_=optionsFrame, anchor=W, relx=0.55, rely=0.125, relwidth=0.2, relheight=0.1)
        self.attack1En.place(in_=optionsFrame, anchor=W, relx=0.75, rely=0.125, relwidth=0.15, relheight=0.1)

        attack2Label = Label(optionsFrame, text="Slash", font=("Times New Roman", 12))
        self.attack2En = Entry(optionsFrame, text="w", font=("Times New Roman", 12), relief=SOLID, justify=CENTER)
        self.attack2En.insert(0, "w")
        attack2Label.place(in_=optionsFrame, anchor=W, relx=0.55, rely=0.225, relwidth=0.2, relheight=0.1)
        self.attack2En.place(in_=optionsFrame, anchor=W, relx=0.75, rely=0.225, relwidth=0.15, relheight=0.1)

        attack3Label = Label(optionsFrame, text="Shield", font=("Times New Roman", 12))
        self.attack3En = Entry(optionsFrame, text="e", font=("Times New Roman", 12), relief=SOLID, justify=CENTER)
        self.attack3En.insert(0, "e")
        attack3Label.place(in_=optionsFrame, anchor=W, relx=0.55, rely=0.325, relwidth=0.2, relheight=0.1)
        self.attack3En.place(in_=optionsFrame, anchor=W, relx=0.75, rely=0.325, relwidth=0.15, relheight=0.1)

        attack4Label = Label(optionsFrame, text="Burst", font=("Times New Roman", 12))
        self.attack4En = Entry(optionsFrame, text="r", font=("Times New Roman", 12), relief=SOLID, justify=CENTER)
        self.attack4En.insert(0, "r")
        attack4Label.place(in_=optionsFrame, anchor=W, relx=0.55, rely=0.425, relwidth=0.2, relheight=0.1)
        self.attack4En.place(in_=optionsFrame, anchor=W, relx=0.75, rely=0.425, relwidth=0.15, relheight=0.1)

        pauseKeyLabel = Label(optionsFrame, text="Pause", font=("Times New Roman", 12))
        self.pauseKeyEn = Entry(optionsFrame, font=("Times New Roman", 12), relief=SOLID, justify=CENTER)
        self.pauseKeyEn.insert(0, "p")
        pauseKeyLabel.place(in_=optionsFrame, anchor=W, relx=0.1, rely=0.5625, relwidth=0.2, relheight=0.1)
        self.pauseKeyEn.place(in_=optionsFrame, anchor=W, relx=0.3, rely=0.5625, relwidth=0.15, relheight=0.1)

        bossKeyLabel = Label(optionsFrame, text="Boss Key", font=("Times New Roman", 12))
        self.bossKeyEn = Entry(optionsFrame, font=("Times New Roman", 12), relief=SOLID, justify=CENTER)
        self.bossKeyEn.insert(0, "b")
        bossKeyLabel.place(in_=optionsFrame, anchor=W, relx=0.1, rely=0.6625, relwidth=0.2, relheight=0.1)
        self.bossKeyEn.place(in_=optionsFrame, anchor=W, relx=0.3, rely=0.6625, relwidth=0.15, relheight=0.1)

        cheatKeyLabel = Label(optionsFrame, text="Cheat", font=("Times New Roman", 12))
        self.cheatKeyEn = Entry(optionsFrame, font=("Times New Roman", 12), relief=SOLID, justify=CENTER)
        self.cheatKeyEn.insert(0, "c")
        cheatKeyLabel.place(in_=optionsFrame, anchor=W, relx=0.1, rely=0.7625, relwidth=0.2, relheight=0.1)
        self.cheatKeyEn.place(in_=optionsFrame, anchor=W, relx=0.3, rely=0.7625, relwidth=0.15, relheight=0.1)

        buffLabel = Label(optionsFrame, text="Transform", font=("Times New Roman", 12))
        self.buffEn = Entry(optionsFrame, text="t", font=("Times New Roman", 12), relief=SOLID, justify=CENTER)
        self.buffEn.insert(0, "t")
        buffLabel.place(in_=optionsFrame, anchor=W, relx=0.55, rely=0.525, relwidth=0.2, relheight=0.1)
        self.buffEn.place(in_=optionsFrame, anchor=W, relx=0.75, rely=0.525, relwidth=0.15, relheight=0.1)

        sAtk1Label = Label(optionsFrame, text="Gattling", font=("Times New Roman", 12))
        self.sAtk1En = Entry(optionsFrame, text="a", font=("Times New Roman", 12), relief=SOLID, justify=CENTER)
        self.sAtk1En.insert(0, "a")
        sAtk1Label.place(in_=optionsFrame, anchor=W, relx=0.55, rely=0.625, relwidth=0.2, relheight=0.1)
        self.sAtk1En.place(in_=optionsFrame, anchor=W, relx=0.75, rely=0.625, relwidth=0.15, relheight=0.1)

        sAtk2Label = Label(optionsFrame, text="Time Stop", font=("Times New Roman", 12))
        self.sAtk2En = Entry(optionsFrame, text="s", font=("Times New Roman", 12), relief=SOLID, justify=CENTER)
        self.sAtk2En.insert(0, "s")
        sAtk2Label.place(in_=optionsFrame, anchor=W, relx=0.55, rely=0.725, relwidth=0.2, relheight=0.1)
        self.sAtk2En.place(in_=optionsFrame, anchor=W, relx=0.75, rely=0.725, relwidth=0.15, relheight=0.1)

        sAtk3Label = Label(optionsFrame, text="White Hole", font=("Times New Roman", 12))
        self.sAtk3En = Entry(optionsFrame, text="d", font=("Times New Roman", 12), relief=SOLID, justify=CENTER)
        self.sAtk3En.insert(0, "d")
        sAtk3Label.place(in_=optionsFrame, anchor=W, relx=0.55, rely=0.825, relwidth=0.2, relheight=0.1)
        self.sAtk3En.place(in_=optionsFrame, anchor=W, relx=0.75, rely=0.825, relwidth=0.15, relheight=0.1)

        saveBindingBtn = Button(optionsFrame, text="Save Bindings", font=("Times New Roman", 14), relief=SOLID, border=2, width=10, command=self.saveBinding)
        saveBindingBtn.place(in_=optionsFrame, anchor=W, relx=0.1, rely=0.9, relwidth=0.35, relheight=0.1)

        # Hide button to prevent duplicate keys
        self.bindHider = Label(self.optionsPage, text="Fix Bindings", font=("Times New Roman", 14))
        self.optBackButton = Button(self.optionsPage, text="Back", font=("Times New Roman", 20), relief=SOLID, border=2, width=10, command=self.BackButton)
        self.optBackButton.place(in_=self.optionsPage, anchor=CENTER, relx=0.5, rely=0.92)
        self.bindHider.place(in_=self.optBackButton, anchor=CENTER, relx=0.5, rely=0.5, relwidth=1, relheight=1)

    def saveBinding(self):
        # Clear list
        self.keyBinds.clear()

        # Check if keys are used more than once
        self.keyBinds.append(self.moveUpKeyEn.get())
        if self.moveLeftKeyEn.get() in self.keyBinds:
            messagebox.showerror("Warning", str(self.moveUpKeyEn.get()) + " is already used")
        else:
            self.keyBinds.append(self.moveLeftKeyEn.get())
        if self.moveDownKeyEn.get() in self.keyBinds:
            messagebox.showerror("Warning", str(self.moveDownKeyEn.get()) + " is already used")
        else:
            self.keyBinds.append(self.moveDownKeyEn.get())
        if self.moveRightKeyEn.get() in self.keyBinds:
            messagebox.showerror("Warning", str(self.moveRightKeyEn.get()) + " is already used")
        else:
            self.keyBinds.append(self.moveRightKeyEn.get())

        if self.attack1En.get() in self.keyBinds:
            messagebox.showerror("Warning", str(self.attack1En.get()) + " is already used")
        else:
            self.keyBinds.append(self.attack1En.get())
        if self.attack2En.get() in self.keyBinds:
            messagebox.showerror("Warning", str(self.attack2En.get()) + " is already used")
        else:
            self.keyBinds.append(self.attack2En.get())
        if self.attack3En.get() in self.keyBinds:
            messagebox.showerror("Warning", str(self.attack3En.get()) + " is already used")
        else:
            self.keyBinds.append(self.attack3En.get())
        if self.attack4En.get() in self.keyBinds:
            messagebox.showerror("Warning", str(self.attack4En.get()) + " is already used")
        else:
            self.keyBinds.append(self.attack4En.get())
        if self.buffEn.get() in self.keyBinds:
            messagebox.showerror("Warning", str(self.buffEn.get()) + " is already used")
        else:
            self.keyBinds.append(self.buffEn.get())
        if self.sAtk1En.get() in self.keyBinds:
            messagebox.showerror("Warning", str(self.sAtk1En.get()) + " is already used")
        else:
            self.keyBinds.append(self.sAtk1En.get())
        if self.sAtk2En.get() in self.keyBinds:
            messagebox.showerror("Warning", str(self.sAtk2En.get()) + " is already used")
        else:
            self.keyBinds.append(self.sAtk2En.get())
        if self.sAtk3En.get() in self.keyBinds:
            messagebox.showerror("Warning", str(self.sAtk3En.get()) + " is already used")
        else:
            self.keyBinds.append(self.sAtk3En.get())

        if self.pauseKeyEn.get() in self.keyBinds:
            messagebox.showerror("Warning", str(self.pauseKeyEn.get()) + " is already used")
        else:
            self.keyBinds.append(self.pauseKeyEn.get())
        if self.bossKeyEn.get() in self.keyBinds:
            messagebox.showerror("Warning", str(self.bossKeyEn.get()) + " is already used")
        else:
            self.keyBinds.append(self.bossKeyEn.get())
        if self.cheatKeyEn.get() in self.keyBinds:
            messagebox.showerror("Warning", str(self.cheatKeyEn.get()) + " is already used")
        else:
            self.keyBinds.append(self.cheatKeyEn.get())

        # Key Validation
        if len(self.keyBinds) < 15:
            self.bindHider.lift()
        elif len(self.keyBinds) == 15:
            self.optBackButton.lift()

        for i in range(len(self.keyBinds)):
            if self.keyBinds[i] in [',', '.', '[', ']']:
                messagebox.showwarning("Invalid Keys", "Please do not use ',', '.', '[' or ']' for bindings")
                self.root.focus_force()
                self.bindHider.lift()
                break
            if i == 14 and self.keyBinds[i] not in [',', '.', '[', ']']:
                self.optBackButton.lift()

        for i in range(len(self.keyBinds)):
            if "<" not in self.keyBinds[i] and ">" not in self.keyBinds[i] and len(self.keyBinds[i]) != 1:
                messagebox.showwarning("Invalid Keys", "Please use one character to bind if you are not using special event keys")
                self.root.focus_force()
                self.bindHider.lift()
                break
            if i == 14 and "<" not in self.keyBinds[i] and ">" not in self.keyBinds[i] and len(self.keyBinds[i]) == 1:
                self.optBackButton.lift()

    def makeCreditsPage(self):
        # Make Credits Page
        self.creditsPage = Frame(self.container, width=self.containerWidth, height=600, bg="SteelBlue")
        self.creditsPage.place(in_=self.container, anchor=CENTER, relx=0.5, rely=0.5, relwidth=1, relheight=1)
        creditsPageLabel = Label(self.creditsPage, text="Credits", font=("Times New Roman", 30), width=20, relief=SOLID, border=2)
        creditsPageLabel.place(in_=self.creditsPage, anchor=CENTER, relx=0.5, rely=0.1)

        # Make a container
        creditsFrame = Frame(self.creditsPage, width=400, height=400, relief=SOLID, border=5, bg="White")
        creditsFrame.place(in_=self.creditsPage, anchor=CENTER, relx=0.5, rely=0.52)

        # Credits Text
        spritesLabel = Label(creditsFrame, text="Sprites from Final Boss Blues", font=("Times New Roman", 20))
        spritesLabel.place(in_=creditsFrame, anchor=W, relx=0.1, rely=0.3)
        tilesLabel = Label(creditsFrame, text="Tiles from Final Boss Blues", font=("Times New Roman", 20))
        tilesLabel.place(in_=creditsFrame, anchor=W, relx=0.1, rely=0.5)
        creatorLabel = Label(creditsFrame, text="Game made by Kenji Phang", font=("Times New Roman", 20))
        creatorLabel.place(in_=creditsFrame, anchor=W, relx=0.1, rely=0.7)

        # Back Button
        crBackButton = Button(self.creditsPage, text="Back", font=("Times New Roman", 20), relief=SOLID, border=2, width=10, command=self.BackButton)
        crBackButton.place(in_=self.creditsPage, anchor=CENTER, relx=0.5, rely=0.92)

    def BackButton(self):
        self.mainMenuPage.lift()

    def LoadGameButton(self):
        self.loadPage.lift()

    def LeaderboardPageButton(self):
        self.leaderboardPage.lift()

    def OptionsPageButton(self):
        self.optionsPage.lift()

    def CreditsPageButton(self):
        self.creditsPage.lift()

    def makeTutorialPage(self):
        # Make a container
        self.tutorialCont = Frame(self.root, bg="Black")
        self.tutorialCont.place(in_=self.root, anchor=CENTER, relwidth=1, relheight=1, relx=0.5, rely=0.5)

        # Make a page for tutorial
        self.tutorialFrame = Frame(self.tutorialCont, bg="Black")
        self.tutorialFrame.place(in_=self.tutorialCont, anchor=CENTER, relwidth=1, relheight=1, relx=0.5, rely=0.5)
        self.tutorialTitle = Label(self.tutorialFrame, text="Tutorial", bg="Black", fg="White", font=("Times New Roman", 30))
        self.tutorialTitle.place(in_=self.tutorialFrame, anchor=CENTER, relwidth=0.1, relheight=0.05, relx=0.5, rely=0.1)
        self.tutorialImg = PhotoImage(file="gameAssets/tutorial.png")
        self.tutorialDisp = Label(self.tutorialFrame, image=self.tutorialImg, bg="Black")
        self.tutorialDisp.place(in_=self.tutorialFrame, anchor=CENTER, relwidth=0.7, relheight=0.7, relx=0.5, rely=0.5)
        self.startGameBtn = Button(self.tutorialFrame, text="Start", font=("Times New Roman", 14), command=self.StartGame)
        self.startGameBtn.place(in_=self.tutorialFrame, anchor=CENTER, relwidth=0.075, relheight=0.05, relx=0.9, rely=0.9)

        # Make a page for story
        self.storyFrame = Frame(self.tutorialCont, bg="Black")
        self.storyFrame.place(in_=self.tutorialCont, anchor=CENTER, relwidth=1, relheight=1, relx=0.5, rely=0.5)
        story1Text = "You are Rai, a normal student living in society.\nOne day while reading a book called \"The Trapped Angel\",\nyou were magically transported into another world."
        self.story1Label = Label(self.storyFrame, text=story1Text, bg="Black", fg="White", font=("Times New Roman", 18))
        self.story1Label.place(in_=self.storyFrame, anchor=CENTER, relwidth=0.4, relheight=0.3, relx=0.5, rely=0.2)
        story2Text = "You wake up in an ancient hall,\nthere is only one door ahead.\nYou try using your smart phone,\nonly to find that there is no signal.\nYou hear footsteps and growling from the door.\nYou panicked because of the fear."
        self.story2Label = Label(self.storyFrame, text=story2Text, bg="Black", fg="White", font=("Times New Roman", 18))
        self.story2Label.place(in_=self.storyFrame, anchor=CENTER, relwidth=0.4, relheight=0.3, relx=0.5, rely=0.4)
        story3Text = "You hear a voice in your head.\nHe claims to be the an angel and he is trapped here.\nHe offers to work together but he needs a host.\nWith no other choice, you form a pact with the\nangel in hopes of finding a way out."
        self.story3Label = Label(self.storyFrame, text=story3Text, bg="Black", fg="White", font=("Times New Roman", 18))
        self.story3Label.place(in_=self.storyFrame, anchor=CENTER, relwidth=0.4, relheight=0.3, relx=0.5, rely=0.65)
        self.nextBtn = Button(self.storyFrame, text="Next", font=("Times New Roman", 14), command=self.tutorialFrame.lift)
        self.nextBtn.place(in_=self.storyFrame, anchor=CENTER, relwidth=0.075, relheight=0.05, relx=0.9, rely=0.85)

    def StartGame(self, floor=0, level=0, mobMaxLvl=0, miniBossCtr=0, bossCtr=0, scoreThisRnd=0, angelLvl=0, holyEnergy=0, keyBindOpt=0, keybinds=None):
        # Make Game
        self.gameFrame.lift()
        self.canvasWidth = 1080
        self.canvasHeight = 860
        self.barWidth = 225

        # Game Settings
        if keyBindOpt:
            self.keyBinds = keybinds
        self.afterGameMove = False
        self.pause = False
        self.cheatMode = False
        self.zW = False

        # Initialize Game Objects
        self.canvas = Canvas(self.gameFrame, width=self.canvasWidth, height=self.canvasHeight, background="Black", relief=SOLID)
        self.tower = Tower(floor, level, mobMaxLvl, miniBossCtr, bossCtr, scoreThisRnd)
        self.angel = Angel(540, 740, angelLvl, holyEnergy)

        # Char Bindings
        self.canvas.focus_set()
        self.canvas.bind(self.keyBinds[0], self.angel.moveUp)
        self.canvas.bind(self.keyBinds[1], self.angel.moveLeft)
        self.canvas.bind(self.keyBinds[2], self.angel.moveDown)
        self.canvas.bind(self.keyBinds[3], self.angel.moveRight)
        self.canvas.bind(self.keyBinds[4], self.angel.orbAttack)
        self.canvas.bind(self.keyBinds[5], self.angel.slashAttack)
        self.canvas.bind(self.keyBinds[6], self.angel.shieldAngel)
        self.canvas.bind(self.keyBinds[7], self.angel.burstAttack)
        self.canvas.bind(self.keyBinds[8], self.angel.transform)
        self.canvas.bind(self.keyBinds[9], self.angel.wingAtk)
        self.canvas.bind(self.keyBinds[10], self.angel.theWorld)
        self.canvas.bind(self.keyBinds[11], self.angel.heavensFeel)
        self.canvas.bind(self.keyBinds[12], self.angel.inPauseGame)
        self.canvas.bind(self.keyBinds[13], self.angel.showBossKey)
        self.canvas.bind(self.keyBinds[14], self.angel.onCheat)

        # Start Game load or fresh
        if floor == 0:
            self.tower.startGame()
        self.angel.update()
        self.tower.update()

        # Make Side Menus
        self.makeLeftSideBar(self.gameFrame)
        self.canvas.place(in_=self.gameFrame, anchor=CENTER, relx=0.5, rely=0.5)
        self.makeRightSideBar(self.gameFrame)
        self.updateLSBar()
        self.updateRSBar()

    def makeLeftSideBar(self, root):
        # Left Side Menu
        fontSet0 = ("Times New Roman", 15)
        fontSet = ("Times New Roman", 12)

        # Make a container
        self.leftSideBar = Frame(root, bg="Gray", relief=SOLID, border=3)
        self.leftSideBar.place(in_=self.gameFrame, anchor=NW, relx=0, rely=0, relwidth=0.1485, relheight=1)

        # Display score and save menu
        self.floorVal = StringVar()
        self.scoreVal = StringVar()
        self.floorVal.set("Floor: ")
        self.scoreVal.set("Score: ")
        self.saveButton = Button(self.leftSideBar, text="Save Game", font=fontSet0, command=self.makeSaveMenu)
        self.floorLabel = Label(self.leftSideBar, textvariable=self.floorVal, font=fontSet0)
        self.scoreLabel = Label(self.leftSideBar, textvariable=self.scoreVal, font=fontSet0)
        self.saveButton.place(in_=self.leftSideBar, anchor=NW, relx=0.1, rely=0.025, relwidth=0.45)
        self.floorLabel.place(in_=self.leftSideBar, anchor=CENTER, relx=0.5, rely=0.15, relwidth=0.6)
        self.scoreLabel.place(in_=self.leftSideBar, anchor=CENTER, relx=0.5, rely=0.2, relwidth=0.6)

        # Layer 2 control menus
        self.controlsMenu0 = LabelFrame(self.leftSideBar, text="Controls", font=fontSet0)
        self.controlsMenu = LabelFrame(self.leftSideBar, text="Special Skills", font=fontSet0)
        self.controlsMenu.place(in_=self.leftSideBar, anchor=CENTER, relx=0.5, rely=0.6, relwidth=0.9, relheight=0.7)
        self.controlsMenu0.place(in_=self.leftSideBar, anchor=CENTER, relx=0.5, rely=0.6, relwidth=0.9, relheight=0.7)

        # Advanced Control Menu 2
        self.gattImage = PhotoImage(file="gameAssets/gameMisc/blueBalls.png")
        self.gattCdVal = StringVar()
        self.gattCdVal.set("")
        self.gattCooldown = Label(self.controlsMenu, textvariable=self.gattCdVal)
        self.gattButton = Button(self.controlsMenu, image=self.gattImage, relief=SOLID, command=self.angel.wingAtk)
        self.gattButton.place(in_=self.controlsMenu, anchor=W, relx=0.05, rely=0.1)
        self.gattCooldown.place(in_=self.gattButton, anchor=NW, relx=0, rely=0, relwidth=1, relheight=1)
        self.gattText = "\nReleases a\nbarrage of orbs\nfrom your wings\nfor 5 seconds.\nEnergy Cost: 5\n"+"Button: "+str(self.keyBinds[9])
        self.gattExp = Label(self.controlsMenu, text=self.gattText, justify=LEFT)
        self.gattExp.place(in_=self.controlsMenu, anchor=E, relx=0.95, rely=0.1)

        self.tWorldImage = PhotoImage(file="gameAssets/gameMisc/clock.png")
        self.tWorldCdVal = StringVar()
        self.tWorldCdVal.set("")
        self.tWorldCooldown = Label(self.controlsMenu, textvariable=self.tWorldCdVal)
        self.tWorldButton = Button(self.controlsMenu, image=self.tWorldImage, relief=SOLID, command=self.angel.theWorld)
        self.tWorldButton.place(in_=self.controlsMenu, anchor=W, relx=0.05, rely=0.33)
        self.tWorldCooldown.place(in_=self.tWorldButton, anchor=NW, relx=0, rely=0, relwidth=1, relheight=1)
        self.tWText = "\nStops time for\n5 seconds.\nDeals cumulative\ndamage when\ntime resumes.\nEnergy Cost: 10\n"+"Button: "+str(self.keyBinds[10])
        self.tWorldExp = Label(self.controlsMenu, text=self.tWText, justify=LEFT)
        self.tWorldExp.place(in_=self.controlsMenu, anchor=E, relx=0.95, rely=0.325)

        self.hFeelImage = PhotoImage(file="gameAssets/gameMisc/whiteHoleIcon.png")
        self.hFeelCdVal = StringVar()
        self.hFeelCdVal.set("")
        self.hFeelCooldown = Label(self.controlsMenu, textvariable=self.hFeelCdVal)
        self.hFeelButton = Button(self.controlsMenu, image=self.hFeelImage, relief=SOLID, command=self.angel.heavensFeel)
        self.hFeelButton.place(in_=self.controlsMenu, anchor=W, relx=0.05, rely=0.56)
        self.hFeelCooldown.place(in_=self.hFeelButton, anchor=NW, relx=0, rely=0, relwidth=1, relheight=1)
        self.hFeelText = "\nUnleashes an orb\nthat swallows\neverything in\nexchange for\nhalf of the\nangel's HP.\nEnergy Cost: 15\n"+"Button: "+str(self.keyBinds[11])
        self.hFeelExp = Label(self.controlsMenu, text=self.hFeelText, justify=LEFT)
        self.hFeelExp.place(in_=self.controlsMenu, anchor=E, relx=0.95, rely=0.58)

        self.transText = "You are in Angel Mode,\nyour stats are doubled\nand all your attacks\nhave been enhanced."
        self.angelMode = Label(self.controlsMenu, text=self.transText, font=fontSet, relief=SOLID)
        self.angelMode.place(in_=self.controlsMenu, anchor=CENTER, relx=0.5, rely=0.85, relwidth=0.9)

        # Basic Control Menu
        self.atk1Label0 = Label(self.controlsMenu0, text="Orb Attack:     "+str(self.keyBinds[4]), font=fontSet)
        self.atk2Label0 = Label(self.controlsMenu0, text="Slash Attack:    "+str(self.keyBinds[5]), font=fontSet)
        self.shieldLabel0 = Label(self.controlsMenu0, text="Shield Block:    "+str(self.keyBinds[6]), font=fontSet)
        self.atk3Label0 = Label(self.controlsMenu0, text="Burst Attack:    "+str(self.keyBinds[7]), font=fontSet)
        self.transLabel0 = Label(self.controlsMenu0, text="Angel Mode:    "+str(self.keyBinds[8]), font=fontSet)
        self.transLabel1 = Label(self.controlsMenu0, text="  Cost: 10 Energy", font=("Times New Roman", 10), justify=LEFT)
        self.atk1Label0.place(in_=self.controlsMenu0, anchor=W, relx=0.1, rely=0.095, relwidth=0.8, relheight=0.075)
        self.atk2Label0.place(in_=self.controlsMenu0, anchor=W, relx=0.1, rely=0.15, relwidth=0.8, relheight=0.075)
        self.shieldLabel0.place(in_=self.controlsMenu0, anchor=W, relx=0.1, rely=0.2, relwidth=0.8, relheight=0.075)
        self.atk3Label0.place(in_=self.controlsMenu0, anchor=W, relx=0.1, rely=0.25, relwidth=0.8, relheight=0.075)
        self.transLabel0.place(in_=self.controlsMenu0, anchor=W, relx=0.1, rely=0.31, relwidth=0.8, relheight=0.05)
        self.transLabel1.place(in_=self.controlsMenu0, anchor=W, relx=0.135, rely=0.35, relwidth=0.5, relheight=0.04)

        self.upLabel0 = Label(self.controlsMenu0, text="Up:        "+str(self.keyBinds[0]), font=fontSet)
        self.leftLabel0 = Label(self.controlsMenu0, text="Left:    "+str(self.keyBinds[1]), font=fontSet)
        self.downLabel0 = Label(self.controlsMenu0, text="Down:    "+str(self.keyBinds[2]), font=fontSet)
        self.rightLabel0 = Label(self.controlsMenu0, text="Right:   "+str(self.keyBinds[3]), font=fontSet)
        self.upLabel0.place(in_=self.controlsMenu0, anchor=W, relx=0.1, rely=0.45, relwidth=0.8, relheight=0.075)
        self.leftLabel0.place(in_=self.controlsMenu0, anchor=W, relx=0.1, rely=0.5, relwidth=0.8, relheight=0.075)
        self.downLabel0.place(in_=self.controlsMenu0, anchor=W, relx=0.1, rely=0.55, relwidth=0.8, relheight=0.075)
        self.rightLabel0.place(in_=self.controlsMenu0, anchor=W, relx=0.1, rely=0.6, relwidth=0.8, relheight=0.075)

        self.pauseLabel0 = Label(self.controlsMenu0, text="Pause Game:  "+str(self.keyBinds[12]), font=fontSet)
        self.bossKeyLabel0 = Label(self.controlsMenu0, text="Boss Key:      "+str(self.keyBinds[13]), font=fontSet)
        self.cheatLabel0 = Label(self.controlsMenu0, text="Cheat Mode:  "+str(self.keyBinds[14]), font=fontSet)
        self.pauseLabel0.place(in_=self.controlsMenu0, anchor=W, relx=0.1, rely=0.75, relwidth=0.8, relheight=0.075)
        self.bossKeyLabel0.place(in_=self.controlsMenu0, anchor=W, relx=0.1, rely=0.81, relwidth=0.8, relheight=0.075)
        self.cheatLabel0.place(in_=self.controlsMenu0, anchor=W, relx=0.1, rely=0.865, relwidth=0.8, relheight=0.075)

        self.controlsMenu0.lift()

    def makeRightSideBar(self, root):
        # Make a container
        self.rightSideBar = Frame(root, bg="Gray", relief=SOLID, border=3)
        self.rightSideBar.place(in_=self.gameFrame, anchor=NE, relx=1, rely=0, relwidth=0.1485, relheight=1)

        # Display character stats and pause button
        self.unpauseButton = Button(self.rightSideBar, text="Unpause", font=("Times New Roman", 15), command=self.pauseGame)
        self.pauseButton = Button(self.rightSideBar, text="Pause", font=("Times New Roman", 15), command=self.pauseGame)
        self.LevelVal = StringVar()
        self.ExpBarVal = StringVar()
        self.HpBarVal = StringVar()
        self.MpBarVal = StringVar()
        self.atkVal = StringVar()
        self.LevelVal.set("Level: ")
        self.ExpBarVal.set("Exp: ")
        self.HpBarVal.set("HP: ")
        self.MpBarVal.set("MP: ")
        self.atkVal.set("Atk: ")
        self.angelLvl = Label(self.rightSideBar, textvariable=self.LevelVal, font=("Times New Roman", 15))
        self.EXPBar = Label(self.rightSideBar, textvariable=self.ExpBarVal, font=("Times New Roman", 15))
        self.HPBar = Label(self.rightSideBar, textvariable=self.HpBarVal, font=("Times New Roman", 15))
        self.MPBar = Label(self.rightSideBar, textvariable=self.MpBarVal, font=("Times New Roman", 15))
        self.atkBar = Label(self.rightSideBar, textvariable=self.atkVal, font=("Times New Roman", 15))
        self.unpauseButton.place(in_=self.rightSideBar, anchor=NE, relx=0.9, rely=0.025, relwidth=0.4)
        self.pauseButton.place(in_=self.rightSideBar, anchor=NE, relx=0.9, rely=0.025, relwidth=0.4)
        self.angelLvl.place(in_=self.rightSideBar, anchor=CENTER, relx=0.5, rely=0.15, relwidth=0.6)
        self.EXPBar.place(in_=self.rightSideBar, anchor=CENTER, relx=0.5, rely=0.2, relwidth=0.6)
        self.HPBar.place(in_=self.rightSideBar, anchor=CENTER, relx=0.5, rely=0.25, relwidth=0.6)
        self.MPBar.place(in_=self.rightSideBar, anchor=CENTER, relx=0.5, rely=0.3, relwidth=0.6)
        self.atkBar.place(in_=self.rightSideBar, anchor=CENTER, relx=0.5, rely=0.35, relwidth=0.6)

        # Game tips
        tips = "Tip\nIf your HP or MP goes\nbelow zero, you will lose.\nSwitch to angel mode to\nrefill your HP and MP."
        self.gameTips = Label(self.rightSideBar, text=tips, font=("Times New Roman", 12))
        self.gameTips.place(in_=self.rightSideBar, anchor=CENTER, relx = 0.5, rely=0.5, relwidth=0.7)

        # Character transformation information
        self.energyCtr = StringVar()
        self.energyCtr.set("Holy energy: \n")
        self.energyCtrLabel = Label(self.rightSideBar, textvariable=self.energyCtr, font=("Times New Roman", 15))
        self.energyCtrLabel.place(in_=self.rightSideBar, anchor=CENTER, relx=0.5, rely=0.7, relwidth=0.6)
        self.transTimer = StringVar()
        self.transTimer.set("Angel Mode Duration: ")
        self.transTimerLabel = Label(self.rightSideBar, textvariable=self.transTimer, font=("Times New Roman", 15))
        self.transTimerLabel.place(in_=self.rightSideBar, anchor=CENTER, relx=0.5, rely=0.825, relwidth=0.6, relheight=0.15)
        self.wingImg = PhotoImage(file="gameAssets/gameMisc/wing.png")
        self.wingButton = Button(self.rightSideBar, image=self.wingImg, command=self.angel.transform, relief=SOLID, border=5)
        self.wingButton.place(in_=self.rightSideBar, anchor=CENTER, relx=0.5, rely=0.825, relwidth=0.6, relheight=0.15)

    def updateLSBar(self):
        # Update displayed values
        if not self.tower.gameOver:
            self.floorVal.set("Floor: " + str(self.tower.floor%30))
            self.scoreVal.set("Score: " + str(self.tower.score))
            self.gattCdVal.set(self.angel.wingAtkCd)
            self.tWorldCdVal.set(self.angel.tWorldCd)
            self.hFeelCdVal.set(self.angel.hFeelCd)
            self.canvas.after(200, self.updateLSBar)

    def updateRSBar(self):
        # Update displayed values
        if not self.tower.gameOver:
            self.LevelVal.set("Level: " + str(self.angel.lvl))
            self.ExpBarVal.set("Exp: " + str(self.angel.exp))
            self.HpBarVal.set("HP: " + str(self.angel.hp))
            self.MpBarVal.set("MP: " + str(self.angel.mp))
            self.atkVal.set("Atk: " + str(self.angel.atk))
            self.energyCtr.set("Holy energy: \n" + str(self.angel.mobCtr))
            if self.angel.transformed:
                self.transTimer.set("Angel Mode\nDuration: \n" + str(self.angel.buffTime))
            self.canvas.after(200, self.updateRSBar)

    def pauseGame(self):
        # Pause function
        if not self.pause:
            self.unpauseButton.lift()
            self.pause = True
        elif self.pause:
            self.pauseButton.lift()
            self.pause = False

    def unpauseGame(self):
        self.gameFrame.lift()
        self.pauseGame()

    def makeSaveMenu(self):
        self.pauseGame()

        # Make a container
        self.saveMenu = Frame(self.root, bg="Grey")
        self.saveMenu.place(in_=self.gameFrame, anchor=CENTER, relx=0.5, rely=0.5, relwidth=0.3, relheight=0.3)

        # Make a sub container
        self.saveOptionsFrame = Frame(self.saveMenu, bg="SlateGray")
        self.saveOptionsFrame.place(in_=self.saveMenu, anchor=CENTER, relx=0.5, rely=0.5, relwidth=0.8, relheight=0.8)

        # Sub container buttons
        self.cancelButton = Button(self.saveOptionsFrame, text="Save Game", font=("Times New Roman", 20), command=self.chooseSlot)
        self.cancelButton.place(in_=self.saveOptionsFrame, anchor=CENTER, relx=0.5, rely=0.33, relwidth=0.5, relheight=0.2)
        self.saveButton = Button(self.saveOptionsFrame, text="Back", font=("Times New Roman", 20), command=self.unpauseGame)
        self.saveButton.place(in_=self.saveOptionsFrame, anchor=CENTER, relx=0.5, rely=0.66, relwidth=0.5, relheight=0.2)

    def saveGame1(self):
        self.slot1HideButton.lift()

        # Produce string containing data to save
        settingsStr = ""
        settingsStr += "floor:" + str(self.tower.floor) + "\n"
        settingsStr += "level:" + str(self.tower.level) + "\n"
        settingsStr += "mobMaxLvl:" + str(self.tower.mobMaxLvl) + "\n"
        settingsStr += "miniBossCtr:" + str(self.tower.miniBossCtr) + "\n"
        settingsStr += "bossCtr:" + str(self.tower.bossCtr) + "\n"
        settingsStr += "scoreThisRnd:" + str(self.tower.scoreThisRnd) + "\n"
        settingsStr += "AngelLevel:" + str(self.angel.lvl) + "\n"
        settingsStr += "HolyEnergy:" + str(self.angel.mobCtr) + "\n"
        settingsStr += "Bindings:" + str(self.keyBinds) + "\n"

        # Write string to file
        saveFile = open("saveMemory1.txt", "w")
        saveFile.write(settingsStr)
        saveFile.close()

    def saveGame2(self):
        self.slot2HideButton.lift()

        # Produce string containing data to save
        settingsStr = ""
        settingsStr += "floor:" + str(self.tower.floor) + "\n"
        settingsStr += "level:" + str(self.tower.level) + "\n"
        settingsStr += "mobMaxLvl:" + str(self.tower.mobMaxLvl) + "\n"
        settingsStr += "miniBossCtr:" + str(self.tower.miniBossCtr) + "\n"
        settingsStr += "bossCtr:" + str(self.tower.bossCtr) + "\n"
        settingsStr += "scoreThisRnd:" + str(self.tower.scoreThisRnd) + "\n"
        settingsStr += "AngelLevel:" + str(self.angel.lvl) + "\n"
        settingsStr += "HolyEnergy:" + str(self.angel.mobCtr) + "\n"
        settingsStr += "Bindings:" + str(self.keyBinds) + "\n"

        # Write string to file
        saveFile = open("saveMemory2.txt", "w")
        saveFile.write(settingsStr)
        saveFile.close()

    def toSaveMenu(self):
        # Back Button
        self.saveOptionsFrame.lift()

    def chooseSlot(self):
        # Make a container
        self.chooseSlotFrame = Frame(self.saveMenu, bg="SlateGrey")
        self.chooseSlotFrame.place(in_=self.saveMenu, anchor=CENTER, relx=0.5, rely=0.5, relwidth=0.8, relheight=0.8)

        # Save Slot 1
        self.slot1HideButton = Label(self.chooseSlotFrame, text="Done", font=("Times New Roman", 20))
        self.slot1HideButton.place(in_=self.chooseSlotFrame, anchor=CENTER, relx=0.5, rely=0.25, relwidth=0.3, relheight=0.3)
        slot1Button = Button(self.chooseSlotFrame, text="Slot 1", font=("Times New Roman", 20), command=self.saveGame1)
        slot1Button.place(in_=self.chooseSlotFrame, anchor=CENTER, relx=0.5, rely=0.25, relwidth=0.3, relheight=0.3)

        # Save Slot 2
        self.slot2HideButton = Label(self.chooseSlotFrame, text="Done", font=("Times New Roman", 20))
        self.slot2HideButton.place(in_=self.chooseSlotFrame, anchor=CENTER, relx=0.5, rely=0.6, relwidth=0.3, relheight=0.3)
        slot2Button = Button(self.chooseSlotFrame, text="Slot 2", font=("Times New Roman", 20), command=self.saveGame2)
        slot2Button.place(in_=self.chooseSlotFrame, anchor=CENTER, relx=0.5, rely=0.6, relwidth=0.3, relheight=0.3)

        backButton = Button(self.chooseSlotFrame, text="Back", font=("Times New Roman", 15), command=self.toSaveMenu)
        backButton.place(in_=self.chooseSlotFrame, anchor=CENTER, relx=0.5, rely=0.9, relwidth=0.2, relheight=0.15)

    def makeGameOverFrame(self):
        # Create Game Over Page
        self.finalFrame = Frame(self.root, width=1920, height=1080, bg="Gray")
        self.finalFrame.place(in_=self.root, anchor=CENTER, relx=0.5, rely=0.5, relwidth=1, relheight=1)
        self.gBg = PhotoImage(file="gameAssets/mainMenuBg.png")
        self.gBgLabel = Label(self.finalFrame, image=self.gBg)
        self.gBgLabel.place(in_=self.finalFrame, anchor=CENTER, relx=0.5, rely=0.5, relwidth=1, relheight=1)

        # Make a container
        self.gameOverFrame = Frame(self.finalFrame, bg="SteelBlue", relief=SOLID, border=3)
        self.gameOverFrame.place(in_=self.finalFrame, anchor=CENTER, relx=0.5, rely=0.5, relwidth=0.4, relheight=0.8)

        # Scores and game stats
        self.gameOverLabel = Label(self.gameOverFrame, text="GAME OVER \n YOU LOSE", font=("Times New Roman", 50))
        self.gameOverLabel.place(in_=self.gameOverFrame, anchor=CENTER, relx=0.5, rely=0.2, relwidth=1, relheight=0.2)
        self.finalFloorVal = StringVar()
        self.finalFloorVal.set("You survived " + str(self.tower.floor-1) + " floors")
        self.finalFloorLabel = Label(self.gameOverFrame, textvariable=self.finalFloorVal, font=("Times New Roman", 40))
        self.finalFloorLabel.place(in_=self.gameOverFrame, anchor=CENTER, relx=0.5, rely=0.4, relwidth=0.8, relheight=0.1)
        self.finalScoreVal = str(self.tower.score)
        self.finalScore = StringVar()
        self.finalScore.set("Your score:  " + self.finalScoreVal + " points")
        self.finalScoreLabel = Label(self.gameOverFrame, textvariable=self.finalScore, font=("Times New Roman", 30))
        self.finalScoreLabel.place(in_=self.gameOverFrame, anchor=CENTER, relx=0.5, rely=0.5, relwidth=0.8, relheight=0.1)

        # Add to leaderboard
        self.playerInitialsLabel = Label(self.gameOverFrame, text="Your Name: ", font=("Times New Roman", 20))
        self.playerInitialsLabel.place(in_=self.gameOverFrame, anchor=W, relx=0.15, rely=0.65, relwidth=0.25, relheight=0.05)
        self.playerInitials = Entry(self.gameOverFrame, font=("Times New Roman", 20))
        self.playerInitials.place(in_=self.gameOverFrame, anchor=E, relx=0.85, rely=0.65, relwidth=0.45, relheight=0.05)
        self.addToLbButtonHider = Label(self.gameOverFrame, text="Done", font=("Times New Roman", 16))
        self.addToLbButtonHider.place(in_=self.gameOverFrame, anchor=CENTER, relx=0.5, rely=0.715, relwidth=0.7, relheight=0.05)
        self.addToLeaderboardButton = Button(self.gameOverFrame, text="Add to Leaderboard", font=("Times New Roman", 16), command=self.AddToLeaderboard)
        self.addToLeaderboardButton.place(in_=self.gameOverFrame, anchor=CENTER, relx=0.5, rely=0.715, relwidth=0.7, relheight=0.05)

        # Nav Buttons
        self.replayButton = Button(self.gameOverFrame, text="Replay", font=("Times New Roman", 20), command=self.StartGame)
        self.replayButton.place(in_=self.gameOverFrame, anchor=W, relx=0.1, rely=0.85, relwidth=0.2, relheight=0.1)
        self.mainMenuButton = Button(self.gameOverFrame, text="Main Menu", font=("Times New Roman", 20), command=self.MainMenuButton)
        self.mainMenuButton.place(in_=self.gameOverFrame, anchor=CENTER, relx=0.5, rely=0.85, relwidth=0.3, relheight=0.1)
        self.quitButton = Button(self.gameOverFrame, text="Quit", font=("Times New Roman", 20), command=self.QuitGame)
        self.quitButton.place(in_=self.gameOverFrame, anchor=E, relx=0.9, rely=0.85, relwidth=0.2, relheight=0.1)

        self.gameOverFrame.lift()

    def AddToLeaderboard(self):
        self.addToLbButtonHider.lift()

        # Get and store data
        playerData = []
        playerData.append(self.playerInitials.get())
        playerData.append(str(self.finalScoreVal))

        # Sort Scores Algorithm
        leaderboardFile = open("leaderboardInfo.txt", "r+")
        leaderboardInfo = leaderboardFile.readlines()
        leaderboardFile.close()
        for i in range(1, len(leaderboardInfo)):
            if "\n" in leaderboardInfo[i]:
                leaderboardInfo[i] = leaderboardInfo[i].strip("\n")
            leaderboardInfo[i] = leaderboardInfo[i].split("-")

        leaderboardInfo.remove(leaderboardInfo[0])
        leaderboardInfo.append(playerData)
        leaderboardInfo = sorted(leaderboardInfo, reverse=True, key=self.takeSecondElem)

        # Store back into file
        leaderboardData = "Name:-Score\n"
        for i in range(len(leaderboardInfo)):
            if i == len(leaderboardInfo)-1:
                leaderboardData += leaderboardInfo[i][0] + "-" + leaderboardInfo[i][1]
            else:
                leaderboardData += leaderboardInfo[i][0] + "-" + leaderboardInfo[i][1] + "\n"
        leaderboardFile = open("leaderboardInfo.txt", "w")
        leaderboardFile.write(leaderboardData)
        leaderboardFile.close()

    def takeSecondElem(self, elem):
        # Used for sorting algorithm
        return int(elem[1])

    def MainMenuButton(self):
        self.mainFrame.lift()
        self.loadLeaderboard()
        self.leaderboardPage.update()

    def QuitGame(self):
        self.root.destroy()

    def makeWinFrame(self):
        # Story Frame
        self.winStory = Frame(self.root, bg="Black")
        self.winStory.place(in_=self.root, anchor=CENTER, relx=0.5, rely=0.5, relwidth=1, relheight=1)
        winText1 = "The Angel's Perspective\n\n\nWe have finally defeated the dark angel!\nLet's get out of here, I can't wait to return home, Rai exclaims\nThese are words of joy, but I have\nalready heard it so many times I lost count."
        self.winStory1Label = Label(self.winStory, text=winText1, font=("Times New Roman", 18), bg="Black", fg="White")
        self.winStory1Label.place(in_=self.winStory, anchor=CENTER, relx=0.5, rely=0.2, relwidth=0.6, relheight=0.3)
        winText2 = "Rai's body is suddenly engulfed in a bright flame, killing him instantly.\nNo matter how many times I am forced to witness this fate,\nit still hurts me to see Rai like this.\nI muster up all my remaining power and reset time\nto when I first met Rai"
        self.winStory2Label = Label(self.winStory, text=winText2, font=("Times New Roman", 18), bg="Black", fg="White")
        self.winStory2Label.place(in_=self.winStory, anchor=CENTER, relx=0.5, rely=0.475, relwidth=0.8, relheight=0.3)
        winText3 = "I have been stuck in this infinite loop for centuries,\nmeeting Rai, fighting with him and watching him mysteriously die.\nI swear I will get you out of here.\nI awake only to see a paranoid Rai..."
        self.winStory3Label = Label(self.winStory, text=winText3, font=("Times New Roman", 18), bg="Black", fg="White")
        self.winStory3Label.place(in_=self.winStory, anchor=CENTER, relx=0.5, rely=0.7, relwidth=0.8, relheight=0.25)
        self.summaryBtn = Button(self.winStory, text="Continue", font=("Times New Roman", 14), command=self.continueGame)
        self.summaryBtn.place(in_=self.winStory, anchor=CENTER, relx=0.85, rely=0.85, relwidth=0.1, relheight=0.075)

    def continueGame(self):
        self.gameFrame.lift()
        self.pauseGame()


class Tower:
    def __init__(self, floor=0, level=0, mobMaxLvl=0, miniBossCtr=0, bossCtr=0, scoreThisRnd=0):
        # Game object data
        self.floor = floor
        self.level = level
        self.mobMaxLvl = mobMaxLvl
        self.noOfMobs = 20
        self.miniBossCtr = miniBossCtr
        self.bossCtr = bossCtr
        self.startFloor = True
        self.mobList = []
        self.attackProjectilesList = []
        self.scoreThisRnd = scoreThisRnd
        self.score = self.scoreThisRnd
        self.gameOver = False
        self.stopMoving = False

        # Conditions for load or fresh game
        if self.floor != 0:
            self.floor -= 1
            if self.floor % 30 == 4:
                self.miniBossCtr = 0
            elif self.floor % 30 == 14:
                self.miniBossCtr = 1
            elif self.floor % 30 == 24:
                self.miniBossCtr = 2
            if self.floor % 30 == 9:
                self.bossCtr = 0
            elif self.floor % 30 == 19:
                self.bossCtr = 1
            elif self.floor % 30 == 29:
                self.bossCtr = 2

    def startGame(self):
        if self.startFloor:
            self.createFloor()
            self.startFloor = False

    def update(self):
        # Do nothing when paused
        if game.pause:
            game.canvas.after(3000, self.update)
        elif not game.pause:
            # Next floor algorithm
            if not self.gameOver:
                if self.startFloor:
                    self.createFloor()
                if not self.startFloor:
                    self.startFloor = self.checkClear()
                game.canvas.after(3000, self.update)
            # Game over instructions
            if self.gameOver:
                # Garbage Collection
                game.afterGameMove = True
                game.canvas.delete("all")
                self.stopMoving = True
                for i in range(len(self.attackProjectilesList)):
                    del self.attackProjectilesList[0]
                for i in range(len(self.mobList)):
                    del self.mobList[0]
                # Game over page
                game.makeGameOverFrame()

    def createFloor(self):
        self.startFloor = False
        # Garbage Collection
        for mob in range(len(self.mobList)):
            del self.mobList[0]
        for id in range(len(self.attackProjectilesList)):
            del self.attackProjectilesList[0]
        self.floor += 1

        # Increase difficulty every 10 floors
        if self.floor % 10 == 1:
            self.level += 1
            self.mobMaxLvl = 0

        # Win story
        if self.floor > 1 and self.floor % 30 == 1:
            game.angel.winged = False
            game.angel.buffTime = 0
            game.angel.wingTimer = 0
            game.angel.gattCd = 0
            game.angel.hFeelCd = 0
            game.angel.wingAtkCd = 0
            game.angel.dWorldTime = 0
            game.angel.tWorldCd = 0
            game.angel.mobCtr = 0
            game.pauseGame()
            game.makeWinFrame()

        # Floor types
        if self.floor % 10 == 0:
            self.spawnBoss()
        elif self.floor % 10 == 5:
            self.spawnMiniBoss()
        else:
            self.spawnWave()

    def spawnBoss(self):
        # Make a boss object
        boss = Boss(0, 500, 150, self.bossCtr, self.level, self.floor)
        self.mobList.append(boss)
        boss.update()

        # Cycle through different sprites
        self.bossCtr += 1
        if self.bossCtr == 3:
            self.bossCtr = 0

    def spawnMiniBoss(self):
        # Make a mini boss object
        miniBoss = MiniBoss(0, 500, 150, self.miniBossCtr, self.level, self.floor)
        self.mobList.append(miniBoss)
        miniBoss.draw()
        miniBoss.update()

        # Cycle through mini boss sprites
        self.miniBossCtr += 1
        if self.miniBossCtr == 3:
            self.miniBossCtr = 0

    def spawnWave(self):
        # Set wave difficulty
        if self.mobMaxLvl < 7:
                self.mobMaxLvl += 1

        # Generate wave
        for id in range(self.noOfMobs):
            mobType = randint(0, self.mobMaxLvl)
            # 1st Wave
            if id < 10:
                tempMob = Mob(id, 200+(75*id), 350, mobType, self.level, self.floor)
                tempMob.draw()
                tempMob.update()
                self.mobList.append(tempMob)
            # 2nd Wave
            if id >= 10:
                tempMob = Mob(id, 200+(75*(id-10)), 250, mobType, self.level, self.floor)
                tempMob.draw()
                tempMob.update()
                self.mobList.append(tempMob)

    def checkClear(self):
        # Check if no more mobs are alive in floor
        for mob in self.mobList:
            if not mob.dead:
                return False
        # Update score
        self.scoreThisRnd = self.score
        return True


class MagicAttack:
    def __init__(self, x, y, direction, type):
        # Magic Attack data
        self.duration = 0
        self.x = x
        self.y = y
        self.direction = direction
        self.type = type
        if self.direction == "Up":
            self.yVelocity = -10
        elif self.direction == "Down":
            self.yVelocity = 10
        self.exist = True

    def burnOut(self):
        # Attack dissapear after a certain distance
        if self.duration == 60 or self.y < 140:
            game.canvas.delete(self.explosionSprite)
            self.exist = False


class DarkMagicAttack(MagicAttack):
    def __init__(self, x, y, direction, type, dmg):
        # Mob Magic Attack data
        super().__init__(x, y, direction, type)
        self.dmgMultList = [1, 1.3, 1.7, 2]
        self.dmgMult = self.dmgMultList[self.type]
        self.dmg = dmg * self.dmgMult
        game.tower.attackProjectilesList.append(self)

    def draw(self):
        # Attack Sprites
        self.magicList = [PhotoImage(file="gameAssets/mobAtks/rocks.png"),
                          PhotoImage(file="gameAssets/mobAtks/spikes.png"),
                          PhotoImage(file="gameAssets/mobAtks/swordThrow.png"),
                          PhotoImage(file="gameAssets/mobAtks/swordThrow.png")
                          ]
        self.img = self.magicList[self.type]
        self.explosionSprite = game.canvas.create_image(self.x, self.y, image=self.img)

    def update(self):
        if game.pause or game.zW:
            game.canvas.after(50, self.update)
        elif self.exist and not game.pause and not game.zW:
            # Attack object instructions
            game.canvas.move(self.explosionSprite, 0, self.yVelocity)
            self.y += self.yVelocity
            self.duration += 1
            self.burnOut()
            if not game.afterGameMove:
                self.checkAtkCollision()
            game.canvas.after(50, self.update)

    def checkAtkCollision(self):
        if game.angel.alive:
            if game.angel.shielded:
                # Shield Collision
                if abs(game.angel.x-self.x) <= 50 and abs(game.angel.y-50-self.y) <= 10:
                    game.angel.shieldHp -= self.dmg
                    self.exist = False
                    game.canvas.delete(self.explosionSprite)
            # Character Collision
            elif abs(game.angel.x-self.x) <= 30 and abs(game.angel.y-self.y) <= 30:
                self.exist = False
                game.angel.hp -= self.dmg
                game.canvas.delete(self.explosionSprite)


class SummonMagicAttack(DarkMagicAttack):
    def __init__(self, x, y, direction, type, dmg):
        # Inherit object data
        super().__init__(x, y, direction, type, dmg)

    def draw(self):
        # Attack Sprites
        if not self.type:
            self.magicList = [PhotoImage(file="gameAssets/mobAtks/iceShard.png"),
                              PhotoImage(file="gameAssets/mobAtks/iceSpikes.png")
                              ]
        if self.type:
            self.magicList = [PhotoImage(file="gameAssets/mobAtks/fireBall.png"),
                              PhotoImage(file="gameAssets/mobAtks/fireElement.png")
                              ]
        self.img = self.magicList[randint(0, len(self.magicList)-1)]
        self.explosionSprite = game.canvas.create_image(self.x, self.y, image=self.img)


class MiniBossMagicAttack(DarkMagicAttack):
    def __init__(self, x, y, direction, type, dmg):
        # Attack Object data
        super().__init__(x, y, direction, type, dmg)
        self.dmgMultList = [1, 1.3, 1.7]
        self.dmgMult = self.dmgMultList[self.type]
        self.dmg = dmg * self.dmgMult

    def draw(self):
        # Attack Sprites
        if self.type == 0:
            self.magicList = [PhotoImage(file="gameAssets/miniBossAtks/darkOrb.png"),
                              PhotoImage(file="gameAssets/miniBossAtks/darkOrbMini.png")
                              ]
        if self.type == 1:
            self.magicList = [PhotoImage(file="gameAssets/miniBossAtks/darkPunch.png"),
                              PhotoImage(file="gameAssets/miniBossAtks/darkSlam.png"),
                              ]
        if self.type == 2:
            self.magicList = [PhotoImage(file="gameAssets/miniBossAtks/sliceRed.png"),
                              PhotoImage(file="gameAssets/miniBossAtks/darkFireSlash.png"),
                              PhotoImage(file="gameAssets/miniBossAtks/darkExplosion.png")
                              ]
        self.img = self.magicList[randint(0, len(self.magicList)-1)]
        self.explosionSprite = game.canvas.create_image(self.x, self.y, image=self.img)


class BossMagicAttack(MiniBossMagicAttack):
    def __init__(self, x, y, direction, type, dmg, bossLife):
        # Attack Object data
        super().__init__(x, y, direction, type, dmg)
        self.bossLife = bossLife
        self.dmgMultList = [1, 1.3, 1.7, 2]
        self.dmgMult = self.dmgMultList[self.type]
        self.dmg = dmg * self.dmgMult
        if self.bossLife:
            self.hitboxRange = 50
        elif not self.bossLife:
            self.hitboxRange = 100

    def draw(self):
        # Attack Sprites
        if self.type == 0:
            if self.bossLife:
                self.magicList = [PhotoImage(file="gameAssets/bossAtks/darkOrb.png"),
                                  PhotoImage(file="gameAssets/bossAtks/darkOrbMini.png")
                                  ]
            if not self.bossLife:
                self.magicList = [PhotoImage(file="gameAssets/bossAtks/skull.png").zoom(2),
                                  PhotoImage(file="gameAssets/bossAtks/dirt.png")
                                  ]
        if self.type == 1:
            if self.bossLife:
                self.magicList = [PhotoImage(file="gameAssets/bossAtks/iceAxe.png"),
                                  PhotoImage(file="gameAssets/bossAtks/icePike.png"),
                                  PhotoImage(file="gameAssets/bossAtks/iceStaff.png"),
                                  PhotoImage(file="gameAssets/bossAtks/iceSword.png")
                                  ]
            if not self.bossLife:
                self.magicList = [PhotoImage(file="gameAssets/bossAtks/fireAxe.png").zoom(2),
                                  PhotoImage(file="gameAssets/bossAtks/firePike.png").zoom(2),
                                  PhotoImage(file="gameAssets/bossAtks/fireStaff.png").zoom(2),
                                  PhotoImage(file="gameAssets/bossAtks/fireSword.png").zoom(2)
                                  ]
        if self.type == 2:
            if self.bossLife:
                self.magicList = [PhotoImage(file="gameAssets/bossAtks/sliceRed.png"),
                                  PhotoImage(file="gameAssets/bossAtks/darkExplosion.png"),
                                  PhotoImage(file="gameAssets/bossAtks/darkFireSlash.png"),
                                  PhotoImage(file="gameAssets/bossAtks/nukeHeavy.png"),
                                  ]
            if not self.bossLife:
                self.magicList = [PhotoImage(file="gameAssets/bossAtks/shadowPike.png").zoom(2),
                                  PhotoImage(file="gameAssets/bossAtks/shadowSpear.png").zoom(2),
                                  PhotoImage(file="gameAssets/bossAtks/shadowSword.png").zoom(2),
                                  PhotoImage(file="gameAssets/bossAtks/shadowStaff.png").zoom(2),
                                  PhotoImage(file="gameAssets/bossAtks/shadowWand.png").zoom(2)
                                  ]
        self.img = self.magicList[randint(0, len(self.magicList)-1)]
        self.explosionSprite = game.canvas.create_image(self.x, self.y, image=self.img)

    def checkAtkCollision(self):
        if game.angel.alive:
            if game.angel.shielded:
                # Shield Collision
                if abs(game.angel.x-self.x) <= self.hitboxRange and abs(game.angel.y-50-self.y) <= self.hitboxRange-40:
                    game.angel.shieldHp -= self.dmg
                    self.exist = False
                    game.canvas.delete(self.explosionSprite)
            # Character Collision
            elif (abs(game.angel.x-self.x <= self.hitboxRange) and abs(game.angel.y-self.y <= self.hitboxRange)):
                self.exist = False
                game.angel.hp -= self.dmg
                game.canvas.delete(self.explosionSprite)


class Mob:
    def __init__(self, id, x, y, type, lvl, floor):
        # Mob Object data
        self.id = id
        self.x = x
        self.y = y
        self.type = type
        self.floor = floor
        self.level = lvl
        self.maxHp = 10*self.level + 10*self.type*self.level
        self.hp = self.maxHp
        self.atk = 10 + 5*self.type*self.level
        self.expVal = 5*(1+self.type//10)
        self.fireDelay = 50
        self.fireTimer = 0
        self.xVelocity = -10
        self.yVelocity = 50
        self.dead = False

    def draw(self):
        # Mob Sprites
        self.imgList = [PhotoImage(file="gameAssets/mobSprites/Mob1.png"),
                        PhotoImage(file="gameAssets/mobSprites/Mob2.png"),
                        PhotoImage(file="gameAssets/mobSprites/Mob3.png"),
                        PhotoImage(file="gameAssets/mobSprites/Mob4.png"),
                        PhotoImage(file="gameAssets/mobSprites/Mob5.png"),
                        PhotoImage(file="gameAssets/mobSprites/Mob6.png"),
                        PhotoImage(file="gameAssets/mobSprites/Mob7.png"),
                        PhotoImage(file="gameAssets/mobSprites/Mob8.png")
                        ]
        self.img = self.imgList[self.type]
        self.mobSprite = game.canvas.create_image(self.x, self.y, image=self.img)
        self.hpBar = game.canvas.create_rectangle(self.x-10, self.y-35, self.x+10, self.y-30, fill="red")

    def update(self):
        if game.pause or game.zW:
            game.canvas.after(50, self.update)
        elif not game.pause:
            # Hp Bar
            hpScale = self.hp/self.maxHp*20
            # Move when game over
            if not self.dead and game.tower.gameOver:
                game.canvas.move(self.mobSprite, self.xVelocity, 0)
                self.x += self.xVelocity
                game.canvas.coords(self.hpBar, self.x-10, self.y-35, self.x+hpScale-10, self.y-30)
                if self.x <= 35 or self.x >= 1045:
                    self.xVelocity *= -1
                    game.canvas.move(self.mobSprite, 0, self.yVelocity)
                    self.y += self.yVelocity
                if not game.tower.stopMoving:
                    game.canvas.after(50, self.update)
            elif not self.dead and not game.tower.gameOver and not game.zW:
                # Mob and hp bar movement
                game.canvas.move(self.mobSprite, self.xVelocity, 0)
                self.x += self.xVelocity
                game.canvas.coords(self.hpBar, self.x-10, self.y-35, self.x+hpScale-10, self.y-30)
                if self.x <= 35 or self.x >= 1045:
                    self.xVelocity *= -1
                    game.canvas.move(self.mobSprite, 0, self.yVelocity)
                    self.y += self.yVelocity
                # Attack character with projectiles
                if self.fireTimer % self.fireDelay == 0:
                    self.attack()
                self.fireTimer += 1
                # Attack character physically
                if self.y > 500:
                    self.checkCollision()
                # Disappear after certain point
                if self.y > 800:
                    self.hp = 0
                    game.tower.score -= 10
                    game.angel.exp -= 10
                self.checkDead()
                game.canvas.after(50, self.update)

    def checkDead(self):
        if self.hp <= 0:
            self.dead = True
            # Add score and exp
            game.tower.score += self.expVal
            game.angel.exp += self.expVal
            game.angel.mobCtr += 1
            # Garbage Prep
            self.x = 0
            self.y = 0
            game.canvas.delete(self.mobSprite)
            game.canvas.delete(self.hpBar)

    def attack(self):
        # Shoot projectile
        self.projectile = DarkMagicAttack(self.x, self.y, "Down", self.type//2, self.atk)
        game.tower.attackProjectilesList.append(self.projectile)
        self.projectile.draw()
        self.projectile.update()

    def checkCollision(self):
        # Physical Collision
        if abs(self.x-game.angel.x) < 30 and abs(self.y-game.angel.y) < 30:
            game.angel.hp -= self.atk*2


class SummonedMob(Mob):
    def __init__(self, id, x, y, type, lvl, floor):
        # Mob Object data
        super().__init__(id, x, y, type, lvl, floor)
        self.maxHp = 10 + 25*self.type*self.level + 10*self.floor
        self.hp = self.maxHp
        self.atk = 10 + 10*self.type*self.level
        self.expVal = 20*(1+self.type//10)

    def draw(self):
        # Mob Sprites
        self.imgList = [PhotoImage(file="gameAssets/mobSprites/lichBlueSummon.png"),
                        PhotoImage(file="gameAssets/mobSprites/lichRedSummon.png"),
                        ]
        self.img = self.imgList[self.type]
        self.mobSprite = game.canvas.create_image(self.x, self.y, image=self.img)
        self.hpBar = game.canvas.create_rectangle(self.x-10, self.y-35, self.x+10, self.y-30, fill="red")

    def attack(self):
        # Shoot projectile
        self.projectile = SummonMagicAttack(self.x, self.y, "Down", self.type, self.atk)
        self.projectile.draw()
        self.projectile.update()


class MiniBoss(Mob):
    def __init__(self, id, x, y, type, lvl, floor):
        # Mini Boss object data
        super().__init__(id, x, y, type, lvl, floor)
        self.maxHp = 700*self.level + 50*(self.type+self.floor)
        self.hp = self.maxHp
        self.atk = 10 + 10*(self.type + self.level)
        self.expVal = 40 + 10*(self.type + self.level)
        self.fireDelay = 20
        self.summonMinionDelay = 200
        self.fireTimer = 0
        self.xVelocity = -15

    def draw(self):
        # Mini Boss Sprites
        self.imgList = [PhotoImage(file="gameAssets/miniBossSprites/lich.png"),
                        PhotoImage(file="gameAssets/miniBossSprites/darkMan.png"),
                        PhotoImage(file="gameAssets/miniBossSprites/angelRed.png")
                        ]

        self.img = self.imgList[self.type]
        self.mobSprite = game.canvas.create_image(self.x, self.y, image=self.img)
        self.hpBar = game.canvas.create_rectangle(self.x-15, self.y-35, self.x+15, self.y-30, fill="red")

    def update(self):
        if game.pause or game.zW:
            game.canvas.after(50, self.update)
        elif not game.pause:
            if not self.dead and not game.tower.gameOver and not game.zW:
                # Move mini boss and hp bar
                hpScale = self.hp/self.maxHp*30
                game.canvas.move(self.mobSprite, self.xVelocity, 0)
                self.x += self.xVelocity
                game.canvas.coords(self.hpBar, self.x-15, self.y-35, self.x+hpScale-15, self.y-30)
                if self.x <= 300 or self.x >= 780:
                    self.xVelocity *= -1
                # Shoot projectile
                if self.fireTimer % self.fireDelay == 0:
                    self.attack()
                # Summon minions
                if self.fireTimer % self.summonMinionDelay == 0:
                    self.summonMinions()
                self.fireTimer += 1
                self.checkDead()
                game.canvas.after(50, self.update)

    def checkDead(self):
        if self.hp <= 0:
            self.dead = True
            # Add score and exp
            game.tower.score += self.expVal
            game.angel.exp += self.expVal
            game.angel.mobCtr += 1
            # Garbage prep
            self.x = 0
            self.y = 0
            game.canvas.delete(self.mobSprite)
            game.canvas.delete(self.hpBar)

    def summonMinions(self):
        # Generate a wave of mobs
        noOfMobs = 5
        for id in range(0, noOfMobs):
            mobType = randint(0, game.tower.mobMaxLvl)
            tempMob = Mob(id, 500+(75*id), self.y+150, mobType, game.tower.level, game.tower.floor)
            tempMob.draw()
            tempMob.update()
            game.tower.mobList.append(tempMob)

    def attack(self):
        # Shoot Projectiles
        self.projectile = MiniBossMagicAttack(self.x, self.y, "Down", self.type, self.atk)
        self.projectile.draw()
        self.projectile.update()


class Boss(MiniBoss):
    def __init__(self, id, x, y, type, lvl, floor):
        # Boss object data
        super().__init__(id, x, y, type, lvl, floor)
        self.maxHp = 1500*self.level + 100*(self.type+self.floor)
        self.hp = self.maxHp
        self.atk = 10 + 15*(self.type + self.level)
        self.expVal = 80 + 20*(self.type + self.level)
        self.fireDelay = 15
        self.summonMinionDelay = 150
        self.specialSkillDelay = 150
        self.fireTimer = 0
        self.bossLife = 1
        self.xVelocity = -15
        self.powUpFactor = 2
        self.skillDur = 5

        self.draw()

    def draw(self):
        # Boss Sprites
        if self.type == 0:
            self.img = PhotoImage(file="gameAssets/bossSprites/darkManRobe.png")
            self.img2 = PhotoImage(file="gameAssets/bossSprites/darkSkeletonRobe.png")
            self.img2 = self.img2.zoom(2)
        if self.type == 1:
            self.img = PhotoImage(file="gameAssets/bossSprites/lichBlue.png")
            self.img2 = PhotoImage(file="gameAssets/bossSprites/lichRed.png")
            self.img2 = self.img2.zoom(2)
        if self.type == 2:
            self.img = PhotoImage(file="gameAssets/bossSprites/angelWhite.png")
            self.img2 = PhotoImage(file="gameAssets/bossSprites/angelDark.png")
            self.img2 = self.img2.zoom(2)

        self.mobSprite = game.canvas.create_image(self.x, self.y, image=self.img)
        self.hpBar = game.canvas.create_rectangle(self.x-30, self.y-37, self.x+30, self.y-30, fill="red")

    def update(self):
        if game.pause or game.zW:
            game.canvas.after(50, self.update)
        elif not game.pause:
            if not self.dead and not game.tower.gameOver and not game.zW:
                # Movement
                game.canvas.move(self.mobSprite, self.xVelocity, 0)
                self.x += self.xVelocity
                if self.x <= 300 or self.x >= 780:
                    self.xVelocity *= -1
                # Boss transformations
                if self.bossLife:
                    hpScale = self.hp/self.maxHp*60
                    game.canvas.coords(self.hpBar, self.x-30, self.y-37, self.x+hpScale-30, self.y-30)
                elif not self.bossLife:
                    hpScale = self.hp/self.maxHp*100
                    game.canvas.coords(self.hpBar, self.x-100, self.y-67, self.x+hpScale-100, self.y-60)
                # Shoot projectiles
                if self.fireTimer % self.fireDelay == 0:
                    self.attack()
                # Summon minions
                if self.fireTimer % self.summonMinionDelay == 0:
                    if self.type == 1:
                        self.summonSpecialMinions()
                    else:
                        self.summonMinions()
                if self.fireTimer % self.specialSkillDelay == 0:
                    self.specialSkill()
                self.fireTimer += 1
                self.checkDead()
                game.canvas.after(50, self.update)

    def checkDead(self):
        if self.hp <= 0:
            # Final form dead
            if self.bossLife == 0:
                self.dead = True
                # Add score and exp
                game.tower.score += self.expVal
                game.angel.exp += self.expVal
                game.angel.mobCtr += 1
                game.canvas.delete(self.mobSprite)
                game.canvas.delete(self.hpBar)
            # Change to final form
            elif self.bossLife == 1:
                game.canvas.delete(self.mobSprite)
                game.canvas.delete(self.hpBar)
                # Change sprite
                self.mobSprite = game.canvas.create_image(self.x, self.y, image=self.img2)
                self.hpBar = game.canvas.create_rectangle(self.x-95, self.y-67, self.x+5, self.y-60, fill="red")
                # Increase stats
                self.hp = self.maxHp*self.powUpFactor
                self.atk *= self.powUpFactor
                self.fireDelay *= self.powUpFactor
                self.bossLife -= 1

    def attack(self):
        # Shoot projectile
        self.projectile = BossMagicAttack(self.x, self.y, "Down", self.type, self.atk, self.bossLife)
        self.projectile.draw()
        self.projectile.update()

    def summonSpecialMinions(self):
        # Generate a wave of minions
        noOfMobs = 5
        for id in range(0, noOfMobs):
            tempMob = SummonedMob(id, 500+(75*id), self.y+150, not(self.bossLife), game.tower.level, game.tower.floor)
            tempMob.draw()
            tempMob.update()
            game.tower.mobList.append(tempMob)

    def specialSkill(self):
        # Boss Special Skill
        skill = randint(1, (self.type+1)*2)
        if skill == 1:
            game.drainLabel.lift()
            self.skillDur = 2
            game.angel.hp *= 0.6
            self.drain()
        elif skill == 2:
            game.slowLabel.lift()
            self.skillDur = 6
            game.angel.speed /= 2
            self.slow()
        elif skill == 3:
            game.hasteLabel.lift()
            self.skillDur = 6
            self.fireDelay /= 3
            self.xVelocity *= 1.5
            self.haste()
        elif skill == 4:
            game.silenceLabel.lift()
            self.skillDur = 6
            game.angel.silenced = True
            self.silence()
        elif skill == 6:
            game.demiLabel.lift()
            self.skillDur = 2
            self.demi()
        elif skill == 6:
            game.weakenLabel.lift()
            self.skillDur = 6
            game.angel.atk = 0
            self.weaken()

    def silence(self):
        if self.skillDur > 0:
            self.skillDur -= 1
            game.canvas.after(1000, self.silence)
        elif self.skillDur == 0:
            game.angel.silenced = False
            game.silenceLabel.lower()

    def drain(self):
        if self.skillDur > 0:
            self.skillDur -= 1
            game.canvas.after(1000, self.drain)
        elif self.skillDur == 0:
            self.hp += self.maxHp*0.15
            game.drainLabel.lower()

    def slow(self):
        if self.skillDur > 0:
            self.skillDur -= 1
            game.canvas.after(1000, self.slow)
        elif self.skillDur == 0:
            game.angel.speed *= 2
            game.slowLabel.lower()

    def haste(self):
        if self.skillDur > 0:
            self.skillDur -= 1
            game.canvas.after(1000, self.haste)
        elif self.skillDur == 0:
            self.fireDelay *= 3
            self.xVelocity /= 1.5
            game.hasteLabel.lower()

    def demi(self):
        if self.skillDur > 0:
            self.skillDur -= 1
            game.canvas.after(1000, self.demi)
        elif self.skillDur == 0:
            game.angel.hp /= 2
            game.demiLabel.lower()

    def weaken(self):
        if self.skillDur > 0:
            self.skillDur -= 1
            game.canvas.after(1000, self.weaken)
        elif self.skillDur == 0:
            game.angel.atk = game.angel.maxAtk
            game.weakenLabel.lower()


class AngelMagicAttack(MagicAttack):
    def __init__(self, x, y, direction, type, atk):
        # Attack Object data
        super().__init__(x, y, direction, type)
        self.angelAtk = atk
        self.dmgMultList = [1, 2, 4, 1.5, 3, 6]
        self.dmg = self.dmgMultList[self.type] * self.angelAtk
        self.hitboxList = [20, 40, 60, 30, 50, 70]
        self.hitbox = self.hitboxList[self.type]
        game.tower.attackProjectilesList.append(self)
        self.draw()
        self.update()

    def draw(self):
        # Attack Sprites
        self.magicList = [PhotoImage(file="gameAssets/charAtks/orb.png"),
                          PhotoImage(file="gameAssets/charAtks/slash.png"),
                          PhotoImage(file="gameAssets/charAtks/burst.png"),
                          PhotoImage(file="gameAssets/charAtks/enhancedOrb.png"),
                          PhotoImage(file="gameAssets/charAtks/enhancedSlash.png"),
                          PhotoImage(file="gameAssets/charAtks/enhancedBurst.png")
                          ]
        self.img = self.magicList[self.type]
        self.explosionSprite = game.canvas.create_image(self.x, self.y, image=self.img)

    def update(self):
        if game.pause:
            game.canvas.after(50, self.update)
        elif not game.pause:
            # Continue moving after game over
            if self.exist and game.tower.gameOver:
                game.canvas.move(self.explosionSprite, 0, self.yVelocity)
                self.y += self.yVelocity
                self.duration += 1
                self.burnOut()
                if not game.tower.stopMoving:
                    game.canvas.after(50, self.update)
            if self.exist and not game.tower.gameOver:
                # Object movement
                game.canvas.move(self.explosionSprite, 0, self.yVelocity)
                self.y += self.yVelocity
                self.duration += 1
                self.burnOut()
                self.checkAtkCollision(game.tower.mobList)
                game.canvas.after(50, self.update)

    def checkAtkCollision(self, floorMobs):
        # Check collision with mobs
        for mob in floorMobs:
            if abs(self.x-mob.x) <= self.hitbox and abs(self.y-mob.y) <= self.hitbox:
                # Make attack be able to plow through multiple mobs
                temp = mob.hp
                mob.hp -= self.dmg
                self.dmg -= temp
                if self.dmg <= 10:
                    self.exist = False
                    game.canvas.delete(self.explosionSprite)


class Angel:
    def __init__(self, x, y, lvl=1, holyEnergy=0):
        # Angel object data
        self.x = x
        self.y = y
        self.speed = 20
        self.alive = True
        self.mobCtr = holyEnergy
        self.shielded = False
        self.winged = False
        self.transformed = False
        self.buffTime = 21
        self.tWorldCd = 11
        self.hFeelCd = 11
        self.wingAtkCd = 11
        self.gattCd = False
        self.tWCd = False
        self.hFCd = False
        self.silenced = False

        # Char Stats
        self.exp = 0
        self.lvl = lvl
        self.maxHp = 200 + 50*self.lvl
        self.maxMp = 200 + 50*self.lvl
        self.maxAtk = 10 + 1*self.lvl
        self.hp = self.maxHp
        self.mp = self.maxMp
        self.atk = self.maxAtk
        self.shieldHp = self.maxHp

        # Game background
        self.bgimg = PhotoImage(file="gameAssets/gameMisc/map.png")
        game.canvas.create_image(542, 550, image=self.bgimg)

        # Angel Sprites
        self.img = PhotoImage(file="gameAssets/charSprites/mcUp.png")
        self.MCharSprite = game.canvas.create_image(self.x, self.y, image=self.img)
        self.upImg = PhotoImage(file="gameAssets/charSprites/mcUp.png")
        self.leftImg = PhotoImage(file="gameAssets/charSprites/mcLeft.png")
        self.downImg = PhotoImage(file="gameAssets/charSprites/mcDown.png")
        self.rightImg = PhotoImage(file="gameAssets/charSprites/mcRight.png")
        self.transImg = PhotoImage(file="gameAssets/charSprites/Mc.png")

        # Bars
        self.hpBar = game.canvas.create_rectangle(self.x-15, self.y+30, self.x+15, self.y+35, fill="Red")
        self.mpBar = game.canvas.create_rectangle(self.x-15, self.y+37, self.x+15, self.y+42, fill="SteelBlue")

    def moveUp(self, event):
        if not game.pause:
            # Move angel
            if self.y < 500:
                game.canvas.move(self.MCharSprite, 0, self.speed)
                self.y += self.speed
            else:
                game.canvas.move(self.MCharSprite, 0, self.speed*-1)
                self.y -= self.speed
            if self.transformed:
                game.canvas.itemconfig(self.MCharSprite, image=self.transImg)
            else:
                game.canvas.itemconfig(self.MCharSprite, image=self.upImg)
            # Move bars
            game.canvas.coords(self.hpBar, self.x-15, self.y+30, self.x+self.hpScale-15, self.y+35)
            game.canvas.coords(self.mpBar, self.x-15, self.y+37, self.x+self.mpScale-15, self.y+42)
            # Move shield or wings
            if self.shielded:
                game.canvas.coords(self.shield, self.x-20, self.y-50, self.x+20, self.y-20)
                game.canvas.coords(self.sHpBar, self.x-15, self.y+30, self.x+self.sHpScale-15, self.y+35)
            if self.winged:
                game.canvas.coords(self.leftWing, self.x-40, self.y-20)
                game.canvas.coords(self.rightWing, self.x+40, self.y-20)

    def moveLeft(self, event):
        if not game.pause:
            # Move angel
            if self.x <= 50:
                game.canvas.move(self.MCharSprite, self.speed, 0)
                self.x += self.speed
            else:
                game.canvas.move(self.MCharSprite, self.speed*-1, 0)
                self.x -= self.speed
            if self.transformed:
                game.canvas.itemconfig(self.MCharSprite, image=self.transImg)
            else:
                game.canvas.itemconfig(self.MCharSprite, image=self.leftImg)
            # Move bars
            game.canvas.coords(self.hpBar, self.x-15, self.y+30, self.x+self.hpScale-15, self.y+35)
            game.canvas.coords(self.mpBar, self.x-15, self.y+37, self.x+self.mpScale-15, self.y+42)
            # Move shield or wings
            if self.shielded:
                game.canvas.coords(self.shield, self.x-20, self.y-50, self.x+20, self.y-20)
                game.canvas.coords(self.sHpBar, self.x-15, self.y+30, self.x+self.sHpScale-15, self.y+35)
            if self.winged:
                game.canvas.coords(self.leftWing, self.x-40, self.y-20)
                game.canvas.coords(self.rightWing, self.x+40, self.y-20)

    def moveDown(self, event):
        if not game.pause:
            # Move Angel
            if self.y >= 780:
                game.canvas.move(self.MCharSprite, 0, self.speed*-1)
                self.y -= self.speed
            else:
                game.canvas.move(self.MCharSprite, 0, self.speed)
                self.y += self.speed
            if self.transformed:
                game.canvas.itemconfig(self.MCharSprite, image=self.transImg)
            else:
                game.canvas.itemconfig(self.MCharSprite, image=self.downImg)
            # Move bars
            game.canvas.coords(self.hpBar, self.x-15, self.y+30, self.x+self.hpScale-15, self.y+35)
            game.canvas.coords(self.mpBar, self.x-15, self.y+37, self.x+self.mpScale-15, self.y+42)
            # Move shield or wings
            if self.shielded:
                game.canvas.coords(self.shield, self.x-20, self.y-50, self.x+20, self.y-20)
                game.canvas.coords(self.sHpBar, self.x-15, self.y+30, self.x+self.sHpScale-15, self.y+35)
            if self.winged:
                game.canvas.coords(self.leftWing, self.x-40, self.y-20)
                game.canvas.coords(self.rightWing, self.x+40, self.y-20)

    def moveRight(self, event):
        if not game.pause:
            # Move angel
            if self.x > 1030:
                game.canvas.move(self.MCharSprite, self.speed*-1, 0)
                self.x -= self.speed
            else:
                game.canvas.move(self.MCharSprite, self.speed, 0)
                self.x += self.speed
            if self.transformed:
                game.canvas.itemconfig(self.MCharSprite, image=self.transImg)
            else:
                game.canvas.itemconfig(self.MCharSprite, image=self.rightImg)
            # Move bars
            game.canvas.coords(self.hpBar, self.x-15, self.y+30, self.x+self.hpScale-15, self.y+35)
            game.canvas.coords(self.mpBar, self.x-15, self.y+37, self.x+self.mpScale-15, self.y+42)
            # Move shield or wings
            if self.shielded:
                game.canvas.coords(self.shield, self.x-20, self.y-50, self.x+20, self.y-20)
                game.canvas.coords(self.sHpBar, self.x-15, self.y+30, self.x+self.sHpScale-15, self.y+35)
            if self.winged:
                game.canvas.coords(self.leftWing, self.x-40, self.y-20)
                game.canvas.coords(self.rightWing, self.x+40, self.y-20)

    def orbAttack(self, event):
        if not game.pause:
            if self.alive:
                # Enhanced attack
                if self.transformed:
                    game.canvas.itemconfig(self.MCharSprite, image=self.transImg)
                    self.projectile = AngelMagicAttack(self.x, self.y-25, "Up", 3, self.atk)
                    game.tower.attackProjectilesList.append(self.projectile)
                # Normal Attack
                else:
                    game.canvas.itemconfig(self.MCharSprite, image=self.upImg)
                    self.projectile = AngelMagicAttack(self.x, self.y-25, "Up", 0, self.atk)
                    game.tower.attackProjectilesList.append(self.projectile)
                self.mp -= 1

    def slashAttack(self, event):
        if not game.pause:
            if self.alive:
                # Enhanced attack
                if self.transformed:
                    game.canvas.itemconfig(self.MCharSprite, image=self.transImg)
                    self.projectile = AngelMagicAttack(self.x, self.y-25, "Up", 4, self.atk)
                    game.tower.attackProjectilesList.append(self.projectile)
                # Normal attack
                else:
                    game.canvas.itemconfig(self.MCharSprite, image=self.upImg)
                    self.projectile = AngelMagicAttack(self.x, self.y-25, "Up", 1, self.atk)
                    game.tower.attackProjectilesList.append(self.projectile)
                self.mp -= 10

    def shieldAngel(self, event):
        if not game.pause:
            # Create a shield
            if not self.shielded:
                self.shielded = True
                self.shieldHp = self.maxHp
                self.shield = game.canvas.create_arc(self.x-20, self.y-50, self.x+20, self.y-20, style=ARC, width=5, start=0, extent="180", outline="Cyan")
                self.sHpBar = game.canvas.create_rectangle(self.x-15, self.y+30, self.x-15, self.y+35, fill="Blue")
                game.canvas.tag_raise(self.sHpBar)
            # Remove shield
            else:
                self.shieldHp = 0
                game.canvas.tag_raise(self.hpBar)
                self.shielded = False
                game.canvas.delete(self.shield)
                game.canvas.delete(self.sHpBar)

    def burstAttack(self, event):
        if not game.pause:
            if self.alive:
                # Enhanced attack
                if self.transformed:
                    game.canvas.itemconfig(self.MCharSprite, image=self.transImg)
                    self.projectile = AngelMagicAttack(self.x, self.y-25, "Up", 5, self.atk)
                    game.tower.attackProjectilesList.append(self.projectile)
                # Normal attack
                else:
                    game.canvas.itemconfig(self.MCharSprite, image=self.upImg)
                    self.projectile = AngelMagicAttack(self.x, self.y-25, "Up", 2, self.atk)
                    game.tower.attackProjectilesList.append(self.projectile)
                self.mp -= 25

    def inPauseGame(self, event):
        game.pauseGame()

    def showBossKey(self, event):
        # Display boss key
        if game.bossKeyOn:
            game.pauseGame()
            game.bossKeyOn = False
            game.bossKeyFrame.lower()
            game.mainFrame.lift()
            game.gameFrame.lift()
        # Return to game
        elif not game.bossKeyOn:
            game.pauseGame()
            game.bossKeyOn = True
            game.bossKeyFrame.lift()

    def onCheat(self, event):
        # Turn on cheatcodes
        if not game.cheatMode:
            game.cheatMode = True
            self.speed = 100
            # Store temp value
            self.mobMaxCtr = self.mobCtr
        # Turn off cheatcodes
        elif game.cheatMode:
            game.cheatMode = False
            # Return to normal stats
            self.speed = 20
            self.atk = self.maxAtk
            self.hp = self.maxHp
            self.mp = self.maxMp
            self.mobCtr = self.mobMaxCtr

    def transform(self, event=None):
        if not game.pause:
            # Transform buff
            if self.mobCtr >= 10 and not self.transformed and not self.silenced:
                game.wingButton.lower()
                game.transTimerLabel.lift()
                self.mobCtr -= 10
                self.transformed = True
                self.transImg = PhotoImage(file="gameAssets/charSprites/Mc.png")
                game.canvas.itemconfig(self.MCharSprite, image=self.transImg)
                # Double stats
                self.speed *= 2
                self.hp = self.maxHp * 2
                self.mp = self.maxMp * 2
                self.atk = self.maxAtk * 2
                self.buffTimer()
                # Display advanced controls
                game.controlsMenu.lift()

    def buffTimer(self):
        # Transformation duration
        if game.pause:
            game.canvas.after(1000, self.buffTimer)
        elif not game.pause:
            # Decrement timer
            if self.buffTime > 0:
                self.buffTime -= 1
                game.canvas.after(1000, self.buffTimer)
            elif self.buffTime == 0:
                # Show button
                game.transTimerLabel.lower()
                game.wingButton.lift()
                self.transformed = False
                self.buffTime = 21
                game.canvas.itemconfig(self.MCharSprite, image=self.upImg)
                # Return stats to normal
                self.hp = self.maxHp
                self.mp = self.maxMp
                self.atk = self.maxAtk
                self.speed /= 2
                game.controlsMenu0.lift()

    def wingAtk(self, event=None):
        if not game.pause and self.mobCtr >= 5 and not self.gattCd and self.transformed and not self.winged and not self.silenced:
            self.mobCtr -= 5
            self.gattCd = True
            self.wingAtkCd = 5
            self.winged = True
            # Display wings
            self.ltWing = PhotoImage(file="gameAssets/gameMisc/wingLeft.png")
            self.rtWing = PhotoImage(file="gameAssets/gameMisc/wingRight.png")
            self.leftWing = game.canvas.create_image(self.x-40, self.y-20, image=self.ltWing)
            self.rightWing = game.canvas.create_image(self.x+40, self.y-20, image=self.rtWing)
            self.wingTimer = 50
            # Wings movement
            self.wingAtkMov()

    def wingAtkMov(self):
        if game.pause:
            game.canvas.after(100, self.wingAtkMov)
        elif not game.pause:
            if self.wingTimer > 0:
                # Shoot projectiles
                self.projectile = AngelMagicAttack(self.x-40, self.y-35, "Up", 3, self.atk)
                game.tower.attackProjectilesList.append(self.projectile)
                self.projectile = AngelMagicAttack(self.x+40, self.y-35, "Up", 3, self.atk)
                game.tower.attackProjectilesList.append(self.projectile)
                self.wingTimer -= 1
                game.canvas.after(100, self.wingAtkMov)
            elif self.wingTimer == 0:
                # Remove wings
                self.winged = False
                game.canvas.delete(self.leftWing)
                game.canvas.delete(self.rightWing)
                # Hide button and start cooldown
                game.gattCooldown.lift()
                self.wingAttackCd()

    def wingAttackCd(self):
        # Cooldown timer
        if game.pause:
            game.canvas.after(1000, self.wingAttackCd)
        elif not game.pause:
            self.wingAtkCd -= 1
            if self.wingAtkCd == 0:
                # Show button
                game.gattButton.lift()
                self.gattCd = False
            else:
                game.canvas.after(1000, self.wingAttackCd)

    def theWorld(self, event=None):
        # Stops time
        if not game.zW and not game.pause and self.mobCtr >= 10 and not self.tWCd and self.transformed and not self.silenced:
            self.mobCtr -= 10
            self.tWCd = True
            # Creates an arc
            self.dWorld = game.canvas.create_arc(self.x-5, self.y-35, self.x+5, self.y-25, style=ARC, width=5, start=0, extent="180", outline="Violet")
            pos = game.canvas.coords(self.dWorld)
            self.tWorldX1 = pos[0]
            self.tWorldY1 = pos[1]
            self.tWorldX2 = pos[2]
            self.tWorldY2 = pos[3]
            self.tWX = self.x
            self.dWorldTime = 5
            self.tWorldCd = 11
            # Create a shockwave effect
            self.theWorldMove()
            # Stopped time timer
            self.theWorldTimer()

    def theWorldMove(self):
        if game.pause:
            game.canvas.after(50, self.theWorldMove)
        elif not game.pause:
            # Pauses time
            if not game.zW:
                # Grows arc and makes an outward shockwave effect
                if self.tWorldY1 > 101:
                    self.tWorldX1 -= 100
                    self.tWorldY1 -= 100
                    self.tWorldX2 += 100
                    game.canvas.coords(self.dWorld, self.tWorldX1, self.tWorldY1, self.tWorldX2, self.tWorldY2)
                    game.canvas.after(50, self.theWorldMove)
                # Hide arc
                elif self.tWorldY1 <= 100:
                    game.canvas.tag_lower(self.dWorld)
                    game.zW = True
            # Resumes time
            elif game.zW:
                # Shrinks the arc and makes an inward shockwave effect
                if self.tWorldY1 < self.y-100:
                    self.tWorldX1 += 100
                    self.tWorldY1 += 100
                    self.tWorldX2 -= 100
                    game.canvas.coords(self.dWorld, self.tWorldX1, self.tWorldY1, self.tWorldX2, self.tWorldY2)
                    game.canvas.after(50, self.theWorldMove)
                elif self.tWorldY1 >= self.y-100:
                    game.canvas.delete(self.dWorld)
                    game.zW = False
                    # Start cooldown
                    game.tWorldCooldown.lift()
                    self.theWorldCD()

    def theWorldTimer(self):
        # Stop time duration
        if game.pause:
            game.canvas.after(1000, self.theWorldTimer)
        elif not game.pause:
            self.dWorldTime -= 1
            if self.dWorldTime == 0:
                # Reposition the shockwave
                xOffset = self.x - self.tWX
                self.tWorldX1 += xOffset
                self.tWorldX2 += xOffset
                game.canvas.tag_raise(self.dWorld)
                # Resumes time
                self.theWorldMove()
            if self.dWorldTime > 0:
                game.canvas.after(1000, self.theWorldTimer)

    def theWorldCD(self):
        # Skill cooldown
        if game.pause:
            game.canvas.after(1000, self.theWorldCD)
        elif not game.pause:
            self.tWorldCd -= 1
            if self.tWorldCd == 0:
                # Show button
                game.tWorldButton.lift()
                self.tWCd = False
            else:
                game.canvas.after(1000, self.theWorldCD)

    def heavensFeel(self, event=None):
        if not game.pause and self.mobCtr >= 10 and not self.hFCd and self.transformed and not self.silenced:
            self.mobCtr -= 15
            self.hFCd = True
            self.hFeelCd = 10
            self.hFRad = 10
            self.hFX = self.x
            self.hFY = self.y
            self.hp /= 2
            # Create a white orb and move
            self.hFeel = game.canvas.create_oval(self.hFX-5, self.hFY-35, self.hFX+5, self.hFY-25, fill="White")
            self.heavensFeelMov()

    def heavensFeelMov(self):
        if game.pause:
            game.canvas.after(100, self.heavensFeelMov)
        elif not game.pause:
            # Move the orb to the center of map
            if self.hFY > 300:
                game.canvas.move(self.hFeel, 0, -40)
                self.hFY -= 40
                game.canvas.after(100, self.heavensFeelMov)
            # Grow the orb
            elif self.hFY <= 300 and self.hFRad < 20:
                self.hFRad += 1
                pos = game.canvas.coords(self.hFeel)
                xPos1 = pos[0]-self.hFRad*5
                yPos1 = pos[1]-self.hFRad*5
                xPos2 = pos[2]+self.hFRad*5
                yPos2 = pos[3]+self.hFRad*5
                game.canvas.coords(self.hFeel, xPos1, yPos1, xPos2, yPos2)
                game.canvas.after(50, self.heavensFeelMov)
            elif self.hFRad == 20:
                # Damage boss hp by half
                if game.tower.floor % 10 == 5 or game.tower.floor % 10 == 0:
                    game.tower.mobList[0].hp -= game.tower.mobList[0].hp*0.5
                    for i in range(1, len(game.tower.mobList)):
                        game.tower.mobList[i].hp = 0
                # Kills all the mobs
                else:
                    for i in range(0, len(game.tower.mobList)):
                        game.tower.mobList[i].hp = 0
                game.canvas.delete(self.hFeel)
                game.hFeelCooldown.lift()
                self.heavensFeelCD()

    def heavensFeelCD(self):
        # Skill cooldown
        if game.pause:
            game.canvas.after(1000, self.heavensFeelCD)
        elif not game.pause:
            self.hFeelCd -= 1
            if self.hFeelCd == 0:
                # Show button
                game.hFeelButton.lift()
                self.hFCd = False
            else:
                game.canvas.after(1000, self.heavensFeelCD)

    def update(self):
        if game.pause:
            game.canvas.after(50, self.update)
        elif not game.pause:
            if self.alive and not game.tower.gameOver:
                # Cheatcode stats
                if game.cheatMode:
                    self.hpScale = 30
                    self.mpScale = 30
                    self.atk = 99999
                    self.hp = 99999
                    self.mp = 99999
                    self.mobCtr = 999
                else:
                    # Buff stats
                    if self.transformed:
                        self.hpScale = self.hp/self.maxHp * 15
                        self.mpScale = self.mp/self.maxMp * 15
                    # Normal stats
                    else:
                        self.hpScale = self.hp/self.maxHp * 30
                        self.mpScale = self.mp/self.maxMp * 30
                # Move Bars
                game.canvas.coords(self.hpBar, self.x-15, self.y+30, self.x+self.hpScale-15, self.y+35)
                game.canvas.coords(self.mpBar, self.x-15, self.y+37, self.x+self.mpScale-15, self.y+42)
                # Create and move Shield Bar
                if self.shielded:
                    self.sHpScale = self.shieldHp/self.maxHp * 30
                    game.canvas.coords(self.sHpBar, self.x-15, self.y+30, self.x+self.sHpScale-15, self.y+35)
                    self.mp -= 1
                    # Remove shield
                    if self.shieldHp <= 0:
                        self.shielded = False
                        game.canvas.delete(self.shield)
                        game.canvas.delete(self.sHpBar)
                # Dead
                if self.hp <= 0 or self.mp <= 0:
                    self.alive = False
                    game.canvas.delete(self.MCharSprite)
                    game.tower.gameOver = True
                # Level up
                if self.exp >= 100:
                    self.lvl += 1
                    self.exp -= 100
                    self.maxHp = 200 + 50*self.lvl
                    self.maxMp = 200 + 50*self.lvl
                    self.maxAtk = 10 + 1*self.lvl
                    # Temp values
                    self.hp = self.maxHp
                    self.mp = self.maxMp
                    self.atk = self.maxAtk
                game.canvas.after(50, self.update)


game = Game()
game.root.mainloop()
