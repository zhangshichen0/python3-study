# 初始化窗口，当窗口变化时，组件不能随着变化，缺点过多

import wx

app = wx.App()
win = wx.Frame(None, title="Demo", size=(410, 335))
win.Show()
loadButton = wx.Button(win, label="Open", pos=(225, 5), size=(85, 25))
saveButton = wx.Button(win, label="Save", pos=(310, 5), size=(85, 25))
fileName = wx.TextCtrl(win, pos=(5,5), size=(220, 25))
contents = wx.TextCtrl(win, pos=(5, 35), size=(390, 260), style=wx.TE_MULTILINE | wx.HSCROLL)
app.MainLoop()