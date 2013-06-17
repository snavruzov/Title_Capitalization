__author__ = 'snavruzov'

import wx


def ShowTitle(event):
    labelValue = titleLabel.GetValue()
    textArea.SetValue(capitalizeTitle(labelValue))


def capitalizeTitle(value):
    global lowerCaseConsts
    title = ""
    value = value.lower()
    splitWord = value.split(' ')
    for word in splitWord:
        if word not in lowerCaseConsts:
            title += " " + word.capitalize()
        else:
            title += " " + word

    return title.strip()


app = wx.App()

lowerCaseConsts = ['the', 'a', 'to', 'at', 'in', 'with', 'and', 'but', 'or', 'on']

frame = wx.Frame(None, title="Title Capitalization", size=(400, 400))
frame.Show()

goButton = wx.Button(frame, label="Capitalize", pos=(160, 20), size=(80, 30))
goButton.Bind(wx.EVT_BUTTON, ShowTitle)

textArea = wx.TextCtrl(frame, style=wx.TE_MULTILINE, pos=(20, 100), size=(360, 250))

titleLabel = wx.TextCtrl(frame, pos=(20, 60), size=(360, 30))
titleLabel.SetValue("Enter the title...")

app.MainLoop()
