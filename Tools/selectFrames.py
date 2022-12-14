import shutil as sh
import pickle
import cv2
import os


def mkCheckpointFile(checkpointFile, idxFile, inputFolder, outputFolder):
	frames = os.listdir(inputFolder)
	if not os.path.exists(outputFolder):
		os.mkdir(outputFolder)

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
			key = int(slots[-1])
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



def main(inputFolder, outputFolder, checkpointFile, idxFile):
	disp_size = (960,480)

	if os.path.exists(idxFile) and os.path.exists(checkpointFile):
		foo  = loadCheckpoint
		args = ()
	else:
		foo  = mkCheckpointFile
		args = (inputFolder, outputFolder)

	idx, frames = foo(checkpointFile, idxFile, *args)

	amt = len(frames)

	last_key = None
	momentum = 0

	while True:
		img = cv2.imread(os.path.join(inputFolder, frames[idx]))
		
		cv2.imshow('img', cv2.resize(img, disp_size))
		cv2.setWindowTitle('img', os.path.splitext(frames[idx])[0])
		print('{1:06d}/{0:06d}'.format(amt, idx), end='\r')

		key = cv2.waitKey(0) & 0xff

		if key == ord('s'):
			sh.copy(os.path.join(inputFolder, frames[idx]), os.path.join(outputFolder, frames[idx]))

		if key == last_key:
			momentum = min(momentum+1,100)
			if   momentum >= 100: idx+=19*mod
			elif momentum >=  50: idx+=9*mod
			elif momentum >=  25: idx+=4*mod
		else:
			momentum = 0

		if key == ord('a'):
			idx = max(0, idx-1)
			mod = -1
		if key == ord('d'):
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

	parser = argparse.ArgumentParser(description="Tool for manually choosing frames from the ones extracted.")

	parser.add_argument('--frames_path', type=str, required=True,
	            help='Relative path to the folder containing the frames to be analyzed.')


	parser.add_argument('--output_folder', type=str, required=True,
	            help='Relative path to the folder where the frames will be saved.')


	parser.add_argument('--idx', type=str, default='.idx.ckpt',
	            help='File to write the last image analyzed, for continued usage after closing the application.')


	parser.add_argument('--checkpoint', type=str, default='.checkpoint.ckpt',
	            help='File to write the checkpoint list, for continued usage after closing the application.')


	args = parser.parse_args()
	main(args.frames_path, args.output_folder, args.checkpoint, args.idx)