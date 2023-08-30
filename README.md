## FiDaSS Dataset

Dataset created for research "FiDaSS: A Benchmark Dataset for Firearm Threat Detection in Real-World Scenes".
The dataset is available on [Google Drive](https://bit.ly/3nLP8YG).

The videos gathered from YouTube to enrich our dataset are available on two playlists:
The [first](https://www.youtube.com/playlist?list=PLnq5fLsdu5RqPUGq3r4rgyY5m_pM9h3HB) containing 193 videos, and the
[second](https://www.youtube.com/playlist?list=PLnq5fLsdu5RrVUoLyilkkiL3bvTPr5-VK) containing 201 videos.

## Languages Included in our Dataset
Below we present a table with the most frequent languages in our dataset, except for english.
| Language   | #Videos |   | Language   | #Videos |   | Language | #Videos |
|------------|---------|---|------------|---------|---|----------|---------|
| Somali     | 22      |   | Hungarian  | 10      |   | Swahili  | 4       |
| Welsh      | 19      |   | Catalan    | 9       |   | Dutch    | 3       |
| Polish     | 18      |   | Afrikaans  | 7       |   | Spanish  | 3       |
| Croatian   | 15      |   | Danish     | 6       |   | German   | 3       |
| Albanian   | 11      |   | Swedish    | 6       |   | Romanian | 3       |
| Portuguese | 11      |   | Czech      | 6       |   | Finnish  | 3       |
| Slovenian  | 10      |   | Vietnamese | 5       |   | Others   | 10      |

## Sample Images from our Dataset

<img src="/DatasetSamples/sample00.jpg" width=200><img src="/DatasetSamples/sample01.jpg" width=200><img src="/DatasetSamples/sample02.jpg" width=200><img src="/DatasetSamples/sample03.jpg" width=200><br/>
<img src="/DatasetSamples/sample04.jpg" width=200><img src="/DatasetSamples/sample05.jpg" width=200><img src="/DatasetSamples/sample06.jpg" width=200><img src="/DatasetSamples/sample07.jpg" width=200><br/>
<img src="/DatasetSamples/sample08.jpg" width=200><img src="/DatasetSamples/sample09.jpg" width=200><img src="/DatasetSamples/sample10.jpg" width=200><img src="/DatasetSamples/sample11.jpg" width=200><br/>
<img src="/DatasetSamples/sample12.jpg" width=200><img src="/DatasetSamples/sample13.jpg" width=200><img src="/DatasetSamples/sample14.jpg" width=200><img src="/DatasetSamples/sample15.jpg" width=200><br/>

- The samples presented follow the color scheme: green for the "armed" label, blue for the "unarmed", and red for "gun".
- Although the images had varying dimensions, we standardized them to 768x480 pixels.
- Image annotations are available in the PASCAL VOC-YOLO format.

## Detections Demo

https://user-images.githubusercontent.com/101901295/187836784-5da3b2ce-613b-4431-bb49-cbf76c2365b6.mp4

## Other Repositories Used

- [FacesDetection](https://github.com/Tencent/FaceDetection-DSFD)

- [PyTracking](https://github.com/visionml/pytracking)
