# !/usr/bin/python
# coding:utf-8

# 功能：WxPythonj绘制界面
# 作者：吴勇
# 创建时间：2020/9/92

import wx
import wx.xrc


class MyFrame1(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title="界面", pos=wx.DefaultPosition,
                          size=wx.Size(768, 790), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        self.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_MENU))

        sbSizer1 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, wx.EmptyString), wx.VERTICAL)

        self.m_notebook1 = wx.Notebook(sbSizer1.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_notebook1.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_MENU))

        self.m_panel29 = wx.Panel(self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        sbSizer33 = wx.StaticBoxSizer(wx.StaticBox(self.m_panel29, wx.ID_ANY, wx.EmptyString), wx.VERTICAL)

        self.m_panel30 = wx.Panel(sbSizer33.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                  wx.TAB_TRAVERSAL)
        sbSizer37 = wx.StaticBoxSizer(wx.StaticBox(self.m_panel30, wx.ID_ANY, wx.EmptyString), wx.HORIZONTAL)

        self.m_staticText22 = wx.StaticText(sbSizer37.GetStaticBox(), wx.ID_ANY, u"     ", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText22.Wrap(-1)
        sbSizer37.Add(self.m_staticText22, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_button17 = wx.Button(sbSizer37.GetStaticBox(), wx.ID_ANY, u"按钮1", wx.DefaultPosition, wx.DefaultSize,
                                    0)
        self.m_button17.SetDefault()
        sbSizer37.Add(self.m_button17, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_staticText23 = wx.StaticText(sbSizer37.GetStaticBox(), wx.ID_ANY, u"     ", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText23.Wrap(-1)
        sbSizer37.Add(self.m_staticText23, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_button18 = wx.Button(sbSizer37.GetStaticBox(), wx.ID_ANY, u"按钮2", wx.DefaultPosition, wx.DefaultSize,
                                    0)
        self.m_button18.SetDefault()
        sbSizer37.Add(self.m_button18, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_staticText16 = wx.StaticText(sbSizer37.GetStaticBox(), wx.ID_ANY, u"     ", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText16.Wrap(-1)
        sbSizer37.Add(self.m_staticText16, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_button10 = wx.Button(sbSizer37.GetStaticBox(), wx.ID_ANY, u"按钮3", wx.DefaultPosition, wx.DefaultSize,
                                    0)
        self.m_button10.SetDefault()
        sbSizer37.Add(self.m_button10, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_staticText17 = wx.StaticText(sbSizer37.GetStaticBox(), wx.ID_ANY, u"     ", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText17.Wrap(-1)
        sbSizer37.Add(self.m_staticText17, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_button111 = wx.Button(sbSizer37.GetStaticBox(), wx.ID_ANY, u"按钮4", wx.DefaultPosition,
                                     wx.DefaultSize, 0)
        self.m_button111.SetDefault()
        sbSizer37.Add(self.m_button111, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_staticText171 = wx.StaticText(sbSizer37.GetStaticBox(), wx.ID_ANY, u"    ", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText171.Wrap(-1)
        sbSizer37.Add(self.m_staticText171, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_button11 = wx.Button(sbSizer37.GetStaticBox(), wx.ID_ANY, u"按钮5", wx.DefaultPosition, wx.DefaultSize,
                                    0)
        self.m_button11.SetDefault()
        sbSizer37.Add(self.m_button11, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_panel30.SetSizer(sbSizer37)
        self.m_panel30.Layout()
        sbSizer37.Fit(self.m_panel30)
        sbSizer33.Add(self.m_panel30, 1, wx.EXPAND | wx.ALL, 5)

        self.m_panel19 = wx.Panel(sbSizer33.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                  wx.TAB_TRAVERSAL)
        sbSizer20 = wx.StaticBoxSizer(wx.StaticBox(self.m_panel19, wx.ID_ANY, wx.EmptyString), wx.HORIZONTAL)

        self.m_textCtrl10 = wx.TextCtrl(sbSizer20.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                        wx.DefaultSize, wx.TE_MULTILINE)
        sbSizer20.Add(self.m_textCtrl10, 1, wx.ALL | wx.EXPAND, 5)

        self.m_panel19.SetSizer(sbSizer20)
        self.m_panel19.Layout()
        sbSizer20.Fit(self.m_panel19)
        sbSizer33.Add(self.m_panel19, 1, wx.EXPAND | wx.ALL, 5)

        self.m_panel29.SetSizer(sbSizer33)
        self.m_panel29.Layout()
        sbSizer33.Fit(self.m_panel29)
        self.m_notebook1.AddPage(self.m_panel29, u"Page1", False)
        self.m_panel8 = wx.Panel(self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.m_panel8.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_MENU))

        sbSizer9 = wx.StaticBoxSizer(wx.StaticBox(self.m_panel8, wx.ID_ANY, wx.EmptyString), wx.VERTICAL)

        self.m_panel2 = wx.Panel(sbSizer9.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                 wx.TAB_TRAVERSAL)
        sbSizer3 = wx.StaticBoxSizer(wx.StaticBox(self.m_panel2, wx.ID_ANY, u""), wx.VERTICAL)

        self.m_textCtrl1 = wx.TextCtrl(sbSizer3.GetStaticBox(), wx.ID_ANY,"",
                                       wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE)
        sbSizer3.Add(self.m_textCtrl1, 1, wx.ALL | wx.EXPAND, 5)

        self.m_panel2.SetSizer(sbSizer3)
        self.m_panel2.Layout()
        sbSizer3.Fit(self.m_panel2)
        sbSizer9.Add(self.m_panel2, 1, wx.EXPAND | wx.ALL, 5)

        self.m_panel4 = wx.Panel(sbSizer9.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                 wx.TAB_TRAVERSAL)
        sbSizer6 = wx.StaticBoxSizer(wx.StaticBox(self.m_panel4, wx.ID_ANY, u""), wx.HORIZONTAL)

        self.m_textCtrl3 = wx.TextCtrl(sbSizer6.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                       wx.DefaultSize, wx.TE_MULTILINE)
        sbSizer6.Add(self.m_textCtrl3, 1, wx.ALL | wx.EXPAND, 5)

        self.m_button1 = wx.Button(sbSizer6.GetStaticBox(), wx.ID_ANY, u"按钮", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button1.SetDefault()
        sbSizer6.Add(self.m_button1, 0, wx.ALL | wx.ALIGN_BOTTOM, 5)

        self.m_button3 = wx.Button(sbSizer6.GetStaticBox(), wx.ID_ANY, u"按钮", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button3.SetDefault()
        sbSizer6.Add(self.m_button3, 0, wx.ALL | wx.ALIGN_BOTTOM, 5)

        self.m_panel4.SetSizer(sbSizer6)
        self.m_panel4.Layout()
        sbSizer6.Fit(self.m_panel4)
        sbSizer9.Add(self.m_panel4, 1, wx.EXPAND | wx.ALL, 5)

        self.m_panel8.SetSizer(sbSizer9)
        self.m_panel8.Layout()
        sbSizer9.Fit(self.m_panel8)
        self.m_notebook1.AddPage(self.m_panel8, u"Page 2", False)
        self.m_panel81 = wx.Panel(self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.m_panel81.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_MENU))

        sbSizer91 = wx.StaticBoxSizer(wx.StaticBox(self.m_panel81, wx.ID_ANY, wx.EmptyString), wx.VERTICAL)

        self.m_panel21 = wx.Panel(sbSizer91.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                  wx.TAB_TRAVERSAL)
        sbSizer31 = wx.StaticBoxSizer(wx.StaticBox(self.m_panel21, wx.ID_ANY, u""), wx.VERTICAL)

        self.m_textCtrl11 = wx.TextCtrl(sbSizer31.GetStaticBox(), wx.ID_ANY,
                                        u"",
                                        wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE)
        sbSizer31.Add(self.m_textCtrl11, 1, wx.ALL | wx.EXPAND, 5)

        self.m_panel21.SetSizer(sbSizer31)
        self.m_panel21.Layout()
        sbSizer31.Fit(self.m_panel21)
        sbSizer91.Add(self.m_panel21, 1, wx.EXPAND | wx.ALL, 5)

        self.m_panel41 = wx.Panel(sbSizer91.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                  wx.TAB_TRAVERSAL)
        sbSizer61 = wx.StaticBoxSizer(wx.StaticBox(self.m_panel41, wx.ID_ANY, u""), wx.HORIZONTAL)

        self.m_textCtrl31 = wx.TextCtrl(sbSizer61.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                        wx.DefaultSize, wx.TE_MULTILINE)
        sbSizer61.Add(self.m_textCtrl31, 1, wx.ALL | wx.EXPAND, 5)

        self.m_button12 = wx.Button(sbSizer61.GetStaticBox(), wx.ID_ANY, u"按钮", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button12.SetDefault()
        sbSizer61.Add(self.m_button12, 0, wx.ALL | wx.ALIGN_BOTTOM, 5)

        self.m_button31 = wx.Button(sbSizer61.GetStaticBox(), wx.ID_ANY, u"按钮", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button31.SetDefault()
        sbSizer61.Add(self.m_button31, 0, wx.ALL | wx.ALIGN_BOTTOM, 5)

        self.m_panel41.SetSizer(sbSizer61)
        self.m_panel41.Layout()
        sbSizer61.Fit(self.m_panel41)
        sbSizer91.Add(self.m_panel41, 1, wx.EXPAND | wx.ALL, 5)

        self.m_panel81.SetSizer(sbSizer91)
        self.m_panel81.Layout()
        sbSizer91.Fit(self.m_panel81)
        self.m_notebook1.AddPage(self.m_panel81, u"Page 3", True)
        self.m_panel11 = wx.Panel(self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.m_panel11.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_MENU))

        sbSizer11 = wx.StaticBoxSizer(wx.StaticBox(self.m_panel11, wx.ID_ANY, wx.EmptyString), wx.VERTICAL)

        self.m_panel15 = wx.Panel(sbSizer11.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                  wx.TAB_TRAVERSAL)
        sbSizer16 = wx.StaticBoxSizer(wx.StaticBox(self.m_panel15, wx.ID_ANY, u""), wx.VERTICAL)

        self.m_textCtrl4 = wx.TextCtrl(sbSizer16.GetStaticBox(), wx.ID_ANY,
                                       u"",
                                       wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE)
        sbSizer16.Add(self.m_textCtrl4, 1, wx.ALL | wx.EXPAND, 5)

        self.m_panel15.SetSizer(sbSizer16)
        self.m_panel15.Layout()
        sbSizer16.Fit(self.m_panel15)
        sbSizer11.Add(self.m_panel15, 1, wx.EXPAND | wx.ALL, 5)

        self.m_panel16 = wx.Panel(sbSizer11.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                  wx.TAB_TRAVERSAL)
        sbSizer17 = wx.StaticBoxSizer(wx.StaticBox(self.m_panel16, wx.ID_ANY, u""), wx.HORIZONTAL)

        self.m_textCtrl5 = wx.TextCtrl(sbSizer17.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                       wx.DefaultSize, wx.TE_MULTILINE)
        sbSizer17.Add(self.m_textCtrl5, 1, wx.ALL | wx.EXPAND, 5)

        self.m_button5 = wx.Button(sbSizer17.GetStaticBox(), wx.ID_ANY, u"按钮", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button5.SetDefault()
        sbSizer17.Add(self.m_button5, 0, wx.ALL | wx.ALIGN_BOTTOM, 5)

        self.m_button6 = wx.Button(sbSizer17.GetStaticBox(), wx.ID_ANY, u"按钮", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button6.SetDefault()
        sbSizer17.Add(self.m_button6, 0, wx.ALL | wx.ALIGN_BOTTOM, 5)

        self.m_panel16.SetSizer(sbSizer17)
        self.m_panel16.Layout()
        sbSizer17.Fit(self.m_panel16)
        sbSizer11.Add(self.m_panel16, 1, wx.EXPAND | wx.ALL, 5)

        self.m_panel11.SetSizer(sbSizer11)
        self.m_panel11.Layout()
        sbSizer11.Fit(self.m_panel11)
        self.m_notebook1.AddPage(self.m_panel11, u"Page 4", False)
        self.m_panel12 = wx.Panel(self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.m_panel12.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_MENU))

        sbSizer111 = wx.StaticBoxSizer(wx.StaticBox(self.m_panel12, wx.ID_ANY, wx.EmptyString), wx.VERTICAL)

        self.m_panel151 = wx.Panel(sbSizer111.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                   wx.TAB_TRAVERSAL)
        sbSizer161 = wx.StaticBoxSizer(wx.StaticBox(self.m_panel151, wx.ID_ANY, u""), wx.VERTICAL)

        self.m_textCtrl41 = wx.TextCtrl(sbSizer161.GetStaticBox(), wx.ID_ANY,
                                        u"",
                                        wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE)
        sbSizer161.Add(self.m_textCtrl41, 1, wx.ALL | wx.EXPAND, 5)

        self.m_panel151.SetSizer(sbSizer161)
        self.m_panel151.Layout()
        sbSizer161.Fit(self.m_panel151)
        sbSizer111.Add(self.m_panel151, 1, wx.EXPAND | wx.ALL, 5)

        self.m_panel161 = wx.Panel(sbSizer111.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                   wx.TAB_TRAVERSAL)
        sbSizer171 = wx.StaticBoxSizer(wx.StaticBox(self.m_panel161, wx.ID_ANY, u""), wx.HORIZONTAL)

        self.m_textCtrl51 = wx.TextCtrl(sbSizer171.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                        wx.DefaultSize, wx.TE_MULTILINE)
        sbSizer171.Add(self.m_textCtrl51, 1, wx.ALL | wx.EXPAND, 5)

        self.m_button51 = wx.Button(sbSizer171.GetStaticBox(), wx.ID_ANY, u"按钮", wx.DefaultPosition, wx.DefaultSize,
                                    0)
        self.m_button51.SetDefault()
        sbSizer171.Add(self.m_button51, 0, wx.ALL | wx.ALIGN_BOTTOM, 5)

        self.m_button61 = wx.Button(sbSizer171.GetStaticBox(), wx.ID_ANY, u"按钮", wx.DefaultPosition, wx.DefaultSize,
                                    0)
        self.m_button61.SetDefault()
        sbSizer171.Add(self.m_button61, 0, wx.ALL | wx.ALIGN_BOTTOM, 5)

        self.m_panel161.SetSizer(sbSizer171)
        self.m_panel161.Layout()
        sbSizer171.Fit(self.m_panel161)
        sbSizer111.Add(self.m_panel161, 1, wx.EXPAND | wx.ALL, 5)

        self.m_panel12.SetSizer(sbSizer111)
        self.m_panel12.Layout()
        sbSizer111.Fit(self.m_panel12)
        self.m_notebook1.AddPage(self.m_panel12, u"Page 5", False)

        sbSizer1.Add(self.m_notebook1, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(sbSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_button17.Bind(wx.EVT_BUTTON, self.cshihuanjing)
        self.m_button18.Bind(wx.EVT_BUTTON, self.yufabu)
        self.m_button10.Bind(wx.EVT_BUTTON, self.xianshanghuanj)
        self.m_button111.Bind(wx.EVT_BUTTON, self.yunkong)
        self.m_button11.Bind(wx.EVT_BUTTON, self.chakan)
        self.m_button1.Bind(wx.EVT_BUTTON, self.test_1)
        self.m_button3.Bind(wx.EVT_BUTTON, self.test_2)
        self.m_button12.Bind(wx.EVT_BUTTON, self.test_3)
        self.m_button31.Bind(wx.EVT_BUTTON, self.test_4)
        self.m_button5.Bind(wx.EVT_BUTTON, self.fasongoffice)
        self.m_button6.Bind(wx.EVT_BUTTON, self.qingchuoffice)
        self.m_button51.Bind(wx.EVT_BUTTON, self.fasongxiazaiqi)
        self.m_button61.Bind(wx.EVT_BUTTON, self.qingchuxiazaiqi)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def cshihuanjing(self, event):
        pass

    def yufabu(self, event):
        pass

    def xianshanghuanj(self, event):
        pass

    def yunkong(self, event):
        pass

    def chakan(self, event):
        pass

    # ====================================================Page 2================================================================================
    def test_1(self, event):
        pass


    def test_2(self, event):
        pass

    def test_3(self, event):
        pass

    def test_4(self, event):
        pass

    # =========================================================================Page 3===============================================================
    def fasongoffice(self, event):
        pass

    def qingchuoffice(self, event):
        pass

# =======================================================================Page 4================================================================
    def fasongxiazaiqi(self, event):
        pass

    def qingchuxiazaiqi(self, event):
        pass

def main():
    app = wx.App(False)
    frame = MyFrame1(None)
    frame.Show(True)
    app.MainLoop()

if __name__ == '__main__':
    main()
