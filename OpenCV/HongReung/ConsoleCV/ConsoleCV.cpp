// ConsoleCV.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "ConsoleCV.h"

// OpenCV 관련 헤더파일 
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
		// OpenCV 버전 확인
		// verifyVersion();

		// 영상 보기
		// imageViewer();

		// 영상 입출력 관련 함수 사용 예제
		// allImageFuncUsage();

		// 직접 접근
		// directAccessPixel();

		// GetReal2D(), SetReal2D() 함수를 사용
		// funcAccessPixel();

		// 행렬 함수 예
		// testMatrixFunc();

		// 행렬 사용 + 필터링
		// matrixUsage();

		// cvAdd() 함수의 인자가 CvArr이면, lplImage, CvMat 적용 여부 확인
		// testCvArr();

		// 마우스 핸들러
		// testMouseEvent();
	
		// 트랙바 핸들러
		// testTrackBarEvent();

		// 카메라에서 입력 받아서 보여주기
		//testViewFromCamera();

		// 카메라에서 입력 받은 프레임을 AVI로 저장하기
		//testWriterCamera();

		// cvcam 테스트 1
		//testViewFromCVCAM_1();

		// cvcam 테스트 2
		// testViewFromCVCAM_2();

		// cvcam 테스트 3
		//testViewFromCVCAM_3();

		// 카메라 2대 일때의 cvcam 테스트
		//testViewFromCVCAM_two();
	}

	return nRetCode;
}

// cvcam 라이브러리의 cvcamSetProperty() 속성에 설정한 콜백 함수
void cvcam_callback(IplImage* image);

// cvcam 라이브러리 사용 예제 코드 1 
// 카메라 선택창 보기, 창 크기를 기본으로 둘 경우  
void testViewFromCVCAM_1()
{
	// STEP 1 : 카메라 연결
	// 카메라 선택창이 나타남.
	int *out;
	int nSelected = cvcamSelectCamera( &out );
	if( nSelected == 0 )
	{
		printf("카메라가 연결되지 않았습니다.\n");
		return;
	}

	// STEP 2 : 속성 설정
	char *title = "cvcam 창 - 기본 크기";
	cvNamedWindow( title, CV_WINDOW_AUTOSIZE );
	HWND hwnd = (HWND)cvGetWindowHandle( title );

	cvcamSetProperty( out[0], CVCAM_PROP_ENABLE, CVCAMTRUE );
	cvcamSetProperty( out[0], CVCAM_PROP_RENDER, CVCAMTRUE );
	cvcamSetProperty( out[0], CVCAM_PROP_WINDOW, &hwnd );

	// 콜백 함수 지정
	cvcamSetProperty( out[0], CVCAM_PROP_CALLBACK, cvcam_callback );
 
	// STEP 3 : 초기화 & 시작
    cvcamInit();
    cvcamStart();
 
	// 임의 키를 누르면 창 닫힘.
	cvWaitKey(0);

	// STEP 4 : 중단 & 종료 
	cvcamStop();
	cvcamExit();

	// 
	cvDestroyAllWindows();

	return;
}

// cvcam 라이브러리 사용 예제 코드 2 
// 카메라 선택 창 없애기, 창 크기를 지정할 경우 
void testViewFromCVCAM_2()
{
	// STEP 1 : 카메라 연결
	int nSelected = cvcamGetCamerasCount(); 
	if( nSelected == 0 )
	{
		printf("카메라가 연결되지 않았습니다.\n");
		return;
	}

	// STEP 2 : 속성 설정
	char *title = "cvcam 창 - 지정한 크기";
	cvNamedWindow( title, CV_WINDOW_AUTOSIZE );
	HWND hwnd = (HWND)cvGetWindowHandle( title );

    cvcamSetProperty( 0, CVCAM_PROP_ENABLE, CVCAMTRUE );
	cvcamSetProperty( 0, CVCAM_PROP_RENDER, CVCAMTRUE );
	cvcamSetProperty( 0, CVCAM_PROP_WINDOW, &hwnd );

	// 보여줄 창의 높이, 너비 지정
	int height = 240; int width = 320;
	cvcamSetProperty( 0, CVCAM_RNDHEIGHT, &height ); 
	cvcamSetProperty( 0, CVCAM_RNDWIDTH, &width ); 

	// 콜백 함수 지정
	cvcamSetProperty( 0, CVCAM_PROP_CALLBACK, cvcam_callback ); 
 
	// STEP 3 : 초기화 & 시작
    cvcamInit();
    cvcamStart();
 
	// 임의 키를 누르면 창 닫힘.
	cvWaitKey(0);

	// STEP 4 : 중단 & 종료 
	cvcamStop();
	cvcamExit();

	//
	cvDestroyAllWindows();

	return;
}

// cvcam 라이브러리 사용 예제 코드 3 
// HWND 사용하지 않기, 카메라 선택 창 없애기, 창 크기를 지정할 경우, 
// 창 제목은 항상 "cvcam window" 임.
void testViewFromCVCAM_3()
{
	// STEP 1 : 카메라 연결
	// 카메라 선택창 없이 바로 연결
	int nSelected = cvcamGetCamerasCount();  
	if( nSelected == 0 )
	{
		printf("카메라가 연결되지 않았습니다.\n");
		return;
	}

	// STEP 2 : 속성 설정
    cvcamSetProperty( 0, CVCAM_PROP_ENABLE, CVCAMTRUE );
	cvcamSetProperty( 0, CVCAM_PROP_RENDER, CVCAMTRUE );

	// 보여줄 창의 높이, 너비 지정
	int height = 240; int width = 320;
	cvcamSetProperty( 0, CVCAM_RNDHEIGHT, &height ); 
	cvcamSetProperty( 0, CVCAM_RNDWIDTH, &width ); 

	// 콜백 함수 지정
	cvcamSetProperty( 0, CVCAM_PROP_CALLBACK, cvcam_callback ); 
 
	// STEP 3 : 초기화 & 시작
    cvcamInit();
    cvcamStart();
 
	// 임의 키를 누르면 창 닫힘.
	cvWaitKey(0);

	// STEP 4 : 중단 & 종료 
	cvcamStop();
	cvcamExit();

	//
	cvDestroyAllWindows();

	return;
}

void cvcam_stereo_callback(IplImage* image1, IplImage* image2);

// 카메라 2대 연결시 
void testViewFromCVCAM_two()
{
	// STEP 1 : 카메라 연결
	int *out;
	int nSelected = cvcamSelectCamera( &out );
	if( nSelected == 0 )
	{
		printf("카메라가 연결되지 않았습니다.\n");
		return;
	}

	// STEP 2 : 창 생성
	char *title1 = "cvcam 창 - First";
	cvNamedWindow( title1, CV_WINDOW_AUTOSIZE );
	HWND hwnd1 = (HWND)cvGetWindowHandle( title1 );

	char *title2 = "cvcam 창 - Second";
	cvNamedWindow( title2, CV_WINDOW_AUTOSIZE );
	HWND hwnd2 = (HWND)cvGetWindowHandle( title2 );

	// STEP 3 : 첫 번째 카메라의 속성 설정
    cvcamSetProperty( out[0], CVCAM_PROP_ENABLE, CVCAMTRUE );
	cvcamSetProperty( out[0], CVCAM_PROP_RENDER, CVCAMTRUE );
	cvcamSetProperty( out[0], CVCAM_PROP_WINDOW, &hwnd1 );
	cvcamSetProperty( out[0], CVCAM_STEREO_CALLBACK, cvcam_stereo_callback ); 

	// STEP 4 : 두 번째 카메라가 선택되었을 때 속성 설정
	if( nSelected == 2 ) 
	{
		cvcamSetProperty( out[1], CVCAM_PROP_ENABLE, CVCAMTRUE );
		cvcamSetProperty( out[1], CVCAM_PROP_RENDER, CVCAMTRUE );
		cvcamSetProperty( out[1], CVCAM_PROP_WINDOW, &hwnd2 );
		cvcamSetProperty( out[1], CVCAM_STEREO_CALLBACK, cvcam_stereo_callback ); 
	}

	// STEP 5 : 초기화 & 시작
    cvcamInit();
    cvcamStart();
 
	// 임의 키를 누르면 창 닫힘.
	cvWaitKey(0);

	// STEP 6 : 중단 & 종료 
	cvcamStop();
	cvcamExit();

	//
	cvDestroyAllWindows();

	return;
}

// 콜백 함수 - 카메라 2대일 경우 
void cvcam_stereo_callback(IplImage* image1, IplImage* image2)
{
	return;
}

// 콜백 함수 - 공간 영역 필터링 
void cvcam_callback(IplImage* image)
{
	// image 복사 
	IplImage *src_image = cvCloneImage( image );

	// Enhance detail filter - 물체를 둘러싼 것을 상세히 드러내는 효과를 냄.
	float kernel[] =  { 0.0f/5.0f, -1.0f/5.0f,  0.0f/5.0f,
					   -1.0f/5.0f,  9.0f/5.0f, -1.0f/5.0f,
			            0.0f/5.0f, -1.0f/5.0f,  0.0f/5.0f };
	
	// CvMat 변환
	CvMat mat_kernel = cvMat( 3, 3, CV_32FC1, kernel );

	// 필터링 수행 결과를 담을 영상 초기화
	IplImage *dst_image = cvCreateImage( cvGetSize(src_image), 
										  IPL_DEPTH_8U, 
										  src_image->nChannels );

	// 필터링 수행 : 회선(convolution)
	cvFilter2D( src_image, dst_image, &mat_kernel, cvPoint(-1,-1) );

	// 수행 결과를 복사
	cvCopy(dst_image, image);

	// 할당한 메모리 해제 
	cvReleaseData( &mat_kernel );
	cvReleaseImage( &src_image );
	cvReleaseImage( &dst_image );

	return;
}

// 카메라에서 입력 받은 프레임을 AVI로 저장하기
void testWriterCamera()
{
	IplImage* image;
	CvCapture *capture;

	char *captureWindow = "camera";

	// AVI 포맷 저장 관련 정보 설정 
	// 비디오 파일 작성기를 생성한다.
	CvVideoWriter* videoWriter;
	double fps = 30.0; 
	char *writeFileName = getSaveAVIFromFileDialog(); 

	// 카메라 캡쳐 초기화
	// 0 번째 연결된 카메라로부터 연결 
	if( !(capture = cvCaptureFromCAM(0)) )
	{
		printf("프레임을 가져올 수 없습니다!");
		return;
	}

	// 카메라에서 잡은 프레임을 반환한다.
	image = cvQueryFrame( capture ); 
	cvNamedWindow( captureWindow, CV_WINDOW_AUTOSIZE );
	//cvResizeWindow( captureWidow, 640, 480 );
	cvShowImage( captureWindow, image );

	// -1로 설정했으면, 코덱을 어떻게 할건지 물어보는 창이 나타난다.
	videoWriter = cvCreateVideoWriter( writeFileName, -1,  fps , 
				   cvSize(image->width, image->height), 1 );

	while(1)
	{
		// 카메라에서 잡은 프레임을 반환한다.
		image = cvQueryFrame( capture );

		// 영상 데이타를 저장한다.
		cvWriteFrame( videoWriter, image ); 

		// 영상 데이타를 창에서 보여준다.
		cvShowImage( captureWindow, image );

		// 무한루프안에 cvWaitKey() 함수 호출 않을시
		// 동작하지 않으므로 반드시 있어야 함.
		// ESC 키를 만나면 종료한다.
		if( cvWaitKey(10) == 27 )
			break;
	}

	// 해제 및 카메라 연결 종료 
	cvReleaseVideoWriter( &videoWriter ); 
	cvReleaseCapture( &capture );
	cvDestroyWindow( captureWindow );

	return;
}

char *getSaveAVIFromFileDialog()
{
	char *saveFileName = (char *)NULL;

	// 파일 포맷
	char szFilter[] = "AVI 파일(*.avi)|*.avi|";

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

// 카메라에서 입력 받아서 보여주기
void testViewFromCamera()
{
	IplImage *image;


	// 카메라 캡쳐 초기화
	// 0 번째 연결된 카메라로부터 연결 
	CvCapture *capture = cvCaptureFromCAM(0);

	char *captureWidow = "camera";
	cvNamedWindow( captureWidow, CV_WINDOW_AUTOSIZE );
    //cvResizeWindow( captureWidow, 640, 480 );
	
	while(1)
	{
		// 카메라로부터 입력된 프레임을 잡는다.
		// 만약에 실패할시 에러 메시지를 보여준다.
		if( !cvGrabFrame( capture ) ) 
		{
			printf("프레임을 가져올 수 없습니다! \n");
			break;
		}

		// 가져온 프레임으로부터 영상 데이터를 얻는다.
		image = cvRetrieveFrame( capture );

		// 영상 데이타를 창에서 보여준다.
		cvShowImage( captureWidow, image );

		// 무한루프안에 cvWaitKey() 함수 호출 않을시
		// 동작하지 않으므로 반드시 있어야 함.
		// ESC 키를 만나면 종료한다.
		if( cvWaitKey(10) == 27 )
			break;
	}

	// 카메라 연결 종료
	cvReleaseCapture( &capture );
	cvDestroyWindow( captureWidow );
 }


IplImage *track_src_image;
IplImage *track_dst_image;
char *track_title = "트랙바 조절에 의한 이진화 수행";
int track_threshold = 128;

void testTrackBarEvent()
{
	// 파일 대화상자에서 영상 파일을 선택한다.
	char *readFileName = getFileDialog();
	if( !readFileName ) return;

	// 영상을 읽는다. 
	track_src_image = cvLoadImage(readFileName, CV_LOAD_IMAGE_GRAYSCALE);
	cvNamedWindow(  track_title, CV_WINDOW_AUTOSIZE );
	cvShowImage( track_title, track_src_image );

	// 이진화 수행 결과를 담을 영상 생성
	track_dst_image = cvCreateImage( cvGetSize(track_src_image), IPL_DEPTH_8U, 1 );
	
	// 트랙바 생성 후, 트랙바 핸들러를 호출한다.
	cvCreateTrackbar("Track", track_title, &track_threshold, 255, trackbarHandler); 

	// 키보드 입력을 기다린다.
	cvWaitKey(0);

	// 해제
	cvReleaseImage( &track_src_image );
	cvReleaseImage( &track_dst_image );
	cvDestroyAllWindows();
}

// 트랙바 핸들러 
void trackbarHandler(int pos)
{
	// 이진화 수행
	cvThreshold(track_src_image, track_dst_image, pos, 255, CV_THRESH_BINARY); 

	// 이진화 수행한 결과를 보여준다.
	cvShowImage( track_title, track_dst_image );	
}

void testMouseEvent()
{
	// 파일 대화상자에서 영상 파일을 선택한다.
	char *readFileName = getFileDialog();
	if( !readFileName ) return;

	// 영상을 읽는다. 
	IplImage *src_image = cvLoadImage(readFileName, CV_LOAD_IMAGE_UNCHANGED);

	char *src_title = "영상";
	cvNamedWindow( src_title, CV_WINDOW_AUTOSIZE );
	cvShowImage( src_title, src_image );

	// 마우스 핸들러 등록 
	int mouseParam = 5;
	cvSetMouseCallback( src_title, mouseHandler, &mouseParam ); 

	// 키보드 입력을 기다린다.
	cvWaitKey(0);

	// 해제
	cvReleaseImage( &src_image );
	cvDestroyAllWindows();
}

void mouseHandler(int event, int x, int y, int flags, void *param)
{
	switch(event) {
		case CV_EVENT_LBUTTONDOWN :
			if( flags & CV_EVENT_FLAG_CTRLKEY )
				printf("CTRL 키를 누른채, 왼쪽 마우스 버튼을 누르셨습니다. \n\n");
			break;
		case CV_EVENT_RBUTTONDOWN :
			printf("오른쪽 마우스 버튼으로 누르셨습니다.\n\n");
			break;
	}
}

// cvAdd() 함수의 인자가 CvArr이면, lplImage, CvMat 적용 여부 확인
void testCvArr()
{
	int i, j;

	/*----------------------------------------------------*/
	/*------------ 두 IplImage 간의 덧셈 ----------------------*/ 
	/*----------------------------------------------------*/
	// 파일 대화상자에서 영상 파일을 선택한다.
	char *readFileName1 = getFileDialog();
	if( !readFileName1 ) return;

	char *readFileName2 = getFileDialog();
	if( !readFileName2 ) return;

	// 컬러 영상을 읽어 명암도 영상으로 바꾼다.
	IplImage *src_image1 = cvLoadImage(readFileName1, CV_LOAD_IMAGE_GRAYSCALE);
	IplImage *src_image2 = cvLoadImage(readFileName2, CV_LOAD_IMAGE_GRAYSCALE);
	IplImage *dst_image = cvCreateImage( cvGetSize(src_image1), IPL_DEPTH_8U, 1 );

	cvAdd( src_image1, src_image2, dst_image, NULL);

	// 창 출력
	char *src_title1 = "영상 1";
	cvNamedWindow( src_title1, CV_WINDOW_AUTOSIZE );
	cvShowImage( src_title1, src_image1 );

	char *src_title2 = "영상 2";
	cvNamedWindow( src_title2, CV_WINDOW_AUTOSIZE );
	cvShowImage( src_title2, src_image2 );
	
	char *dst_title = "cvAdd() 수행 결과 영상";
	cvNamedWindow( dst_title, CV_WINDOW_AUTOSIZE );
	cvShowImage( dst_title, dst_image );

	/*----------------------------------------------------*/
	/*------------ 두 CvMat 간의 덧셈 -----------------------*/ 
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

	printf("두 CvMat 간의 덧셈 결과 \n");

	for(i=0; i<size.height; i++)
		for(j=0; j<size.width; j++)
			printf("[%d][%d] : %f + %f = %f \n", i, j,
					cvmGet(mat1, i, j),
					cvmGet(mat2, i, j),
					cvmGet(mat3, i, j) );

	// 키보드 입력을 기다린다.
	cvWaitKey(0);

	// 해제
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

	// 원소값을 0으로 초기화
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

	// 행렬값 출력
	printf("mat1\n"); printMatrix( mat1 ); 
	printf("mat2\n"); printMatrix( mat2 ); 
	printf("mat3\n"); printMatrix( mat3 ); 

	cvReleaseMat( &mat1 );
	cvReleaseMat( &mat2 );
	cvReleaseMat( &mat3 );
}

// 행렬값 출력
void printMatrix(CvMat *matrix) 
{
	int i, j;

	// 행렬의 크기를 가져오기
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

	// 파일 대화상자에서 영상 파일을 선택한다.
	char *readFileName = getFileDialog();
	if( !readFileName ) return;

	// 영상을 읽는다. 
	IplImage *src_image = cvLoadImage(readFileName, CV_LOAD_IMAGE_COLOR);
	
	// 
	IplImage *src_red   = cvCreateImage( cvGetSize(src_image), IPL_DEPTH_8U, 1);
	IplImage *src_green = cvCreateImage( cvGetSize(src_image), IPL_DEPTH_8U, 1);
	IplImage *src_blue  = cvCreateImage( cvGetSize(src_image), IPL_DEPTH_8U, 1);

	// RGB 컬러공간을 Red, Green, Blue 채널로 분리한다.
	cvCvtPixToPlane( src_image, src_blue, src_green, src_red, NULL );

	//
	IplImage *dst_red   = cvCreateImage( cvGetSize(src_image), IPL_DEPTH_8U, 1);
	IplImage *dst_green = cvCreateImage( cvGetSize(src_image), IPL_DEPTH_8U, 1);
	IplImage *dst_blue  = cvCreateImage( cvGetSize(src_image), IPL_DEPTH_8U, 1);

	// 행렬 정적 초기화는 두가지 방법이 있다.
	// kernel = cvMat( 3, 3, CV_32FC1, mask ); 
	cvInitMatHeader(&kernel, 3, 3, CV_32FC1, mask);

	//
	cvFilter2D(src_red, dst_red, &kernel);
	cvFilter2D(src_green, dst_green, &kernel);
	cvFilter2D(src_blue, dst_blue, &kernel);

	// 분리한 Red, Green, Blue 채널을 RGB 컬러 공간으로 합친다.
	IplImage *dst_image = cvCreateImage( cvGetSize(src_image), IPL_DEPTH_8U, 3 );
	cvCvtPlaneToPix( dst_blue, dst_green, dst_red, NULL, dst_image ); 

	// 결과 출력
	char *src_title = "원 영상";
	cvNamedWindow( src_title, CV_WINDOW_AUTOSIZE );
	cvShowImage( src_title, src_image );

	char *dst_title = "cvFilter2D() 수행 영상";
	cvNamedWindow( dst_title, CV_WINDOW_AUTOSIZE );
	cvShowImage( dst_title, dst_image );

	// 키보드 입력을 기다린다.
	cvWaitKey(0);

	// 해제
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

/* --- TIP : 행렬 동적 초기화 (Dynamic allocated to CvMat) ----
	//
	// cvCreateMat() 함수로 생성한 cvMat을 사용하고 싶으면 아래와 같이 수행한다.
	// 즉, CvMat *kernel = cvCreateMat( 3, 3, CV_32FC1 );
	//     cvReleaseMat( &kernel );
	//
	// 예제 코드  

    ..(중략)...
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

    ...(중략)...

	cvReleaseMat( &kernel );
*/
}


void directAccessPixel()
{
	int i, j;
	BYTE r, g, b, var; // BYTE는 unsigned char의 다른 표현이다. (0~255의 범위 가짐)
					   // 참고로 영상 데이터는 0~255까지의 값을 가지므로, 
					   // 이에 대응하는 자료형인 BYTE로 선언하는 것이다.

	// 파일 대화상자에서 영상 파일을 선택한다.
	char *readFileName = getFileDialog();
	if( !readFileName ) return;

	// 영상을 읽는다. 
	IplImage *src_image = cvLoadImage( readFileName, CV_LOAD_IMAGE_COLOR );

	// 명암도 영상
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
	// 결과 출력
	char *title = "명암도 영상";
	cvNamedWindow( title, CV_WINDOW_AUTOSIZE );
	cvShowImage( title, dst_image );

	// 키보드 입력을 기다린다.
	cvWaitKey(0);

	// 해제
	cvReleaseImage( &src_image );
	cvReleaseImage( &dst_image );
	cvDestroyWindow( title );
}

void funcAccessPixel()
{
	int i, j;
	double r, g, b, var;

	// 파일 대화상자에서 영상 파일을 선택한다.
	char *readFileName = getFileDialog();
	if( !readFileName ) return;

	// 영상을 읽는다. 
	IplImage *src_image = cvLoadImage( readFileName, CV_LOAD_IMAGE_COLOR );
	
	// 분할한다.
	IplImage *src_red   = cvCreateImage( cvGetSize(src_image), IPL_DEPTH_8U, 1);
	IplImage *src_green = cvCreateImage( cvGetSize(src_image), IPL_DEPTH_8U, 1);
	IplImage *src_blue  = cvCreateImage( cvGetSize(src_image), IPL_DEPTH_8U, 1);
	
	// RGB 컬러공간을 Red, Green, Blue 채널로 분리한다.
	cvCvtPixToPlane( src_image, src_blue, src_green, src_red, NULL );

	// 명암도 영상
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

	// 결과 출력
	char *title = "명암도 영상";
	cvNamedWindow( title, CV_WINDOW_AUTOSIZE );
	cvShowImage( title, dst_image );

	// 키보드 입력을 기다린다.
	cvWaitKey(0);

	// 해제
	cvReleaseImage( &src_image );
	cvReleaseImage( &src_red); 
	cvReleaseImage( &src_green); 
	cvReleaseImage( &src_blue); 
	cvReleaseImage( &dst_image );
	cvDestroyWindow( title );
}


// 영상 입출력 관련 함수 사용 예제
void allImageFuncUsage() 
{
	char *saveFileName = "c:\\save_image.jpg";

	// 파일 대화상자에서 영상 파일을 선택한다.
	char *readFileName = getFileDialog();
	if( !readFileName ) return;

	// 영상을 읽는다. 
	IplImage *image = cvLoadImage( readFileName, CV_LOAD_IMAGE_UNCHANGED );
	
	// 캡션이 title인 창을 생성
	char *title = "영상";
	cvNamedWindow( title, CV_WINDOW_AUTOSIZE ); 

	// 영상을 창에 보여준다.
	cvShowImage( title, image );

	// 창 크기를 조절한다.
	cvResizeWindow( title, image->width, image->height );

	// 창을 이동한다.
	cvMoveWindow( title, 100, 100 );

	// 영상 데이터를 생성한다.
	CvSize size = cvSize( image->width, image->height );
	IplImage *create_image = cvCreateImage( size, IPL_DEPTH_8U, 3 );

	// 영상 데이타를 복제한 후, 저장한다.
	IplImage *clone_image = cvCloneImage( image );
	cvSaveImage( saveFileName, clone_image );

	// 저장한 파일을 다시 불러들인다.
	char *save_title = "저장한 영상";
	IplImage *save_image = cvLoadImage( saveFileName, CV_LOAD_IMAGE_UNCHANGED );
	cvNamedWindow( save_title, CV_WINDOW_AUTOSIZE );
	cvShowImage( save_title, save_image );

	// 키보드 입력을 기다린다.
	cvWaitKey(0);

	// 할당된 리소스를 해제하고 창을 파괴한다.
	cvReleaseImage( &image );
	cvReleaseImage( &create_image );
	cvReleaseImage( &clone_image );
	cvReleaseImage( &save_image );

	// 열려 있는 창을 모두 파괴한다.
	cvDestroyAllWindows(); 

	// cvDestroyAllWindows() 대신 아래와 같이 하여도 동일하다.
	// cvDestroyWindow( title ); 
	// cvDestroyWindow( save_title ); 

	return;
}

// OpenCV 버전 확인
void verifyVersion()
{
	const char *opencv_liberies = 0;
	const char *addon_modules = 0;
	cvGetModuleInfo( 0, &opencv_liberies, &addon_modules );
	printf( "* OpenCV : %s \n* Add-on Modules : %s \n",
			opencv_liberies, addon_modules);

	return;
}

// 영상 보기
void imageViewer()
{
	IplImage *color_image;
	IplImage *gray_image;

	// STEP 1 : 영상 파일 선택
	char *readFileName = getFileDialog();
	if( !readFileName ) return;

	// STEP 2 : 컬러 영상을 읽는다.
	color_image = cvLoadImage( readFileName, CV_LOAD_IMAGE_COLOR );
	
	// STEP 3 : 읽기 성공이면
	if( color_image != 0 )
	{
		// 변환 결과를 담을 명암도 영상을 초기화 한다.
 		gray_image = cvCreateImage( cvGetSize(color_image), IPL_DEPTH_8U, 1 ); 

		// 컬러 영상을 명암도 영상으로 변환한다.
		cvCvtColor( color_image, gray_image, CV_BGR2GRAY );
		
		char *title = "First Image Viewer using OpenCV";

		// 캡션 제목이 title을 갖는 창을 생성
		cvNamedWindow( title, CV_WINDOW_AUTOSIZE ); 
		
		// 생성된 창에 image 객체를 뿌려준다.
		cvShowImage( title, gray_image );

		// 키보드 입력을 기다린다.
		cvWaitKey(0);
	
		// 할당된 리소스를 해제한다.
		cvReleaseImage( &color_image );
		cvReleaseImage( &gray_image );

		// 창을 닫는다.
		cvDestroyWindow( title );       
	}
	else
	{
		printf("[ERROR] 영상 파일을 읽어올 수 없습니다.\n");
	}

	return;	
}

// 파일 대화상자에서 갖고 온다.
char *getFileDialog()
{
	char *readFileName = (char *)NULL;

	// 파일 포맷
	char szFilter[] = "지원 영상 파일(*.bmp, *.jpg, *.gif, *.png, *.tif) \
						|*.bmp;*.jpg;*.gif;*.png;*.tif||";

	printf("\n");
	printf("\t * 파일 대화상자를 이용하여 영상 파일을 선택하십시오. \n\n");
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