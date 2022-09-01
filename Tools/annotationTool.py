import shutil as sh
import pickle
import cv2
import os


KEYS = {
	'tab'       : 9,
	'shift+tab' : 11,
	'esc'       : 27,
	"'"         : 39
}


OBJ_DIR  = 'objs'
FACE_DIR = 'faces'



points = []
drawing = False
done = False
moving = False

disp_size = (960,480)

def draw(rect, x=None, y=None):
	image = img.copy()
	if rect:
		cv2.rectangle(image, points[0], points[1], (0, 255, 0), 2)
	else:
		cv2.line(image, (0, y), (disp_size[0], y), (100, 100, 100), 1)
		cv2.line(image, (x, 0), (x, disp_size[1]), (100, 100, 100), 1)

	cv2.imshow('img', image)

def drag(event, x, y, flags, param):
	global points, drawing, done, moving

	if event == cv2.EVENT_LBUTTONDOWN:
		points = [(x, y),(x, y)]
		drawing = True
		done = False

	if event == 0 and not done and not drawing: ## show perpendicular lines
		draw(False, x, y)

	if event == 0 and drawing: ## dragging the mouse
		points[-1] = (x, y)

	if event == 0 and moving and len(points): ## dragging the box
		w, h = [abs(points[0][i]-points[1][i]) for i in range(2)]
		hw = int(w/2)
		hh = int(h/2)

		tmp = [(x+hw, y+hh), (x-hw, y-hh)]

		points = tmp[:]
		draw(True)


	if event == 3: ## middle click (down) -> move the box
		moving = True

	if drawing:
		draw(True)

	if event == 6: ## middle click (up) -> move the box
		moving = False

	if event == cv2.EVENT_LBUTTONUP:
		drawing = False
		done = True



def convert(size, box):
	global points
	check_x = lambda x : max(0, min(size[0], x))
	check_y = lambda y : max(0, min(size[1], y))

	newbox = [
		check_x(box[0]),
		check_y(box[1]),
		check_x(box[2]),
		check_y(box[3]),
	]

	points = [(newbox[0], newbox[1]), (newbox[2], newbox[3])]
	draw(True)

	dw = 1./size[0]
	dh = 1./size[1]
	x = (newbox[0] + newbox[2])/2.0
	y = (newbox[1] + newbox[3])/2.0
	w = newbox[2] - newbox[0]
	h = newbox[3] - newbox[1]
	x = abs(x*dw)
	w = abs(w*dw)
	y = abs(y*dh)
	h = abs(h*dh)

	return [x,y,w,h]



def mkCheckpointFile(checkpointFile, idxFile, inputFolder):
	frames = os.listdir(inputFolder)

	def order(x):
		if '_' not in x:
			name, idx = x.split(' (')
			idx = int(idx.split(')')[0])
			return name, idx

		slots = x.split('_')
		slots[-1] = slots[-1].split('.')[0]

		if slots[-2].isdigit():
			key = int("{0:03d}{1:06d}".format((int(slots[-2])+1),(int(slots[-1])+1)))
			last = -2
		else:
			key = int(''.join([x for x in slots[-1] if x.isdigit()]))
			last = -1

		return '_'.join(slots[:last]), key

	frames = sorted(frames, key = order)
	with open(checkpointFile, 'wb') as outfile:
		pickle.dump(frames, outfile)

	with open(idxFile, 'w') as outfile:
		outfile.write('0')

	return 0, frames



def loadCheckpoint(checkpointFile, idxFile):
	with open(idxFile, 'r') as infile:
		idx = int(infile.read())

	with open(checkpointFile, 'rb') as infile:
		frames = pickle.load(infile)

	return idx, frames



def convertBack(size, bbox):
	check_x = lambda x : int(max(0, min(size[0], x)))
	check_y = lambda y : int(max(0, min(size[1], y)))

	cs, cx, cy, w, h = [float(v) for v in bbox]

	dw = size[0]
	dh = size[1]
	x = abs(cx*dw)
	y = abs(cy*dh)
	hw = abs(w*dw)/2
	hh = abs(h*dh)/2

	x1 = x-hw
	x2 = x+hw
	y1 = y-hh
	y2 = y+hh

	newbox = [
		check_x(x1),
		check_y(y1),
		check_x(x2),
		check_y(y2),
	]
	return newbox



def loadAnnots(yolo_lines):
	bxs = []
	for line in yolo_lines:
		if not len(line): continue
		bxs.append(line.split(' '))
	return bxs


def main(inputFolder, outputFolder, checkpointFile, idxFile, classes):
	class_id  = 0
	cName = lambda n : classes[n] if n!=-1 else "face"
	
	OBJ_PATH  = os.path.join(outputFolder,  OBJ_DIR)
	FACE_PATH = os.path.join(outputFolder, FACE_DIR)

	for path in [outputFolder, OBJ_PATH, FACE_PATH]:
		if not os.path.exists(path):
			os.mkdir(path)

	global img, done, points, cur_name

	if os.path.exists(idxFile) and os.path.exists(checkpointFile):
		foo  = loadCheckpoint
		args = ()
	else:
		foo  = mkCheckpointFile
		args = (inputFolder, )

	idx, frames = foo(checkpointFile, idxFile, *args)

	cv2.namedWindow("img")
	cv2.namedWindow("display")

	cv2.setMouseCallback("img", drag)
	cv2.setMouseCallback("display", drag)

	###TODO:: BETTER WINDOW POSITIONING
	cv2.moveWindow("img", 400, 150)
	cv2.moveWindow("display", 400+disp_size[0], 150)

	amt = len(frames)

	last_key = None
	momentum = 0

	boxes = []
	faces = []

	alist = boxes
	key   = None

	line = ''

	cur_box  = None
	loaded   = False
	saved    = []

	cv2.setWindowTitle('img', 'Current Class: {}'.format(cName(class_id)))
	cv2.setWindowTitle('display', "Current Annots")


	while True:
		img = cv2.imread(os.path.join(inputFolder, frames[idx]))
		img = cv2.resize(img, disp_size)

		name = os.path.splitext(frames[idx])[0]

		if key != ord('s'):
			cv2.imshow('img', img)

			if not loaded:
				annotsfile = os.path.join( OBJ_PATH, name)+'.txt'
				facesfile  = os.path.join(FACE_PATH, name)+'.txt'
				
				loaded = True
				saved.clear()

				if os.path.exists(annotsfile):
					with open(annotsfile, 'r') as infile:
						boxes = loadAnnots(infile.read().split('\n'))
					saved  = boxes[:]

					if class_id != -1:
						alist = boxes


				if os.path.exists(facesfile):
					with open(facesfile, 'r') as infile:
						faces = loadAnnots(infile.read().split('\n'))
					saved = saved + faces

					if class_id == -1:
						alist = faces



		disp = img.copy()
		for i, bbox in enumerate(alist):
			x1,y1, x2,y2 = convertBack(disp_size, bbox)

			c = cName(int(bbox[0]))

			if cur_box == i:
				color = (255, 0, 0)
			else:
				color = (0, 255, 0)

			cv2.rectangle(disp, (x1, y1), (x2, y2), color, 3)
			cv2.putText(disp, c, (x1+5,y1+15), 0, .5, color, 2)

			if bbox not in saved:
				cv2.putText(disp, '*', (x2-15,y1+15), 0, .7, (0,0,255), 2)

		cv2.imshow('display', disp)


		print(' '*(len(line)+2*8), end='\r') ## Clears the last print (line lenght + 2* the tabs)
		line = '{1:06d}/{0:06d}\t\t{2}'.format(amt, idx+1, frames[idx])
		print(line, end='\r')

		key = cv2.waitKey(0) & 0xff

		# print()
		# print(key)
		# print()

		if key > ord('0') and key <= ord('9'): ## key in the interval (0, 9]
			class_id = key-ord('1')
			if class_id < len(classes):
				cv2.setWindowTitle('img', 'Current Class: {}'.format(cName(class_id)))
				alist = boxes

				if cur_box is not None and alist == boxes:
					boxes[cur_box][0] = str(class_id)

		if key == KEYS["'"]:
			class_id = -1
			cv2.setWindowTitle('img', 'Current Class: {}'.format(cName(class_id)))
			alist = faces

		if key == KEYS['esc']:
			cur_box = None

		if key == ord('e') and cur_box is not None:
			del alist[cur_box]
			if cur_box == len(alist):
				cur_box = None

		if key == KEYS['tab'] and len(alist):
			if cur_box is None:
				cur_box = 0
			elif cur_box+1 >= len(alist):
				cur_box = None
			else:
				cur_box+= 1

		if key == KEYS['shift+tab'] and len(alist):
			if cur_box is None:
				cur_box = len(alist)-1
			elif cur_box == 0:
				cur_box = None
			else:
				cur_box-= 1

		if key == ord('w'):
			name = os.path.splitext(frames[idx])[0]

			for path, obj in [(OBJ_PATH,boxes), (FACE_PATH,faces)]:
				with open(os.path.join(path, name)+'.txt', 'w') as outfile:
					outfile.write(
						'\n'.join(
							map(
								lambda x:
								' '.join(x),
								obj
							)
						)
					)
				# sh.copy(os.path.join(inputFolder,frames[idx]), os.path.join(OBJ_PATH, frames[idx]))


		if key in [ord('w'), ord('a'), ord('d')]: ## Movement keys
			boxes.clear()
			faces.clear()
			points.clear()
			done = False
			cur_box = None
			loaded = False


		# if key == ord('f'):
		# 	if cur_box is None:
		# 		cur_box = len(alist)-1
		# 	elif cur_box == 0:
		# 		cur_box = None
		# 	else:
		# 		cur_box-= 1

		# 	if cur_box is not None:
		# 		boxes[cur_box][0] = str(class_id)


		if key == ord('r'):
			img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
			cv2.imwrite(os.path.join(inputFolder, frames[idx]), img)

		if key == ord('s') and done:
			done = False
			box = list(points[0])+list(points[1])
			print (box)

			if cur_box is None:
				alist.append([str(x) for x in [class_id]+convert(disp_size, box)])
							##c, x, y, w, h
			else:
				alist[cur_box] = [str(x) for x in [class_id]+convert(disp_size, box)]
				cur_box = None

			points = []
			

		if key == last_key and (key == ord('a') or key == ord('d')):
			momentum = min(momentum+1,100)
			if   momentum >= 100: idx+=19*mod
			elif momentum >=  50: idx+=9*mod
			elif momentum >=  25: idx+=4*mod
		else:
			momentum = 0
			
		if key == ord('a'):
			idx = max(0, idx-1)
			mod = -1
		if key == ord('d') or key == ord('w'):
			idx = min(amt-1, idx+1)
			mod = 1
			
		if key == ord('q'):
			break
		last_key = key

	print()
	with open(idxFile, 'w') as outfile:
		outfile.write(str(idx))


if __name__ == "__main__":
	import argparse

	parser = argparse.ArgumentParser(description="Tool for annotating images with the specified labels."
		"\n\nUsage:"
		"\n\tLeft click + Drag -> Select area of interest"
		"\n\tMiddle click + Drag -> Move the bounding box"
		"\n\t['1'-'9'] keys -> Selects current class (according to order informed in the file)"
		"\n\t'\'' key -> Swaps to face annotations"
		"\n\t's' key -> Save current bounding box"
		"\n\t'w' key -> Write all saved bounding boxes for current image"
		"\n\t'r' key -> Inverts RGB to BGR color space"
		"\n\t'tab' and 'shift+tab' keys -> Move to previous/next registered bounding box"
		"\n\t'e' key -> Erases selected bounding box"
		"\n\t'esc' key -> Resets bounding box selection"
		"\n\t'a' and 'd' keys -> Move to previous/next image"
		"\n\t'q' key -> leave application"
		"\nMoving to a new image erases all saved bounding boxes",
		formatter_class=argparse.RawTextHelpFormatter
	)

	parser.add_argument('--input_path', type=str, required=True,
	            help='Relative path to the folder containing the images.')


	parser.add_argument('--output_path', type=str, required=True,
	            help='Relative path to the folder where the labels will be written.')


	parser.add_argument('--classes', type=str, required=True,
	            help='File where the class names are stored (one per line).')


	parser.add_argument('--idx', type=str, default='.idx.ckpt',
	            help='File to write the last file analyzed, for continued usage after closing the application.')


	parser.add_argument('--checkpoint', type=str, default='.checkpoint.ckpt',
	            help='File to write the checkpoint list, for continued usage after closing the application.')


	args = parser.parse_args()

	with open(args.classes, 'r') as infile:
		classes = [c for c in infile.read().split('\n') if len(c)]

	print (classes)
	assert len(classes) > 0
	main(args.input_path, args.output_path, args.checkpoint, args.idx, classes)
