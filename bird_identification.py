#bird identification program

from tkinter import *
from PIL import ImageTk, Image
from playsound import playsound
import random
import sqlite3

conn = sqlite3.connect("allbirds.db")
c = conn.cursor()

conn1 = sqlite3.connect("mybirds.db")
c1 = conn1.cursor()

mainbg = "#eeffff"
mainfont = "Arial 14"
otherfont = "Arial"
Ftitle = "Display choice of birds"
Ftext = "Can you see your bird?"
Fstitle = "Choose feature"
Fstext = "Which feature is on the bird?"
Mtext = "Back to menu"
Mfont = "Arial 11"
btnbg = "#dbfbfa"
activebtnbg = "#c0f9f7"

menu_birds = ["blackbirdBig", "blackcapBig", "bluetitBig", "bullfinchBig", "buzzardBig", "chaffinchBig",
              "chiffchaffBig", "coaltitBig", "collareddoveBig", "crowBig", "cuckooBig", "dunnockBig",
              "fieldfareBig", "goldcrestBig", "goldfinchBig", "greatspottedwoodpeckerBig", "greattitBig",
              "greenfinchBig", "greenwoodpeckerBig", "greywagtailBig", "housemartinBig", "housesparrowBig",
              "jackdawBig", "jayBig", "kestrelBig", "kingfisherBig", "lesserspottedwoodpeckerBig",
              "linnetBig", "longtailedtitBig", "magpieBig", "mistlethrushBig", "nuthatchBig", "partridgeBig",
              "pheasantfBig", "pheasantmBig", "piedflycatcherfBig", "piedflycatchermBig", "piedwagtailBig",
              "ravenBig", "redkiteBig", "redwingBig", "reedbuntingBig", "robinBig", "rookBig", "siskinBig",
              "skylarkBig", "songthrushBig", "sparrowhawkBig", "spottedflycatcherBig", "starlingBig",
              "swallowBig", "swiftBig", "treecreeperBig", "whitethroatBig", "woodpigeonBig", "wrenBig",
              "yellowhammerBig", "yellowwagtailBig"
              ] #menu will pick a random bird from this list to display every time app is started

def main_menu(menu_birds):
    MM = Tk()
    MM.title("Main menu")
    MM.geometry("300x570+250+50") #the size of the application should be suitable for mobile devices
    MM["bg"] = mainbg #create a window with specific size and colour

    def search_birds_page():
        MM.withdraw()
        SB = Toplevel()
        SB.title("Search birds")
        SB.geometry("300x570+250+50")
        SB["bg"] = mainbg

        entrybg = "#ffffff"
        entrywidth = 24
        btnwidth = 20
        btnheight = 20


        frame1 = Frame(SB)

        entry_search = Entry(frame1, font=mainfont, bg=entrybg, width=entrywidth)
        entry_search.pack(side=LEFT)

        def search_all_birds():

            birdtosearch = entry_search.get()
            entry_search.delete(0, "end")

            def close_failed():
                failed.destroy()

            def close_failed2():
                failed2.destroy()

            try:
                birdtosearchjoined = "".join(birdtosearch.split())
                birdtosearchjoined = birdtosearchjoined.lower() #now ready to search database
            except:
                failed = Toplevel()
                failed.geometry("200x100+300+200")
                failed["bg"] = mainbg
                
                lab0 = Label(failed, text="", bg=mainbg)
                lab0.pack()
                lab_stop = Label(failed, text="Please only use letters", font=mainfont, bg=mainbg)
                lab_stop.pack()
                btn_close = Button(failed, command=close_failed, text="OK", font=mainfont, bg=mainbg, activebackground=activebtnbg)
                btn_close.pack()
                failed.mainloop()
                
            try:
                birds_retrieved = []
                c.execute("SELECT bird FROM birdfiles WHERE bird = ? ",(birdtosearchjoined,))
                for row in c.fetchall():
                    birds_retrieved.append(row[0])
                bird_to_view = birds_retrieved[0]
            except:
                failed2 = Toplevel()
                failed2.geometry("200x100+300+200")
                failed2["bg"] = mainbg
                
                lab0 = Label(failed2, text="", bg=mainbg)
                lab0.pack()
                lab_stop = Label(failed2, text="Found nothing", font=mainfont, bg=mainbg)
                lab_stop.pack()
                btn_close = Button(failed2, command=close_failed2, text="OK", font=mainfont, bg=mainbg, activebackground=activebtnbg)
                btn_close.pack()
                failed2.mainloop()            

            def view_details_3():
                SB.destroy()
                btnwidth = 40
                btnheight = 40
                VD3 = Toplevel()
                VD3.title("View details")
                VD3.geometry("300x570+250+50")
                VD3["bg"] = mainbg

                #bird name goes here 'full_name[0]'
                full_name = []
                c.execute("SELECT birdname FROM birdfiles WHERE bird = ? ",(bird_to_view,))
                for row in c.fetchall():
                    full_name.append(row[0])
                lab_full_name = Label(VD3, text=full_name[0], font=mainfont, bg=mainbg)
                lab_full_name.pack()

                #bird image goes here
                bird_image = []
                c.execute("SELECT image FROM birdfiles WHERE bird = ? ",(bird_to_view,))
                for row in c.fetchall():
                    bird_image.append(row[0])
                
                load_bird_image = Image.open(bird_image[0])
                render_bird_image = ImageTk.PhotoImage(load_bird_image)
                lab_bird_image = Label(VD3, image=render_bird_image, bg=mainbg)
                lab_bird_image.pack()

                frame1 = Frame(VD3, bg=mainbg)
                frame2 = Frame(VD3, bg=mainbg)

                def add_bird():

                    def close_label():
                        stopwindow.destroy()
                    def close_label_2():
                        topwindow.destroy()

                    match_list = []
                    c1.execute("SELECT name FROM mybirdlist")
                    for row in c1.fetchall():
                        match_list.append(row[0])

                    if len(match_list) >= 14:
                        stopwindow = Toplevel()
                        stopwindow.geometry("200x100+300+200")
                        stopwindow["bg"] = mainbg
                        
                        lab0 = Label(stopwindow, text="", bg=mainbg)
                        lab0.pack()
                        lab_stop = Label(stopwindow, text="Cannot add any\n more birds", font=mainfont, bg=mainbg)
                        lab_stop.pack()
                        btn_close = Button(stopwindow, command=close_label, text="OK", font=mainfont, bg=mainbg, activebackground=activebtnbg)
                        btn_close.pack()
                        stopwindow.mainloop()
                    else:                        
                        added = 0
                        for i in range(len(match_list)): # prevents duplicates
                            if bird_to_view == match_list[i]:
                                added += 1
                        if added == 0: #will only add bird if it's not already in the table
                            c1.execute('''INSERT INTO mybirdlist(name) VALUES(?)''',
                                       (bird_to_view,))
                            conn1.commit()
                        else:
                            topwindow = Toplevel()
                            topwindow.geometry("200x100+300+200")
                            topwindow["bg"] = mainbg
                            
                            lab0 = Label(topwindow, text="", bg=mainbg)
                            lab0.pack()
                            lab_stop = Label(topwindow, text="Already added", font=mainfont, bg=mainbg)
                            lab_stop.pack()
                            btn_close = Button(topwindow, command=close_label_2, text="OK", font=mainfont, bg=mainbg, activebackground=activebtnbg)
                            btn_close.pack()
                            topwindow.mainloop()
                        

                load_add = Image.open("add.jpg")
                render_add = ImageTk.PhotoImage(load_add) 
                btn_add = Button(frame1, command=add_bird, image=render_add, bg=mainbg, height=btnheight, width=btnwidth, activebackground=activebtnbg)
                btn_add.pack(side=LEFT)

                bird_sound = []
                c.execute("SELECT sound FROM birdfiles WHERE bird = ? ",(bird_to_view,))
                for row in c.fetchall():
                    bird_sound.append(row[0])

                def play():
                    playsound(bird_sound[0])
                
                load_playsound = Image.open("playsound.jpg")
                render_playsound = ImageTk.PhotoImage(load_playsound)
                btn_playsound = Button(frame1, image=render_playsound, command=play, bg=mainbg, height=btnheight, width=btnwidth, activebackground=activebtnbg)
                btn_playsound.pack(side=LEFT)

                def main_menu_btn():
                    VD3.destroy()
                    MM.deiconify()

                load_back = Image.open("back.jpg")
                render_back = ImageTk.PhotoImage(load_back)
                btn_back = Button(frame1, image=render_back, command=main_menu_btn, bg=mainbg, height=btnheight, width=btnwidth, activebackground=activebtnbg)
                btn_back.pack(side=LEFT)

                frame1.pack()

                bird_text = []
                c.execute("SELECT description FROM birdfiles WHERE bird = ? ",(bird_to_view,))
                for row in c.fetchall():
                    bird_text.append(row[0])

                Bfile = open(bird_text[0], "r")
                bird_details = Label(frame2, text=Bfile.read(), justify=LEFT, font=mainfont, bg=mainbg)
                bird_details.pack()

                frame2.pack()

                VD3.mainloop()
                
            btn_bird = Button(SB, command=view_details_3, text=bird_to_view, bg=mainbg, font=mainfont, activebackground=activebtnbg, width=20)
            btn_bird.pack()

        load_search = Image.open("search.jpg")
        render_search = ImageTk.PhotoImage(load_search)
        btn_search = Button(frame1, command=search_all_birds, image=render_search, bg=mainbg, activebackground=activebtnbg, width=btnwidth, height=btnheight)
        btn_search.pack()

        frame1.pack()

        def main_menu_btn():
                SB.destroy()
                MM.deiconify()
                
        menu_btn = Button(SB, command=main_menu_btn, text=Mtext, font=Mfont, bg=mainbg, activebackground=activebtnbg)
        menu_btn.pack()

        SB.mainloop()

    def my_identified_birds():
        MM.withdraw()
        MB = Toplevel()
        MB.title("My birds")
        MB.geometry("300x570+250+50")
        MB["bg"] = mainbg

        frame1 = Frame(MB, bg=mainbg)

        lab_title = Label(frame1, text="My birds", font=mainfont, bg=mainbg)
        lab_title.pack(side=LEFT)

        def main_menu_btn():
            MB.destroy()
            MM.deiconify()

        menu_btn = Button(frame1, command=main_menu_btn, text=Mtext, font=Mfont, bg=mainbg, activebackground=activebtnbg)
        menu_btn.pack()

        frame1.pack()

        def view_details_2(bird):
            MB.destroy()
            btnwidth = 40
            btnheight = 40
            VD2 = Toplevel()
            VD2.title("View details")
            VD2.geometry("300x570+250+50")
            VD2["bg"] = mainbg

            #bird name goes here 'full_name[0]'
            full_name = []
            c.execute("SELECT birdname FROM birdfiles WHERE bird = ? ",(bird,))
            for row in c.fetchall():
                full_name.append(row[0])
            lab_full_name = Label(VD2, text=full_name[0], font=mainfont, bg=mainbg)
            lab_full_name.pack()

            #bird image goes here
            bird_image = []
            c.execute("SELECT image FROM birdfiles WHERE bird = ? ",(bird,))
            for row in c.fetchall():
                bird_image.append(row[0])
            
            load_bird_image = Image.open(bird_image[0])
            render_bird_image = ImageTk.PhotoImage(load_bird_image)
            lab_bird_image = Label(VD2, image=render_bird_image, bg=mainbg)
            lab_bird_image.pack()

            frame1 = Frame(VD2, bg=mainbg)
            frame2 = Frame(VD2, bg=mainbg)

            def remove_bird(): 

                def close_label():
                    topwindow.destroy()


                c1.execute('''DELETE FROM mybirdlist WHERE name=?''',
                           (bird,))
                conn1.commit()

                topwindow = Toplevel()
                topwindow.geometry("200x100+300+200")
                topwindow["bg"] = mainbg
                
                lab0 = Label(topwindow, text="", bg=mainbg)
                lab0.pack()
                lab_stop = Label(topwindow, text="Bird removed", font=mainfont, bg=mainbg)
                lab_stop.pack()
                btn_close = Button(topwindow, command=close_label, text="OK", font=mainfont, bg=mainbg, activebackground=activebtnbg)
                btn_close.pack()
                topwindow.mainloop()
                

            load_remove = Image.open("remove.jpg")
            render_remove = ImageTk.PhotoImage(load_remove) 
            btn_add = Button(frame1, command=remove_bird, image=render_remove, bg=mainbg, height=btnheight, width=btnwidth, activebackground=activebtnbg)
            btn_add.pack(side=LEFT)

            bird_sound = []
            c.execute("SELECT sound FROM birdfiles WHERE bird = ? ",(bird,))
            for row in c.fetchall():
                bird_sound.append(row[0])

            def play():
                playsound(bird_sound[0])
            
            load_playsound = Image.open("playsound.jpg")
            render_playsound = ImageTk.PhotoImage(load_playsound)
            btn_playsound = Button(frame1, image=render_playsound, command=play, bg=mainbg, height=btnheight, width=btnwidth, activebackground=activebtnbg)
            btn_playsound.pack(side=LEFT)

            def main_menu_btn():
                VD2.destroy()
                MM.deiconify()

            load_back = Image.open("back.jpg")
            render_back = ImageTk.PhotoImage(load_back)
            btn_back = Button(frame1, image=render_back, command=main_menu_btn, bg=mainbg, height=btnheight, width=btnwidth, activebackground=activebtnbg)
            btn_back.pack(side=LEFT)

            frame1.pack()

            bird_text = []
            c.execute("SELECT description FROM birdfiles WHERE bird = ? ",(bird,))
            for row in c.fetchall():
                bird_text.append(row[0])

            Bfile = open(bird_text[0], "r")
            bird_details = Label(frame2, text=Bfile.read(), justify=LEFT, font=mainfont, bg=mainbg)
            bird_details.pack()

            frame2.pack()

            VD2.mainloop()

        my_birds_list = []
        c1.execute("SELECT name FROM mybirdlist")
        for row in c1.fetchall():
            my_birds_list.append(row[0])

        for i in my_birds_list:
            def cmd(x=i):
                view_details_2(x)
            btn = Button(MB, command=cmd, text=i, font=mainfont, width=20, bg=mainbg, activebackground=activebtnbg)
            btn.pack()

        MB.mainloop()

    def view_details(bird):
        btnwidth = 40
        btnheight = 40
        VD = Toplevel()
        VD.title("View details")
        VD.geometry("300x570+250+50")
        VD["bg"] = mainbg

        #bird name goes here 'full_name[0]'
        full_name = []
        c.execute("SELECT birdname FROM birdfiles WHERE bird = ? ",(bird,))
        for row in c.fetchall():
            full_name.append(row[0])
        lab_full_name = Label(VD, text=full_name[0], font=mainfont, bg=mainbg)
        lab_full_name.pack()

        #bird image goes here
        bird_image = []
        c.execute("SELECT image FROM birdfiles WHERE bird = ? ",(bird,))
        for row in c.fetchall():
            bird_image.append(row[0])
        
        load_bird_image = Image.open(bird_image[0])
        render_bird_image = ImageTk.PhotoImage(load_bird_image)
        lab_bird_image = Label(VD, image=render_bird_image, bg=mainbg)
        lab_bird_image.pack()

        frame1 = Frame(VD, bg=mainbg)
        frame2 = Frame(VD, bg=mainbg)

        def add_bird():

            def close_label():
                stopwindow.destroy()
            def close_label_2():
                topwindow.destroy()

            match_list = []
            c1.execute("SELECT name FROM mybirdlist")
            for row in c1.fetchall():
                match_list.append(row[0])

            if len(match_list) >= 14:
                stopwindow = Toplevel()
                stopwindow.geometry("200x100+300+200")
                stopwindow["bg"] = mainbg
                
                lab0 = Label(stopwindow, text="", bg=mainbg)
                lab0.pack()
                lab_stop = Label(stopwindow, text="Cannot add any \nmore birds", font=mainfont, bg=mainbg)
                lab_stop.pack()
                btn_close = Button(stopwindow, command=close_label, text="OK", font=mainfont, bg=mainbg, activebackground=activebtnbg)
                btn_close.pack()
                stopwindow.mainloop()
            else:                        
                added = 0
                for i in range(len(match_list)): # prevents duplicates
                    if bird == match_list[i]:
                        added += 1
                if added == 0: #will only add bird if it's not already in the table
                    c1.execute('''INSERT INTO mybirdlist(name) VALUES(?)''',
                               (bird,))
                    conn1.commit()
                else:
                    topwindow = Toplevel()
                    topwindow.geometry("200x100+300+200")
                    topwindow["bg"] = mainbg
                    
                    lab0 = Label(topwindow, text="", bg=mainbg)
                    lab0.pack()
                    lab_stop = Label(topwindow, text="Already added", font=mainfont, bg=mainbg)
                    lab_stop.pack()
                    btn_close = Button(topwindow, command=close_label_2, text="OK", font=mainfont, bg=mainbg, activebackground=activebtnbg)
                    btn_close.pack()
                    topwindow.mainloop()
                

        load_add = Image.open("add.jpg")
        render_add = ImageTk.PhotoImage(load_add)
        btn_add = Button(frame1, command=add_bird, image=render_add, bg=mainbg, height=btnheight, width=btnwidth, activebackground=activebtnbg)
        btn_add.pack(side=LEFT)

        bird_sound = []
        c.execute("SELECT sound FROM birdfiles WHERE bird = ? ",(bird,))
        for row in c.fetchall():
            bird_sound.append(row[0])

        def play():
            playsound(bird_sound[0])
        
        load_playsound = Image.open("playsound.jpg")
        render_playsound = ImageTk.PhotoImage(load_playsound)
        btn_playsound = Button(frame1, image=render_playsound, command=play, bg=mainbg, height=btnheight, width=btnwidth, activebackground=activebtnbg)
        btn_playsound.pack(side=LEFT)

        def main_menu_btn():
            VD.destroy()
            MM.deiconify()

        load_back = Image.open("back.jpg")
        render_back = ImageTk.PhotoImage(load_back)
        btn_back = Button(frame1, image=render_back, command=main_menu_btn, bg=mainbg, height=btnheight, width=btnwidth, activebackground=activebtnbg)
        btn_back.pack(side=LEFT)

        frame1.pack()

        bird_text = []
        c.execute("SELECT description FROM birdfiles WHERE bird = ? ",(bird,))
        for row in c.fetchall():
            bird_text.append(row[0])

        Bfile = open(bird_text[0], "r")
        bird_details = Label(frame2, text=Bfile.read(), justify=LEFT, font=mainfont, bg=mainbg)
        bird_details.pack()

        frame2.pack()

        VD.mainloop()

    def search_birds(): #define functions before creating buttons that use them
        print("search function")

    def my_birds():
        print("my birds list")

    def fCS(): #function Choose Size
        MM.withdraw()
        otherfont = "Arial"
        CStitle = "Choose size"
        CStext = "What size is the bird?"
        btnwidth = 140
        btnheight = 150 
        
        CS = Toplevel()
        CS.title(CStitle)
        CS.geometry("300x570+250+50")
        CS["bg"] = mainbg 

        def fCCs(): #CHOOSE COLOUR SMALL
            CS.destroy()
            CCtitle = "Choose colour"
            CCtext = "Which main colour is the bird?"
            Ftitle = "Display choice of birds"
            Ftext = "Can you see your bird?"
            btnwidth = 140
            btnheight = 100
            
            CCs = Toplevel()
            CCs.title(CCtitle)
            CCs.geometry("300x570+250+50")
            CCs["bg"] = mainbg

            lab_title = Label(CCs, text=CCtext, bg=mainbg, font=mainfont)
            lab_title.pack()

            def main_menu_btn():
                CCs.destroy()
                MM.deiconify()

            menu_btn = Button(CCs, command=main_menu_btn, text=Mtext, bg=btnbg, activebackground=activebtnbg, font=Mfont)
            menu_btn.pack()

            lab_space = Label(CCs, text="", bg=mainbg)
            lab_space.pack()

            ##### COMMANDS FOR COLOUR CHOICES #####

            def fsBl():
                CCs.destroy()
                sBl = Toplevel()
                sBl.title(Ftitle)
                sBl.geometry("300x570+250+50")
                sBl["bg"] = mainbg

                btnwidth = 250

                frame1 = Frame(sBl)

                lab_title = Label(frame1, text=Ftext, bg=mainbg, font=mainfont)
                lab_title.pack(side=LEFT)

                def main_menu_btn():
                    sBl.destroy()
                    MM.deiconify()

                menu_btn = Button(frame1, command=main_menu_btn, text=Mtext, bg=btnbg, activebackground=activebtnbg, font=Mfont)
                menu_btn.pack()

                frame1.pack()

                def bridgebt():
                    sBl.destroy()
                    view_details("bluetit")

                def bridgekf():
                    sBl.destroy()
                    view_details("kingfisher")

                load_bluetit = Image.open("bluetit.jpg")
                render_bluetit = ImageTk.PhotoImage(load_bluetit)
                btn_bluetit = Button(sBl, compound=LEFT, command=bridgebt, image=render_bluetit, text="Blue Tit", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                btn_bluetit.pack()

                load_kingfisher = Image.open("kingfisher.jpg")
                render_kingfisher = ImageTk.PhotoImage(load_kingfisher)
                btn_kingfisher = Button(sBl, compound=LEFT, command=bridgekf, image=render_kingfisher, text="Kingfisher", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                btn_kingfisher.pack()
                
                sBl.mainloop()

            def fsGrey():
                CCs.destroy()
                sGrey = Toplevel()
                sGrey.title(Fstitle)
                sGrey.geometry("300x570+250+50")
                sGrey["bg"] = mainbg

                btnwidth = 140
                btnheight = 100

                lab_title = Label(sGrey, text=Fstext, bg=mainbg, font=mainfont)
                lab_title.pack()

                def main_menu_btn():
                    sGrey.destroy()
                    MM.deiconify()

                menu_btn = Button(sGrey, command=main_menu_btn, text=Mtext, bg=btnbg, activebackground=activebtnbg, font=Mfont)
                menu_btn.pack()

                lab_space = Label(sGrey, text="", bg=mainbg)
                lab_space.pack()

                def fsGBY():
                    sGrey.destroy()
                    sGBY = Toplevel()
                    sGBY.title(Ftitle)
                    sGBY.geometry("300x570+250+50")
                    sGBY["bg"] = mainbg

                    btnwidth = 250

                    frame1 = Frame(sGBY)

                    lab_title = Label(frame1, text=Ftext, bg=mainbg, font=mainfont)
                    lab_title.pack(side=LEFT)

                    def main_menu_btn():
                        sGBY.destroy()
                        MM.deiconify()

                    menu_btn = Button(frame1, command=main_menu_btn, text=Mtext, bg=btnbg, activebackground=activebtnbg, font=Mfont)
                    menu_btn.pack()

                    frame1.pack()

                    def bridgebc():
                        sGBY.destroy()
                        view_details("blackcap")

                    def bridgect():
                        sGBY.destroy()
                        view_details("coaltit")

                    load_blackcap = Image.open("blackcap.jpg")
                    render_blackcap = ImageTk.PhotoImage(load_blackcap)
                    btn_blackcap = Button(sGBY, command=bridgebc, compound=LEFT, image=render_blackcap, text="Blackcap", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_blackcap.pack()

                    load_coaltit = Image.open("coaltit.jpg")
                    render_coaltit = ImageTk.PhotoImage(load_coaltit)
                    btn_coaltit = Button(sGBY, command=bridgect, compound=LEFT, image=render_coaltit, text="Coal Tit", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_coaltit.pack()

                    sGBY.mainloop()

                def fsGBN():
                    sGrey.destroy()
                    sGBN = Toplevel() 
                    sGBN.title(Ftitle)
                    sGBN.geometry("300x570+250+50")
                    sGBN["bg"] = mainbg

                    btnwidth = 250

                    frame1 = Frame(sGBN)

                    lab_title = Label(frame1, text=Ftext, bg=mainbg, font=mainfont)
                    lab_title.pack(side=LEFT)

                    def main_menu_btn():
                        sGBN.destroy()
                        MM.deiconify()

                    menu_btn = Button(frame1, command=main_menu_btn, text=Mtext, bg=btnbg, activebackground=activebtnbg, font=Mfont)
                    menu_btn.pack()

                    frame1.pack()

                    def bridged():
                        sGBN.destroy()
                        view_details("dunnock")

                    def bridgegw():
                        sGBN.destroy()
                        view_details("greywagtail")

                    def bridgehs():
                        sGBN.destroy()
                        view_details("housesparrow")

                    def bridgen():
                        sGBN.destroy()
                        view_details("nuthatch")

                    load_dunnock = Image.open("dunnock.jpg")
                    render_dunnock = ImageTk.PhotoImage(load_dunnock)
                    btn_dunnock = Button(sGBN, command=bridged, compound=LEFT, image=render_dunnock, text="Dunnock", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_dunnock.pack()

                    load_greywagtail = Image.open("greywagtail.jpg")
                    render_greywagtail = ImageTk.PhotoImage(load_greywagtail)
                    btn_greywagtail = Button(sGBN, command=bridgegw, compound=LEFT, image=render_greywagtail, text="Grey Wagtail", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_greywagtail.pack()

                    load_housesparrow = Image.open("housesparrow.jpg")
                    render_housesparrow = ImageTk.PhotoImage(load_housesparrow)
                    btn_housesparrow = Button(sGBN, command=bridgehs, compound=LEFT, image=render_housesparrow, text="House Sparrow", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_housesparrow.pack()

                    load_nuthatch = Image.open("nuthatch.jpg")
                    render_nuthatch = ImageTk.PhotoImage(load_nuthatch)
                    btn_nuthatch = Button(sGBN, command=bridgen, compound=LEFT, image=render_nuthatch, text="Nuthatch", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_nuthatch.pack()

                    sGBN.mainloop()

                frame1 = Frame(sGrey)

                load_blacktophead = Image.open("blacktophead.jpg")
                render_blacktophead = ImageTk.PhotoImage(load_blacktophead)
                btn_blacktophead = Button(frame1, command=fsGBY, compound=TOP, image=render_blacktophead, text="Black top of head", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth, height=btnheight)
                btn_blacktophead.pack(side=LEFT)

                load_none = Image.open("none.jpg")
                render_none = ImageTk.PhotoImage(load_none)
                btn_none = Button(frame1, command=fsGBN, compound=TOP, image=render_none, text="None", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth, height=btnheight)
                btn_none.pack(side=LEFT)

                frame1.pack()

                sGrey.mainloop()

            def fsPalebrown():
                CCs.destroy()
                sPalebrown = Toplevel()
                sPalebrown.title(Fstitle)
                sPalebrown.geometry("300x570+250+50")
                sPalebrown["bg"] = mainbg

                btnwidth = 140
                btnheight = 100

                lab_title = Label(sPalebrown, text=Fstext, bg=mainbg, font=mainfont)
                lab_title.pack()

                def main_menu_btn():
                    sPalebrown.destroy()
                    MM.deiconify()

                menu_btn = Button(sPalebrown, command=main_menu_btn, text=Mtext, bg=btnbg, activebackground=activebtnbg, font=Mfont)
                menu_btn.pack()

                lab_space = Label(sPalebrown, text="", bg=mainbg)
                lab_space.pack()

                def fsPBY():
                    sPalebrown.destroy()
                    sPBY = Toplevel()
                    sPBY.title(Ftitle)
                    sPBY.geometry("300x570+250+50")
                    sPBY["bg"] = mainbg

                    btnwidth = 250

                    frame1 = Frame(sPBY)

                    lab_title = Label(frame1, text=Ftext, bg=mainbg, font=mainfont)
                    lab_title.pack(side=LEFT)

                    def main_menu_btn():
                        sPBY.destroy()
                        MM.deiconify()

                    menu_btn = Button(frame1, command=main_menu_btn, text=Mtext, bg=btnbg, activebackground=activebtnbg, font=Mfont)
                    menu_btn.pack()

                    frame1.pack()

                    def bridgect():
                        sPBY.destroy()
                        view_details("coaltit")

                    def bridgegf():
                        sPBY.destroy()
                        view_details("goldfinch")

                    def bridgeltt():
                        sPBY.destroy()
                        view_details("longtailedtit")

                    load_coaltit = Image.open("coaltit.jpg")
                    render_coaltit = ImageTk.PhotoImage(load_coaltit)
                    btn_coaltit = Button(sPBY, command=bridgect, compound=LEFT, image=render_coaltit, text="Coal Tit", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_coaltit.pack()

                    load_goldfinch = Image.open("goldfinch.jpg")
                    render_goldfinch = ImageTk.PhotoImage(load_goldfinch)
                    btn_goldfinch = Button(sPBY, command=bridgegf, compound=LEFT, image=render_goldfinch, text="Goldfinch", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_goldfinch.pack()

                    load_longtailedtit = Image.open("longtailedtit.jpg")
                    render_longtailedtit = ImageTk.PhotoImage(load_longtailedtit)
                    btn_longtailedtit = Button(sPBY, command=bridgeltt, compound=LEFT, image=render_longtailedtit, text="Long Tailed Tit", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_longtailedtit.pack()

                    sPBY.mainloop()

                def fsPBN():
                    sPalebrown.destroy()
                    sPBN = Toplevel()
                    sPBN.title(Ftitle)
                    sPBN.geometry("300x570+250+50")
                    sPBN["bg"] = mainbg

                    btnwidth = 250

                    frame1 = Frame(sPBN)

                    lab_title = Label(frame1, text=Ftext, bg=mainbg, font=mainfont)
                    lab_title.pack(side=LEFT)

                    def main_menu_btn():
                        sPBN.destroy()
                        MM.deiconify()

                    menu_btn = Button(frame1, command=main_menu_btn, text=Mtext, bg=btnbg, activebackground=activebtnbg, font=Mfont)
                    menu_btn.pack()

                    frame1.pack()

                    def bridgec():
                        sPBN.destroy()
                        view_details("chiffchaff")

                    def bridges():
                        sPBN.destroy()
                        view_details("skylark")

                    load_chiffchaff = Image.open("chiffchaff.jpg")
                    render_chiffchaff = ImageTk.PhotoImage(load_chiffchaff)
                    btn_chiffchaff = Button(sPBN, command=bridgec, compound=LEFT, image=render_chiffchaff, text="Chiffchaff", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_chiffchaff.pack()

                    load_skylark = Image.open("skylark.jpg")
                    render_skylark = ImageTk.PhotoImage(load_skylark)
                    btn_skylark = Button(sPBN, command=bridges, compound=LEFT, image=render_skylark, text="Skylark", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_skylark.pack()

                    sPBN.mainloop()

                frame1 = Frame(sPalebrown)

                load_blackonhead = Image.open("blackonhead.jpg")
                render_blackonhead = ImageTk.PhotoImage(load_blackonhead)
                btn_blackonhead = Button(frame1, command=fsPBY, compound=TOP, image=render_blackonhead, text="Black on head", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth, height=btnheight)
                btn_blackonhead.pack(side=LEFT)

                load_none = Image.open("none.jpg")
                render_none = ImageTk.PhotoImage(load_none)
                btn_none = Button(frame1, command=fsPBN, compound=TOP, image=render_none, text="None", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth, height=btnheight)
                btn_none.pack(side=LEFT)

                frame1.pack()

                sPalebrown.mainloop()

            def fsYellowgreen():
                CCs.destroy()
                sYellowgreen = Toplevel()
                sYellowgreen.title(Fstitle)
                sYellowgreen.geometry("300x570+250+50")
                sYellowgreen["bg"] = mainbg

                btnwidth = 140
                btnheight = 100    

                lab_title = Label(sYellowgreen, text=Fstext, bg=mainbg, font=mainfont)
                lab_title.pack()

                def main_menu_btn():
                    sYellowgreen.destroy()
                    MM.deiconify()

                menu_btn = Button(sYellowgreen, command=main_menu_btn, text=Mtext, bg=btnbg, activebackground=activebtnbg, font=Mfont)
                menu_btn.pack()

                lab_space = Label(sYellowgreen, text="", bg=mainbg)
                lab_space.pack()

                def fsYBY():
                    sYellowgreen.destroy()
                    sYBY = Toplevel()
                    sYBY.title(Ftitle)
                    sYBY.geometry("300x570+250+50")
                    sYBY["bg"] = mainbg

                    btnwidth = 250

                    frame1 = Frame(sYBY)

                    lab_title = Label(frame1, text=Ftext, bg=mainbg, font=mainfont)
                    lab_title.pack(side=LEFT)

                    def main_menu_btn():
                        sYBY.destroy()
                        MM.deiconify()

                    menu_btn = Button(frame1, command=main_menu_btn, text=Mtext, bg=btnbg, activebackground=activebtnbg, font=Mfont)
                    menu_btn.pack()

                    frame1.pack()

                    def bridgebt():
                        sYBY.destroy()
                        view_details("bluetit")

                    def bridgegt():
                        sYBY.destroy()
                        view_details("greattit")

                    def bridges():
                        sYBY.destroy()
                        view_details("siskin")

                    load_bluetit = Image.open("bluetit.jpg")
                    render_bluetit = ImageTk.PhotoImage(load_bluetit)
                    btn_bluetit = Button(sYBY, command=bridgebt, compound=LEFT, image=render_bluetit, text="Blue Tit", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_bluetit.pack()

                    load_greattit = Image.open("greattit.jpg")
                    render_greattit = ImageTk.PhotoImage(load_greattit)
                    btn_greattit = Button(sYBY, command=bridgegt, compound=LEFT, image=render_greattit, text="Great Tit", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_greattit.pack()

                    load_siskin = Image.open("siskin.jpg")
                    render_siskin = ImageTk.PhotoImage(load_siskin)
                    btn_siskin = Button(sYBY, command=bridges, compound=LEFT, image=render_siskin, text="Siskin", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_siskin.pack()

                    sYBY.mainloop()

                def fsYBN():
                    sYellowgreen.destroy()
                    sYBN = Toplevel()
                    sYBN.title(Ftitle)
                    sYBN.geometry("300x570+250+50")
                    sYBN["bg"] = mainbg

                    btnwidth = 250

                    frame1 = Frame(sYBN)

                    lab_title = Label(frame1, text=Ftext, bg=mainbg, font=mainfont)
                    lab_title.pack(side=LEFT)

                    def main_menu_btn():
                        sYBN.destroy()
                        MM.deiconify()

                    menu_btn = Button(frame1, command=main_menu_btn, text=Mtext, bg=btnbg, activebackground=activebtnbg, font=Mfont)
                    menu_btn.pack()

                    frame1.pack()

                    def bridgegf():
                        sYBN.destroy()
                        view_details("greenfinch")

                    def bridgegw():
                        sYBN.destroy()
                        view_details("greywagtail")

                    def bridgeyw():
                        sYBN.destroy()
                        view_details("yellowwagtail")

                    def bridgeyh():
                        sYBN.destroy()
                        view_details("yellowhammer")

                    load_greenfinch = Image.open("greenfinch.jpg")
                    render_greenfinch = ImageTk.PhotoImage(load_greenfinch)
                    btn_greenfinch = Button(sYBN, command=bridgegf, compound=LEFT, image=render_greenfinch, text="Greenfinch", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_greenfinch.pack()

                    load_greywagtail = Image.open("greywagtail.jpg")
                    render_greywagtail = ImageTk.PhotoImage(load_greywagtail)
                    btn_greywagtail = Button(sYBN, command=bridgegw, compound=LEFT, image=render_greywagtail, text="Grey Wagtail", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_greywagtail.pack()

                    load_yellowwagtail = Image.open("yellowwagtail.jpg")
                    render_yellowwagtail = ImageTk.PhotoImage(load_yellowwagtail)
                    btn_yellowwagtail = Button(sYBN, command=bridgeyw, compound=LEFT, image=render_yellowwagtail, text="Yellow Wagtail", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_yellowwagtail.pack()

                    load_yellowhammer = Image.open("yellowhammer.jpg")
                    render_yellowhammer = ImageTk.PhotoImage(load_yellowhammer)
                    btn_yellowhammer = Button(sYBN, command=bridgeyh, compound=LEFT, image=render_yellowhammer, text="Yellowhammer", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_yellowhammer.pack()

                    sYBN.mainloop()

                frame1 = Frame(sYellowgreen)

                load_blueblackhead = Image.open("blueblackhead.jpg")
                render_blueblackhead = ImageTk.PhotoImage(load_blueblackhead)
                btn_blueblackhead = Button(frame1, command=fsYBY, compound=TOP, image=render_blueblackhead, text="Blue/black on head", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth, height=btnheight)
                btn_blueblackhead.pack(side=LEFT)

                load_none = Image.open("none.jpg")
                render_none = ImageTk.PhotoImage(load_none)
                btn_none = Button(frame1, command=fsYBN, compound=TOP, image=render_none, text="None", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth, height=btnheight)
                btn_none.pack(side=LEFT)

                frame1.pack()

                sYellowgreen.mainloop()

            def fsOrangeredpink():
                CCs.destroy()
                sOrangeredpink = Toplevel()
                sOrangeredpink.title(Fstitle)
                sOrangeredpink.geometry("300x570+250+50")
                sOrangeredpink["bg"] = mainbg

                btnwidth = 140
                btnheight = 100

                lab_title = Label(sOrangeredpink, text=Fstext, bg=mainbg, font=mainfont)
                lab_title.pack()

                def main_menu_btn():
                    sOrangeredpink.destroy()
                    MM.deiconify()

                menu_btn = Button(sOrangeredpink, command=main_menu_btn, text=Mtext, bg=btnbg, activebackground=activebtnbg, font=Mfont)
                menu_btn.pack()

                lab_space = Label(sOrangeredpink, text="", bg=mainbg)
                lab_space.pack()

                def fsOG():
                    sOrangeredpink.destroy()
                    sOG = Toplevel()
                    sOG.title(Ftitle)
                    sOG.geometry("300x570+250+50")
                    sOG["bg"] = mainbg

                    btnwidth = 250

                    frame1 = Frame(sOG)

                    lab_title = Label(frame1, text=Ftext, bg=mainbg, font=mainfont)
                    lab_title.pack(side=LEFT)

                    def main_menu_btn():
                        sOG.destroy()
                        MM.deiconify()

                    menu_btn = Button(frame1, command=main_menu_btn, text=Mtext, bg=btnbg, activebackground=activebtnbg, font=Mfont)
                    menu_btn.pack()

                    frame1.pack()

                    def bridgec():
                        sOG.destroy()
                        view_details("chaffinch")

                    def bridgel():
                        sOG.destroy()
                        view_details("linnet")

                    def bridgen():
                        sOG.destroy()
                        view_details("nuthatch")

                    load_chaffinch = Image.open("chaffinch.jpg")
                    render_chaffinch = ImageTk.PhotoImage(load_chaffinch)
                    btn_chaffinch = Button(sOG, command=bridgec, compound=LEFT, image=render_chaffinch, text="Chaffinch", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_chaffinch.pack()

                    load_linnet = Image.open("linnet.jpg")
                    render_linnet = ImageTk.PhotoImage(load_linnet)
                    btn_linnet = Button(sOG, command=bridgel, compound=LEFT, image=render_linnet, text="Linnet", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_linnet.pack()

                    load_nuthatch = Image.open("nuthatch.jpg")
                    render_nuthatch = ImageTk.PhotoImage(load_nuthatch)
                    btn_nuthatch = Button(sOG, command=bridgen, compound=LEFT, image=render_nuthatch, text="Nuthatch", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_nuthatch.pack()

                    sOG.mainloop()

                def fsON():
                    sOrangeredpink.destroy()
                    sON = Toplevel()
                    sON.title(Ftitle)
                    sON.geometry("300x570+250+50")
                    sON["bg"] = mainbg

                    btnwidth = 250

                    frame1 = Frame(sON)

                    lab_title = Label(frame1, text=Ftext, bg=mainbg, font=mainfont)
                    lab_title.pack(side=LEFT)

                    def main_menu_btn():
                        sON.destroy()
                        MM.deiconify()

                    def bridgeb():
                        sON.destroy()
                        view_details("bullfinch")

                    def bridgegf():
                        sON.destroy()
                        view_details("goldfinch")

                    def bridger():
                        sON.destroy()
                        view_details("robin")

                    menu_btn = Button(frame1, command=main_menu_btn, text=Mtext, bg=btnbg, activebackground=activebtnbg, font=Mfont)
                    menu_btn.pack()

                    frame1.pack()

                    load_bullfinch = Image.open("bullfinch.jpg")
                    render_bullfinch = ImageTk.PhotoImage(load_bullfinch)
                    btn_bullfinch = Button(sON, command=bridgeb, compound=LEFT, image=render_bullfinch, text="Bullfinch", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_bullfinch.pack()

                    load_goldfinch = Image.open("goldfinch.jpg")
                    render_goldfinch = ImageTk.PhotoImage(load_goldfinch)
                    btn_goldfinch = Button(sON, command=bridgegf, compound=LEFT, image=render_goldfinch, text="Goldfinch", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_goldfinch.pack()

                    load_robin = Image.open("robin.jpg")
                    render_robin = ImageTk.PhotoImage(load_robin)
                    btn_robin = Button(sON, command=bridger, compound=LEFT, image=render_robin, text="Robin", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_robin.pack()

                    sON.mainloop()

                frame1 = Frame(sOrangeredpink)

                load_greyonhead = Image.open("greyonhead.jpg")
                render_greyonhead = ImageTk.PhotoImage(load_greyonhead)
                btn_greyonhead = Button(frame1, command=fsOG, compound=TOP, image=render_greyonhead, text="Grey on head", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth, height=btnheight)
                btn_greyonhead.pack(side=LEFT)

                load_none = Image.open("none.jpg")
                render_none = ImageTk.PhotoImage(load_none)
                btn_none = Button(frame1, command=fsON, compound=TOP, image=render_none, text="None", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth, height=btnheight)
                btn_none.pack(side=LEFT)

                frame1.pack()

                sOrangeredpink.mainloop()

            def fsWhite():
                CCs.destroy()
                sWhite = Toplevel()
                sWhite.title(Fstitle)
                sWhite.geometry("300x570+250+50")
                sWhite["bg"] = mainbg

                btnwidth = 140
                btnheight = 100

                lab_title = Label(sWhite, text=Fstext, bg=mainbg, font=mainfont)
                lab_title.pack()

                def main_menu_btn():
                    sWHite.destroy()
                    MM.deiconify()

                menu_btn = Button(sWhite, command=main_menu_btn, text=Mtext, bg=btnbg, activebackground=activebtnbg, font=Mfont)
                menu_btn.pack()

                lab_space = Label(sWhite, text="", bg=mainbg)
                lab_space.pack()

                def fsWR():
                    sWhite.destroy()
                    sWR = Toplevel()
                    sWR.title(Ftitle)
                    sWR.geometry("300x570+250+50")
                    sWR["bg"] = mainbg

                    btnwidth = 250

                    frame1 = Frame(sWR)

                    lab_title = Label(frame1, text=Ftext, bg=mainbg, font=mainfont)
                    lab_title.pack(side=LEFT)

                    def main_menu_btn():
                        sWR.destroy()
                        MM.deiconify()

                    menu_btn = Button(frame1, command=main_menu_btn, text=Mtext, bg=btnbg, activebackground=activebtnbg, font=Mfont)
                    menu_btn.pack()

                    frame1.pack()
                    
                    def bridgehm():
                        sWR.destroy()
                        view_details("housemartin")

                    def bridgel():
                        sWR.destroy()
                        view_details("lesserspottedwoodpecker")

                    def bridges():
                        sWR.destroy()
                        view_details("swallow")

                    load_housemartin = Image.open("housemartin.jpg")
                    render_housemartin = ImageTk.PhotoImage(load_housemartin)
                    btn_housemartin = Button(sWR, command=bridgehm, compound=LEFT, image=render_housemartin, text="House Martin", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_housemartin.pack()

                    load_lesserspottedwoodpecker = Image.open("lesserspottedwoodpecker.jpg")
                    render_lesserspottedwoodpecker = ImageTk.PhotoImage(load_lesserspottedwoodpecker)
                    btn_lesserspottedwoodpecker = Button(sWR, command=bridgel, compound=LEFT, image=render_lesserspottedwoodpecker, text="Lesser Spotted\nWoodpecker", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_lesserspottedwoodpecker.pack()

                    load_swallow = Image.open("swallow.jpg")
                    render_swallow = ImageTk.PhotoImage(load_swallow)
                    btn_swallow = Button(sWR, command=bridges, compound=LEFT, image=render_swallow, text="Swallow", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_swallow.pack()

                    sWR.mainloop()

                def fsWN():
                    sWhite.destroy()
                    sWN = Toplevel()
                    sWN.title(Ftitle)
                    sWN.geometry("300x570+250+50")
                    sWN["bg"] = mainbg

                    btnwidth = 250

                    frame1 = Frame(sWN)

                    lab_title = Label(frame1, text=Ftext, bg=mainbg, font=mainfont)
                    lab_title.pack(side=LEFT)

                    def main_menu_btn():
                        sWN.destroy()
                        MM.deiconify()

                    menu_btn = Button(frame1, command=main_menu_btn, text=Mtext, bg=btnbg, activebackground=activebtnbg, font=Mfont)
                    menu_btn.pack()

                    frame1.pack()

                    def bridgepf():
                        sWN.destroy()
                        view_details("piedflycatcherf")

                    def bridgepm():
                        sWN.destroy()
                        view_details("piedflycatcherm")

                    def bridgepw():
                        sWN.destroy()
                        view_details("piedwagtail")

                    def bridget():
                        sWN.destroy()
                        view_details("treecreeper")

                    load_piedflycatcherf = Image.open("piedflycatcherf.jpg")
                    render_piedflycatcherf = ImageTk.PhotoImage(load_piedflycatcherf)
                    btn_piedflycatcherf = Button(sWN, command=bridgepf, compound=LEFT, image=render_piedflycatcherf, text="Pied Flycatcher\nFemale", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_piedflycatcherf.pack()

                    load_piedflycatcherm = Image.open("piedflycatcherm.jpg")
                    render_piedflycatcherm = ImageTk.PhotoImage(load_piedflycatcherm)
                    btn_piedflycatcherm = Button(sWN, command=bridgepm, compound=LEFT, image=render_piedflycatcherm, text="Pied Flycatcher\nMale", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_piedflycatcherm.pack()

                    load_piedwagtail = Image.open("piedwagtail.jpg")
                    render_piedwagtail = ImageTk.PhotoImage(load_piedwagtail)
                    btn_piedwagtail = Button(sWN, command=bridgepw, compound=LEFT, image=render_piedwagtail, text="Pied Wagtail", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_piedwagtail.pack()

                    load_treecreeper = Image.open("treecreeper.jpg")
                    render_treecreeper = ImageTk.PhotoImage(load_treecreeper)
                    btn_treecreeper = Button(sWN, command=bridget, compound=LEFT, image=render_treecreeper, text="Treecreeper", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_treecreeper.pack()

                    sWN.mainloop()

                frame1 = Frame(sWhite)

                load_orangeredpink = Image.open("orangeredpink.jpg")
                render_orangeredpink = ImageTk.PhotoImage(load_orangeredpink)
                btn_orangeredpink = Button(frame1, command=fsWR, compound=TOP, image=render_orangeredpink, text="Orange/red/pink", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth, height=btnheight)
                btn_orangeredpink.pack(side=LEFT)

                load_none = Image.open("none.jpg")
                render_none = ImageTk.PhotoImage(load_none)
                btn_none = Button(frame1, command=fsWN, compound=TOP, image=render_none, text="None", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth, height=btnheight)
                btn_none.pack(side=LEFT)

                frame1.pack()

                sWhite.mainloop()

            def fsBlack():
                CCs.destroy()
                sBlack = Toplevel()
                sBlack.title(Fstitle)
                sBlack.geometry("300x570+250+50")
                sBlack["bg"] = mainbg

                btnwidth = 140
                btnheight = 100

                lab_title = Label(sBlack, text=Fstext, bg=mainbg, font=mainfont)
                lab_title.pack()

                def main_menu_btn():
                    sBlack.destroy()
                    MM.deiconify()

                menu_btn = Button(sBlack, command=main_menu_btn, text=Mtext, bg=btnbg, activebackground=activebtnbg, font=Mfont)
                menu_btn.pack()

                lab_space = Label(sBlack, text="", bg=mainbg)
                lab_space.pack()

                def fsBlS():
                    sBlack.destroy()
                    sBlS = Toplevel()
                    sBlS.title(Ftitle)
                    sBlS.geometry("300x570+250+50")
                    sBlS["bg"] = mainbg

                    btnwidth = 250

                    frame1 = Frame(sBlS)

                    lab_title = Label(frame1, text=Ftext, bg=mainbg, font=mainfont)
                    lab_title.pack(side=LEFT)

                    def main_menu_btn():
                        sBlS.destroy()
                        MM.deiconify()

                    menu_btn = Button(frame1, command=main_menu_btn, text=Mtext, bg=btnbg, activebackground=activebtnbg, font=Mfont)
                    menu_btn.pack()

                    frame1.pack()

                    def bridgehm():
                        sBlS.destroy()
                        view_details("housemartin")

                    def bridgesw():
                        sBlS.destroy()
                        view_details("swallow")

                    def bridgest():
                        sBlS.destroy()
                        view_details("swift")

                    load_housemartin = Image.open("housemartin.jpg")
                    render_housemartin = ImageTk.PhotoImage(load_housemartin)
                    btn_housemartin = Button(sBlS, command=bridgehm, compound=LEFT, image=render_housemartin, text="House Martin", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_housemartin.pack()

                    load_swallow = Image.open("swallow.jpg")
                    render_swallow = ImageTk.PhotoImage(load_swallow)
                    btn_swallow = Button(sBlS, command=bridgesw, compound=LEFT, image=render_swallow, text="Swallow", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_swallow.pack()

                    load_swift = Image.open("swift.jpg")
                    render_swift = ImageTk.PhotoImage(load_swift)
                    btn_swift = Button(sBlS, command=bridgest, compound=LEFT, image=render_swift, text="Lesser Spotted\nWoodpecker", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_swift.pack()

                    sBlS.mainloop()

                def fsBlL():
                    sBlack.destroy()
                    sBlL = Toplevel()
                    sBlL.title(Ftitle)
                    sBlL.geometry("300x570+250+50")
                    sBlL["bg"] = mainbg

                    btnwidth = 250

                    frame1 = Frame(sBlL)

                    lab_title = Label(frame1, text=Ftext, bg=mainbg, font=mainfont)
                    lab_title.pack(side=LEFT)

                    def main_menu_btn():
                        sBlL.destroy()
                        MM.deiconify()

                    menu_btn = Button(frame1, command=main_menu_btn, text=Mtext, bg=btnbg, activebackground=activebtnbg, font=Mfont)
                    menu_btn.pack()

                    frame1.pack()

                    def bridgeltt():
                        sBlL.destroy()
                        view_details("longtailedtit")

                    def bridgepw():
                        sBlL.destroy()
                        view_details("piedwagtail")

                    load_longtailedtit = Image.open("longtailedtit.jpg")
                    render_longtailedtit = ImageTk.PhotoImage(load_longtailedtit)
                    btn_longtailedtit = Button(sBlL, command=bridgeltt, compound=LEFT, image=render_longtailedtit, text="Long Tailed Tit", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_longtailedtit.pack()

                    load_piedwagtail = Image.open("piedwagtail.jpg")
                    render_piedwagtail = ImageTk.PhotoImage(load_piedwagtail)
                    btn_piedwagtail = Button(sBlL, command=bridgepw, compound=LEFT, image=render_piedwagtail, text="Pied Wagtail", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_piedwagtail.pack()

                    sBlL.mainloop()

                def fsBlT():
                    sBlack.destroy()
                    sBlT = Toplevel()
                    sBlT.title(Ftitle)
                    sBlT.geometry("300x570+250+50")
                    sBlT["bg"] = mainbg

                    btnwidth = 250

                    frame1 = Frame(sBlT)

                    lab_title = Label(frame1, text=Ftext, bg=mainbg, font=mainfont)
                    lab_title.pack(side=LEFT)

                    def main_menu_btn():
                        sBlT.destroy()
                        MM.deiconify()

                    menu_btn = Button(frame1, command=main_menu_btn, text=Mtext, bg=btnbg, activebackground=activebtnbg, font=Mfont)
                    menu_btn.pack()

                    frame1.pack()

                    def bridgeb():
                        sBlT.destroy()
                        view_details("bullfinch")

                    load_bullfinch = Image.open("bullfinch.jpg")
                    render_bullfinch = ImageTk.PhotoImage(load_bullfinch)
                    btn_bullfinch = Button(sBlT, command=bridgeb, compound=LEFT, image=render_bullfinch, text="Bullfinch", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_bullfinch.pack()

                    sBlT.mainloop()

                def fsBlN():
                    sBlack.destroy()
                    sBlN = Toplevel()
                    sBlN.title(Ftitle)
                    sBlN.geometry("300x570+250+50")
                    sBlN["bg"] = mainbg

                    btnwidth = 250

                    frame1 = Frame(sBlN)

                    lab_title = Label(frame1, text=Ftext, bg=mainbg, font=mainfont)
                    lab_title.pack(side=LEFT)

                    def main_menu_btn():
                        sBlN.destroy()
                        MM.deiconify()

                    menu_btn = Button(frame1, command=main_menu_btn, text=Mtext, bg=btnbg, activebackground=activebtnbg, font=Mfont)
                    menu_btn.pack()

                    frame1.pack()

                    def bridgeg():
                        sBlN.destroy()
                        view_details("greattit")

                    def bridgel():
                        sBlN.destroy()
                        view_details("lesserspottedwoodpecker")

                    def bridgepm():
                        sBlN.destroy()
                        view_details("piedflycatcherm")

                    def bridgerb():
                        sBlN.destroy()
                        view_details("reedbunting")

                    load_greattit = Image.open("greattit.jpg")
                    render_greattit = ImageTk.PhotoImage(load_greattit)
                    btn_greattit = Button(sBlN, command=bridgeg, compound=LEFT, image=render_greattit, text="Great Tit", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_greattit.pack()

                    load_lesserspottedwoodpecker = Image.open("lesserspottedwoodpecker.jpg")
                    render_lesserspottedwoodpecker = ImageTk.PhotoImage(load_lesserspottedwoodpecker)
                    btn_lesserspottedwoodpecker = Button(sBlN, command=bridgel, compound=LEFT, image=render_lesserspottedwoodpecker, text="Lesser Spotted\nWoodpecker", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_lesserspottedwoodpecker.pack()

                    load_piedflycatcherm = Image.open("piedflycatcherm.jpg")
                    render_piedflycatcherm = ImageTk.PhotoImage(load_piedflycatcherm)
                    btn_piedflycatcherm = Button(sBlN, command=bridgepm, compound=LEFT, image=render_piedflycatcherm, text="Pied Flycatcher\nMale", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_piedflycatcherm.pack()

                    load_reedbunting = Image.open("reedbunting.jpg")
                    render_reedbunting = ImageTk.PhotoImage(load_reedbunting)
                    btn_reedbunting = Button(sBlN, command=bridgerb, compound=LEFT, image=render_reedbunting, text="Reed Bunting", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_reedbunting.pack()

                    sBlN.mainloop()

                frame1 = Frame(sBlack)
                frame2 = Frame(sBlack)

                load_longtail = Image.open("longtail.jpg")
                render_longtail = ImageTk.PhotoImage(load_longtail)
                btn_longtail = Button(frame1, command=fsBlL, compound=TOP, image=render_longtail, text="Long tail", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth, height=btnheight)
                btn_longtail.pack(side=LEFT)

                load_similarshape = Image.open("similarshape.jpg")
                render_similarshape = ImageTk.PhotoImage(load_similarshape)
                btn_similarshape = Button(frame1, command=fsBlS, compound=TOP, image=render_similarshape, text="Similar shape", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth, height=btnheight)
                btn_similarshape.pack(side=LEFT)

                frame1.pack()

                load_thickbeak = Image.open("thickbeak.jpg")
                render_thickbeak = ImageTk.PhotoImage(load_thickbeak)
                btn_thickbeak = Button(frame2, command=fsBlT, compound=TOP, image=render_thickbeak, text="Thick beak", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth, height=btnheight)
                btn_thickbeak.pack(side=LEFT)

                load_none = Image.open("none.jpg")
                render_none = ImageTk.PhotoImage(load_none)
                btn_none = Button(frame2, command=fsBlN, compound=TOP, image=render_none, text="None", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth, height=btnheight)
                btn_none.pack(side=LEFT)

                frame2.pack()

                sBlack.mainloop()

            def fsBrown():
                CCs.destroy()
                sBrown = Toplevel()
                sBrown.title(Fstitle)
                sBrown.geometry("300x570+250+50")
                sBrown["bg"] = mainbg

                btnwidth = 140
                btnheight = 100

                frame0 = Frame(sBrown, bg=mainbg)

                lab_title = Label(frame0, text=Fstext, bg=mainbg, font=mainfont)
                lab_title.pack(side=LEFT)

                def main_menu_btn():
                    sBrown.destroy()
                    MM.deiconify()

                menu_btn = Button(frame0, command=main_menu_btn, text="Menu", bg=btnbg, activebackground=activebtnbg, font=Mfont)
                menu_btn.pack()

                frame0.pack()

                def fsBrG():
                    sBrown.destroy()
                    sBrG = Toplevel()
                    sBrG.title(Ftitle)
                    sBrG.geometry("300x570+250+50")
                    sBrG["bg"] = mainbg

                    btnwidth = 250

                    frame1 = Frame(sBrG)

                    lab_title = Label(frame1, text=Ftext, bg=mainbg, font=mainfont)
                    lab_title.pack(side=LEFT)

                    def main_menu_btn():
                        sBrG.destroy()
                        MM.deiconify()

                    menu_btn = Button(frame1, command=main_menu_btn, text=Mtext, bg=btnbg, activebackground=activebtnbg, font=Mfont)
                    menu_btn.pack()

                    frame1.pack()

                    def bridgec():
                        sBrG.destroy()
                        view_details("chaffinch")

                    def bridged():
                        sBrG.destroy()
                        view_details("dunnock")

                    def bridgehs():
                        sBrG.destroy()
                        view_details("housesparrow")

                    def bridgel():
                        sBrG.destroy()
                        view_details("linnet")

                    def bridgew():
                        sBrG.destroy()
                        view_details("whitethroat")

                    load_chaffinch = Image.open("chaffinch.jpg")
                    render_chaffinch = ImageTk.PhotoImage(load_chaffinch)
                    btn_chaffinch = Button(sBrG, command=bridgec, compound=LEFT, image=render_chaffinch, text="Chaffinch", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_chaffinch.pack()

                    load_dunnock = Image.open("dunnock.jpg")
                    render_dunnock = ImageTk.PhotoImage(load_dunnock)
                    btn_dunnock = Button(sBrG, command=bridged, compound=LEFT, image=render_dunnock, text="Dunnock", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_dunnock.pack()

                    load_housesparrow = Image.open("housesparrow.jpg")
                    render_housesparrow = ImageTk.PhotoImage(load_housesparrow)
                    btn_housesparrow = Button(sBrG, command=bridgehs, compound=LEFT, image=render_housesparrow, text="House Sparrow", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_housesparrow.pack()

                    load_linnet = Image.open("linnet.jpg")
                    render_linnet = ImageTk.PhotoImage(load_linnet)
                    btn_linnet = Button(sBrG, command=bridgel, compound=LEFT, image=render_linnet, text="Linnet", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_linnet.pack()

                    load_whitethroat = Image.open("whitethroat.jpg")
                    render_whitethroat = ImageTk.PhotoImage(load_whitethroat)
                    btn_whitethroat = Button(sBrG, command=bridgew, compound=LEFT, image=render_whitethroat, text="Whitethroat", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_whitethroat.pack()

                    sBrG.mainloop()

                def fsBrB():
                    sBrown.destroy()
                    sBrB = Toplevel()
                    sBrB.title(Ftitle)
                    sBrB.geometry("300x570+250+50")
                    sBrB["bg"] = mainbg

                    btnwidth = 250

                    frame1 = Frame(sBrB)

                    lab_title = Label(frame1, text=Ftext, bg=mainbg, font=mainfont)
                    lab_title.pack(side=LEFT)

                    def main_menu_btn():
                        sBrB.destroy()
                        MM.deiconify()

                    menu_btn = Button(frame1, command=main_menu_btn, text=Mtext, bg=btnbg, activebackground=activebtnbg, font=Mfont)
                    menu_btn.pack()

                    frame1.pack()

                    def bridgebc():
                        sBrB.destroy()
                        view_details("blackcap")

                    def bridgeg():
                        sBrB.destroy()
                        view_details("goldcrest")

                    def bridgerb():
                        sBrB.destroy()
                        view_details("reedbunting")

                    load_blackcap = Image.open("blackcap.jpg")
                    render_blackcap = ImageTk.PhotoImage(load_blackcap)
                    btn_blackcap = Button(sBrB, command=bridgebc, compound=LEFT, image=render_blackcap, text="Blackcap", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_blackcap.pack()

                    load_goldcrest = Image.open("goldcrest.jpg")
                    render_goldcrest = ImageTk.PhotoImage(load_goldcrest)
                    btn_goldcrest = Button(sBrB, command=bridgeg, compound=LEFT, image=render_goldcrest, text="Goldcrest", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_goldcrest.pack()

                    load_reedbunting = Image.open("reedbunting.jpg")
                    render_reedbunting = ImageTk.PhotoImage(load_reedbunting)
                    btn_reedbunting = Button(sBrB, command=bridgerb, compound=LEFT, image=render_reedbunting, text="Reed Bunting", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_reedbunting.pack()

                    sBrB.mainloop()

                def fsBrE():
                    sBrown.destroy()
                    sBrE = Toplevel()
                    sBrE.title(Ftitle)
                    sBrE.geometry("300x570+250+50")
                    sBrE["bg"] = mainbg

                    btnwidth = 250

                    frame1 = Frame(sBrE)

                    lab_title = Label(frame1, text=Ftext, bg=mainbg, font=mainfont)
                    lab_title.pack(side=LEFT)

                    def main_menu_btn():
                        sGBY.destroy()
                        MM.deiconify()

                    menu_btn = Button(frame1, command=main_menu_btn, text=Mtext, bg=btnbg, activebackground=activebtnbg, font=Mfont)
                    menu_btn.pack()

                    frame1.pack()

                    def bridgec():
                        sBrE.destroy()
                        view_details("chiffchaff")

                    def bridges():
                        sBrE.destroy()
                        view_details("skylark")

                    def bridget():
                        sBrE.destroy()
                        view_details("treecreeper")

                    def bridgew():
                        sBrE.destroy()
                        view_details("wren")

                    load_chiffchaff = Image.open("chiffchaff.jpg")
                    render_chiffchaff = ImageTk.PhotoImage(load_chiffchaff)
                    btn_chiffchaff = Button(sBrE, command=bridgec, compound=LEFT, image=render_chiffchaff, text="Chiffchaff", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_chiffchaff.pack()

                    load_skylark = Image.open("skylark.jpg")
                    render_skylark = ImageTk.PhotoImage(load_skylark)
                    btn_skylark = Button(sBrE, command=bridges, compound=LEFT, image=render_skylark, text="Skylark", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_skylark.pack()

                    load_treecreeper = Image.open("treecreeper.jpg")
                    render_treecreeper = ImageTk.PhotoImage(load_treecreeper)
                    btn_treecreeper = Button(sBrE, command=bridget, compound=LEFT, image=render_treecreeper, text="Treecreeper", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_treecreeper.pack()

                    load_wren = Image.open("wren.jpg")
                    render_wren = ImageTk.PhotoImage(load_wren)
                    btn_wren = Button(sBrE, command=bridgew, compound=LEFT, image=render_wren, text="Wren", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_wren.pack()

                    sBrE.mainloop()

                def fsBrC():
                    sBrown.destroy()
                    sBrC = Toplevel()
                    sBrC.title(Ftitle)
                    sBrC.geometry("300x570+250+50")
                    sBrC["bg"] = mainbg

                    btnwidth = 250

                    frame1 = Frame(sBrC)

                    lab_title = Label(frame1, text=Ftext, bg=mainbg, font=mainfont)
                    lab_title.pack(side=LEFT)

                    def main_menu_btn():
                        sBrC.destroy()
                        MM.deiconify()

                    menu_btn = Button(frame1, command=main_menu_btn, text=Mtext, bg=btnbg, activebackground=activebtnbg, font=Mfont)
                    menu_btn.pack()

                    frame1.pack()

                    def bridget():
                        sBrC.destroy()
                        view_details("treecreeper")

                    load_treecreeper = Image.open("treecreeper.jpg")
                    render_treecreeper = ImageTk.PhotoImage(load_treecreeper)
                    btn_treecreeper = Button(sBrC, command=bridget, compound=LEFT, image=render_treecreeper, text="Treecreeper", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_treecreeper.pack()

                    sBrC.mainloop()

                def fsBrWi():
                    sBrown.destroy()
                    sBrWi = Toplevel()
                    sBrWi.title(Ftitle)
                    sBrWi.geometry("300x570+250+50")
                    sBrWi["bg"] = mainbg

                    btnwidth = 250

                    frame1 = Frame(sBrWi)

                    lab_title = Label(frame1, text=Ftext, bg=mainbg, font=mainfont)
                    lab_title.pack(side=LEFT)

                    def main_menu_btn():
                        sBrWi.destroy()
                        MM.deiconify()

                    menu_btn = Button(frame1, command=main_menu_btn, text=Mtext, bg=btnbg, activebackground=activebtnbg, font=Mfont)
                    menu_btn.pack()

                    frame1.pack()

                    def bridgec():
                        sBrWi.destroy()
                        view_details("chaffinch")

                    def bridgeg():
                        sBrWi.destroy()
                        view_details("goldcrest")

                    def bridgeh():
                        sBrWi.destroy()
                        view_details("housesparrow")

                    def bridgep():
                        sBrWi.destroy()
                        view_details("piedflycatcherf")

                    load_chaffinch = Image.open("chaffinch.jpg")
                    render_chaffinch = ImageTk.PhotoImage(load_chaffinch)
                    btn_chaffinch = Button(sBrWi, command=bridgec, compound=LEFT, image=render_chaffinch, text="Chaffinch", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_chaffinch.pack()

                    load_goldcrest = Image.open("goldcrest.jpg")
                    render_goldcrest = ImageTk.PhotoImage(load_goldcrest)
                    btn_goldcrest = Button(sBrWi, command=bridgeg, compound=LEFT, image=render_goldcrest, text="Goldcrest", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_goldcrest.pack()

                    load_housesparrow = Image.open("housesparrow.jpg")
                    render_housesparrow = ImageTk.PhotoImage(load_housesparrow)
                    btn_housesparrow = Button(sBrWi, command=bridgeh, compound=LEFT, image=render_housesparrow, text="House Sparrow", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_housesparrow.pack()

                    load_piedflycatcherf = Image.open("piedflycatcherf.jpg")
                    render_piedflycatcherf = ImageTk.PhotoImage(load_piedflycatcherf)
                    btn_piedflycatcherf = Button(sBrWi, command=bridgep, compound=LEFT, image=render_piedflycatcherf, text="Pied Flycatcher\nFemale", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_piedflycatcherf.pack()

                    sBrWi.mainloop()

                def fsBrR():
                    sBrown.destroy()
                    sBrR = Toplevel()
                    sBrR.title(Ftitle)
                    sBrR.geometry("300x570+250+50")
                    sBrR["bg"] = mainbg

                    btnwidth = 250

                    frame1 = Frame(sBrR)

                    lab_title = Label(frame1, text=Ftext, bg=mainbg, font=mainfont)
                    lab_title.pack(side=LEFT)

                    def main_menu_btn():
                        sBrR.destroy()
                        MM.deiconify()

                    menu_btn = Button(frame1, command=main_menu_btn, text=Mtext, bg=btnbg, activebackground=activebtnbg, font=Mfont)
                    menu_btn.pack()

                    frame1.pack()

                    def bridgec():
                        sBrR.destroy()
                        view_details("chaffinch")

                    def bridgel():
                        sBrR.destroy()
                        view_details("linnet")

                    def bridger():
                        sBrR.destroy()
                        view_details("robin")

                    load_chaffinch = Image.open("chaffinch.jpg")
                    render_chaffinch = ImageTk.PhotoImage(load_chaffinch)
                    btn_chaffinch = Button(sBrR, command=bridgec, compound=LEFT, image=render_chaffinch, text="Chaffinch", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_chaffinch.pack()

                    load_linnet = Image.open("linnet.jpg")
                    render_linnet = ImageTk.PhotoImage(load_linnet)
                    btn_linnet = Button(sBrR, command=bridgel, compound=LEFT, image=render_linnet, text="Linnet", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_linnet.pack()

                    load_robin = Image.open("robin.jpg")
                    render_robin = ImageTk.PhotoImage(load_robin)
                    btn_robin = Button(sBrR, command=bridger, compound=LEFT, image=render_robin, text="Robin", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_robin.pack()

                    sBrR.mainloop()

                def fsBrS():
                    sBrown.destroy()
                    sBrS = Toplevel()
                    sBrS.title(Ftitle)
                    sBrS.geometry("300x570+250+50")
                    sBrS["bg"] = mainbg

                    btnwidth = 250

                    frame1 = Frame(sBrS)

                    lab_title = Label(frame1, text=Ftext, bg=mainbg, font=mainfont)
                    lab_title.pack(side=LEFT)

                    def main_menu_btn():
                        sBrS.destroy()
                        MM.deiconify()

                    menu_btn = Button(frame1, command=main_menu_btn, text=Mtext, bg=btnbg, activebackground=activebtnbg, font=Mfont)
                    menu_btn.pack()

                    frame1.pack()

                    def bridged():
                        sBrS.destroy()
                        view_details("dunnock")

                    def bridger():
                        sBrS.destroy()
                        view_details("reedbunting")

                    def bridges():
                        sBrS.destroy()
                        view_details("skylark")

                    def bridget():
                        sBrS.destroy()
                        view_details("treecreeper")

                    def bridgey():
                        sBrS.destroy()
                        view_details("yellowhammer")

                    load_dunnock = Image.open("dunnock.jpg")
                    render_dunnock = ImageTk.PhotoImage(load_dunnock)
                    btn_dunnock = Button(sBrS, command=bridged, compound=LEFT, image=render_dunnock, text="Dunnock", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_dunnock.pack()

                    load_reedbunting = Image.open("reedbunting.jpg")
                    render_reedbunting = ImageTk.PhotoImage(load_reedbunting)
                    btn_reedbunting = Button(sBrS, command=bridger, compound=LEFT, image=render_reedbunting, text="Reed Bunting", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_reedbunting.pack()

                    load_skylark = Image.open("skylark.jpg")
                    render_skylark = ImageTk.PhotoImage(load_skylark)
                    btn_skylark = Button(sBrS, command=bridges, compound=LEFT, image=render_skylark, text="Skylark", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_skylark.pack()

                    load_treecreeper = Image.open("treecreeper.jpg")
                    render_treecreeper = ImageTk.PhotoImage(load_treecreeper)
                    btn_treecreeper = Button(sBrS, command=bridget, compound=LEFT, image=render_treecreeper, text="Treecreeper", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_treecreeper.pack()
                    
                    load_yellowhammer = Image.open("yellowhammer.jpg")
                    render_yellowhammer = ImageTk.PhotoImage(load_yellowhammer)
                    btn_yellowhammer = Button(sBrS, command=bridgey, compound=LEFT, image=render_yellowhammer, text="Yellowhammer", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_yellowhammer.pack()
                    
                    sBrS.mainloop()

                def fsBrWh():
                    sBrown.destroy()
                    sBrWh = Toplevel()
                    sBrWh.title(Ftitle)
                    sBrWh.geometry("300x570+250+50")
                    sBrWh["bg"] = mainbg

                    btnwidth = 250

                    frame1 = Frame(sBrWh)

                    lab_title = Label(frame1, text=Ftext, bg=mainbg, font=mainfont)
                    lab_title.pack(side=LEFT)

                    def main_menu_btn():
                        sBrWh.destroy()
                        MM.deiconify()

                    menu_btn = Button(frame1, command=main_menu_btn, text=Mtext, bg=btnbg, activebackground=activebtnbg, font=Mfont)
                    menu_btn.pack()

                    frame1.pack()

                    def bridgeh():
                        sBrWh.destroy()
                        view_details("housesparrow")

                    def bridger():
                        sBrWh.destroy()
                        view_details("reedbunting")

                    def bridges():
                        sBrWh.destroy()
                        view_details("spottedflycatcher")

                    def bridget():
                        sBrWh.destroy()
                        view_details("treecreeper")

                    load_housesparrow = Image.open("housesparrow.jpg")
                    render_housesparrow = ImageTk.PhotoImage(load_housesparrow)
                    btn_housesparrow = Button(sBrWh, command=bridgeh, compound=LEFT, image=render_housesparrow, text="House Sparrow", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_housesparrow.pack()

                    load_reedbunting = Image.open("reedbunting.jpg")
                    render_reedbunting = ImageTk.PhotoImage(load_reedbunting)
                    btn_reedbunting = Button(sBrWh, command=bridger, compound=LEFT, image=render_reedbunting, text="Reed Bunting", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_reedbunting.pack()

                    load_spottedflycatcher = Image.open("spottedflycatcher.jpg")
                    render_spottedflycatcher = ImageTk.PhotoImage(load_spottedflycatcher)
                    btn_spottedflycatcher = Button(sBrWh, command=bridges, compound=LEFT, image=render_spottedflycatcher, text="Spotted\nFlycatcher", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_spottedflycatcher.pack()

                    load_treecreeper = Image.open("treecreeper.jpg")
                    render_treecreeper = ImageTk.PhotoImage(load_treecreeper)
                    btn_treecreeper = Button(sBrWh, command=bridget, compound=LEFT, image=render_treecreeper, text="Treecreeper", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_treecreeper.pack()
                    
                    sBrWh.mainloop()

                def fsBrY():
                    sBrown.destroy()
                    sBrY = Toplevel()
                    sBrY.title(Ftitle)
                    sBrY.geometry("300x570+250+50")
                    sBrY["bg"] = mainbg

                    btnwidth = 250

                    frame1 = Frame(sBrY)

                    lab_title = Label(frame1, text=Ftext, bg=mainbg, font=mainfont)
                    lab_title.pack(side=LEFT)

                    def main_menu_btn():
                        sBrY.destroy()
                        MM.deiconify()

                    menu_btn = Button(frame1, command=main_menu_btn, text=Mtext, bg=btnbg, activebackground=activebtnbg, font=Mfont)
                    menu_btn.pack()

                    frame1.pack()

                    def bridgeg():
                        sBrY.destroy()
                        view_details("goldcrest")

                    def bridgey():
                        sBrY.destroy()
                        view_details("yellowhammer")

                    load_goldcrest = Image.open("goldcrest.jpg")
                    render_goldcrest = ImageTk.PhotoImage(load_goldcrest)
                    btn_goldcrest = Button(sBrY, command=bridgeg, compound=LEFT, image=render_goldcrest, text="Goldcrest", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_goldcrest.pack()

                    load_yellowhammer = Image.open("yellowhammer.jpg")
                    render_yellowhammer = ImageTk.PhotoImage(load_yellowhammer)
                    btn_yellowhammer = Button(sBrY, command=bridgey, compound=LEFT, image=render_yellowhammer, text="Yellowhammer", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_yellowhammer.pack()
                    
                    sBrY.mainloop()

                frame1 = Frame(sBrown)
                frame2 = Frame(sBrown)
                frame3 = Frame(sBrown)
                frame4 = Frame(sBrown)
                frame5 = Frame(sBrown, bg=mainbg)

                load_greyonhead = Image.open("greyonhead.jpg")
                render_greyonhead = ImageTk.PhotoImage(load_greyonhead)
                btn_greyonhead = Button(frame1, command=fsBrG, compound=TOP, image=render_greyonhead, text="Grey on head", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth, height=btnheight)
                btn_greyonhead.pack(side=LEFT)

                load_blacktophead = Image.open("blacktophead.jpg")
                render_blacktophead = ImageTk.PhotoImage(load_blacktophead)
                btn_blacktophead = Button(frame1, command=fsBrB, compound=TOP, image=render_blacktophead, text="Black top of head", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth, height=btnheight)
                btn_blacktophead.pack(side=LEFT)

                frame1.pack()

                load_curvedbeak = Image.open("curvedbeak.jpg")
                render_curvedbeak = ImageTk.PhotoImage(load_curvedbeak)
                btn_curvedbeak = Button(frame2, command=fsBrC, compound=TOP, image=render_curvedbeak, text="Curved beak", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth, height=btnheight)
                btn_curvedbeak.pack(side=LEFT)

                load_eyestripe = Image.open("eyestripe.jpg")
                render_eyestripe = ImageTk.PhotoImage(load_eyestripe)
                btn_eyestripe = Button(frame2, command=fsBrE, compound=TOP, image=render_eyestripe, text="Eye stripe", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth, height=btnheight)
                btn_eyestripe.pack(side=LEFT)

                frame2.pack()

                load_wingbar = Image.open("wingbar.jpg")
                render_wingbar = ImageTk.PhotoImage(load_wingbar)
                btn_wingbar = Button(frame3, command=fsBrWi, compound=TOP, image=render_wingbar, text="Wing bar", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth, height=btnheight)
                btn_wingbar.pack(side=LEFT)

                load_redonchest = Image.open("redonchest.jpg")
                render_redonchest = ImageTk.PhotoImage(load_redonchest)
                btn_redonchest = Button(frame3, command=fsBrR, compound=TOP, image=render_redonchest, text="Red on chest", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth, height=btnheight)
                btn_redonchest.pack(side=LEFT)

                frame3.pack()

                load_streakyback = Image.open("streakyback.jpg")
                render_streakyback = ImageTk.PhotoImage(load_streakyback)
                btn_streakyback = Button(frame4, command=fsBrS, compound=TOP, image=render_streakyback, text="Streaky back", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth, height=btnheight)
                btn_streakyback.pack(side=LEFT)

                load_whitetummy = Image.open("whitetummy.jpg")
                render_whitetummy = ImageTk.PhotoImage(load_whitetummy)
                btn_whitetummy = Button(frame4, command=fsBrWh, compound=TOP, image=render_whitetummy, text="White tummy", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth, height=btnheight)
                btn_whitetummy.pack(side=LEFT)

                frame4.pack()

                load_yellowcolour = Image.open("yellowcolour.jpg")
                render_yellowcolour = ImageTk.PhotoImage(load_yellowcolour)
                btn_yellowcolour = Button(frame5, command=fsBrY, compound=TOP, image=render_yellowcolour, text="Yellow colour", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth, height=btnheight)
                btn_yellowcolour.pack()

                frame5.pack()

                sBrown.mainloop()

            frame1 = Frame(CCs)
            frame2 = Frame(CCs)
            frame3 = Frame(CCs)
            frame4 = Frame(CCs)

            load_black = Image.open("black.jpg")
            render_black = ImageTk.PhotoImage(load_black)
            btn_black = Button(frame1, command=fsBlack, compound=TOP, image=render_black, text="Black", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth, height=btnheight)
            btn_black.pack(side=LEFT)

            load_blue = Image.open("blue.jpg")
            render_blue = ImageTk.PhotoImage(load_blue)
            btn_blue = Button(frame1, compound=TOP, command=fsBl, image=render_blue, text="Blue", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth, height=btnheight)
            btn_blue.pack(side=LEFT)

            frame1.pack()

            load_brown = Image.open("brown.jpg")
            render_brown = ImageTk.PhotoImage(load_brown)
            btn_brown = Button(frame2, command=fsBrown, compound=TOP, image=render_brown, text="Brown", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth, height=btnheight)
            btn_brown.pack(side=LEFT)

            load_grey = Image.open("grey.jpg")
            render_grey = ImageTk.PhotoImage(load_grey)
            btn_grey = Button(frame2, command=fsGrey, compound=TOP, image=render_grey, text="Grey", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth, height=btnheight)
            btn_grey.pack(side=LEFT)

            frame2.pack()

            load_orangeredpink = Image.open("orangeredpink.jpg")
            render_orangeredpink = ImageTk.PhotoImage(load_orangeredpink)
            btn_orangeredpink = Button(frame3, command=fsOrangeredpink, compound=TOP, image=render_orangeredpink, text="Orange/red/pink", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth, height=btnheight)
            btn_orangeredpink.pack(side=LEFT)

            load_palebrown = Image.open("palebrown.jpg")
            render_palebrown = ImageTk.PhotoImage(load_palebrown)
            btn_palebrown = Button(frame3, command=fsPalebrown, compound=TOP, image=render_palebrown, text="Pale brown", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth, height=btnheight)
            btn_palebrown.pack(side=LEFT)

            frame3.pack()

            load_white = Image.open("white.jpg")
            render_white = ImageTk.PhotoImage(load_white)
            btn_white = Button(frame4, command=fsWhite, compound=TOP, image=render_white, text="White", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth, height=btnheight)
            btn_white.pack(side=LEFT)

            load_yellowgreen = Image.open("yellowgreen.jpg")
            render_yellowgreen = ImageTk.PhotoImage(load_yellowgreen)
            btn_yellowgreen = Button(frame4, command=fsYellowgreen, compound=TOP, image=render_yellowgreen, text="Yellow/green", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth, height=btnheight)
            btn_yellowgreen.pack(side=LEFT)

            frame4.pack()

            ##### COMMANDS FOR COLOUR CHOICES #####

            CCs.mainloop()

        def fCCl(): #COOSE COLOUR LARGE
            CS.destroy()
            
            CCtitle = "Choose colour"
            CCtext = "Which main colour is the bird?"
            btnwidth = 140
            btnheight = 100
            
            CCl = Toplevel()
            CCl.title(CCtitle)
            CCl.geometry("300x570+250+50")
            CCl["bg"] = mainbg

            lab_title = Label(CCl, text=CCtext, bg=mainbg, font=mainfont)
            lab_title.pack()

            def main_menu_btn():
                CCl.destroy()
                MM.deiconify()

            menu_btn = Button(CCl, command=main_menu_btn, text=Mtext, bg=btnbg, activebackground=activebtnbg, font=Mfont)
            menu_btn.pack()

            lab_space = Label(CCl, text="", bg=mainbg)
            lab_space.pack()

            def flW():
                CCl.destroy()
                lW = Toplevel()
                lW.title(Ftitle)
                lW.geometry("300x570+250+50")
                lW["bg"] = mainbg

                btnwidth = 250

                frame1 = Frame(lW)

                lab_title = Label(frame1, text=Ftext, bg=mainbg, font=mainfont)
                lab_title.pack(side=LEFT)

                def main_menu_btn():
                    lW.destroy()
                    MM.deiconify()

                menu_btn = Button(frame1, command=main_menu_btn, text=Mtext, bg=btnbg, activebackground=activebtnbg, font=Mfont)
                menu_btn.pack()

                frame1.pack()

                def bridgemp():
                    lW.destroy()
                    view_details("magpie")

                def bridgegsw():
                    lW.destroy()
                    view_details("greatspottedwoodpecker")

                load_magpie = Image.open("magpie.jpg")
                render_magpie = ImageTk.PhotoImage(load_magpie)
                btn_magpie = Button(lW, command=bridgemp, compound=LEFT, image=render_magpie, text="Magpie", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                btn_magpie.pack()

                load_greatspottedwoodpecker = Image.open("greatspottedwoodpecker.jpg")
                render_greatspottedwoodpecker = ImageTk.PhotoImage(load_greatspottedwoodpecker)
                btn_greatspottedwoodpecker = Button(lW, command=bridgegsw, compound=LEFT, image=render_greatspottedwoodpecker, text="Great Spotted\nWoodpecker", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                btn_greatspottedwoodpecker.pack()
                
                lW.mainloop()

            def flY():
                CCl.destroy()
                lY = Toplevel()
                lY.title(Ftitle)
                lY.geometry("300x570+250+50")
                lY["bg"] = mainbg

                btnwidth = 250

                frame1 = Frame(lY)

                lab_title = Label(frame1, text=Ftext, bg=mainbg, font=mainfont)
                lab_title.pack(side=LEFT)

                def main_menu_btn():
                    lY.destroy()
                    MM.deiconify()

                menu_btn = Button(frame1, command=main_menu_btn, text=Mtext, bg=btnbg, activebackground=activebtnbg, font=Mfont)
                menu_btn.pack()

                frame1.pack()

                def bridgegwp():
                    lY.destroy()
                    view_details("greenwoodpecker")

                load_greenwoodpecker = Image.open("greenwoodpecker.jpg")
                render_greenwoodpecker = ImageTk.PhotoImage(load_greenwoodpecker)
                btn_greenwoodpecker = Button(lY, command=bridgegwp, compound=LEFT, image=render_greenwoodpecker, text="Green\nWoodpecker", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                btn_greenwoodpecker.pack()

                lY.mainloop()

            def flSpeckled():
                CCl.destroy()
                lSpeckled = Toplevel()
                lSpeckled.title(Fstitle)
                lSpeckled.geometry("300x570+250+50")
                lSpeckled["bg"] = mainbg

                btnwidth = 140
                btnheight = 100

                lab_title = Label(lSpeckled, text=Fstext, bg=mainbg, font=mainfont)
                lab_title.pack()

                def main_menu_btn():
                    lSpeckled.destroy()
                    MM.deiconify()

                menu_btn = Button(lSpeckled, command=main_menu_btn, text=Mtext, bg=btnbg, activebackground=activebtnbg, font=Mfont)
                menu_btn.pack()

                lab_space = Label(lSpeckled, text="", bg=mainbg)
                lab_space.pack()

                def flSI():
                    lSpeckled.destroy()
                    lSI = Toplevel()
                    lSI.title(Ftitle)
                    lSI.geometry("300x570+250+50")
                    lSI["bg"] = mainbg

                    btnwidth = 250

                    frame1 = Frame(lSI)

                    lab_title = Label(frame1, text=Ftext, bg=mainbg, font=mainfont)
                    lab_title.pack(side=LEFT)

                    def main_menu_btn():
                        lSI.destroy()
                        MM.deiconify()

                    menu_btn = Button(frame1, command=main_menu_btn, text=Mtext, bg=btnbg, activebackground=activebtnbg, font=Mfont)
                    menu_btn.pack()

                    frame1.pack()

                    def bridges():
                        lSI.destroy()
                        view_details("starling")

                    load_starling = Image.open("starling.jpg")
                    render_starling = ImageTk.PhotoImage(load_starling)
                    btn_starling = Button(lSI, command=bridges, compound=LEFT, image=render_starling, text="Starling", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_starling.pack()

                    lSI.mainloop()

                def flSN():
                    lSpeckled.destroy()
                    lSN = Toplevel()
                    lSN.title(Ftitle)
                    lSN.geometry("300x570+250+50")
                    lSN["bg"] = mainbg

                    btnwidth = 250

                    frame1 = Frame(lSN)

                    lab_title = Label(frame1, text=Ftext, bg=mainbg, font=mainfont)
                    lab_title.pack(side=LEFT)

                    def main_menu_btn():
                        lSN.destroy()
                        MM.deiconify()

                    menu_btn = Button(frame1, command=main_menu_btn, text=Mtext, bg=btnbg, activebackground=activebtnbg, font=Mfont)
                    menu_btn.pack()

                    frame1.pack()

                    def bridgef():
                        lSN.destroy()
                        view_details("fieldfare")

                    def bridgem():
                        lSN.destroy()
                        view_details("mistlethrush")

                    def bridger():
                        lSN.destroy()
                        view_details("redwing")

                    def bridges():
                        lSN.destroy()
                        view_details("songthrush")

                    load_fieldfare = Image.open("fieldfare.jpg")
                    render_fieldfare = ImageTk.PhotoImage(load_fieldfare)
                    btn_fieldfare = Button(lSN, command=bridgef, compound=LEFT, image=render_fieldfare, text="Fieldfare", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_fieldfare.pack()

                    load_mistlethrush = Image.open("mistlethrush.jpg")
                    render_mistlethrush = ImageTk.PhotoImage(load_mistlethrush)
                    btn_mistlethrush = Button(lSN, command=bridgem, compound=LEFT, image=render_mistlethrush, text="Mistle Thrush", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_mistlethrush.pack()

                    load_redwing = Image.open("redwing.jpg")
                    render_redwing = ImageTk.PhotoImage(load_redwing)
                    btn_redwing = Button(lSN, command=bridger, compound=LEFT, image=render_redwing, text="Redwing", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_redwing.pack()

                    load_songthrush = Image.open("songthrush.jpg")
                    render_songthrush = ImageTk.PhotoImage(load_songthrush)
                    btn_songthrush = Button(lSN, command=bridges, compound=LEFT, image=render_songthrush, text="Song Thrush", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_songthrush.pack()

                    lSN.mainloop()

                frame1 = Frame(lSpeckled)

                load_irridescence = Image.open("irridescence.jpg")
                render_irridescence = ImageTk.PhotoImage(load_irridescence)
                btn_irridescence = Button(frame1, command=flSI, compound=TOP, image=render_irridescence, text="Irridescence", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth, height=btnheight)
                btn_irridescence.pack(side=LEFT)

                load_none = Image.open("none.jpg")
                render_none = ImageTk.PhotoImage(load_none)
                btn_none = Button(frame1, command=flSN, compound=TOP, image=render_none, text="None", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth, height=btnheight)
                btn_none.pack(side=LEFT)

                frame1.pack()

                lSpeckled.mainloop()

            def flBlack():
                CCl.destroy()
                lBlack = Toplevel()
                lBlack.title(Fstitle)
                lBlack.geometry("300x570+250+50")
                lBlack["bg"] = mainbg

                btnwidth = 140
                btnheight = 100

                lab_title = Label(lBlack, text=Fstext, bg=mainbg, font=mainfont)
                lab_title.pack()

                def main_menu_btn():
                    lBlack.destroy()
                    MM.deiconify()

                menu_btn = Button(lBlack, command=main_menu_btn, text=Mtext, bg=btnbg, activebackground=activebtnbg, font=Mfont)
                menu_btn.pack()

                lab_space = Label(lBlack, text="", bg=mainbg)
                lab_space.pack()

                def flBlW():
                    lBlack.destroy()
                    lBlW = Toplevel()
                    lBlW.title(Ftitle)
                    lBlW.geometry("300x570+250+50")
                    lBlW["bg"] = mainbg

                    btnwidth = 250

                    frame1 = Frame(lBlW)

                    lab_title = Label(frame1, text=Ftext, bg=mainbg, font=mainfont)
                    lab_title.pack(side=LEFT)

                    def main_menu_btn():
                        lBlW.destroy()
                        MM.deiconify()

                    menu_btn = Button(frame1, command=main_menu_btn, text=Mtext, bg=btnbg, activebackground=activebtnbg, font=Mfont)
                    menu_btn.pack()

                    frame1.pack()

                    def bridgem():
                        lBlW.destroy()
                        view_details("magpie")

                    def bridgeg():
                        lBlW.destroy()
                        view_details("greatspottedwoodpecker")

                    load_magpie = Image.open("magpie.jpg")
                    render_magpie = ImageTk.PhotoImage(load_magpie)
                    btn_magpie = Button(lBlW, command=bridgem, compound=LEFT, image=render_magpie, text="Magpie", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_magpie.pack()

                    load_greatspottedwoodpecker = Image.open("greatspottedwoodpecker.jpg")
                    render_greatspottedwoodpecker = ImageTk.PhotoImage(load_greatspottedwoodpecker)
                    btn_greatspottedwoodpecker = Button(lBlW, command=bridgeg, compound=LEFT, image=render_greatspottedwoodpecker, text="Great Spotted\nWoodpecker", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_greatspottedwoodpecker.pack()

                    lBlW.mainloop()

                def flBlI():
                    lBlack.destroy()
                    lBlI = Toplevel()
                    lBlI.title(Ftitle)
                    lBlI.geometry("300x570+250+50")
                    lBlI["bg"] = mainbg

                    btnwidth = 250

                    frame1 = Frame(lBlI)

                    lab_title = Label(frame1, text=Ftext, bg=mainbg, font=mainfont)
                    lab_title.pack(side=LEFT)

                    def main_menu_btn():
                        lBlI.destroy()
                        MM.deiconify()

                    menu_btn = Button(frame1, command=main_menu_btn, text=Mtext, bg=btnbg, activebackground=activebtnbg, font=Mfont)
                    menu_btn.pack()

                    frame1.pack()

                    def bridges():
                        lBlI.destroy()
                        view_details("starling")

                    load_starling = Image.open("starling.jpg")
                    render_starling = ImageTk.PhotoImage(load_starling)
                    btn_starling = Button(lBlI, command=bridges, compound=LEFT, image=render_starling, text="Starling", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_starling.pack()

                    lBlI.mainloop()

                def flBlY():
                    lBlack.destroy()
                    lBlY = Toplevel()
                    lBlY.title(Ftitle)
                    lBlY.geometry("300x570+250+50")
                    lBlY["bg"] = mainbg

                    btnwidth = 250

                    frame1 = Frame(lBlY)

                    lab_title = Label(frame1, text=Ftext, bg=mainbg, font=mainfont)
                    lab_title.pack(side=LEFT)

                    def main_menu_btn():
                        lBlY.destroy()
                        MM.deiconify()

                    menu_btn = Button(frame1, command=main_menu_btn, text=Mtext, bg=btnbg, activebackground=activebtnbg, font=Mfont)
                    menu_btn.pack()

                    frame1.pack()

                    def bridgeb():
                        lBlY.destroy()
                        view_details("blackbird")

                    def bridges():
                        lBlY.destroy()
                        view_details("starling")

                    load_blackbird = Image.open("blackbird.jpg")
                    render_blackbird = ImageTk.PhotoImage(load_blackbird)
                    btn_blackbird = Button(lBlY, command=bridgeb, compound=LEFT, image=render_blackbird, text="Blackbird", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_blackbird.pack()

                    load_starling = Image.open("starling.jpg")
                    render_starling = ImageTk.PhotoImage(load_starling)
                    btn_starling = Button(lBlY, command=bridges, compound=LEFT, image=render_starling, text="Starling", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_starling.pack()

                    lBlY.mainloop()

                def flBlN():
                    lBlack.destroy()
                    lBlN = Toplevel()
                    lBlN.title(Ftitle)
                    lBlN.geometry("300x570+250+50")
                    lBlN["bg"] = mainbg

                    btnwidth = 250

                    frame1 = Frame(lBlN)

                    lab_title = Label(frame1, text=Ftext, bg=mainbg, font=mainfont)
                    lab_title.pack(side=LEFT)

                    def main_menu_btn():
                        lBlN.destroy()
                        MM.deiconify()

                    menu_btn = Button(frame1, command=main_menu_btn, text=Mtext, bg=btnbg, activebackground=activebtnbg, font=Mfont)
                    menu_btn.pack()

                    frame1.pack()

                    def bridgec():
                        lBlN.destroy()
                        view_details("crow")

                    def bridgej():
                        lBlN.destroy()
                        view_details("jackdaw")

                    def bridgera():
                        lBlN.destroy()
                        view_details("raven")

                    def bridgero():
                        lBlN.destroy()
                        view_details("rook")

                    load_crow = Image.open("crow.jpg")
                    render_crow = ImageTk.PhotoImage(load_crow)
                    btn_crow = Button(lBlN, command=bridgec, compound=LEFT, image=render_crow, text="Carrion Crow", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_crow.pack()

                    load_jackdaw = Image.open("jackdaw.jpg")
                    render_jackdaw = ImageTk.PhotoImage(load_jackdaw)
                    btn_jackdaw = Button(lBlN, command=bridgej, compound=LEFT, image=render_jackdaw, text="Jackdaw", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_jackdaw.pack()

                    load_raven = Image.open("raven.jpg")
                    render_raven = ImageTk.PhotoImage(load_raven)
                    btn_raven = Button(lBlN, command=bridgera, compound=LEFT, image=render_raven, text="Raven", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_raven.pack()

                    load_rook = Image.open("rook.jpg")
                    render_rook = ImageTk.PhotoImage(load_rook)
                    btn_rook = Button(lBlN, command=bridgero, compound=LEFT, image=render_rook, text="Rook", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_rook.pack()

                    lBlN.mainloop()

                frame1 = Frame(lBlack)
                frame2 = Frame(lBlack)

                load_irridescence = Image.open("irridescence.jpg")
                render_irridescence = ImageTk.PhotoImage(load_irridescence)
                btn_irridescence = Button(frame1, command=flBlI, compound=TOP, image=render_irridescence, text="Irridescence", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth, height=btnheight)
                btn_irridescence.pack(side=LEFT)

                load_whitecolour = Image.open("whitecolour.jpg")
                render_whitecolour = ImageTk.PhotoImage(load_whitecolour)
                btn_whitecolour = Button(frame1, command=flBlW, compound=TOP, image=render_whitecolour, text="White colour", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth, height=btnheight)
                btn_whitecolour.pack(side=LEFT)

                frame1.pack()

                load_yellowbeak = Image.open("yellowbeak.jpg")
                render_yellowbeak = ImageTk.PhotoImage(load_yellowbeak)
                btn_yellowbeak = Button(frame2, command=flBlY, compound=TOP, image=render_yellowbeak, text="Yellow beak", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth, height=btnheight)
                btn_yellowbeak.pack(side=LEFT)

                load_none = Image.open("none.jpg")
                render_none = ImageTk.PhotoImage(load_none)
                btn_none = Button(frame2, command=flBlN, compound=TOP, image=render_none, text="None", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth, height=btnheight)
                btn_none.pack(side=LEFT)

                frame2.pack()

                lBlack.mainloop()

            def flGrey():
                CCl.destroy()
                lGrey = Toplevel()
                lGrey.title(Fstitle)
                lGrey.geometry("300x570+250+50")
                lGrey["bg"] = mainbg

                btnwidth = 140
                btnheight = 100

                lab_title = Label(lGrey, text=Fstext, bg=mainbg, font=mainfont)
                lab_title.pack()

                def main_menu_btn():
                    lGrey.destroy()
                    MM.deiconify()

                menu_btn = Button(lGrey, command=main_menu_btn, text=Mtext, bg=btnbg, activebackground=activebtnbg, font=Mfont)
                menu_btn.pack()

                lab_space = Label(lGrey, text="", bg=mainbg)
                lab_space.pack()

                def flGBa():
                    lGrey.destroy()
                    lGBa = Toplevel()
                    lGBa.title(Ftitle)
                    lGBa.geometry("300x570+250+50")
                    lGBa["bg"] = mainbg

                    btnwidth = 250

                    frame1 = Frame(lGBa)

                    lab_title = Label(frame1, text=Ftext, bg=mainbg, font=mainfont)
                    lab_title.pack(side=LEFT)

                    def main_menu_btn():
                        lGBa.destroy()
                        MM.deiconify()

                    menu_btn = Button(frame1, command=main_menu_btn, text=Mtext, bg=btnbg, activebackground=activebtnbg, font=Mfont)
                    menu_btn.pack()

                    frame1.pack()

                    def bridgec():
                        lGBa.destroy()
                        view_details("cuckoo")

                    def bridgep():
                        lGBa.destroy()
                        view_details("partridge")

                    load_cuckoo = Image.open("cuckoo.jpg")
                    render_cuckoo = ImageTk.PhotoImage(load_cuckoo)
                    btn_cuckoo = Button(lGBa, command=bridgec, compound=LEFT, image=render_cuckoo, text="Cuckoo", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_cuckoo.pack()

                    load_partridge = Image.open("partridge.jpg")
                    render_partridge = ImageTk.PhotoImage(load_partridge)
                    btn_partridge = Button(lGBa, command=bridgep, compound=LEFT, image=render_partridge, text="Partridge", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_partridge.pack()

                    lGBa.mainloop()

                def flGW():
                    lGrey.destroy()
                    lGW = Toplevel()
                    lGW.title(Ftitle)
                    lGW.geometry("300x570+250+50")
                    lGW["bg"] = mainbg

                    btnwidth = 250

                    frame1 = Frame(lGW)

                    lab_title = Label(frame1, text=Ftext, bg=mainbg, font=mainfont)
                    lab_title.pack(side=LEFT)

                    def main_menu_btn():
                        lGW.destroy()
                        MM.deiconify()

                    menu_btn = Button(frame1, command=main_menu_btn, text=Mtext, bg=btnbg, activebackground=activebtnbg, font=Mfont)
                    menu_btn.pack()

                    frame1.pack()

                    def bridgew():
                        lGW.destroy()
                        view_details("woodpigeon")

                    load_woodpigeon = Image.open("woodpigeon.jpg")
                    render_woodpigeon = ImageTk.PhotoImage(load_woodpigeon)
                    btn_woodpigeon = Button(lGW, command=bridgew, compound=LEFT, image=render_woodpigeon, text="Woodpigeon", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_woodpigeon.pack()

                    lGW.mainloop()

                def flGBl():
                    lGrey.destroy()
                    lGBl = Toplevel()
                    lGBl.title(Ftitle)
                    lGBl.geometry("300x570+250+50")
                    lGBl["bg"] = mainbg

                    btnwidth = 250

                    frame1 = Frame(lGBl)

                    lab_title = Label(frame1, text=Ftext, bg=mainbg, font=mainfont)
                    lab_title.pack(side=LEFT)

                    def main_menu_btn():
                        lGBl.destroy()
                        MM.deiconify()

                    menu_btn = Button(frame1, command=main_menu_btn, text=Mtext, bg=btnbg, activebackground=activebtnbg, font=Mfont)
                    menu_btn.pack()

                    frame1.pack()

                    def bridgec():
                        lGBl.destroy()
                        view_details("collareddove")

                    load_collareddove = Image.open("collareddove.jpg")
                    render_collareddove = ImageTk.PhotoImage(load_collareddove)
                    btn_collareddove = Button(lGBl, command=bridgec, compound=LEFT, image=render_collareddove, text="Collared Dove", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_collareddove.pack()

                    lGBl.mainloop()

                def flGF():
                    lGrey.destroy()
                    lGF = Toplevel()
                    lGF.title(Ftitle)
                    lGF.geometry("300x570+250+50")
                    lGF["bg"] = mainbg

                    btnwidth = 250

                    frame1 = Frame(lGF)

                    lab_title = Label(frame1, text=Ftext, bg=mainbg, font=mainfont)
                    lab_title.pack(side=LEFT)

                    def main_menu_btn():
                        lGF.destroy()
                        MM.deiconify()

                    menu_btn = Button(frame1, command=main_menu_btn, text=Mtext, bg=btnbg, activebackground=activebtnbg, font=Mfont)
                    menu_btn.pack()

                    frame1.pack()

                    def bridger():
                        lGF.destroy()
                        view_details("redkite")

                    load_redkite = Image.open("redkite.jpg")
                    render_redkite = ImageTk.PhotoImage(load_redkite)
                    btn_redkite = Button(lGF, command=bridger, compound=LEFT, image=render_redkite, text="Red Kite", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_redkite.pack()

                    lGF.mainloop()

                def flGN():
                    lGrey.destroy()
                    lGN = Toplevel()
                    lGN.title(Ftitle)
                    lGN.geometry("300x570+250+50")
                    lGN["bg"] = mainbg

                    btnwidth = 250

                    frame1 = Frame(lGN)

                    lab_title = Label(frame1, text=Ftext, bg=mainbg, font=mainfont)
                    lab_title.pack(side=LEFT)

                    def main_menu_btn():
                        lGN.destroy()
                        MM.deiconify()

                    menu_btn = Button(frame1, command=main_menu_btn, text=Mtext, bg=btnbg, activebackground=activebtnbg, font=Mfont)
                    menu_btn.pack()

                    frame1.pack()

                    def bridgej():
                        lGN.destroy()
                        view_details("jackdaw")

                    def bridgep():
                        lGN.destroy()
                        view_details("partridge")

                    load_jackdaw = Image.open("jackdaw.jpg")
                    render_jackdaw = ImageTk.PhotoImage(load_jackdaw)
                    btn_jackdaw = Button(lGN, command=bridgej, compound=LEFT, image=render_jackdaw, text="Jackdaw", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_jackdaw.pack()

                    load_partridge = Image.open("partridge.jpg")
                    render_partridge = ImageTk.PhotoImage(load_partridge)
                    btn_partridge = Button(lGN, command=bridgep, compound=LEFT, image=render_partridge, text="Partridge", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_partridge.pack()

                    lGN.mainloop()

                frame1 = Frame(lGrey)
                frame2 = Frame(lGrey)
                frame3 = Frame(lGrey)

                load_barredtummy = Image.open("barredtummy.jpg")
                render_barredtummy = ImageTk.PhotoImage(load_barredtummy)
                btn_barredtummy = Button(frame1, command=flGBa, compound=TOP, image=render_barredtummy, text="Barred tummy", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth, height=btnheight)
                btn_barredtummy.pack(side=LEFT)

                load_whiteonneck = Image.open("whiteonneck.jpg")
                render_whiteonneck = ImageTk.PhotoImage(load_whiteonneck)
                btn_whiteonneck = Button(frame1, command=flGW, compound=TOP, image=render_whiteonneck, text="White on neck", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth, height=btnheight)
                btn_whiteonneck.pack(side=LEFT)

                frame1.pack()

                load_blackcollar = Image.open("blackcollar.jpg")
                render_blackcollar = ImageTk.PhotoImage(load_blackcollar)
                btn_blackcollar = Button(frame2, command=flGBl, compound=TOP, image=render_blackcollar, text="Black collar", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth, height=btnheight)
                btn_blackcollar.pack(side=LEFT)

                load_forkedtail = Image.open("forkedtail.jpg")
                render_forkedtail = ImageTk.PhotoImage(load_forkedtail)
                btn_forkedtail = Button(frame2, command=flGF, compound=TOP, image=render_forkedtail, text="Forked tail", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth, height=btnheight)
                btn_forkedtail.pack(side=LEFT)

                frame2.pack()

                load_none = Image.open("none.jpg")
                render_none = ImageTk.PhotoImage(load_none)
                btn_none = Button(frame3, command=flGN, compound=TOP, image=render_none, text="None", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth, height=btnheight)
                btn_none.pack(side=LEFT)

                frame3.pack()

                lGrey.mainloop()

            def flBrown():
                CCl.destroy()
                lBrown = Toplevel()
                lBrown.title(Fstitle)
                lBrown.geometry("300x570+250+50")
                lBrown["bg"] = mainbg

                btnwidth = 140
                btnheight = 100

                lab_title = Label(lBrown, text=Fstext, bg=mainbg, font=mainfont)
                lab_title.pack()

                def main_menu_btn():
                    lBrown.destroy()
                    MM.deiconify()

                menu_btn = Button(lBrown, command=main_menu_btn, text=Mtext, bg=btnbg, activebackground=activebtnbg, font=Mfont)
                menu_btn.pack()

                lab_space = Label(lBrown, text="", bg=mainbg)
                lab_space.pack()

                def flBrB():
                    lBrown.destroy()
                    lBrB = Toplevel()
                    lBrB.title(Ftitle)
                    lBrB.geometry("300x570+250+50")
                    lBrB["bg"] = mainbg

                    btnwidth = 250

                    frame1 = Frame(lBrB)

                    lab_title = Label(frame1, text=Ftext, bg=mainbg, font=mainfont)
                    lab_title.pack(side=LEFT)

                    def main_menu_btn():
                        lBrB.destroy()
                        MM.deiconify()

                    menu_btn = Button(frame1, command=main_menu_btn, text=Mtext, bg=btnbg, activebackground=activebtnbg, font=Mfont)
                    menu_btn.pack()

                    frame1.pack()

                    def bridgej():
                        lBrB.destroy()
                        view_details("jay")

                    load_jay = Image.open("jay.jpg")
                    render_jay = ImageTk.PhotoImage(load_jay)
                    btn_jay = Button(lBrB, command=bridgej, compound=LEFT, image=render_jay, text="Jay", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_jay.pack()

                    lBrB.mainloop()

                def flBrO():
                    lBrown.destroy()
                    lBrO = Toplevel()
                    lBrO.title(Ftitle)
                    lBrO.geometry("300x570+250+50")
                    lBrO["bg"] = mainbg

                    btnwidth = 250

                    frame1 = Frame(lBrO)

                    lab_title = Label(frame1, text=Ftext, bg=mainbg, font=mainfont)
                    lab_title.pack(side=LEFT)

                    def main_menu_btn():
                        lBrO.destroy()
                        MM.deiconify()

                    menu_btn = Button(frame1, command=main_menu_btn, text=Mtext, bg=btnbg, activebackground=activebtnbg, font=Mfont)
                    menu_btn.pack()

                    frame1.pack()

                    def bridgek():
                        lBrO.destroy()
                        view_details("kestrel")

                    def bridgerk():
                        lBrO.destroy()
                        view_details("redkite")

                    def bridger():
                        lBrO.destroy()
                        view_details("redwing")

                    load_kestrel = Image.open("kestrel.jpg")
                    render_kestrel = ImageTk.PhotoImage(load_kestrel)
                    btn_kestrel = Button(lBrO, command=bridgek, compound=LEFT, image=render_kestrel, text="Kestrel", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_kestrel.pack()

                    load_redkite = Image.open("redkite.jpg")
                    render_redkite = ImageTk.PhotoImage(load_redkite)
                    btn_redkite = Button(lBrO, command=bridgerk, compound=LEFT, image=render_redkite, text="Red Kite", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_redkite.pack()

                    load_redwing = Image.open("redwing.jpg")
                    render_redwing = ImageTk.PhotoImage(load_redwing)
                    btn_redwing = Button(lBrO, command=bridger, compound=LEFT, image=render_redwing, text="Redwing", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_redwing.pack()

                    lBrO.mainloop()

                def flBrY():
                    lBrown.destroy()
                    lBrY = Toplevel()
                    lBrY.title(Ftitle)
                    lBrY.geometry("300x570+250+50")
                    lBrY["bg"] = mainbg

                    btnwidth = 250

                    frame1 = Frame(lBrY)

                    lab_title = Label(frame1, text=Ftext, bg=mainbg, font=mainfont)
                    lab_title.pack(side=LEFT)

                    def main_menu_btn():
                        lBrY.destroy()
                        MM.deiconify()

                    menu_btn = Button(frame1, command=main_menu_btn, text=Mtext, bg=btnbg, activebackground=activebtnbg, font=Mfont)
                    menu_btn.pack()

                    frame1.pack()

                    def bridgeb():
                        lBrY.destroy()
                        view_details("buzzard")

                    def bridgek():
                        lBrY.destroy()
                        view_details("kestrel")

                    def bridger():
                        lBrY.destroy()
                        view_details("redkite")

                    def bridges():
                        lBrY.destroy()
                        view_details("sparrowhawk")

                    load_buzzard = Image.open("buzzard.jpg")
                    render_buzzard = ImageTk.PhotoImage(load_buzzard)
                    btn_buzzard = Button(lBrY, command=bridgeb, compound=LEFT, image=render_buzzard, text="Buzzard", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_buzzard.pack()

                    load_kestrel = Image.open("kestrel.jpg")
                    render_kestrel = ImageTk.PhotoImage(load_kestrel)
                    btn_kestrel = Button(lBrY, command=bridgek, compound=LEFT, image=render_kestrel, text="Kestrel", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_kestrel.pack()

                    load_redkite = Image.open("redkite.jpg")
                    render_redkite = ImageTk.PhotoImage(load_redkite)
                    btn_redkite = Button(lBrY, command=bridger, compound=LEFT, image=render_redkite, text="Red Kite", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_redkite.pack()

                    load_sparrowhawk = Image.open("sparrowhawk.jpg")
                    render_sparrowhawk = ImageTk.PhotoImage(load_sparrowhawk)
                    btn_sparrowhawk = Button(lBrY, command=bridges, compound=LEFT, image=render_sparrowhawk, text="Sparrowhawk", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_sparrowhawk.pack()

                    lBrY.mainloop()

                def flBrL():
                    lBrown.destroy()
                    lBrL = Toplevel()
                    lBrL.title(Ftitle)
                    lBrL.geometry("300x570+250+50")
                    lBrL["bg"] = mainbg

                    btnwidth = 250

                    frame1 = Frame(lBrL)

                    lab_title = Label(frame1, text=Ftext, bg=mainbg, font=mainfont)
                    lab_title.pack(side=LEFT)

                    def main_menu_btn():
                        lBrL.destroy()
                        MM.deiconify()

                    menu_btn = Button(frame1, command=main_menu_btn, text=Mtext, bg=btnbg, activebackground=activebtnbg, font=Mfont)
                    menu_btn.pack()

                    frame1.pack()

                    def bridgepf():
                        lBrL.destroy()
                        view_details("pheasantf")

                    def bridgepm():
                        lBrL.destroy()
                        view_details("pheasantm")

                    def bridger():
                        lBrL.destroy()
                        view_details("redkite")

                    load_pheasantf = Image.open("pheasantf.jpg")
                    render_pheasantf = ImageTk.PhotoImage(load_pheasantf)
                    btn_pheasantf = Button(lBrL, command=bridgepf, compound=LEFT, image=render_pheasantf, text="Pheasant\nFemale", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_pheasantf.pack()

                    load_pheasantm = Image.open("pheasantm.jpg")
                    render_pheasantm = ImageTk.PhotoImage(load_pheasantm)
                    btn_pheasantm = Button(lBrL, command=bridgepm, compound=LEFT, image=render_pheasantm, text="Pheasant\nMale", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_pheasantm.pack()

                    load_redkite = Image.open("redkite.jpg")
                    render_redkite = ImageTk.PhotoImage(load_redkite)
                    btn_redkite = Button(lBrL, command=bridger, compound=LEFT, image=render_redkite, text="Red Kite", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_redkite.pack()

                    lBrL.mainloop()

                def flBrP():
                    lBrown.destroy()
                    lBrP = Toplevel()
                    lBrP.title(Ftitle)
                    lBrP.geometry("300x570+250+50")
                    lBrP["bg"] = mainbg

                    btnwidth = 250

                    frame1 = Frame(lBrP)

                    lab_title = Label(frame1, text=Ftext, bg=mainbg, font=mainfont)
                    lab_title.pack(side=LEFT)

                    def main_menu_btn():
                        lBrP.destroy()
                        MM.deiconify()

                    menu_btn = Button(frame1, command=main_menu_btn, text=Mtext, bg=btnbg, activebackground=activebtnbg, font=Mfont)
                    menu_btn.pack()

                    frame1.pack()

                    def bridgej():
                        lBrP.destroy()
                        view_details("jay")

                    def bridger():
                        lBrP.destroy()
                        view_details("redkite")

                    load_jay = Image.open("jay.jpg")
                    render_jay = ImageTk.PhotoImage(load_jay)
                    btn_jay = Button(lBrP, command=bridgej, compound=LEFT, image=render_jay, text="Jay", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_jay.pack()

                    load_redkite = Image.open("redkite.jpg")
                    render_redkite = ImageTk.PhotoImage(load_redkite)
                    btn_redkite = Button(lBrP, command=bridger, compound=LEFT, image=render_redkite, text="Red Kite", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_redkite.pack()

                    lBrP.mainloop()

                def flBrS():
                    lBrown.destroy()
                    lBrS = Toplevel()
                    lBrS.title(Ftitle)
                    lBrS.geometry("300x570+250+50")
                    lBrS["bg"] = mainbg

                    btnwidth = 250

                    frame1 = Frame(lBrS)

                    lab_title = Label(frame1, text=Ftext, bg=mainbg, font=mainfont)
                    lab_title.pack(side=LEFT)

                    def main_menu_btn():
                        lBrS.destroy()
                        MM.deiconify()

                    menu_btn = Button(frame1, command=main_menu_btn, text=Mtext, bg=btnbg, activebackground=activebtnbg, font=Mfont)
                    menu_btn.pack()

                    frame1.pack()

                    def bridgef():
                        lBrS.destroy()
                        view_details("fieldfare")

                    def bridgem():
                        lBrS.destroy()
                        view_details("mistlethrush")

                    def bridger():
                        lBrS.destroy()
                        view_details("redwing")

                    def bridges():
                        lBrS.destroy()
                        view_details("songthrush")

                    load_fieldfare = Image.open("fieldfare.jpg")
                    render_fieldfare = ImageTk.PhotoImage(load_fieldfare)
                    btn_fieldfare = Button(lBrS, command=bridgef, compound=LEFT, image=render_fieldfare, text="Fieldfare", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_fieldfare.pack()

                    load_mistlethrush = Image.open("mistlethrush.jpg")
                    render_mistlethrush = ImageTk.PhotoImage(load_mistlethrush)
                    btn_mistlethrush = Button(lBrS, command=bridgem, compound=LEFT, image=render_mistlethrush, text="Mistle Thrush", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_mistlethrush.pack()

                    load_redwing = Image.open("redwing.jpg")
                    render_redwing = ImageTk.PhotoImage(load_redwing)
                    btn_redwing = Button(lBrS, command=bridger, compound=LEFT, image=render_redwing, text="Redwing", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_redwing.pack()

                    load_songthrush = Image.open("songthrush.jpg")
                    render_songthrush = ImageTk.PhotoImage(load_songthrush)
                    btn_songthrush = Button(lBrS, command=bridges, compound=LEFT, image=render_songthrush, text="Song Thrush", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth)
                    btn_songthrush.pack()

                    lBrS.mainloop()

                frame1 = Frame(lBrown)
                frame2 = Frame(lBrown)
                frame3 = Frame(lBrown)

                load_bluefeathers = Image.open("bluefeathers.jpg")
                render_bluefeathers = ImageTk.PhotoImage(load_bluefeathers)
                btn_bluefeathers = Button(frame1, command=flBrB, compound=TOP, image=render_bluefeathers, text="Blue feathers", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth, height=btnheight)
                btn_bluefeathers.pack(side=LEFT)

                load_orangeredpink = Image.open("orangeredpink.jpg")
                render_orangeredpink = ImageTk.PhotoImage(load_orangeredpink)
                btn_orangeredpink = Button(frame1, command=flBrO, compound=TOP, image=render_orangeredpink, text="Orange/red/pink", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth, height=btnheight)
                btn_orangeredpink.pack(side=LEFT)

                frame1.pack()

                load_yellowlegs = Image.open("yellowlegs.jpg")
                render_yellowlegs = ImageTk.PhotoImage(load_yellowlegs)
                btn_yellowlegs = Button(frame2, command=flBrY, compound=TOP, image=render_yellowlegs, text="Yellow legs", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth, height=btnheight)
                btn_yellowlegs.pack(side=LEFT)

                load_longtail = Image.open("longtail.jpg")
                render_longtail = ImageTk.PhotoImage(load_longtail)
                btn_longtail = Button(frame2, command=flBrL, compound=TOP, image=render_longtail, text="Long tail", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth, height=btnheight)
                btn_longtail.pack(side=LEFT)

                frame2.pack()

                load_speckledchest = Image.open("speckledchest.jpg")
                render_speckledchest = ImageTk.PhotoImage(load_speckledchest)
                btn_speckledchest = Button(frame3, command=flBrS, compound=TOP, image=render_speckledchest, text="Speckled chest", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth, height=btnheight)
                btn_speckledchest.pack(side=LEFT)

                load_palehead = Image.open("palehead.jpg")
                render_palehead = ImageTk.PhotoImage(load_palehead)
                btn_palehead = Button(frame3, command=flBrP, compound=TOP, image=render_palehead, text="Pale head", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth, height=btnheight)
                btn_palehead.pack(side=LEFT)

                frame3.pack()

                lBrown.mainloop()


            frame1 = Frame(CCl)
            frame2 = Frame(CCl)
            frame3 = Frame(CCl)

            load_black = Image.open("black.jpg")
            render_black = ImageTk.PhotoImage(load_black)
            btn_black = Button(frame1, command=flBlack, compound=TOP, image=render_black, text="Black", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth, height=btnheight)
            btn_black.pack(side=LEFT)

            load_brown = Image.open("brown.jpg")
            render_brown = ImageTk.PhotoImage(load_brown)
            btn_brown = Button(frame1, command=flBrown, compound=TOP, image=render_brown, text="Brown", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth, height=btnheight)
            btn_brown.pack(side=LEFT)

            frame1.pack()

            load_grey = Image.open("grey.jpg")
            render_grey = ImageTk.PhotoImage(load_grey)
            btn_grey = Button(frame2, command=flGrey, compound=TOP, image=render_grey, text="Grey", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth, height=btnheight)
            btn_grey.pack(side=LEFT)

            load_speckled = Image.open("speckled.jpg")
            render_speckled = ImageTk.PhotoImage(load_speckled)
            btn_speckled = Button(frame2, command=flSpeckled, compound=TOP, image=render_speckled, text="Speckled", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth, height=btnheight)
            btn_speckled.pack(side=LEFT)

            frame2.pack()

            load_white = Image.open("white.jpg")
            render_white = ImageTk.PhotoImage(load_white)
            btn_white = Button(frame3, command=flW, compound=TOP, image=render_white, text="White", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth, height=btnheight)
            btn_white.pack(side=LEFT)

            load_yellowgreen = Image.open("yellowgreen.jpg")
            render_yellowgreen = ImageTk.PhotoImage(load_yellowgreen)
            btn_yellowgreen = Button(frame3, command=flY, compound=TOP, image=render_yellowgreen, text="Yellow/green", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth, height=btnheight)
            btn_yellowgreen.pack(side=LEFT)

            frame3.pack()

            CCl.mainloop()

        lab_title = Label(CS, text=CStext, font=mainfont, bg=mainbg)
        lab_title.pack()

        def main_menu_btn():
                CS.destroy()
                MM.deiconify()

        menu_btn = Button(CS, command=main_menu_btn, text=Mtext, bg=btnbg, activebackground=activebtnbg, font=Mfont)
        menu_btn.pack()

        lab1 = Label(CS, text="", bg=mainbg, height = 6)
        lab1.pack()

        frame1 = Frame(CS)

        load_small = Image.open("small.jpg")
        render_small = ImageTk.PhotoImage(load_small)
        btn_small = Button(frame1, compound=TOP, command=fCCs, image=render_small, text="Small \n< 6 inches", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth, height=btnheight)
        btn_small.pack(side=LEFT)

        load_large = Image.open("buzzard.jpg")
        render_large = ImageTk.PhotoImage(load_large)
        btn_large = Button(frame1, compound=TOP, command=fCCl, image=render_large, text="Medium-large\n> 6 inches", font=mainfont, bg=btnbg, activebackground=activebtnbg, width=btnwidth, height=btnheight)
        btn_large.pack()

        frame1.pack()

        CS.mainloop()
    

    lab0 = Label(MM, text="", bg=mainbg)
    lab0.pack()

    #selects a different bird to be displayed every time
    randombird = random.choice(menu_birds)
    randombird = randombird + ".jpg"

    load_bird = Image.open(randombird)
    render_bird = ImageTk.PhotoImage(load_bird)
    lab_bird = Label(MM, bg=mainbg, image=render_bird)
    lab_bird.pack()

    lab1 = Label(MM, text="", bg=mainbg)
    lab1.pack()
    btn_identify = Button(MM, command=fCS, text="Identify a bird", width=15, height=2, font=mainfont, bg=btnbg, activebackground=activebtnbg)
    btn_identify.pack()
    lab2 = Label(MM, text="", bg=mainbg)
    lab2.pack()
    btn_mybirds = Button(MM, command=my_identified_birds, text="My birds", width=15, height=2, font=mainfont, bg=btnbg, activebackground=activebtnbg)
    btn_mybirds.pack()
    lab3 = Label(MM, text="", bg=mainbg)
    lab3.pack()
    btn_searchbirds = Button(MM, command=search_birds_page, text="Search birds", width=15, height=2, font=mainfont, bg=btnbg, activebackground=activebtnbg)
    btn_searchbirds.pack()
    
    MM.mainloop()

main_menu(menu_birds)

c.close()
conn.close()

c1.close()
conn1.close()


