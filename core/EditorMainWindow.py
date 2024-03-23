#!/usr/bin/env python
# coding: utf-8

# 编辑器的主界面

import tkinter as tk
import ttkbootstrap as ttk
from .EditorUtils import Link
import sys

class EditorMainWindow(ttk.Window):
    def __init__(
            self
            )->None:
        # 系统缩放比例
        self.sz = self.get_screenzoom()
        Link['sz'] = self.sz
        super().__init__(
            iconphoto   = './assets/icon.png',
            size        = (int(1500*self.sz),int(800*self.sz)),
            resizable   = (True,True),
        )
    # 获取系统的缩放比例
    def get_screenzoom(self)->float:
        if 'win32' in sys.platform:
            try:
                from ctypes import windll
                return windll.shcore.GetScaleFactorForDevice(0) / 100
            except:
                return 1.0
        elif 'linux' in sys.platform:
            return 1.0
        else:
            print(sys.platform)
            return 2.0