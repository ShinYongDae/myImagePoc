; CLW file contains information for the MFC ClassWizard

[General Info]
Version=1
LastClass=COpenMFCView
LastTemplate=CDialog
NewFileInclude1=#include "stdafx.h"
NewFileInclude2=#include "openmfc.h"
LastPage=0

ClassCount=7
Class1=CChildFrame
Class2=CMainFrame
Class3=COpenMFCApp
Class4=CAboutDlg
Class5=COpenMFCDoc
Class6=COpenMFCView

ResourceCount=4
Resource1=IDD_ABOUTBOX
Resource2=IDR_OPENMFTYPE
Class7=CMyLogViewDlg
Resource3=IDR_MAINFRAME
Resource4=IDD_LOGVIEW_BAR (English (U.S.))

[CLS:CChildFrame]
Type=0
BaseClass=CMDIChildWnd
HeaderFile=ChildFrm.h
ImplementationFile=ChildFrm.cpp

[CLS:CMainFrame]
Type=0
BaseClass=CMDIFrameWnd
HeaderFile=MainFrm.h
ImplementationFile=MainFrm.cpp

[CLS:COpenMFCApp]
Type=0
BaseClass=CWinApp
HeaderFile=OpenMFC.h
ImplementationFile=OpenMFC.cpp
Filter=N
VirtualFilter=AC
LastObject=COpenMFCApp

[CLS:CAboutDlg]
Type=0
BaseClass=CDialog
HeaderFile=OpenMFC.cpp
ImplementationFile=OpenMFC.cpp
LastObject=ID_EDIT_CUT

[CLS:COpenMFCDoc]
Type=0
BaseClass=CDocument
HeaderFile=OpenMFCDoc.h
ImplementationFile=OpenMFCDoc.cpp

[CLS:COpenMFCView]
Type=0
BaseClass=CScrollView
HeaderFile=OpenMFCView.h
ImplementationFile=OpenMFCView.cpp
LastObject=COpenMFCView
Filter=C
VirtualFilter=VWC

[DLG:IDD_ABOUTBOX]
Type=1
Class=CAboutDlg
ControlCount=4
Control1=IDC_STATIC,static,1342177283
Control2=IDC_STATIC,static,1342308480
Control3=IDC_STATIC,static,1342308352
Control4=IDOK,button,1342373889

[MNU:IDR_OPENMFTYPE]
Type=1
Class=COpenMFCView
Command1=ID_FILE_NEW
Command2=ID_FILE_OPEN
Command3=ID_FILE_CLOSE
Command4=ID_FILE_SAVE
Command5=ID_FILE_SAVE_AS
Command6=ID_FILE_ALL_CLOSE
Command7=ID_FILE_PRINT
Command8=ID_FILE_PRINT_PREVIEW
Command9=ID_FILE_PRINT_SETUP
Command10=ID_FILE_MRU_FILE1
Command11=ID_APP_EXIT
Command12=ID_EDIT_UNDO
Command13=ID_EDIT_CUT
Command14=ID_EDIT_COPY
Command15=ID_EDIT_PASTE
Command16=ID_VIEW_TOOLBAR
Command17=ID_VIEW_STATUS_BAR
Command18=ID_WINDOW_NEW
Command19=ID_WINDOW_CASCADE
Command20=ID_WINDOW_TILE_HORZ
Command21=ID_WINDOW_ARRANGE
Command22=ID_APP_ABOUT
CommandCount=22

[TB:IDR_MAINFRAME]
Type=1
Class=?
Command1=ID_FILE_NEW
Command2=ID_FILE_OPEN
Command3=ID_FILE_SAVE
Command4=ID_EDIT_CUT
Command5=ID_EDIT_COPY
Command6=ID_EDIT_PASTE
Command7=ID_FILE_PRINT
Command8=ID_APP_ABOUT
CommandCount=8

[MNU:IDR_MAINFRAME]
Type=1
Class=COpenMFCApp
Command1=ID_FILE_NEW
Command2=ID_FILE_OPEN
Command3=ID_FILE_PRINT_SETUP
Command4=ID_FILE_MRU_FILE1
Command5=ID_APP_EXIT
Command6=ID_VIEW_TOOLBAR
Command7=ID_VIEW_STATUS_BAR
Command8=ID_APP_ABOUT
CommandCount=8

[ACL:IDR_MAINFRAME]
Type=1
Class=?
Command1=ID_FILE_NEW
Command2=ID_FILE_OPEN
Command3=ID_FILE_SAVE
Command4=ID_FILE_PRINT
Command5=ID_EDIT_UNDO
Command6=ID_EDIT_CUT
Command7=ID_EDIT_COPY
Command8=ID_EDIT_PASTE
Command9=ID_EDIT_UNDO
Command10=ID_EDIT_CUT
Command11=ID_EDIT_COPY
Command12=ID_EDIT_PASTE
Command13=ID_NEXT_PANE
Command14=ID_PREV_PANE
CommandCount=14

[CLS:CMyLogViewDlg]
Type=0
HeaderFile=MyLogViewDlg.h
ImplementationFile=MyLogViewDlg.cpp
BaseClass=CDialog
Filter=D
LastObject=CMyLogViewDlg

[DLG:IDD_LOGVIEW_BAR (English (U.S.))]
Type=1
Class=?
ControlCount=1
Control1=IDC_LOGVIEW_EDIT,edit,1352728708

