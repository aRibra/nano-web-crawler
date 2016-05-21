#include <opencv2/highgui/highgui.hpp>
#include <opencv2/core/core.hpp>
#include "opencv2/opencv.hpp"
#include <opencv/cv.h>
#include <string>
#include <iostream>
#include "boost/filesystem.hpp"

using namespace cv;
using namespace std;
using namespace boost::filesystem;

void getFrames(string videoFileName);
string pathToSafePlace = "/home/Geany-c++/captured-frames/";

int main() {

	string pathToVideos = "/home/python_workspace/retrieved_videos";
	string videoFolders[] = { "bear", "bird", "eagle", "flower", "kangaroo",
			"snake" };

	boost::filesystem::recursive_directory_iterator itr(pathToVideos);
	while (itr != boost::filesystem::recursive_directory_iterator()) {
		string fileName = itr->path().string();
		if (extension(fileName) == ".3gp") {
			cout << "Getting frames for: " << fileName << endl;
			getFrames(fileName);
		}
		itr++;
	}

	return 0;
}

void getFrames(string videoFileName) {

	cv::VideoCapture cap(videoFileName);
	cv::Mat frame;

	int numberOfFrames = cap.get(CV_CAP_PROP_FRAME_COUNT);
	cout << "Number of Frames: " << numberOfFrames << endl;

	if (!cap.isOpened())
		cout << "No Video Detected";
	else {
		for (int i = 1000;
				cap.get(CV_CAP_PROP_POS_FRAMES)
						< cap.get(CV_CAP_PROP_FRAME_COUNT); i += 10000) {
			cap.set(CV_CAP_PROP_POS_MSEC, i);
			cout << "Frame to be captured:" << cap.get(CV_CAP_PROP_POS_FRAMES)
					<< endl;
			cout << "timestamp (sec): " << cap.get(CV_CAP_PROP_POS_MSEC) / 1000
					<< endl;
			std::ostringstream frameNumber;
			frameNumber << cap.get(CV_CAP_PROP_POS_FRAMES);
			cap >> frame; // get a new frame from video

			cv::namedWindow("Video To be Captured", CV_WINDOW_AUTOSIZE);

			if (!frame.empty()) {
				cv::imshow("Video To be Captured", frame);
				cv::imwrite(pathToSafePlace + frameNumber.str() + ".jpg",
						frame);
				if (cv::waitKey(30) >= 0)
					break;
			} else
				break;

		}
	}

}

