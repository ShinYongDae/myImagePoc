// OpenMFCDoc.cpp : implementation of the COpenMFCDoc class
//

#include "stdafx.h"
#include "OpenMFC.h"

#include "OpenMFCDoc.h"

#ifdef _DEBUG
#define new DEBUG_NEW
#undef THIS_FILE
static char THIS_FILE[] = __FILE__;
#endif

#include "MainFrm.h"

/////////////////////////////////////////////////////////////////////////////
// COpenMFCDoc

IMPLEMENT_DYNCREATE(COpenMFCDoc, CDocument)

BEGIN_MESSAGE_MAP(COpenMFCDoc, CDocument)
	//{{AFX_MSG_MAP(COpenMFCDoc)
		// NOTE - the ClassWizard will add and remove mapping macros here.
		//    DO NOT EDIT what you see in these blocks of generated code!
	//}}AFX_MSG_MAP
END_MESSAGE_MAP()

/////////////////////////////////////////////////////////////////////////////
// COpenMFCDoc construction/destruction

COpenMFCDoc::COpenMFCDoc()
{
	// TODO: add one-time construction code here
}

COpenMFCDoc::~COpenMFCDoc()
{
}

BOOL COpenMFCDoc::OnNewDocument()
{
	if (!CDocument::OnNewDocument())
		return FALSE;

	// TODO: add reinitialization code here
	// (SDI documents will reuse this document)

	return TRUE;
}



/////////////////////////////////////////////////////////////////////////////
// COpenMFCDoc serialization

void COpenMFCDoc::Serialize(CArchive& ar)
{
	if (ar.IsStoring())
	{
		// TODO: add storing code here
	}
	else
	{
		// TODO: add loading code here
	}
}

/////////////////////////////////////////////////////////////////////////////
// COpenMFCDoc diagnostics

#ifdef _DEBUG
void COpenMFCDoc::AssertValid() const
{
	CDocument::AssertValid();
}

void COpenMFCDoc::Dump(CDumpContext& dc) const
{
	CDocument::Dump(dc);
}
#endif //_DEBUG

/////////////////////////////////////////////////////////////////////////////
// COpenMFCDoc commands

BOOL COpenMFCDoc::OnOpenDocument(LPCTSTR lpszPathName) 
{
	if (!CDocument::OnOpenDocument(lpszPathName))
		return FALSE;
	
	// TODO: Add your specialized creation code here

	// 영상 읽기
	m_cvvImage.Load( lpszPathName );

	// 파일 경로명 초기화 및 복사 
	m_szPathName = (char *)calloc(512, sizeof(char));
	strcpy( m_szPathName, (char *)lpszPathName );

	return TRUE;
}

void COpenMFCDoc::DeleteContents() 
{
	// TODO: Add your specialized code here and/or call the base class
	if( m_cvvImage.GetImage() != NULL )
	{
		m_cvvImage.~CvvImage();
	}

	CDocument::DeleteContents();
}

BOOL COpenMFCDoc::OnSaveDocument(LPCTSTR lpszPathName) 
{
	// TODO: Add your specialized code here and/or call the base class

	return m_cvvImage.Save( lpszPathName );
}

void COpenMFCDoc::CopyClipBoard(IplImage *m_pCopyImage)
{
	HANDLE hDIB = (HANDLE)CopyToHandle( m_pCopyImage );
	if( hDIB == NULL ) return;

	// 클립보드 열기
	if(::OpenClipboard(AfxGetMainWnd()->GetSafeHwnd()))
	{
		// 클립보드 초기화
		if(::EmptyClipboard()) 
		{
			// 클립보드에 전송
			if(::SetClipboardData(CF_DIB, hDIB) == NULL ) 
			{
				// 전송 오류 발생시
				AfxMessageBox( "클립보드 데이타를 전송하는 동안 오류가 발생했습니다!" );
			}
		}

	}

	// 클립보드 닫기
	::CloseClipboard();
}

HANDLE COpenMFCDoc::CopyToHandle(IplImage *image)
{
	int height = image->height;
	int width = image->width;
	int nChannels = image->nChannels;
	int bpp = 8*nChannels;

	// STEP 1 : BMP 데이타는 상하로 반전 되어 있으므로 맞춰준다.
	//---------------------------------------------------------
	IplImage *flip_image = cvCloneImage( image );
	cvFlip( image, flip_image, 0 );

	// 영상 데이타를 저장할 실제 크기(단, 가로의 길이가 4의 배수가 되어야 함)
	int bmpDataSize = flip_image->imageSize;

	// BMP 포맷 형식 : 1 ~ 4 순의 조합임.
	// (1) BITMAPFILEHEADER ( 비트맵 파일에 대한 정보 )
	// (2) BITMAPINFOHEADER ( 비트맵 자체에 대한 정보 ) 
	// (3) RGBQUAD (팔레트) : 8bit만 처리
	// (4) 비트맵 구성 
	
	// STEP 2 : 비트맵 자체에 대한 정보 즉, 비트맵 헤더 구성 
	BITMAPINFOHEADER bmpHeader;
	bmpHeader.biSize = sizeof(BITMAPINFOHEADER); // 이 구조체의 크기
	bmpHeader.biHeight = height; // 영상의 높이
	bmpHeader.biWidth = width; // 영상의 너비
	bmpHeader.biPlanes = 1; // 비트 플레인 수 (항상 1임)
	bmpHeader.biBitCount = bpp; // 한 화소당 비트 개수 
	bmpHeader.biCompression = BI_RGB; // BI_RGB : 압축하지 않음
	bmpHeader.biSizeImage = bmpDataSize; // 영상의 크기
	if( bpp == 8 )
	{
		bmpHeader.biClrUsed = 256; // 실제 사용되는 개수
		bmpHeader.biClrImportant = 256;  // 중요한 색생 개수
	}
	else if( bpp == 24 )
	{
		bmpHeader.biClrUsed = 0; // 실제 사용되는 개수
		bmpHeader.biClrImportant = 0;  // 중요한 색생 개수
	}

	// STEP 4 : 클립보드 복사 루틴 구현 시작
	int bmpAllSize = sizeof(BITMAPINFOHEADER) \
					+ sizeof(RGBQUAD)*256 \
					+ bmpDataSize*sizeof(char);

	// STEP 4-1 : 메모리 할당
	HGLOBAL hDIB = (HGLOBAL)::GlobalAlloc(GMEM_MOVEABLE| GMEM_ZEROINIT,
										  bmpAllSize );
	if( hDIB == NULL ) return NULL;

	// STEP 4-2 : 메모리 영역 고정
	LPSTR pDIB = (LPSTR)::GlobalLock((HGLOBAL)hDIB);

	// STEP 4-3 : 비트맵 헤더 정보 복사 
	memcpy( pDIB, &bmpHeader, sizeof(BITMAPINFOHEADER) );

	// STEP 4-4 : 영상 데이터 복사  
	if( bpp == 8 )
	{
		// 팔레트 초기화 
		RGBQUAD palette[256];
		memcpy( pDIB+sizeof(BITMAPINFOHEADER), palette, sizeof(RGBQUAD)*256 );
		memcpy( pDIB+sizeof(BITMAPINFOHEADER)+sizeof(RGBQUAD)*256, 
			    flip_image->imageData, bmpDataSize );
	} 
	else if( bpp == 24 ) 
	{
		memcpy( pDIB+sizeof(BITMAPINFOHEADER), 
			    flip_image->imageData, bmpDataSize );
	}

	// STEP 4-5 : 고정된 메모리 영역을 푼다.
	::GlobalUnlock((HGLOBAL)hDIB);

	// STEP 5 : 메모리 해제 
	cvReleaseImage( &flip_image );

	return hDIB;
}

void COpenMFCDoc::InsertLogWindow(CString msg)
{
	CMainFrame *pFrame = (CMainFrame *)AfxGetMainWnd();

	// 로그 다이얼로그 바를 보여준다.
	pFrame->m_logViewBar.ShowWindow( SW_SHOW );
	pFrame->DockControlBar(&pFrame->m_logViewBar);

	// 위치 조절
	RECT rect;
	pFrame->GetWindowRect(&rect);
	pFrame->FloatControlBar( &pFrame->m_logViewBar, 
							CPoint(rect.right-350, rect.bottom-220));

	// IDC_LOGVIEW_EDIT의 포인터를 얻는다.
	CEdit *pEdit = (CEdit *)pFrame->m_logViewBar.GetDlgItem( IDC_LOGVIEW_EDIT );

	// 줄바꿈 지원
	pEdit->SetSel(-1, -1);
	pEdit->ReplaceSel( msg + "\r\n");
	pEdit->LineScroll( pEdit->GetLineCount() );
	pFrame->RecalcLayout();
}

void COpenMFCDoc::InsertLogFile(CString msg)
{
	// 현재 경로에 있는 실행 파일명을 갖고 온다.
	char pszFilePathName[_MAX_PATH]; 
	GetModuleFileName( NULL, pszFilePathName, _MAX_PATH); 

	// 로그 파일명을 만든다.
	CString szFilePathName;
	szFilePathName.Format("%s", pszFilePathName );
	CString szPathName = szFilePathName.Left( szFilePathName.ReverseFind('.') );
	CString logFileName = szPathName + ".log";
 
	// TRY ~ CATCH ~ END_CATCH : 파일 에러 처리 
	TRY
	{
		CFile file;

		// 파일을 찾는다.
		CFileFind finder;
		int isExists = finder.FindFile( logFileName );
		
		// 파일이 존재하지 않으면 새로 생성한다.
		if( !isExists ) 
		{
			file.Open( _T(logFileName), CFile::modeCreate | \
										CFile::modeWrite | \
										CFile::modeNoTruncate | \
										CFile::shareDenyNone );   
		}
		// 파일이 존재하면 뒷부분에 추가한다.
		else 
		{
			file.Open( _T(logFileName), CFile::modeWrite | \
										CFile::modeNoTruncate | \
										CFile::shareDenyNone );
			file.SeekToEnd();
		}

		msg += "\r\n";
		file.Write( msg, msg.GetLength() );
		file.Close();
	}
	CATCH( CFileException, e ) 
	{
		e->ReportError();
	}
	END_CATCH
}

