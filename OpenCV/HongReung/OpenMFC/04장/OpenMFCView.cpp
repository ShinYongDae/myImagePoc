// OpenMFCView.cpp : implementation of the COpenMFCView class
//

#include "stdafx.h"
#include "OpenMFC.h"

#include "OpenMFCDoc.h"
#include "OpenMFCView.h"

#ifdef _DEBUG
#define new DEBUG_NEW
#undef THIS_FILE
static char THIS_FILE[] = __FILE__;
#endif

/////////////////////////////////////////////////////////////////////////////
// COpenMFCView

IMPLEMENT_DYNCREATE(COpenMFCView, CScrollView)

BEGIN_MESSAGE_MAP(COpenMFCView, CScrollView)
	//{{AFX_MSG_MAP(COpenMFCView)
	ON_COMMAND(ID_FILE_SAVE, OnFileSave)
	ON_COMMAND(ID_FILE_SAVE_AS, OnFileSaveAs)
	ON_COMMAND(ID_EDIT_COPY, OnEditCopy)
	ON_WM_ERASEBKGND()
	//}}AFX_MSG_MAP
	// Standard printing commands
	ON_COMMAND(ID_FILE_PRINT, CScrollView::OnFilePrint)
	ON_COMMAND(ID_FILE_PRINT_DIRECT, CScrollView::OnFilePrint)
	ON_COMMAND(ID_FILE_PRINT_PREVIEW, CScrollView::OnFilePrintPreview)
END_MESSAGE_MAP()

/////////////////////////////////////////////////////////////////////////////
// COpenMFCView construction/destruction

COpenMFCView::COpenMFCView()
{
	// TODO: add construction code here

}

COpenMFCView::~COpenMFCView()
{
}

BOOL COpenMFCView::PreCreateWindow(CREATESTRUCT& cs)
{
	// TODO: Modify the Window class or styles here by modifying
	//  the CREATESTRUCT cs

	return CScrollView::PreCreateWindow(cs);
}

/////////////////////////////////////////////////////////////////////////////
// COpenMFCView drawing

void COpenMFCView::OnDraw(CDC* pDC)
{
	COpenMFCDoc* pDoc = GetDocument();
	ASSERT_VALID(pDoc);
	
	// TODO: add draw code for native data here
	
	if( pDoc->m_cvvImage.GetImage() )
	{		
		int height = pDoc->m_cvvImage.Height();
		int width  = pDoc->m_cvvImage.Width();	

		CRect rect = CRect(0, 0, width, height);
		pDoc->m_cvvImage.DrawToHDC( pDC->GetSafeHdc(), &rect );

		// â ũ�⿡ ���� �ش�.
		ResizeParentToFit(FALSE);
	}
}

void COpenMFCView::OnInitialUpdate()
{
	COpenMFCDoc* pDoc = GetDocument();
	ASSERT_VALID(pDoc);

	CScrollView::OnInitialUpdate();

	CSize sizeTotal;

	if( pDoc->m_cvvImage.GetImage() ) 
	{
		int height = pDoc->m_cvvImage.Height();
		int width  = pDoc->m_cvvImage.Width();	
		sizeTotal = CSize(width, height);
	}
    else 
	{
		sizeTotal.cx = sizeTotal.cy = 100;
	}

	SetScrollSizes(MM_TEXT, sizeTotal);
	ResizeParentToFit(TRUE);
}

/////////////////////////////////////////////////////////////////////////////
// COpenMFCView printing

BOOL COpenMFCView::OnPreparePrinting(CPrintInfo* pInfo)
{
	// default preparation
	return DoPreparePrinting(pInfo);
}

void COpenMFCView::OnBeginPrinting(CDC* /*pDC*/, CPrintInfo* /*pInfo*/)
{
	// TODO: add extra initialization before printing
}

void COpenMFCView::OnEndPrinting(CDC* /*pDC*/, CPrintInfo* /*pInfo*/)
{
	// TODO: add cleanup after printing
}

/////////////////////////////////////////////////////////////////////////////
// COpenMFCView diagnostics

#ifdef _DEBUG
void COpenMFCView::AssertValid() const
{
	CScrollView::AssertValid();
}

void COpenMFCView::Dump(CDumpContext& dc) const
{
	CScrollView::Dump(dc);
}

COpenMFCDoc* COpenMFCView::GetDocument() // non-debug version is inline
{
	ASSERT(m_pDocument->IsKindOf(RUNTIME_CLASS(COpenMFCDoc)));
	return (COpenMFCDoc*)m_pDocument;
}
#endif //_DEBUG

/////////////////////////////////////////////////////////////////////////////
// COpenMFCView message handlers


void COpenMFCView::OnFileSave() 
{
	// TODO: Add your command handler code here
	COpenMFCDoc* pDoc = GetDocument();
	ASSERT_VALID(pDoc);
	
	int iReturn = AfxMessageBox("���� �Ͻðڽ��ϱ�?", 
					MB_YESNO | MB_ICONQUESTION );

	if( iReturn == IDYES )
	{
		// ���� ������� ��� '�ٸ� ���� �̸����� ����' �Լ� ȣ��
		if( !pDoc->m_szPathName || pDoc->m_szPathName[0] == '\0' ) 
		{
			OnFileSaveAs();
		}
		// ���� ������ ��� 
		else
		{
			pDoc->OnSaveDocument( pDoc->m_szPathName );
		}
	}
}

void COpenMFCView::OnFileSaveAs() 
{
	// TODO: Add your command handler code here
	COpenMFCDoc* pDoc = GetDocument();
	ASSERT_VALID(pDoc);

	// TODO: Add your command handler code here

	// ��ȭ���ڿ� ��µ� ���ϵ��� Ȯ���ڿ� ���ؼ� �����ǵ��� ������ ����
	//
	char szFilter[] = "JPEG file(*.jpeg, *.jpg, *.jpe) | *.jpg; *.jpeg; *.jpe |\
Portable Network Graphics file(*.png) | *.png |\
Windows bitmap files(*.bmp, *.dib) | *.bmp; *.dib |\
Sun rasters(*.sr, *.ras) | *.sr; *.ras |\
TIFF files(*.tiff, *.tif) | *.tiff; *.tif |\
�����ϴ� ��� ���� ����|*.jpeg; *.jpg; *.jpe; *.png; *.bmp; *.dib; *.sr; *.ras; *.tiff; *.tif ||";	

	// ���ϸ��� ���� ��� â �������� �����Ѵ�.
	if( !pDoc->m_szPathName || pDoc->m_szPathName[0] == '\0' )
		strcpy( pDoc->m_szPathName, pDoc->GetTitle() );

	CFileDialog fileDlg(FALSE, 
			  pDoc->m_szPathName, 
			  NULL, 
			  OFN_OVERWRITEPROMPT, 
			  szFilter
			  );

	int iReturn = fileDlg.DoModal();
	
	if( iReturn == IDOK )
	{
		// �ٸ� �̸����� ������ ���� ��θ��� �����´�.
		CString save_pathName = fileDlg.GetPathName(); 

		pDoc->OnSaveDocument( save_pathName );
	}
	else
	{
		strcpy( pDoc->m_szPathName, "" );
	}
}

void COpenMFCView::OnEditCopy() 
{
	// TODO: Add your command handler code here
	COpenMFCDoc* pDoc = GetDocument();
	ASSERT_VALID(pDoc);

	// Ŭ�����忡 �����ϱ�
	pDoc->CopyClipBoard( pDoc->m_cvvImage.GetImage() );
}


BOOL COpenMFCView::OnEraseBkgnd(CDC* pDC) 
{
	// TODO: Add your message handler code here and/or call default
	
	//return CScrollView::OnEraseBkgnd(pDC);

	// â ũ�� ������ ����� �������� �ʰ� �Ѵ�.
	// ������ ��� �������� ���� ��쿡�� �� ����� ������ ���� ����.
	return TRUE;
}
