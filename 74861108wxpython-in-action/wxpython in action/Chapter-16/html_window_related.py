import wx
import wx.html

class MyHtmlFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, -1, title, size=(600,400))
        self.CreateStatusBar()
        
        html = wx.html.HtmlWindow(self)
        if "gtk2" in wx.PlatformInfo:
            html.SetStandardFonts()
        html.SetRelatedFrame(self, self.GetTitle() + " -- %s")
        html.SetRelatedStatusBar(0)

        wx.CallAfter(
            html.LoadPage, "http://www.bitunion.org/thread-10185752-1-1.html")

app = wx.PySimpleApp()
frm = MyHtmlFrame(None, "Simple HTML Browser")
frm.Show()
app.MainLoop()
