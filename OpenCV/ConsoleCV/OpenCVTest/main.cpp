/*********************************************************
Heisanbug OpenCV Test
2020.07.04
Hello World
Alta software developer
**********************************************************/

#include "stdafx.h"
//#include "vld.h"

#include <string.h>

//opencv header file include
#include "opencv2/opencv.hpp"
#include "opencv2/videoio.hpp"
#include "opencv2/highgui/highgui.hpp"
#include "opencv2/core/types_c.h"

//CWinApp theApp;
using namespace std;


void verifyVersion();
//void imageViewer();
//char *getFileDialog();
//void allImageFuncUsage();
//void directAccessPixel();
//void funcAccessPixel();
//void matrixUsage();
//void testMatrixFunc();
//void printMatrix(CvMat *matrix);
//void testCvArr();
//void testMouseEvent();
//void mouseHandler(int event, int x, int y, int flags, void *param);
//void testTrackBarEvent();
//void trackbarHandler(int pos);
//void testWriterCamera();
void testViewFromCamera();
//char *getSaveAVIFromFileDialog();
//
//// cvcam
//void testViewFromCVCAM_1();
//void testViewFromCVCAM_2();
//void testViewFromCVCAM_3();
//void testViewFromCVCAM_two();


//project main function
int main(int argc, char** argv) 
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
		//verifyVersion();

		// ���� ����
		//imageViewer();

		// ���� ����� ���� �Լ� ��� ����
		//allImageFuncUsage();

		// ���� ����
		//directAccessPixel();

		// GetReal2D(), SetReal2D() �Լ��� ���
		//funcAccessPixel();

		// ��� �Լ� ��
		//testMatrixFunc();

		// ��� ��� + ���͸�
		//matrixUsage();

		// cvAdd() �Լ��� ���ڰ� CvArr�̸�, lplImage, CvMat ���� ���� Ȯ��
		//testCvArr();

		// ���콺 �ڵ鷯
		//testMouseEvent();

		// Ʈ���� �ڵ鷯
		//testTrackBarEvent();

		// ī�޶󿡼� �Է� �޾Ƽ� �����ֱ�
		testViewFromCamera();

		// ī�޶󿡼� �Է� ���� �������� AVI�� �����ϱ�
		//testWriterCamera();

		// cvcam �׽�Ʈ 1
		//testViewFromCVCAM_1();

		// cvcam �׽�Ʈ 2
		//testViewFromCVCAM_2();

		// cvcam �׽�Ʈ 3
		//testViewFromCVCAM_3();

		// ī�޶� 2�� �϶��� cvcam �׽�Ʈ
		//testViewFromCVCAM_two();


		// Ű���� �Է��� ��ٸ���.
		getchar();
	}

	return nRetCode;


/*
	//create image window
	cv::namedWindow("image", 1);

	//create test Mat, 400 x 400
	cv::Mat testMat = cv::Mat::zeros(200, 850, CV_8UC3);

	//write text
	cv::putText(testMat, "HELLO WORLD!! HEISANBUG", cvPoint(100, 100),
		cv::FONT_HERSHEY_PLAIN, 3, cvScalar(0, 255, 255), 4);

	//show image
	cv::imshow("image", testMat);
	cv::waitKey(0);

	//close all windows
	cv::destroyAllWindows();

	return 0;
*/
}


// OpenCV ���� Ȯ��
void verifyVersion()
{
	//const char *opencv_liberies = 0;
	//const char *addon_modules = 0;
	//cvGetModuleInfo(0, &opencv_liberies, &addon_modules);
	//printf("* OpenCV : %s \n* Add-on Modules : %s \n",
	//	opencv_liberies, addon_modules);
	//printf("* OpenCV : %s \n* Add-on Modules : %s \n",
	//	opencv_liberies, addon_modules);

	string sVersion = cv::getVersionString();	
	printf("* OpenCV version : %s \n", sVersion.c_str());	

	return;
}

// ī�޶󿡼� �Է� �޾Ƽ� �����ֱ�
void testViewFromCamera()
{
	cv::Mat frame;
	//--- INITIALIZE VIDEOCAPTURE
	cv::VideoCapture cap;
	// open the default camera using default API
	// cap.open(0);
	// OR advance usage: select any API backend
	int deviceID = 0;             // 0 = open default camera
	int apiID = cv::CAP_ANY;      // 0 = autodetect default API
								  // open selected camera using selected API
	cap.open(deviceID, apiID);
	// check if we succeeded
	if (!cap.isOpened()) {
		cerr << "ERROR! Unable to open camera\n";
		return;
	}
	//--- GRAB AND WRITE LOOP
	cout << "Start grabbing" << endl
		<< "Press any key to terminate" << endl;
	for (;;)
	{
		// wait for a new frame from camera and store it into 'frame'
		cap.read(frame);
		// check if we succeeded
		if (frame.empty()) {
			cerr << "ERROR! blank frame grabbed\n";
			break;
		}
		// show live and wait for a key with timeout long enough to show images
		imshow("Live", frame);
		if (cv::waitKey(5) >= 0)
			break;
	}
	// the camera will be deinitialized automatically in VideoCapture destructor
}
