## Experimental Results

We used FiDaSS to train five general-purpose state-of-the-art models: YOLOv8, DAFNe, Faster-RCNN, YOLOV, and TransVOD. 

<table class="tg">
<thead>
  <tr>
    <th class="tg-c3ow" rowspan="2">Model</th>
    <th class="tg-c3ow" rowspan="2">Input</th>
    <th class="tg-c3ow" rowspan="2">Backbone</th>
    <th class="tg-c3ow" rowspan="2">mAP50</th>
    <th class="tg-c3ow" colspan="3">AP50</th>
    <th class="tg-c3ow" rowspan="2">#Params</th>
  </tr>
  <tr>
    <th class="tg-c3ow">Arned</th>
    <th class="tg-c3ow">Unarmed</th>
    <th class="tg-c3ow">Firearm</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky">DAFNe</td>
    <td class="tg-0pky">Frames</td>
    <td class="tg-0pky">ResNet-101</td>
    <td class="tg-0pky">34.00%</td>
    <td class="tg-0pky">50.07%</td>
    <td class="tg-0pky">39.83%</td>
    <td class="tg-0pky">12.11%</td>
    <td class="tg-0pky">5M</td>
  </tr>
  <tr>
    <td class="tg-0pky">Faster-RCNN</td>
    <td class="tg-0pky">Frames</td>
    <td class="tg-0pky">ResNet-50</td>
    <td class="tg-0pky">40.65%</td>
    <td class="tg-0pky">45.69%</td>
    <td class="tg-0pky">48.83%</td>
    <td class="tg-0pky">27.42%</td>
    <td class="tg-0pky">42M</td>
  </tr>
  <tr>
    <td class="tg-0pky">YOLOv10</td>
    <td class="tg-0pky">Frames</td>
    <td class="tg-0pky">CSPDarknet-53</td>
    <td class="tg-0pky">44.30%</td>
    <td class="tg-0pky">56.10%</td>
    <td class="tg-0pky">40.50%</td>
    <td class="tg-0pky">36.10%</td>
    <td class="tg-0pky">24M</td>
  </tr>
  <tr>
    <td class="tg-0pky">DINO</td>
    <td class="tg-0pky">Frames</td>
    <td class="tg-0pky">ResNet-50</td>
    <td class="tg-0pky">60.60%</td>
    <td class="tg-0pky">71.30%</td>
    <td class="tg-0pky">66.09%</td>
    <td class="tg-0pky">44.35%</td>
    <td class="tg-0pky">47M</td>
  </tr>
  <tr>
    <td class="tg-0pky">EVA-02</td>
    <td class="tg-0pky">Frames</td>
    <td class="tg-0pky">ResNet-50</td>
    <td class="tg-0pky">72.07%</td>
    <td class="tg-0pky">86.47%</td>
    <td class="tg-0pky">75.48%</td>
    <td class="tg-0pky">54.27%</td>
    <td class="tg-0pky">86M</td>
  </tr>
  <tr>
    <td class="tg-0pky">TransVOD</td>
    <td class="tg-0pky">Clips</td>
    <td class="tg-0pky">ResNet-50</td>
    <td class="tg-0pky">45.00%</td>
    <td class="tg-0pky">57.11%</td>
    <td class="tg-0pky">50.62%</td>
    <td class="tg-0pky">54.27%</td>
    <td class="tg-0pky">59M</td>
  </tr>
</tbody>
</table>

### Configurations

#### DAFNe
- Pretrained model: ResNet50 on ImageNet
- Base LR: 0.0001
- Steps: 60000
- Image Size: 600
- Batch Size: 24

#### Faster-RCNN
- Pretrained model: Faster-RCNN50 on ImageNet
- Base LR: 0.001
- Steps: 15000
- Image Size: 512
- Batch Size: 6

#### YOLOv10
- Pretrained model: YOLOv10-Large on ImageNet
- Optimizer: AdamW
- Base LR: 0.001
- Epochs: 2000
- Image Size: 640
- Batch Size: 16

#### DINO
- Pretrained model: DINO-4Scale on COCO
- Base LR: 0.0001
- Epoch: 40
- Image Size: 1024
- Batch Size: 2

#### EVA-02
- Pretrained model: EVA02 BSL on COCO
- Optimizer: AdamW
- Base LR: 5e-7
- Steps: 10000
- Image Size: 1024
- Batch Size: 2

#### TransVOD
- Pretrained model: ResNet50 on ImageNet
- Base LR: 0.0001
- Steps: 100000
- Image Size: 512
- Batch Size: 24
