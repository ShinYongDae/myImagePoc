// OpenMFC.h : main header file for the OPENMFC application
//

#if !defined(AFX_OPENMFC_H__5624070F_B399_4DC4_9826_0979C309A475__INCLUDED_)
#define AFX_OPENMFC_H__5624070F_B399_4DC4_9826_0979C309A475__INCLUDED_

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000

#ifndef __AFXWIN_H__
	#error include 'stdafx.h' before including this file for PCH
#endif

#include "resource.h"       // main symbols

/////////////////////////////////////////////////////////////////////////////
// COpenMFCApp:
// See OpenMFC.cpp for the implementation of this class
//

class COpenMFCApp : public CWinApp
{
public:
	IplImage * CreateFromHandle( HANDLE hDIB );
	COpenMFCApp();

// Overrides
	// ClassWizard generated virtual function overrides
	//{{AFX_VIRTUAL(COpenMFCApp)
	public:
	virtual BOOL InitInstance();
	//}}AFX_VIRTUAL

// Implementation
	//{{AFX_MSG(COpenMFCApp)
	afx_msg void OnAppAbout();
	afx_msg void OnFileOpen();
	afx_msg void OnFileAllClose();
	afx_msg void OnEditPaste();
	afx_msg void OnUpdateEditPaste(CCmdUI* pCmdUI);
	//}}AFX_MSG
	DECLARE_MESSAGE_MAP()
};


/////////////////////////////////////////////////////////////////////////////

//{{AFX_INSERT_LOCATION}}
// Microsoft Visual C++ will insert additional declarations immediately before the previous line.

#endif // !defined(AFX_OPENMFC_H__5624070F_B399_4DC4_9826_0979C309A475__INCLUDED_)
