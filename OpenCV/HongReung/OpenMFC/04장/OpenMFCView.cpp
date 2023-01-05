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

		// 창 크기에 맞춰 준다.
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
	
	int iReturn = AfxMessageBox("저장 하시겠습니까?", 
					MB_YESNO | MB_ICONQUESTION );

	if( iReturn == IDYES )
	{
		// 새로 만들어진 경우 '다른 파일 이름으로 저장' 함수 호출
		if( !pDoc->m_szPathName || pDoc->m_szPathName[0] == '\0' ) 
		{
			OnFileSaveAs();
		}
		// 기존 파일인 경우 
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

	// 대화상자에 출력될 파일들을 확장자에 의해서 선별되도록 지정한 필터
	//
	char szFilter[] = "JPEG file(*.jpeg, *.jpg, *.jpe) | *.jpg; *.jpeg; *.jpe |\
Portable Network Graphics file(*.png) | *.png |\
Windows bitmap files(*.bmp, *.dib) | *.bmp; *.dib |\
Sun rasters(*.sr, *.ras) | *.sr; *.ras |\
TIFF files(*.tiff, *.tif) | *.tiff; *.tif |\
지원하는 모든 영상 파일|*.jpeg; *.jpg; *.jpe; *.png; *.bmp; *.dib; *.sr; *.ras; *.tiff; *.tif ||";	

	// 파일명이 없을 경우 창 제목으로 설정한다.
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
		// 다른 이름으로 저장할 파일 경로명을 가져온다.
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

	// 클립보드에 복사하기
	pDoc->CopyClipBoard( pDoc->m_cvvImage.GetImage() );
}


BOOL COpenMFCView::OnEraseBkgnd(CDC* pDC) 
{
	// TODO: Add your message handler code here and/or call default
	
	//return CScrollView::OnEraseBkgnd(pDC);

	// 창 크기 조절시 배경이 깜박이지 않게 한다.
	// 실제로 배경 깜빡임이 심한 경우에는 이 방법을 실제로 많이 쓴다.
	return TRUE;
}
