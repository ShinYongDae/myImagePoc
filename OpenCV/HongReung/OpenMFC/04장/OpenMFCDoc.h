// OpenMFCDoc.h : interface of the COpenMFCDoc class
//
/////////////////////////////////////////////////////////////////////////////

#if !defined(AFX_OPENMFCDOC_H__4BE5D6C0_ACEF_4390_A179_8B8C0AAFBCC9__INCLUDED_)
#define AFX_OPENMFCDOC_H__4BE5D6C0_ACEF_4390_A179_8B8C0AAFBCC9__INCLUDED_

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000


class COpenMFCDoc : public CDocument
{
protected: // create from serialization only
	COpenMFCDoc();
	DECLARE_DYNCREATE(COpenMFCDoc)

// Attributes
public:

// Operations
public:

// Overrides
	// ClassWizard generated virtual function overrides
	//{{AFX_VIRTUAL(COpenMFCDoc)
	public:
	virtual BOOL OnNewDocument();
	virtual void Serialize(CArchive& ar);
	virtual BOOL OnOpenDocument(LPCTSTR lpszPathName);
	virtual void DeleteContents();
	virtual BOOL OnSaveDocument(LPCTSTR lpszPathName);
	//}}AFX_VIRTUAL

// Implementation
public:
	void InsertLogWindow( CString msg );
	void InsertLogFile( CString msg );
	HANDLE CopyToHandle( IplImage *image );
	void CopyClipBoard( IplImage *m_pCopyImage );
	CvvImage m_cvvImage;
	char *m_szPathName;
	virtual ~COpenMFCDoc();
#ifdef _DEBUG
	virtual void AssertValid() const;
	virtual void Dump(CDumpContext& dc) const;
#endif

protected:

// Generated message map functions
protected:
	//{{AFX_MSG(COpenMFCDoc)
		// NOTE - the ClassWizard will add and remove member functions here.
		//    DO NOT EDIT what you see in these blocks of generated code !
	//}}AFX_MSG
	DECLARE_MESSAGE_MAP()
};

/////////////////////////////////////////////////////////////////////////////

//{{AFX_INSERT_LOCATION}}
// Microsoft Visual C++ will insert additional declarations immediately before the previous line.

#endif // !defined(AFX_OPENMFCDOC_H__4BE5D6C0_ACEF_4390_A179_8B8C0AAFBCC9__INCLUDED_)
