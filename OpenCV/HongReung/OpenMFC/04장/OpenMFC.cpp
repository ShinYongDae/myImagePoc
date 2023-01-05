// OpenMFC.cpp : Defines the class behaviors for the application.
//

#include "stdafx.h"
#include "OpenMFC.h"

#include "MainFrm.h"
#include "ChildFrm.h"
#include "OpenMFCDoc.h"
#include "OpenMFCView.h"

#ifdef _DEBUG
#define new DEBUG_NEW
#undef THIS_FILE
static char THIS_FILE[] = __FILE__;
#endif

/////////////////////////////////////////////////////////////////////////////
// COpenMFCApp

BEGIN_MESSAGE_MAP(COpenMFCApp, CWinApp)
	//{{AFX_MSG_MAP(COpenMFCApp)
	ON_COMMAND(ID_APP_ABOUT, OnAppAbout)
	ON_COMMAND(ID_FILE_OPEN, OnFileOpen)
	ON_COMMAND(ID_FILE_ALL_CLOSE, OnFileAllClose)
	ON_COMMAND(ID_EDIT_PASTE, OnEditPaste)
	ON_UPDATE_COMMAND_UI(ID_EDIT_PASTE, OnUpdateEditPaste)
	//}}AFX_MSG_MAP
	// Standard file based document commands
	ON_COMMAND(ID_FILE_NEW, CWinApp::OnFileNew)
	// ON_COMMAND(ID_FILE_OPEN, CWinApp::OnFileOpen)
	// Standard print setup command
	ON_COMMAND(ID_FILE_PRINT_SETUP, CWinApp::OnFilePrintSetup)
END_MESSAGE_MAP()

/////////////////////////////////////////////////////////////////////////////
// COpenMFCApp construction

COpenMFCApp::COpenMFCApp()
{
	// TODO: add construction code here,
	// Place all significant initialization in InitInstance
}

/////////////////////////////////////////////////////////////////////////////
// The one and only COpenMFCApp object

COpenMFCApp theApp;

/////////////////////////////////////////////////////////////////////////////
// COpenMFCApp initialization

BOOL COpenMFCApp::InitInstance()
{
	AfxEnableControlContainer();

	// Standard initialization
	// If you are not using these features and wish to reduce the size
	//  of your final executable, you should remove from the following
	//  the specific initialization routines you do not need.

#ifdef _AFXDLL
	Enable3dControls();			// Call this when using MFC in a shared DLL
#else
	Enable3dControlsStatic();	// Call this when linking to MFC statically
#endif

	// Change the registry key under which our settings are stored.
	// TODO: You should modify this string to be something appropriate
	// such as the name of your company or organization.
	SetRegistryKey(_T("Local AppWizard-Generated Applications"));

	LoadStdProfileSettings();  // Load standard INI file options (including MRU)

	// Register the application's document templates.  Document templates
	//  serve as the connection between documents, frame windows and views.

	CMultiDocTemplate* pDocTemplate;
	pDocTemplate = new CMultiDocTemplate(
		IDR_OPENMFTYPE,
		RUNTIME_CLASS(COpenMFCDoc),
		RUNTIME_CLASS(CChildFrame), // custom MDI child frame
		RUNTIME_CLASS(COpenMFCView));
	AddDocTemplate(pDocTemplate);

	// create main MDI Frame window
	CMainFrame* pMainFrame = new CMainFrame;
	if (!pMainFrame->LoadFrame(IDR_MAINFRAME))
		return FALSE;
	m_pMainWnd = pMainFrame;

	// Parse command line for standard shell commands, DDE, file open
	CCommandLineInfo cmdInfo;
	ParseCommandLine(cmdInfo);

	// ���۽� ��Ÿ���� â�� �������� �ʱ�
	if( cmdInfo.m_nShellCommand == CCommandLineInfo::FileNew )
	{
		cmdInfo.m_nShellCommand = CCommandLineInfo::FileNothing;
	}

	// Dispatch commands specified on the command line
	if (!ProcessShellCommand(cmdInfo))
		return FALSE;

	// �巡�� �� ������� ���� ���� ����
	pMainFrame->DragAcceptFiles();

	// The main window has been initialized, so show and update it.
	pMainFrame->ShowWindow(m_nCmdShow);
	pMainFrame->UpdateWindow();

	return TRUE;
}


/////////////////////////////////////////////////////////////////////////////
// CAboutDlg dialog used for App About

class CAboutDlg : public CDialog
{
public:
	CAboutDlg();

// Dialog Data
	//{{AFX_DATA(CAboutDlg)
	enum { IDD = IDD_ABOUTBOX };
	//}}AFX_DATA

	// ClassWizard generated virtual function overrides
	//{{AFX_VIRTUAL(CAboutDlg)
	protected:
	virtual void DoDataExchange(CDataExchange* pDX);    // DDX/DDV support
	//}}AFX_VIRTUAL

// Implementation
protected:
	//{{AFX_MSG(CAboutDlg)
		// No message handlers
	//}}AFX_MSG
	DECLARE_MESSAGE_MAP()
};

CAboutDlg::CAboutDlg() : CDialog(CAboutDlg::IDD)
{
	//{{AFX_DATA_INIT(CAboutDlg)
	//}}AFX_DATA_INIT
}

void CAboutDlg::DoDataExchange(CDataExchange* pDX)
{
	CDialog::DoDataExchange(pDX);
	//{{AFX_DATA_MAP(CAboutDlg)
	//}}AFX_DATA_MAP
}

BEGIN_MESSAGE_MAP(CAboutDlg, CDialog)
	//{{AFX_MSG_MAP(CAboutDlg)
		// No message handlers
	//}}AFX_MSG_MAP
END_MESSAGE_MAP()

// App command to run the dialog
void COpenMFCApp::OnAppAbout()
{
	CAboutDlg aboutDlg;
	aboutDlg.DoModal();
}

/////////////////////////////////////////////////////////////////////////////
// COpenMFCApp message handlers


void COpenMFCApp::OnFileOpen() 
{
	// TODO: Add your command handler code here

	// ����
	int64 tStart = cvGetTickCount();


	// ��ȭ���ڿ� ��µ� ���ϵ��� Ȯ���ڿ� ���ؼ� �����ǵ��� ������ ����
	//
	// ** OpenCV�� �����ϴ� ���� ����
	//
	// (1) Windows bitmaps - BMP, DIB; 
	// (2) JPEG files - JPEG, JPG, JPE; 
	// (3) Portable Network Graphics - PNG; 
	// (4) Portable image format - PBM, PGM, PPM; 
	// (5) Sun rasters - SR, RAS; 
	// (6) TIFF files - TIFF, TIF. 
	//
	char szFilter[] = "JPEG file(*.jpeg, *.jpg, *.jpe) | *.jpeg; *.jpg; *.jpe |\
Portable Network Graphics file(*.png) | *.png |\
Windows bitmap files(*.bmp, *.dib) | *.bmp; *.dib |\
Sun rasters(*.sr, *.ras) | *.sr; *.ras |\
TIFF files(*.tiff, *.tif) | *.tiff; *.tif |\
�����ϴ� ��� ���� ����|*.jpeg; *.jpg; *.jpe; *.png; *.bmp; *.dib; *.sr; *.ras; *.tiff; *.tif ||";


	// FileDialog Ŭ������ �ν��Ͻ� ����
	// ���� ��ȭ���� �Ű� ������ �����Ѵ�.
	// OFN_EXPLORER|OFN_HIDEREADONLY 
	// ?> ������ Ž���� ��Ÿ�� & �б� ���� ������ ������� �ʴ´�.
	CFileDialog fileDlg(TRUE, 
			  NULL, 
			  NULL, 
			  OFN_HIDEREADONLY | OFN_ALLOWMULTISELECT, 
			  szFilter
			  );

	int iReturn = fileDlg.DoModal(); 

	// [����] ��ư�� ������ ��
	if( iReturn == IDOK )
	{
		POSITION pos = fileDlg.GetStartPosition();

		// ������ ������ ���� ��θ� ��������, ���ʴ�� ����
		while( pos ) 
		{
			OpenDocumentFile( fileDlg.GetNextPathName(pos) );
		}
	}

	// 
	int64 tEnd = cvGetTickCount();

	// ���� �ð��� ��´�.
	CString msg = _T("");
	msg.Format("Loading time : %5.3f ms", 0.001*(tEnd - tStart) / cvGetTickFrequency() );
	
	// ���� �ð� ������ �α� â�� ������.
	COpenMFCDoc *pDoc = (COpenMFCDoc*)((CMainFrame*)AfxGetMainWnd())->GetActiveDocument();
	pDoc->InsertLogWindow( msg );
}

void COpenMFCApp::OnFileAllClose() 
{
	// TODO: Add your command handler code here
	POSITION pos;
	CDocTemplate* pTemplate;

	// �����ִ� ��� ��ť��Ʈ ���ø��� �˾Ƴ� ��, 
	// CloseAllDocuments �Լ� ȣ���Ѵ�.
	pos = GetFirstDocTemplatePosition();
	while( pos != NULL )
	{
		pTemplate = GetNextDocTemplate(pos);
		pTemplate->CloseAllDocuments(FALSE);
	}	
}

void COpenMFCApp::OnEditPaste() 
{
	POSITION pos = GetFirstDocTemplatePosition();
	CDocTemplate *pTemplate = GetNextDocTemplate(pos);
	COpenMFCDoc *pDoc
		= (COpenMFCDoc* )pTemplate->OpenDocumentFile(NULL); 

	if( pDoc )	
	{
		HANDLE hDIB = NULL;

		// Ŭ�����忡�� ������ ��������
		if (::OpenClipboard(AfxGetMainWnd()->GetSafeHwnd())) 
			hDIB = ::GetClipboardData(CF_DIB);

		if( hDIB )
		{
			// Ŭ�����忡 �ִ� �����ͷκ��� IplImage ���� 
			IplImage *image = CreateFromHandle( hDIB );
		
			// m_cvvImage�� image�� �����Ѵ�.
			pDoc->m_cvvImage.CopyOf( image, image->nChannels*8 );
			pDoc->m_szPathName = (char *)calloc(512, sizeof(char));

			POSITION pos = pDoc->GetFirstViewPosition();
			COpenMFCView *pView
				= (COpenMFCView *)pDoc->GetNextView(pos);

			CSize sizeTotal = CSize(pDoc->m_cvvImage.Width(),
						pDoc->m_cvvImage.Height());

			pView->SetScrollSizes(MM_TEXT, sizeTotal);
			pView->ResizeParentToFit(FALSE);
		 }

		// Ŭ������ �ݱ�
		::CloseClipboard();
	}
}

IplImage * COpenMFCApp::CreateFromHandle(HANDLE hDIB)
{
	// STEP 1 : �޸� ���� ����
	LPSTR pDIB = (LPSTR)::GlobalLock((HGLOBAL)hDIB);  
	
	// STEP 2 : ��Ʈ�� ��� ������ �����´�.  
	BITMAPINFOHEADER bmpHeader; 
	memcpy( &bmpHeader, pDIB, sizeof(BITMAPINFOHEADER) );  
	
	int height = bmpHeader.biHeight;
	int width = bmpHeader.biWidth;
	int nChannels = bmpHeader.biBitCount/8;
	int bmpDataSize = bmpHeader.biSizeImage;

	// STEP 3 : ���� ���� ����Ÿ�� �����´�.
	char *imageData = (char *)calloc( bmpDataSize, sizeof(char) );

	if( bmpHeader.biBitCount == 8 )
	{
		memcpy( imageData, pDIB+sizeof(BITMAPINFOHEADER)+sizeof(RGBQUAD)*256, 
			    bmpDataSize );
	}
	else if( bmpHeader.biBitCount == 24 )
	{
		memcpy( imageData, pDIB+sizeof(BITMAPINFOHEADER), bmpDataSize );
	}

	// STEP 4 : ���� ���� ����Ÿ�� �����Ѵ�.
	IplImage *flip_image = cvCreateImage(cvSize(width,height), 
									IPL_DEPTH_8U, 
									nChannels);
	memcpy( flip_image->imageData, imageData, bmpDataSize );

	// STEP 5 : ���Ϸ� ������ ������ �ٽ� �����Ѵ�.
	IplImage *recover_image = cvCloneImage( flip_image );
	cvFlip( flip_image, recover_image, 0 );

	// STEP 6 : ������ �޸� ������ Ǭ��. 
	::GlobalUnlock((HGLOBAL)hDIB);  
	
	// STEP 7 : �޸� ���� 
	free(imageData);
	cvReleaseImage( &flip_image );

	return recover_image;
}

void COpenMFCApp::OnUpdateEditPaste(CCmdUI* pCmdUI) 
{
	if( !IsClipboardFormatAvailable(CF_DIB) )
		pCmdUI->Enable( FALSE );
	
}
