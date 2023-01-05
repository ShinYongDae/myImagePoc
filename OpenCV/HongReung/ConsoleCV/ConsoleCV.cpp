// ConsoleCV.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "ConsoleCV.h"

// OpenCV ���� ������� 
#include <cv.h>
#include <cxcore.h>
#include <highgui.h>
#include <cvcam.h>

#ifdef _DEBUG
#define new DEBUG_NEW
#undef THIS_FILE
static char THIS_FILE[] = __FILE__;
#endif

/////////////////////////////////////////////////////////////////////////////
// The one and only application object

CWinApp theApp;

using namespace std;

void verifyVersion();
void imageViewer();
char *getFileDialog();
void allImageFuncUsage(); 
void directAccessPixel();
void funcAccessPixel();
void matrixUsage();
void testMatrixFunc();
void printMatrix(CvMat *matrix);
void testCvArr();
void testMouseEvent();
void mouseHandler(int event, int x, int y, int flags, void *param);
void testTrackBarEvent();
void trackbarHandler(int pos);
void testWriterCamera();
void testViewFromCamera();
char *getSaveAVIFromFileDialog();

// cvcam
void testViewFromCVCAM_1();
void testViewFromCVCAM_2();
void testViewFromCVCAM_3();
void testViewFromCVCAM_two();

int _tmain(int argc, TCHAR* argv[], TCHAR* envp[])
{
	int nRetCode = 0;

	// initialize MFC and print and error on failure
	if (!AfxWinInit(::GetModuleHandle(NULL), NULL, ::GetCommandLine(), 0))
	{
		// TODO: change error code to suit your needs
		cerr << _T("Fatal Error: MFC initialization failed") << endl;
		nRetCode = 1;
	}
	else
	{
		// OpenCV ���� Ȯ��
		// verifyVersion();

		// ���� ����
		// imageViewer();

		// ���� ����� ���� �Լ� ��� ����
		// allImageFuncUsage();

		// ���� ����
		// directAccessPixel();

		// GetReal2D(), SetReal2D() �Լ��� ���
		// funcAccessPixel();

		// ��� �Լ� ��
		// testMatrixFunc();

		// ��� ��� + ���͸�
		// matrixUsage();

		// cvAdd() �Լ��� ���ڰ� CvArr�̸�, lplImage, CvMat ���� ���� Ȯ��
		// testCvArr();

		// ���콺 �ڵ鷯
		// testMouseEvent();
	
		// Ʈ���� �ڵ鷯
		// testTrackBarEvent();

		// ī�޶󿡼� �Է� �޾Ƽ� �����ֱ�
		//testViewFromCamera();

		// ī�޶󿡼� �Է� ���� �������� AVI�� �����ϱ�
		//testWriterCamera();

		// cvcam �׽�Ʈ 1
		//testViewFromCVCAM_1();

		// cvcam �׽�Ʈ 2
		// testViewFromCVCAM_2();

		// cvcam �׽�Ʈ 3
		//testViewFromCVCAM_3();

		// ī�޶� 2�� �϶��� cvcam �׽�Ʈ
		//testViewFromCVCAM_two();
	}

	return nRetCode;
}

// cvcam ���̺귯���� cvcamSetProperty() �Ӽ��� ������ �ݹ� �Լ�
void cvcam_callback(IplImage* image);

// cvcam ���̺귯�� ��� ���� �ڵ� 1 
// ī�޶� ����â ����, â ũ�⸦ �⺻���� �� ���  
void testViewFromCVCAM_1()
{
	// STEP 1 : ī�޶� ����
	// ī�޶� ����â�� ��Ÿ��.
	int *out;
	int nSelected = cvcamSelectCamera( &out );
	if( nSelected == 0 )
	{
		printf("ī�޶� ������� �ʾҽ��ϴ�.\n");
		return;
	}

	// STEP 2 : �Ӽ� ����
	char *title = "cvcam â - �⺻ ũ��";
	cvNamedWindow( title, CV_WINDOW_AUTOSIZE );
	HWND hwnd = (HWND)cvGetWindowHandle( title );

	cvcamSetProperty( out[0], CVCAM_PROP_ENABLE, CVCAMTRUE );
	cvcamSetProperty( out[0], CVCAM_PROP_RENDER, CVCAMTRUE );
	cvcamSetProperty( out[0], CVCAM_PROP_WINDOW, &hwnd );

	// �ݹ� �Լ� ����
	cvcamSetProperty( out[0], CVCAM_PROP_CALLBACK, cvcam_callback );
 
	// STEP 3 : �ʱ�ȭ & ����
    cvcamInit();
    cvcamStart();
 
	// ���� Ű�� ������ â ����.
	cvWaitKey(0);

	// STEP 4 : �ߴ� & ���� 
	cvcamStop();
	cvcamExit();

	// 
	cvDestroyAllWindows();

	return;
}

// cvcam ���̺귯�� ��� ���� �ڵ� 2 
// ī�޶� ���� â ���ֱ�, â ũ�⸦ ������ ��� 
void testViewFromCVCAM_2()
{
	// STEP 1 : ī�޶� ����
	int nSelected = cvcamGetCamerasCount(); 
	if( nSelected == 0 )
	{
		printf("ī�޶� ������� �ʾҽ��ϴ�.\n");
		return;
	}

	// STEP 2 : �Ӽ� ����
	char *title = "cvcam â - ������ ũ��";
	cvNamedWindow( title, CV_WINDOW_AUTOSIZE );
	HWND hwnd = (HWND)cvGetWindowHandle( title );

    cvcamSetProperty( 0, CVCAM_PROP_ENABLE, CVCAMTRUE );
	cvcamSetProperty( 0, CVCAM_PROP_RENDER, CVCAMTRUE );
	cvcamSetProperty( 0, CVCAM_PROP_WINDOW, &hwnd );

	// ������ â�� ����, �ʺ� ����
	int height = 240; int width = 320;
	cvcamSetProperty( 0, CVCAM_RNDHEIGHT, &height ); 
	cvcamSetProperty( 0, CVCAM_RNDWIDTH, &width ); 

	// �ݹ� �Լ� ����
	cvcamSetProperty( 0, CVCAM_PROP_CALLBACK, cvcam_callback ); 
 
	// STEP 3 : �ʱ�ȭ & ����
    cvcamInit();
    cvcamStart();
 
	// ���� Ű�� ������ â ����.
	cvWaitKey(0);

	// STEP 4 : �ߴ� & ���� 
	cvcamStop();
	cvcamExit();

	//
	cvDestroyAllWindows();

	return;
}

// cvcam ���̺귯�� ��� ���� �ڵ� 3 
// HWND ������� �ʱ�, ī�޶� ���� â ���ֱ�, â ũ�⸦ ������ ���, 
// â ������ �׻� "cvcam window" ��.
void testViewFromCVCAM_3()
{
	// STEP 1 : ī�޶� ����
	// ī�޶� ����â ���� �ٷ� ����
	int nSelected = cvcamGetCamerasCount();  
	if( nSelected == 0 )
	{
		printf("ī�޶� ������� �ʾҽ��ϴ�.\n");
		return;
	}

	// STEP 2 : �Ӽ� ����
    cvcamSetProperty( 0, CVCAM_PROP_ENABLE, CVCAMTRUE );
	cvcamSetProperty( 0, CVCAM_PROP_RENDER, CVCAMTRUE );

	// ������ â�� ����, �ʺ� ����
	int height = 240; int width = 320;
	cvcamSetProperty( 0, CVCAM_RNDHEIGHT, &height ); 
	cvcamSetProperty( 0, CVCAM_RNDWIDTH, &width ); 

	// �ݹ� �Լ� ����
	cvcamSetProperty( 0, CVCAM_PROP_CALLBACK, cvcam_callback ); 
 
	// STEP 3 : �ʱ�ȭ & ����
    cvcamInit();
    cvcamStart();
 
	// ���� Ű�� ������ â ����.
	cvWaitKey(0);

	// STEP 4 : �ߴ� & ���� 
	cvcamStop();
	cvcamExit();

	//
	cvDestroyAllWindows();

	return;
}

void cvcam_stereo_callback(IplImage* image1, IplImage* image2);

// ī�޶� 2�� ����� 
void testViewFromCVCAM_two()
{
	// STEP 1 : ī�޶� ����
	int *out;
	int nSelected = cvcamSelectCamera( &out );
	if( nSelected == 0 )
	{
		printf("ī�޶� ������� �ʾҽ��ϴ�.\n");
		return;
	}

	// STEP 2 : â ����
	char *title1 = "cvcam â - First";
	cvNamedWindow( title1, CV_WINDOW_AUTOSIZE );
	HWND hwnd1 = (HWND)cvGetWindowHandle( title1 );

	char *title2 = "cvcam â - Second";
	cvNamedWindow( title2, CV_WINDOW_AUTOSIZE );
	HWND hwnd2 = (HWND)cvGetWindowHandle( title2 );

	// STEP 3 : ù ��° ī�޶��� �Ӽ� ����
    cvcamSetProperty( out[0], CVCAM_PROP_ENABLE, CVCAMTRUE );
	cvcamSetProperty( out[0], CVCAM_PROP_RENDER, CVCAMTRUE );
	cvcamSetProperty( out[0], CVCAM_PROP_WINDOW, &hwnd1 );
	cvcamSetProperty( out[0], CVCAM_STEREO_CALLBACK, cvcam_stereo_callback ); 

	// STEP 4 : �� ��° ī�޶� ���õǾ��� �� �Ӽ� ����
	if( nSelected == 2 ) 
	{
		cvcamSetProperty( out[1], CVCAM_PROP_ENABLE, CVCAMTRUE );
		cvcamSetProperty( out[1], CVCAM_PROP_RENDER, CVCAMTRUE );
		cvcamSetProperty( out[1], CVCAM_PROP_WINDOW, &hwnd2 );
		cvcamSetProperty( out[1], CVCAM_STEREO_CALLBACK, cvcam_stereo_callback ); 
	}

	// STEP 5 : �ʱ�ȭ & ����
    cvcamInit();
    cvcamStart();
 
	// ���� Ű�� ������ â ����.
	cvWaitKey(0);

	// STEP 6 : �ߴ� & ���� 
	cvcamStop();
	cvcamExit();

	//
	cvDestroyAllWindows();

	return;
}

// �ݹ� �Լ� - ī�޶� 2���� ��� 
void cvcam_stereo_callback(IplImage* image1, IplImage* image2)
{
	return;
}

// �ݹ� �Լ� - ���� ���� ���͸� 
void cvcam_callback(IplImage* image)
{
	// image ���� 
	IplImage *src_image = cvCloneImage( image );

	// Enhance detail filter - ��ü�� �ѷ��� ���� ���� �巯���� ȿ���� ��.
	float kernel[] =  { 0.0f/5.0f, -1.0f/5.0f,  0.0f/5.0f,
					   -1.0f/5.0f,  9.0f/5.0f, -1.0f/5.0f,
			            0.0f/5.0f, -1.0f/5.0f,  0.0f/5.0f };
	
	// CvMat ��ȯ
	CvMat mat_kernel = cvMat( 3, 3, CV_32FC1, kernel );

	// ���͸� ���� ����� ���� ���� �ʱ�ȭ
	IplImage *dst_image = cvCreateImage( cvGetSize(src_image), 
										  IPL_DEPTH_8U, 
										  src_image->nChannels );

	// ���͸� ���� : ȸ��(convolution)
	cvFilter2D( src_image, dst_image, &mat_kernel, cvPoint(-1,-1) );

	// ���� ����� ����
	cvCopy(dst_image, image);

	// �Ҵ��� �޸� ���� 
	cvReleaseData( &mat_kernel );
	cvReleaseImage( &src_image );
	cvReleaseImage( &dst_image );

	return;
}

// ī�޶󿡼� �Է� ���� �������� AVI�� �����ϱ�
void testWriterCamera()
{
	IplImage* image;
	CvCapture *capture;

	char *captureWindow = "camera";

	// AVI ���� ���� ���� ���� ���� 
	// ���� ���� �ۼ��⸦ �����Ѵ�.
	CvVideoWriter* videoWriter;
	double fps = 30.0; 
	char *writeFileName = getSaveAVIFromFileDialog(); 

	// ī�޶� ĸ�� �ʱ�ȭ
	// 0 ��° ����� ī�޶�κ��� ���� 
	if( !(capture = cvCaptureFromCAM(0)) )
	{
		printf("�������� ������ �� �����ϴ�!");
		return;
	}

	// ī�޶󿡼� ���� �������� ��ȯ�Ѵ�.
	image = cvQueryFrame( capture ); 
	cvNamedWindow( captureWindow, CV_WINDOW_AUTOSIZE );
	//cvResizeWindow( captureWidow, 640, 480 );
	cvShowImage( captureWindow, image );

	// -1�� ����������, �ڵ��� ��� �Ұ��� ����� â�� ��Ÿ����.
	videoWriter = cvCreateVideoWriter( writeFileName, -1,  fps , 
				   cvSize(image->width, image->height), 1 );

	while(1)
	{
		// ī�޶󿡼� ���� �������� ��ȯ�Ѵ�.
		image = cvQueryFrame( capture );

		// ���� ����Ÿ�� �����Ѵ�.
		cvWriteFrame( videoWriter, image ); 

		// ���� ����Ÿ�� â���� �����ش�.
		cvShowImage( captureWindow, image );

		// ���ѷ����ȿ� cvWaitKey() �Լ� ȣ�� ������
		// �������� �����Ƿ� �ݵ�� �־�� ��.
		// ESC Ű�� ������ �����Ѵ�.
		if( cvWaitKey(10) == 27 )
			break;
	}

	// ���� �� ī�޶� ���� ���� 
	cvReleaseVideoWriter( &videoWriter ); 
	cvReleaseCapture( &capture );
	cvDestroyWindow( captureWindow );

	return;
}

char *getSaveAVIFromFileDialog()
{
	char *saveFileName = (char *)NULL;

	// ���� ����
	char szFilter[] = "AVI ����(*.avi)|*.avi|";

	CFileDialog fileDlg(FALSE, 
				NULL, 
				NULL, 
				OFN_EXPLORER|OFN_HIDEREADONLY|OFN_OVERWRITEPROMPT, 
				szFilter
				);

	if( fileDlg.DoModal() == IDOK ) 
	{
		// CString to char *
		saveFileName 
			= (char *)strdup((char *)(LPCTSTR)fileDlg.GetPathName());
	}

	return saveFileName;	
}

// ī�޶󿡼� �Է� �޾Ƽ� �����ֱ�
void testViewFromCamera()
{
	IplImage *image;


	// ī�޶� ĸ�� �ʱ�ȭ
	// 0 ��° ����� ī�޶�κ��� ���� 
	CvCapture *capture = cvCaptureFromCAM(0);

	char *captureWidow = "camera";
	cvNamedWindow( captureWidow, CV_WINDOW_AUTOSIZE );
    //cvResizeWindow( captureWidow, 640, 480 );
	
	while(1)
	{
		// ī�޶�κ��� �Էµ� �������� ��´�.
		// ���࿡ �����ҽ� ���� �޽����� �����ش�.
		if( !cvGrabFrame( capture ) ) 
		{
			printf("�������� ������ �� �����ϴ�! \n");
			break;
		}

		// ������ ���������κ��� ���� �����͸� ��´�.
		image = cvRetrieveFrame( capture );

		// ���� ����Ÿ�� â���� �����ش�.
		cvShowImage( captureWidow, image );

		// ���ѷ����ȿ� cvWaitKey() �Լ� ȣ�� ������
		// �������� �����Ƿ� �ݵ�� �־�� ��.
		// ESC Ű�� ������ �����Ѵ�.
		if( cvWaitKey(10) == 27 )
			break;
	}

	// ī�޶� ���� ����
	cvReleaseCapture( &capture );
	cvDestroyWindow( captureWidow );
 }


IplImage *track_src_image;
IplImage *track_dst_image;
char *track_title = "Ʈ���� ������ ���� ����ȭ ����";
int track_threshold = 128;

void testTrackBarEvent()
{
	// ���� ��ȭ���ڿ��� ���� ������ �����Ѵ�.
	char *readFileName = getFileDialog();
	if( !readFileName ) return;

	// ������ �д´�. 
	track_src_image = cvLoadImage(readFileName, CV_LOAD_IMAGE_GRAYSCALE);
	cvNamedWindow(  track_title, CV_WINDOW_AUTOSIZE );
	cvShowImage( track_title, track_src_image );

	// ����ȭ ���� ����� ���� ���� ����
	track_dst_image = cvCreateImage( cvGetSize(track_src_image), IPL_DEPTH_8U, 1 );
	
	// Ʈ���� ���� ��, Ʈ���� �ڵ鷯�� ȣ���Ѵ�.
	cvCreateTrackbar("Track", track_title, &track_threshold, 255, trackbarHandler); 

	// Ű���� �Է��� ��ٸ���.
	cvWaitKey(0);

	// ����
	cvReleaseImage( &track_src_image );
	cvReleaseImage( &track_dst_image );
	cvDestroyAllWindows();
}

// Ʈ���� �ڵ鷯 
void trackbarHandler(int pos)
{
	// ����ȭ ����
	cvThreshold(track_src_image, track_dst_image, pos, 255, CV_THRESH_BINARY); 

	// ����ȭ ������ ����� �����ش�.
	cvShowImage( track_title, track_dst_image );	
}

void testMouseEvent()
{
	// ���� ��ȭ���ڿ��� ���� ������ �����Ѵ�.
	char *readFileName = getFileDialog();
	if( !readFileName ) return;

	// ������ �д´�. 
	IplImage *src_image = cvLoadImage(readFileName, CV_LOAD_IMAGE_UNCHANGED);

	char *src_title = "����";
	cvNamedWindow( src_title, CV_WINDOW_AUTOSIZE );
	cvShowImage( src_title, src_image );

	// ���콺 �ڵ鷯 ��� 
	int mouseParam = 5;
	cvSetMouseCallback( src_title, mouseHandler, &mouseParam ); 

	// Ű���� �Է��� ��ٸ���.
	cvWaitKey(0);

	// ����
	cvReleaseImage( &src_image );
	cvDestroyAllWindows();
}

void mouseHandler(int event, int x, int y, int flags, void *param)
{
	switch(event) {
		case CV_EVENT_LBUTTONDOWN :
			if( flags & CV_EVENT_FLAG_CTRLKEY )
				printf("CTRL Ű�� ����ä, ���� ���콺 ��ư�� �����̽��ϴ�. \n\n");
			break;
		case CV_EVENT_RBUTTONDOWN :
			printf("������ ���콺 ��ư���� �����̽��ϴ�.\n\n");
			break;
	}
}

// cvAdd() �Լ��� ���ڰ� CvArr�̸�, lplImage, CvMat ���� ���� Ȯ��
void testCvArr()
{
	int i, j;

	/*----------------------------------------------------*/
	/*------------ �� IplImage ���� ���� ----------------------*/ 
	/*----------------------------------------------------*/
	// ���� ��ȭ���ڿ��� ���� ������ �����Ѵ�.
	char *readFileName1 = getFileDialog();
	if( !readFileName1 ) return;

	char *readFileName2 = getFileDialog();
	if( !readFileName2 ) return;

	// �÷� ������ �о� ��ϵ� �������� �ٲ۴�.
	IplImage *src_image1 = cvLoadImage(readFileName1, CV_LOAD_IMAGE_GRAYSCALE);
	IplImage *src_image2 = cvLoadImage(readFileName2, CV_LOAD_IMAGE_GRAYSCALE);
	IplImage *dst_image = cvCreateImage( cvGetSize(src_image1), IPL_DEPTH_8U, 1 );

	cvAdd( src_image1, src_image2, dst_image, NULL);

	// â ���
	char *src_title1 = "���� 1";
	cvNamedWindow( src_title1, CV_WINDOW_AUTOSIZE );
	cvShowImage( src_title1, src_image1 );

	char *src_title2 = "���� 2";
	cvNamedWindow( src_title2, CV_WINDOW_AUTOSIZE );
	cvShowImage( src_title2, src_image2 );
	
	char *dst_title = "cvAdd() ���� ��� ����";
	cvNamedWindow( dst_title, CV_WINDOW_AUTOSIZE );
	cvShowImage( dst_title, dst_image );

	/*----------------------------------------------------*/
	/*------------ �� CvMat ���� ���� -----------------------*/ 
	/*----------------------------------------------------*/
	CvMat *mat1 = cvCreateMat( 2, 2, CV_32FC1 );
	CvMat *mat2 = cvCreateMat( 2, 2, CV_32FC1 );
	CvMat *mat3 = cvCreateMat( 2, 2, CV_32FC1 );

	// 
	CvSize size = cvGetSize( mat1 );

	for(i=0; i<size.height; i++)
	{
		for(j=0; j<size.width; j++)
		{
			cvmSet( mat1, i, j, (float)(i+j) );
			cvmSet( mat2, i, j, sqrt( (float)(i+j) ) );
		}
	}

	cvAdd( mat1, mat2, mat3, NULL );

	printf("�� CvMat ���� ���� ��� \n");

	for(i=0; i<size.height; i++)
		for(j=0; j<size.width; j++)
			printf("[%d][%d] : %f + %f = %f \n", i, j,
					cvmGet(mat1, i, j),
					cvmGet(mat2, i, j),
					cvmGet(mat3, i, j) );

	// Ű���� �Է��� ��ٸ���.
	cvWaitKey(0);

	// ����
	cvReleaseImage( &src_image1 );
	cvReleaseImage( &src_image2 );
	cvReleaseImage( &dst_image );

	cvReleaseMat( &mat1 );
	cvReleaseMat( &mat2 );
	cvReleaseMat( &mat3 );

	cvDestroyAllWindows();
 	
	return;
}

void testMatrixFunc()
{
	int i,j;

	CvMat *mat1 = cvCreateMat( 2, 2, CV_32FC1 );
	CvMat *mat2 = cvCreateMat( 2, 2, CV_32FC1 );
	CvMat *mat3 = cvCreateMat( 2, 2, CV_32FC1 );

	// ���Ұ��� 0���� �ʱ�ȭ
	cvZero( mat3 );

	for(i=0; i<mat1->height; i++)
	{
		for(j=0; j<mat1->width; j++)
		{
			cvmSet( mat1, i, j, (float)(i*2 + j*2) );
			cvmSet( mat2, i, j, sqrt( (float)(i*2 + j*2) ) );
		}
	}

	//  
	cvMul( mat1, mat2, mat3 );

	// ��İ� ���
	printf("mat1\n"); printMatrix( mat1 ); 
	printf("mat2\n"); printMatrix( mat2 ); 
	printf("mat3\n"); printMatrix( mat3 ); 

	cvReleaseMat( &mat1 );
	cvReleaseMat( &mat2 );
	cvReleaseMat( &mat3 );
}

// ��İ� ���
void printMatrix(CvMat *matrix) 
{
	int i, j;

	// ����� ũ�⸦ ��������
	CvSize size = cvGetSize( matrix );

	for(i=0; i<size.height; i++)
	{
		for(j=0; j<size.width; j++)
		{
			printf( "%5.1f", cvmGet( matrix, i, j ) ); 
		}
	
		printf( "\n" );
	}

	printf( "\n" );
}

void matrixUsage()
{
	CvMat kernel;

	// Enhance detail filter kernel
	float mask[] = {-1.0f/3.0f, 0.0f/3.0f, -1.0f/3.0f, 
		      0.0f/3.0f, 7.0f/3.0f,  0.0f/3.0f, 
		     -1.0f/3.0f, 0.0f/3.0f, -1.0f/3.0f};

	// ���� ��ȭ���ڿ��� ���� ������ �����Ѵ�.
	char *readFileName = getFileDialog();
	if( !readFileName ) return;

	// ������ �д´�. 
	IplImage *src_image = cvLoadImage(readFileName, CV_LOAD_IMAGE_COLOR);
	
	// 
	IplImage *src_red   = cvCreateImage( cvGetSize(src_image), IPL_DEPTH_8U, 1);
	IplImage *src_green = cvCreateImage( cvGetSize(src_image), IPL_DEPTH_8U, 1);
	IplImage *src_blue  = cvCreateImage( cvGetSize(src_image), IPL_DEPTH_8U, 1);

	// RGB �÷������� Red, Green, Blue ä�η� �и��Ѵ�.
	cvCvtPixToPlane( src_image, src_blue, src_green, src_red, NULL );

	//
	IplImage *dst_red   = cvCreateImage( cvGetSize(src_image), IPL_DEPTH_8U, 1);
	IplImage *dst_green = cvCreateImage( cvGetSize(src_image), IPL_DEPTH_8U, 1);
	IplImage *dst_blue  = cvCreateImage( cvGetSize(src_image), IPL_DEPTH_8U, 1);

	// ��� ���� �ʱ�ȭ�� �ΰ��� ����� �ִ�.
	// kernel = cvMat( 3, 3, CV_32FC1, mask ); 
	cvInitMatHeader(&kernel, 3, 3, CV_32FC1, mask);

	//
	cvFilter2D(src_red, dst_red, &kernel);
	cvFilter2D(src_green, dst_green, &kernel);
	cvFilter2D(src_blue, dst_blue, &kernel);

	// �и��� Red, Green, Blue ä���� RGB �÷� �������� ��ģ��.
	IplImage *dst_image = cvCreateImage( cvGetSize(src_image), IPL_DEPTH_8U, 3 );
	cvCvtPlaneToPix( dst_blue, dst_green, dst_red, NULL, dst_image ); 

	// ��� ���
	char *src_title = "�� ����";
	cvNamedWindow( src_title, CV_WINDOW_AUTOSIZE );
	cvShowImage( src_title, src_image );

	char *dst_title = "cvFilter2D() ���� ����";
	cvNamedWindow( dst_title, CV_WINDOW_AUTOSIZE );
	cvShowImage( dst_title, dst_image );

	// Ű���� �Է��� ��ٸ���.
	cvWaitKey(0);

	// ����
	cvReleaseImage( &src_image ); 
	cvReleaseImage( &dst_image );
	
	cvReleaseImage( &src_red); 
	cvReleaseImage( &src_green); 
	cvReleaseImage( &src_blue );
	cvReleaseImage( &dst_red); 
	cvReleaseImage( &dst_green); 
	cvReleaseImage( &dst_blue );

	cvReleaseData( &kernel );
	cvDestroyAllWindows();	

/* --- TIP : ��� ���� �ʱ�ȭ (Dynamic allocated to CvMat) ----
	//
	// cvCreateMat() �Լ��� ������ cvMat�� ����ϰ� ������ �Ʒ��� ���� �����Ѵ�.
	// ��, CvMat *kernel = cvCreateMat( 3, 3, CV_32FC1 );
	//     cvReleaseMat( &kernel );
	//
	// ���� �ڵ�  

    ..(�߷�)...
	CvMat *kernel = cvCreateMat( 3, 3, CV_32FC1 );
	
	cvmSet( kernel, 0, 0, -1.0f/3.0f ); 
	cvmSet( kernel, 0, 1,  0.0f/3.0f );
	cvmSet( kernel, 0, 2, -1.0f/3.0f );

	cvmSet( kernel, 1, 0,  0.0f/3.0f ); 
	cvmSet( kernel, 1, 1,  7.0f/3.0f );
	cvmSet( kernel, 1, 2,  0.0f/3.0f );

	cvmSet( kernel, 2, 0, -1.0f/3.0f ); 
	cvmSet( kernel, 2, 1,  0.0f/3.0f );
	cvmSet( kernel, 2, 2, -1.0f/3.0f );

	cvFilter2D(src_red, dst_red, kernel);
	cvFilter2D(src_green, dst_green, kernel);
	cvFilter2D(src_blue, dst_blue, kernel);

	IplImage *dst_image = cvCreateImage( cvGetSize(src_image), IPL_DEPTH_8U, 3 );
	cvCvtPlaneToPix( dst_blue, dst_green, dst_red, NULL, dst_image ); 

    ...(�߷�)...

	cvReleaseMat( &kernel );
*/
}


void directAccessPixel()
{
	int i, j;
	BYTE r, g, b, var; // BYTE�� unsigned char�� �ٸ� ǥ���̴�. (0~255�� ���� ����)
					   // ����� ���� �����ʹ� 0~255������ ���� �����Ƿ�, 
					   // �̿� �����ϴ� �ڷ����� BYTE�� �����ϴ� ���̴�.

	// ���� ��ȭ���ڿ��� ���� ������ �����Ѵ�.
	char *readFileName = getFileDialog();
	if( !readFileName ) return;

	// ������ �д´�. 
	IplImage *src_image = cvLoadImage( readFileName, CV_LOAD_IMAGE_COLOR );

	// ��ϵ� ����
	IplImage *dst_image = cvCreateImage( cvGetSize(src_image), IPL_DEPTH_8U, 1);
	
	for(i=0; i<dst_image->height; i++)
	{
		for(j=0; j<dst_image->width; j++)
		{
			b = (BYTE)src_image->imageData[(i*src_image->widthStep) + j*3+0];
			g = (BYTE)src_image->imageData[(i*src_image->widthStep) + j*3+1];
			r = (BYTE)src_image->imageData[(i*src_image->widthStep) + j*3+2];

			var = (BYTE)( (r + g + b)/3.0 );

			dst_image->imageData[(i*dst_image->widthStep) + j] = var;
		}
	}
	// ��� ���
	char *title = "��ϵ� ����";
	cvNamedWindow( title, CV_WINDOW_AUTOSIZE );
	cvShowImage( title, dst_image );

	// Ű���� �Է��� ��ٸ���.
	cvWaitKey(0);

	// ����
	cvReleaseImage( &src_image );
	cvReleaseImage( &dst_image );
	cvDestroyWindow( title );
}

void funcAccessPixel()
{
	int i, j;
	double r, g, b, var;

	// ���� ��ȭ���ڿ��� ���� ������ �����Ѵ�.
	char *readFileName = getFileDialog();
	if( !readFileName ) return;

	// ������ �д´�. 
	IplImage *src_image = cvLoadImage( readFileName, CV_LOAD_IMAGE_COLOR );
	
	// �����Ѵ�.
	IplImage *src_red   = cvCreateImage( cvGetSize(src_image), IPL_DEPTH_8U, 1);
	IplImage *src_green = cvCreateImage( cvGetSize(src_image), IPL_DEPTH_8U, 1);
	IplImage *src_blue  = cvCreateImage( cvGetSize(src_image), IPL_DEPTH_8U, 1);
	
	// RGB �÷������� Red, Green, Blue ä�η� �и��Ѵ�.
	cvCvtPixToPlane( src_image, src_blue, src_green, src_red, NULL );

	// ��ϵ� ����
	IplImage *dst_image = cvCreateImage( cvGetSize(src_image), IPL_DEPTH_8U, 1);
	
	for(i=0; i<src_image->height; i++)
	{
		for(j=0; j<src_image->width; j++)
		{
			r = cvGetReal2D( src_red, i, j );
			g = cvGetReal2D( src_green, i, j );
			b = cvGetReal2D( src_blue, i, j );

			var = (r + g + b)/3.0;

			cvSetReal2D( dst_image, i, j, var );
		}
	}

	// ��� ���
	char *title = "��ϵ� ����";
	cvNamedWindow( title, CV_WINDOW_AUTOSIZE );
	cvShowImage( title, dst_image );

	// Ű���� �Է��� ��ٸ���.
	cvWaitKey(0);

	// ����
	cvReleaseImage( &src_image );
	cvReleaseImage( &src_red); 
	cvReleaseImage( &src_green); 
	cvReleaseImage( &src_blue); 
	cvReleaseImage( &dst_image );
	cvDestroyWindow( title );
}


// ���� ����� ���� �Լ� ��� ����
void allImageFuncUsage() 
{
	char *saveFileName = "c:\\save_image.jpg";

	// ���� ��ȭ���ڿ��� ���� ������ �����Ѵ�.
	char *readFileName = getFileDialog();
	if( !readFileName ) return;

	// ������ �д´�. 
	IplImage *image = cvLoadImage( readFileName, CV_LOAD_IMAGE_UNCHANGED );
	
	// ĸ���� title�� â�� ����
	char *title = "����";
	cvNamedWindow( title, CV_WINDOW_AUTOSIZE ); 

	// ������ â�� �����ش�.
	cvShowImage( title, image );

	// â ũ�⸦ �����Ѵ�.
	cvResizeWindow( title, image->width, image->height );

	// â�� �̵��Ѵ�.
	cvMoveWindow( title, 100, 100 );

	// ���� �����͸� �����Ѵ�.
	CvSize size = cvSize( image->width, image->height );
	IplImage *create_image = cvCreateImage( size, IPL_DEPTH_8U, 3 );

	// ���� ����Ÿ�� ������ ��, �����Ѵ�.
	IplImage *clone_image = cvCloneImage( image );
	cvSaveImage( saveFileName, clone_image );

	// ������ ������ �ٽ� �ҷ����δ�.
	char *save_title = "������ ����";
	IplImage *save_image = cvLoadImage( saveFileName, CV_LOAD_IMAGE_UNCHANGED );
	cvNamedWindow( save_title, CV_WINDOW_AUTOSIZE );
	cvShowImage( save_title, save_image );

	// Ű���� �Է��� ��ٸ���.
	cvWaitKey(0);

	// �Ҵ�� ���ҽ��� �����ϰ� â�� �ı��Ѵ�.
	cvReleaseImage( &image );
	cvReleaseImage( &create_image );
	cvReleaseImage( &clone_image );
	cvReleaseImage( &save_image );

	// ���� �ִ� â�� ��� �ı��Ѵ�.
	cvDestroyAllWindows(); 

	// cvDestroyAllWindows() ��� �Ʒ��� ���� �Ͽ��� �����ϴ�.
	// cvDestroyWindow( title ); 
	// cvDestroyWindow( save_title ); 

	return;
}

// OpenCV ���� Ȯ��
void verifyVersion()
{
	const char *opencv_liberies = 0;
	const char *addon_modules = 0;
	cvGetModuleInfo( 0, &opencv_liberies, &addon_modules );
	printf( "* OpenCV : %s \n* Add-on Modules : %s \n",
			opencv_liberies, addon_modules);

	return;
}

// ���� ����
void imageViewer()
{
	IplImage *color_image;
	IplImage *gray_image;

	// STEP 1 : ���� ���� ����
	char *readFileName = getFileDialog();
	if( !readFileName ) return;

	// STEP 2 : �÷� ������ �д´�.
	color_image = cvLoadImage( readFileName, CV_LOAD_IMAGE_COLOR );
	
	// STEP 3 : �б� �����̸�
	if( color_image != 0 )
	{
		// ��ȯ ����� ���� ��ϵ� ������ �ʱ�ȭ �Ѵ�.
 		gray_image = cvCreateImage( cvGetSize(color_image), IPL_DEPTH_8U, 1 ); 

		// �÷� ������ ��ϵ� �������� ��ȯ�Ѵ�.
		cvCvtColor( color_image, gray_image, CV_BGR2GRAY );
		
		char *title = "First Image Viewer using OpenCV";

		// ĸ�� ������ title�� ���� â�� ����
		cvNamedWindow( title, CV_WINDOW_AUTOSIZE ); 
		
		// ������ â�� image ��ü�� �ѷ��ش�.
		cvShowImage( title, gray_image );

		// Ű���� �Է��� ��ٸ���.
		cvWaitKey(0);
	
		// �Ҵ�� ���ҽ��� �����Ѵ�.
		cvReleaseImage( &color_image );
		cvReleaseImage( &gray_image );

		// â�� �ݴ´�.
		cvDestroyWindow( title );       
	}
	else
	{
		printf("[ERROR] ���� ������ �о�� �� �����ϴ�.\n");
	}

	return;	
}

// ���� ��ȭ���ڿ��� ���� �´�.
char *getFileDialog()
{
	char *readFileName = (char *)NULL;

	// ���� ����
	char szFilter[] = "���� ���� ����(*.bmp, *.jpg, *.gif, *.png, *.tif) \
						|*.bmp;*.jpg;*.gif;*.png;*.tif||";

	printf("\n");
	printf("\t * ���� ��ȭ���ڸ� �̿��Ͽ� ���� ������ �����Ͻʽÿ�. \n\n");
	printf("\t \n");

	CFileDialog fileDlg(TRUE, 
			  NULL, 
				NULL, 
				OFN_EXPLORER|OFN_HIDEREADONLY, 
				szFilter
				);

	if( fileDlg.DoModal() == IDOK ) 
	{
		// CString to char *
		readFileName 
			= (char *)strdup((char *)(LPCTSTR)fileDlg.GetPathName());
	}

	return readFileName;
}