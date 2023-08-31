## Experimental Results

We used FiDaSS to train five general-purpose state-of-the-art models: YOLOv8, DAFNe, Faster-RCNN, YOLOV, and TransVOD. 

<table class="tg">
<thead>
  <tr>
    <th class="tg-c3ow" rowspan="2">Model</th>
    <th class="tg-c3ow" rowspan="2">Scope</th>
    <th class="tg-c3ow" rowspan="2">mAP50</th>
    <th class="tg-c3ow" colspan="3">AP50</th>
  </tr>
  <tr>
    <th class="tg-c3ow">Arned</th>
    <th class="tg-c3ow">Unarmed</th>
    <th class="tg-c3ow">Firearm</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky">YOLOv8</td>
    <td class="tg-0pky">Frames</td>
    <td class="tg-0pky">39.70%</td>
    <td class="tg-0pky">55.50%</td>
    <td class="tg-0pky">37.60%</td>
    <td class="tg-0pky">26.00%</td>
  </tr>
  <tr>
    <td class="tg-0pky">DAFNe</td>
    <td class="tg-zahu">Frames</td>
    <td class="tg-0pky">34.00%</td>
    <td class="tg-0pky">50.07%</td>
    <td class="tg-0pky">39.83%</td>
    <td class="tg-0pky">12.11%</td>
  </tr>
  <tr>
    <td class="tg-0pky">Faster-RCNN</td>
    <td class="tg-zahu">Frames</td>
    <td class="tg-0pky">40.65%</td>
    <td class="tg-0pky">45.69%</td>
    <td class="tg-0pky">48.83%</td>
    <td class="tg-0pky">27.42%</td>
  </tr>
</tbody>
</table>

<table class="tg">
<thead>
  <tr>
    <th class="tg-c3ow">Model</th>
    <th class="tg-c3ow">Scope</th>
    <th class="tg-c3ow">mAP50</th>
    <th class="tg-c3ow">mAP50:95</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky">YOLOv8</td>
    <td class="tg-0pky">Frames</td>
    <td class="tg-0pky">33.60%</td>
    <td class="tg-0pky">13.90%</td>
  </tr>
  <tr>
    <td class="tg-0pky">DAFNe</td>
    <td class="tg-zahu">Frames</td>
    <td class="tg-0pky">50.50%</td>
    <td class="tg-0pky">22.00%</td>
  </tr>
</tbody>
</table>

### Configurations

#### YOLOv8
- Pretrained model: YOLOv8-Large on ImageNet
- Optimizer: AdamW
- Epochs: 1000
- Image Size: 512
- Batch Size: 16


#### Faster-RCNN
- Pretrained model: Faster-RCNN50 on ImageNet
- Base LR: 0.001
- Steps: 15000
- Image Size: 512
- Batch Size: 6

#### DAFNe

#### YOLOV

#### TransVOD
