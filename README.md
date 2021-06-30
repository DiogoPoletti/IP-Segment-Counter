
![Header Image](https://github.com/DiogoPoletti/IP-Segment-Counter/blob/main/Documentation/HeaderImage2.png)

# IP Segment Counter
## Description
This Python program helps to count and divide the segments of various IP addresses while counting how many characters are present in the IP address. This program was useful when studying networking and communications.

## Screenshot
![Game Running](https://github.com/DiogoPoletti/IP-Segment-Counter/blob/main/Documentation/IPSegmentAndCharCounter.gif)

## What have I learned
Creating this game enabled me to practice a few aspects:
* Implement Python program to improve effectiveness when studying.
* Get familiar with conditions and loops.

## Code highlight
This block of code was able to print the segment's counting and char counting even when there is no *.* at the end of the IP address, which is usually the format in which an IP address is written.
```
if character != '.':
    print("Segment {} has {} characters.".format(segmentCount, segmentCharacters))
```


> This is a companion project to Python 3.8 Full Stack Masterclass, check out the full course at www.udemy.com


![Footer Image](https://github.com/DiogoPoletti/IP-Segment-Counter/blob/main/Documentation/FooterImage.png)
