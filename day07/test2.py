# 使用尺寸器进行布局

import wx


def load():
    '''
    打开文件
    :return:
    '''
    with open(filename.GetValue()) as file:
        contents.SetValue(file.read())


def save():
    '''
    保存编辑的内容
    :return:
    '''
    with open(filename.GetValue(), mode='w') as file:
        file.write(contents.GetValue())


app = wx.App()
win = wx.Frame(None, title="Demo", size=(410, 335))
panel = wx.Panel(win)

loadButton = wx.Button(panel, label="Open")
saveButton = wx.Button(panel, label="Save")

loadButton.Bind(wx.EVT_BUTTON, load)
saveButton.Bind(wx.EVT_BUTTON, save)

filename = wx.TextCtrl(panel)
contents = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.HSCROLL)

# 构建尺寸器
hbox = wx.BoxSizer()
hbox.Add(filename, proportion=1, flag=wx.EXPAND)
hbox.Add(loadButton, proportion=0, flag=wx.LEFT, border=5)
hbox.Add(saveButton, proportion=0, flag=wx.LEFT, border=5)

vbox = wx.BoxSizer(wx.VERTICAL)
vbox.Add(hbox, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)
vbox.Add(contents, proportion=1, flag=wx.EXPAND | wx.LEFT | wx.BOTTOM | wx.RIGHT, border=5)

panel.SetSizer(vbox)
win.Show()

app.MainLoop()
