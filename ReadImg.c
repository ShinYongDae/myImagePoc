/*********************************************************
				Heisanbug OpenCV Test
				2020.07.04
				Mat �Լ��� �̿��� �̹��� �ҷ����� ����ϱ�
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

	//����� �̹����� image ������ �о�ɴϴ�.
	//imread flag ���� ���� color �̹��� Ȥ�� 
	//gray scale �̹����� �ҷ��ɴϴ�.
	imageColor = cv::imread(IMAGE_PATH, cv::IMREAD_COLOR);
	imageGray = cv::imread(IMAGE_PATH, cv::IMREAD_GRAYSCALE);

	//�̹����� ���������� �о�Դ��� Ȯ��
	if (imageColor.empty() || imageGray.empty()){
		std::cout << IMAGE_PATH 
			<<" �̹����� �ҷ����� �� ������ ������ϴ�." << std::endl;
		return -1;
	}

	//�̹����� window�� �����Ͽ� �����ݴϴ�.
	cv::namedWindow(COLOR_IMAGE_WINDOW_NAME, cv::WINDOW_NORMAL);
	cv::namedWindow(COLOR_IMAGE_WINDOW_NAME, cv::WINDOW_AUTOSIZE);
	cv::imshow(COLOR_IMAGE_WINDOW_NAME, imageColor);
	cv::imshow(GRAY_IMAGE_WINDOW_NAME, imageGray);

	//Ű �Է��� ���� �� ���� ��ٸ��ϴ�.
	cv::waitKey(0);

	//�����Ͽ��� �����츦 �����մϴ�.
	cv::destroyWindow(COLOR_IMAGE_WINDOW_NAME);
	cv::destroyWindow(GRAY_IMAGE_WINDOW_NAME);

	//�Ʒ��� �Լ��� ����ϸ�, ����ϰ� �ִ� ������ ���θ� �����մϴ�.
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
// �̹��� �ҷ�����
Mat image = imread("����.jpg", 1);

// �̹��� ����ϱ�
imshow("Window", image);

waitKey(0);

 

// �̹��� �����ϱ�
imwrite("copy.jpg", image);

return 0;
}

 

version 2

 

#include "opencv\cv.h"
#include "opencv\highgui.h"

int main()
{
// �̹��� �ҷ�����
IplImage* image = cvLoadImage("����.jpg", 1);

// â �����
cvNamedWindow("window");

// �̹��� ����ϱ�
cvShowImage("window", image);
cvWaitKey(0);

// �̹��� �����ϱ�
cvSaveImage("����.jpg", image);

// ����
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
        cout << "�̹����� ���ų�, ��ȿ�� ���� ������ �ƴմϴ�." << std::endl;
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