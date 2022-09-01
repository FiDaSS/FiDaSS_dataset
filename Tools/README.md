## FiDaSS' Creation Tools

This directory contains the tools used to create our dataset.

- The data augmentation scripts we used were from this [github](https://github.com/Paperspace/DataAugmentationForObjectDetection).

## Tools' Usage

- Split a video dataset into individual frames

```sh
python extractFrames.py --videos_folder relative/path/to/videos \
                        --frames_path relative/path/for/saving/frames/to \
                        --skip \#ofConsecutiveFramesToSkip \
                        --extensions list of allowed extensions
```

- Navigate the extracted frames and choose a subset of them

```sh
python selectFrames.py --frames_path relative/path/to/read/frames \
                       --output_folder relative/path/to/save/frames \
                       --idx path/to/tmpfile.idx \
                       --checkpoint path/to/tmpfile.ckpt
```

- Create/Edit bounding boxes

```sh
python annotationTool.py --input_path relative/path/to/frames \
                         --output_path relative/path/for/saving/annotations \
                         --classes path/to/file/containing/class/names \
                         --idx path/to/tmpfile.idx \
                         --checkpoint path/to/tmpfile.ckpt
```
