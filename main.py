"""
@author: Shiva Shanker Reddy
"""


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


        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        
        
        self.quote = wx.StaticText(panel, label= 'Your quote: ', pos= (0, 30))
        vbox.Add(self.quote, 1, wx.ALL|wx.EXPAND, 10)
        # self.text_ctrl = wx.TextCtrl(panel, size=(size[0]/2,40), pos=(100, 30), style=wx.TE_MULTILINE)
        # self.text_ctrl.Bind(wx.EVT_TEXT_ENTER, self.OnEnterPressed)
        
        b1 = wx.Button(panel, label="Btn1")
        vbox.Add(b1, 0, wx.EXPAND)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        b3 = wx.Button(panel, label = "Btn3")
        hbox.Add(b3, 0, wx.ALL|wx.EXPAND)

        self.Show(True)


    def OnEnterPressed(self,event): 
        print ("Enter pressed")
        text = self.text_ctrl.GetValue()
        run(text)




app = wx.App(False)
frame = View(None)
# # frame = MainWindow(None, title="Small Editor")
app.MainLoop()

