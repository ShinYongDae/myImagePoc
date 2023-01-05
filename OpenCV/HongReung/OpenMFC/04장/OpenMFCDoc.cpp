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

	// ���� �б�
	m_cvvImage.Load( lpszPathName );

	// ���� ��θ� �ʱ�ȭ �� ���� 
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

	// Ŭ������ ����
	if(::OpenClipboard(AfxGetMainWnd()->GetSafeHwnd()))
	{
		// Ŭ������ �ʱ�ȭ
		if(::EmptyClipboard()) 
		{
			// Ŭ�����忡 ����
			if(::SetClipboardData(CF_DIB, hDIB) == NULL ) 
			{
				// ���� ���� �߻���
				AfxMessageBox( "Ŭ������ ����Ÿ�� �����ϴ� ���� ������ �߻��߽��ϴ�!" );
			}
		}

	}

	// Ŭ������ �ݱ�
	::CloseClipboard();
}

HANDLE COpenMFCDoc::CopyToHandle(IplImage *image)
{
	int height = image->height;
	int width = image->width;
	int nChannels = image->nChannels;
	int bpp = 8*nChannels;

	// STEP 1 : BMP ����Ÿ�� ���Ϸ� ���� �Ǿ� �����Ƿ� �����ش�.
	//---------------------------------------------------------
	IplImage *flip_image = cvCloneImage( image );
	cvFlip( image, flip_image, 0 );

	// ���� ����Ÿ�� ������ ���� ũ��(��, ������ ���̰� 4�� ����� �Ǿ�� ��)
	int bmpDataSize = flip_image->imageSize;

	// BMP ���� ���� : 1 ~ 4 ���� ������.
	// (1) BITMAPFILEHEADER ( ��Ʈ�� ���Ͽ� ���� ���� )
	// (2) BITMAPINFOHEADER ( ��Ʈ�� ��ü�� ���� ���� ) 
	// (3) RGBQUAD (�ȷ�Ʈ) : 8bit�� ó��
	// (4) ��Ʈ�� ���� 
	
	// STEP 2 : ��Ʈ�� ��ü�� ���� ���� ��, ��Ʈ�� ��� ���� 
	BITMAPINFOHEADER bmpHeader;
	bmpHeader.biSize = sizeof(BITMAPINFOHEADER); // �� ����ü�� ũ��
	bmpHeader.biHeight = height; // ������ ����
	bmpHeader.biWidth = width; // ������ �ʺ�
	bmpHeader.biPlanes = 1; // ��Ʈ �÷��� �� (�׻� 1��)
	bmpHeader.biBitCount = bpp; // �� ȭ�Ҵ� ��Ʈ ���� 
	bmpHeader.biCompression = BI_RGB; // BI_RGB : �������� ����
	bmpHeader.biSizeImage = bmpDataSize; // ������ ũ��
	if( bpp == 8 )
	{
		bmpHeader.biClrUsed = 256; // ���� ���Ǵ� ����
		bmpHeader.biClrImportant = 256;  // �߿��� ���� ����
	}
	else if( bpp == 24 )
	{
		bmpHeader.biClrUsed = 0; // ���� ���Ǵ� ����
		bmpHeader.biClrImportant = 0;  // �߿��� ���� ����
	}

	// STEP 4 : Ŭ������ ���� ��ƾ ���� ����
	int bmpAllSize = sizeof(BITMAPINFOHEADER) \
					+ sizeof(RGBQUAD)*256 \
					+ bmpDataSize*sizeof(char);

	// STEP 4-1 : �޸� �Ҵ�
	HGLOBAL hDIB = (HGLOBAL)::GlobalAlloc(GMEM_MOVEABLE| GMEM_ZEROINIT,
										  bmpAllSize );
	if( hDIB == NULL ) return NULL;

	// STEP 4-2 : �޸� ���� ����
	LPSTR pDIB = (LPSTR)::GlobalLock((HGLOBAL)hDIB);

	// STEP 4-3 : ��Ʈ�� ��� ���� ���� 
	memcpy( pDIB, &bmpHeader, sizeof(BITMAPINFOHEADER) );

	// STEP 4-4 : ���� ������ ����  
	if( bpp == 8 )
	{
		// �ȷ�Ʈ �ʱ�ȭ 
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

	// STEP 4-5 : ������ �޸� ������ Ǭ��.
	::GlobalUnlock((HGLOBAL)hDIB);

	// STEP 5 : �޸� ���� 
	cvReleaseImage( &flip_image );

	return hDIB;
}

void COpenMFCDoc::InsertLogWindow(CString msg)
{
	CMainFrame *pFrame = (CMainFrame *)AfxGetMainWnd();

	// �α� ���̾�α� �ٸ� �����ش�.
	pFrame->m_logViewBar.ShowWindow( SW_SHOW );
	pFrame->DockControlBar(&pFrame->m_logViewBar);

	// ��ġ ����
	RECT rect;
	pFrame->GetWindowRect(&rect);
	pFrame->FloatControlBar( &pFrame->m_logViewBar, 
							CPoint(rect.right-350, rect.bottom-220));

	// IDC_LOGVIEW_EDIT�� �����͸� ��´�.
	CEdit *pEdit = (CEdit *)pFrame->m_logViewBar.GetDlgItem( IDC_LOGVIEW_EDIT );

	// �ٹٲ� ����
	pEdit->SetSel(-1, -1);
	pEdit->ReplaceSel( msg + "\r\n");
	pEdit->LineScroll( pEdit->GetLineCount() );
	pFrame->RecalcLayout();
}

void COpenMFCDoc::InsertLogFile(CString msg)
{
	// ���� ��ο� �ִ� ���� ���ϸ��� ���� �´�.
	char pszFilePathName[_MAX_PATH]; 
	GetModuleFileName( NULL, pszFilePathName, _MAX_PATH); 

	// �α� ���ϸ��� �����.
	CString szFilePathName;
	szFilePathName.Format("%s", pszFilePathName );
	CString szPathName = szFilePathName.Left( szFilePathName.ReverseFind('.') );
	CString logFileName = szPathName + ".log";
 
	// TRY ~ CATCH ~ END_CATCH : ���� ���� ó�� 
	TRY
	{
		CFile file;

		// ������ ã�´�.
		CFileFind finder;
		int isExists = finder.FindFile( logFileName );
		
		// ������ �������� ������ ���� �����Ѵ�.
		if( !isExists ) 
		{
			file.Open( _T(logFileName), CFile::modeCreate | \
										CFile::modeWrite | \
										CFile::modeNoTruncate | \
										CFile::shareDenyNone );   
		}
		// ������ �����ϸ� �޺κп� �߰��Ѵ�.
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

