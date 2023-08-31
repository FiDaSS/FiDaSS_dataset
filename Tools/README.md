## FiDaSS' Creation Tools

This directory contains the tools used to create our dataset.

It is important to note that we always process the data as videos first before processing more specific details.
This guarantees, for example, that data from the same video does not end up in different data splits.

## Tools' Usage

#### Processing a dataset as individual frames

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
python frameAnnot.py --input_path relative/path/to/frames \
                     --output_path relative/path/for/saving/annotations \
                     --classes path/to/file/containing/class/names \
                     --idx path/to/tmpfile.idx \
                     --checkpoint path/to/tmpfile.ckpt
```

#### Processing a dataset as clips

- Create/Edit clips

```sh
python clipLabels.py --save_path relative/path/for/saving/annotations
```

- Organize videos into folders of frames

```sh
python vid2frames.py  --videos_folder relative/path/to/videos \
                      --frames_path relative/path/for/saving/frames/to \
                      --clips_folder relative/path/to/clips/labels \
                      --framerate \#framerate to extract \
                      --extensions list of allowed extensions
```

- Annotate videos

```sh
python vidAnnot.py  --videos_folder relative/path/to/videos/frame/folders \
                    --output_path relative/path/for/saving/annotations \
                    --classes path/to/file/containing/class/names
```


#### Extend video annotations

- Setup PyTracking repository
- Run the script
```sh
python tracker.py   --videos_folder relative/path/to/videos/frame/folders \
                    --annots_path relative/path/to/annotations \
                    --classes path/to/file/containing/class/names
```
- The output can then be loaded back by the `vidAnnot` tool


#### Anonymize data

- Setup FacesDetection repository
- Run the script
```sh
python facesDet.py  --videos_folder relative/path/to/videos/frame/folders \
                    --annots_path relative/path/to/annotations \
                    --human_classes ids of classes containing humans
```
- Verify and correct miss-detections using the `vidAnnnot` tool
- Apply the blur
```sh
python blurFaces.py --videos_folder relative/path/to/videos/frame/folders \
                    --annots_path relative/path/to/annotations
```
