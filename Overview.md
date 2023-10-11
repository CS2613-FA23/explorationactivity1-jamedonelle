# OpenCV

I decided to do my first exploration project on OpenCV. OpenCV piqued my interest since I saw that we use this library at my work, but I've never gone in-depth on any of its implementations. I think computer vision tied with machine learning is one of the most important artificial intelligence problems we now face since we now have very sophisticated text-based AI, but not as sophisticated AI with computer vision capabilities.

## About

OpenCV is a open-source computer vision and machine learning software library.[1] OpenCV is mainly used to provide a common infrastructure for computer vision applications and to help facilitate the use of machine perception in commercial uses.[1]

This library has over 2000 different computer vision algorithms with many different applications. The main application I used in my sample program is facial recognition, but OpenCV also has algorithms to identify objects, classify human actions in videos, track camera movements, track moving objects, extract 3D models of objects, produce 3D point clouds from stereo cameras, and many more.

## Functionality

```
cv2.imshow("My Face Detection Project", video_frame) 
```
Above you will find the imshow function used in my sample program. This function takes in a string and a video frame in the form of a pixel numpy array. This will open a window shoowing the frame with the title above.

```
cv2.imread("cowboy_hat.png", cv2.IMREAD_UNCHANGED)
```

The Above function reads an image and turns it into a pixel numpy array. This is mainly used so that we can make changes to the image systematically. In my sample program, I used this to retrieve the image of a hat and inject the image into the frame read through the face cam.

## History

OpenCV was created in 1999 by an initiative created by the Intel Corporation as an open-source project. The primary goal they wanted to achieve was to create a comprehensive computer vision library that could be used by researchers and developers to facilitate the creation of more computer vision applications.[2]

## Influence

Learning about this library has changed the way I thought about Python. I've always thought Python was very slow in terms of execution, coming from a C++ standpoint. Now I feel that python has a very high level efficiency for prototyping since script building is very easy to create and simple to read.

## Experience

I would recommend this library in this language to a friend if they are prototyping a simple computer vision application. They must take into account python's performance, but overall this library has great ease of use. I will continue exploring this library in my type to see practice image processing and I'd love to learn more machine learning algorithms since I think machine learning will be the future for software development in the coming years.

## References

[1] https://opencv.org/about/

[2] https://ts2.space/en/the-history-of-opencv-from-research-project-to-industry-standard/