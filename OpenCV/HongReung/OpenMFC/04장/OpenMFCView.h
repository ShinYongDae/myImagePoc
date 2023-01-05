// OpenMFCView.h : interface of the COpenMFCView class
//
/////////////////////////////////////////////////////////////////////////////

#if !defined(AFX_OPENMFCVIEW_H__6C7685BB_F1F9_40F9_98F3_E082ED00F525__INCLUDED_)
#define AFX_OPENMFCVIEW_H__6C7685BB_F1F9_40F9_98F3_E082ED00F525__INCLUDED_

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000


class COpenMFCView : public CScrollView
{
protected: // create from serialization only
	COpenMFCView();
	DECLARE_DYNCREATE(COpenMFCView)

// Attributes
public:
	COpenMFCDoc* GetDocument();

// Operations
public:

// Overrides
	// ClassWizard generated virtual function overrides
	//{{AFX_VIRTUAL(COpenMFCView)
	public:
	virtual void OnDraw(CDC* pDC);  // overridden to draw this view
	virtual BOOL PreCreateWindow(CREATESTRUCT& cs);
	protected:
	virtual void OnInitialUpdate(); // called first time after construct
	virtual BOOL OnPreparePrinting(CPrintInfo* pInfo);
	virtual void OnBeginPrinting(CDC* pDC, CPrintInfo* pInfo);
	virtual void OnEndPrinting(CDC* pDC, CPrintInfo* pInfo);
	//}}AFX_VIRTUAL

// Implementation
public:
	virtual ~COpenMFCView();
#ifdef _DEBUG
	virtual void AssertValid() const;
	virtual void Dump(CDumpContext& dc) const;
#endif

protected:

// Generated message map functions
protected:
	//{{AFX_MSG(COpenMFCView)
	afx_msg void OnFileSave();
	afx_msg void OnFileSaveAs();
	afx_msg void OnEditCopy();
	afx_msg BOOL OnEraseBkgnd(CDC* pDC);
	//}}AFX_MSG
	DECLARE_MESSAGE_MAP()
};

#ifndef _DEBUG  // debug version in OpenMFCView.cpp
inline COpenMFCDoc* COpenMFCView::GetDocument()
   { return (COpenMFCDoc*)m_pDocument; }
#endif

/////////////////////////////////////////////////////////////////////////////

//{{AFX_INSERT_LOCATION}}
// Microsoft Visual C++ will insert additional declarations immediately before the previous line.

#endif // !defined(AFX_OPENMFCVIEW_H__6C7685BB_F1F9_40F9_98F3_E082ED00F525__INCLUDED_)
