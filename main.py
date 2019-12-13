"""
@author: Shiva Shanker Reddy
"""


import os
import wx
from tts import run


class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size = (800, 800))
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        # self.CreateStatusBar()

        # Setting up the menu.
        filemenu= wx.Menu()

        # wx.ID_ABOUT and wx.ID_EXIT are standard IDs provided by wxWidgets.
        menuAbout = filemenu.Append(wx.ID_ABOUT, "&About"," Information about this program")
        filemenu.AppendSeparator()
        menuExit = filemenu.Append(wx.ID_EXIT,"E&xit"," Terminate the program")

        # creating the menubar
        menuBar = wx.MenuBar()

        # adding the "filename" to the menubar
        menuBar.Append(filemenu, "&file")
        self.SetMenuBar(menuBar) # Adding the MenuBar to the Frame content.

        # Set events.
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)

        self.lblname = wx.StaticText(self, label="Your name :")

        self.Show(True)

    
    def OnAbout(self, e):
        # A message dialog box with an OK button. wx.OK is a standard ID in wxWidgets.
        dlg = wx.MessageDialog( self, "A small text editor",
                "About Sample Editor",
                wx.OK)
        dlg.ShowModal() #show it
        dlg.Destroy() # finally destroy it when finihed
    

    def OnExit(self, e):
        dlg = wx.MessageDialog(self, "Are you sure to close it..??", "Exit Now",
                wx.OK | wx.CANCEL)
        rel = dlg.ShowModal()
        if rel == wx.ID_OK:
            self.Close(True)
        elif rel == wx.ID_CANCEL:
            dlg.Close(True)

# hbox3 = wx.BoxSizer(wx.HORIZONTAL) 
        # l3 = wx.StaticText(panel, -1, "Multiline Text") 
            
        # hbox3.Add(l3,1, wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5) 
        # self.t3 = wx.TextCtrl(panel,size = (200,100),style = wx.TE_MULTILINE) 
            
        # hbox3.Add(self.t3,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5) 
        # vbox.Add(hbox3) 
        # self.t3.Bind(wx.EVT_TEXT_ENTER,self.OnEnterPressed)



class View(wx.Frame):
    def __init__(self, parent, size= (800, 800)):
        wx.Frame.__init__(self, parent, title="Main View", size=size)


        self.panel = wx.Panel(self)
        self.vbox = wx.BoxSizer(wx.VERTICAL)
        self.hbox = wx.BoxSizer(wx.VERTICAL)
        self.static_text()
        self.text = self.text_ctrl()


        # play button
        play_button = wx.Button(self.panel, label="Play", pos=(100,180))
        self.vbox.Add(play_button, 0, wx.EXPAND)
        self.Bind(wx.EVT_BUTTON, self.play_text, play_button)


        # clear button
        clear_button = wx.Button(self.panel, label="Clear", pos=(200,180))
        self.vbox.Add(clear_button, 0, wx.EXPAND)
        self.Bind(wx.EVT_BUTTON, self.clear_text, clear_button) 


        # this button is for opening the text file
        text_button = wx.Button(self.panel, label="Open and Play", pos=(100,250))
        self.vbox.Add(text_button, 0, wx.EXPAND)
        self.Bind(wx.EVT_BUTTON, self.open_file, text_button)
        self.line_text = self.text_ctrl()
        self.number_text = self.static_text(label="enter the line to read from:", 
                                            pos=(200, 255)
                                        )

        self.numberText = self.text_ctrl(size=(40,20), pos=(345, 250), style=wx.TE_PROCESS_ENTER)
       
        self.Show(True)

    def static_text(self, label= 'Your text to play', pos=(0,30)):
        quote = wx.StaticText(self.panel, label=label, pos= pos)
        return (quote)


    def text_ctrl(self, size=(240, 140), pos=(100, 30), 
                    style=wx.TE_MULTILINE,
                    value=''
                ):
        text = wx.TextCtrl(self.panel, size=size, pos=pos,
                            style=style,
                            value=value
                        )
        return (text)
    

    def clear_text(self, event):
        return (self.text.SetValue(""))


    def open_file(self, event):
        """ Open a file"""
        if (self.numberText.GetValue()):
            line_number = eval(self.numberText.GetValue())
        else:
            line_number = 0
        print("line number:   ", self.numberText.GetValue())
        self.dirname = ''
        self.open_file_text = ''
        dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.*", wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            f = open(os.path.join(self.dirname, self.filename), 'r')
            self.open_file_text = f.read(line_number)
            run(self.open_file_text)
            # self.control.SetValue(f.read())
            f.close()
        dlg.Destroy()


    def play_text(self,event):
        text = self.text.GetValue()
        run(text)


app = wx.App(False)
frame = View(None)
# # frame = MainWindow(None, title="Small Editor")
app.MainLoop()

