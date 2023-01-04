/*********************************************************
				Heisanbug OpenCV Test
				2020.07.04
				Mat 함수를 이용한 이미지 불러오고 출력하기
				Alta software developer
**********************************************************/

//C++ header file 
#include <iostream>

//opencv header file include
#include "opencv2/highgui.hpp"
#include "opencv2/core.hpp"


#define IMAGE_PATH "opencv_test_image.jpg"
#define COLOR_IMAGE_WINDOW_NAME "color image"
#define GRAY_IMAGE_WINDOW_NAME "gray image"

//project main function
int main(int argc, char** argv) {
	
	//OpenCV Mat class
	cv::Mat imageColor;
	cv::Mat imageGray;

	//경로의 이미지를 image 변수에 읽어옵니다.
	//imread flag 값에 따라 color 이미지 혹은 
	//gray scale 이미지를 불러옵니다.
	imageColor = cv::imread(IMAGE_PATH, cv::IMREAD_COLOR);
	imageGray = cv::imread(IMAGE_PATH, cv::IMREAD_GRAYSCALE);

	//이미지를 정상적으로 읽어왔는지 확인
	if (imageColor.empty() || imageGray.empty()){
		std::cout << IMAGE_PATH 
			<<" 이미지를 불러오는 데 문제가 생겼습니다." << std::endl;
		return -1;
	}

	//이미지를 window를 생성하여 보여줍니다.
	cv::namedWindow(COLOR_IMAGE_WINDOW_NAME, cv::WINDOW_NORMAL);
	cv::namedWindow(COLOR_IMAGE_WINDOW_NAME, cv::WINDOW_AUTOSIZE);
	cv::imshow(COLOR_IMAGE_WINDOW_NAME, imageColor);
	cv::imshow(GRAY_IMAGE_WINDOW_NAME, imageGray);

	//키 입력이 있을 때 까지 기다립니다.
	cv::waitKey(0);

	//생성하였던 윈도우를 제거합니다.
	cv::destroyWindow(COLOR_IMAGE_WINDOW_NAME);
	cv::destroyWindow(GRAY_IMAGE_WINDOW_NAME);

	//아래의 함수를 사용하면, 사용하고 있던 윈도우 전부를 제거합니다.
	//cv::destroyAllWindows();

	return 0;
}

/*
version 1

#include "opencv2\highgui\highgui.hpp"
#include "opencv2\core\core.hpp"

#pragma comment(lib,"opencv_highgui248d.lib")
#pragma comment(lib,"opencv_core248d.lib")


using namespace cv;

 

int main()
{
// 이미지 불러오기
Mat image = imread("조석.jpg", 1);

// 이미지 출력하기
imshow("Window", image);

waitKey(0);

 

// 이미지 저장하기
imwrite("copy.jpg", image);

return 0;
}

 

version 2

 

#include "opencv\cv.h"
#include "opencv\highgui.h"

int main()
{
// 이미지 불러오기
IplImage* image = cvLoadImage("조석.jpg", 1);

// 창 만들기
cvNamedWindow("window");

// 이미지 출력하기
cvShowImage("window", image);
cvWaitKey(0);

// 이미지 저장하기
cvSaveImage("복사.jpg", image);

// 해제
cvDestroyWindow("window");
cvReleaseImage(&image);

return 0;
}*/

/*
#include <opencv2/core.hpp>
#include <opencv2/imgcodecs.hpp>
#include <opencv2/highgui.hpp>
#include <opencv2/opencv.hpp>
 
#include <iostream>
#include <string>
 
using namespace cv;
using namespace std;
 
int main()
{
    String filepath("C:\\Users\\Public\\Pictures\\Sample Pictures\\sample.jpg");
    Mat ori_image = imread(filepath, IMREAD_COLOR);
 
    if (ori_image.empty())                      
    {
        cout << "이미지가 없거나, 유효한 파일 형식이 아닙니다." << std::endl;
        return -1;
    }
    
    Mat convert_image;
    cvtColor(ori_image, convert_image, COLOR_BGR2GRAY);
 
    imwrite("C:\\Users\\Public\\Pictures\\Sample Pictures\\sample_convert.jpg", convert_image);
 
    imshow("Original Image", ori_image);
    imshow("Convert image", convert_image);
    
    waitKey(0);
    return 0;
}
Colored by Color Scripter
cs
*/