import os

samples = 2
for i in range(1,samples):
	ret = os.system("copy eng.counter.exp0.box eng.counter.exp%s.box" % i)
	if ret:
		raise Exception(ret)

for i in range(0,samples):
	ret = os.system("tesseract eng.counter.exp%s.png eng.counter.exp%i nobatch box.train.stderr" % (i,i))
	if ret:
		raise

for i in range(0,samples):
	ret = os.system("tesseract eng.counter.exp%s.png eng.counter.exp%i nobatch box.train.stderr" % (i,i))
	if ret:
		raise Exception(ret)



cmd = "unicharset_extractor " 
tr_files = []
for i in range(0,samples):
	cmd += "eng.counter.exp%s.box " % i
	tr_files.append("eng.counter.exp%s.tr " % i)
ret = os.system(cmd)
if ret:
	raise Exception(ret)

cmd = "copy /b %s eng.counter.exp.tr" % "+".join(tr_files)
ret = os.system(cmd)
if ret:
	raise Exception(ret)

cmd = "mftraining -F font_properties -U unicharset -O eng.unicharset eng.counter.exp.tr"
ret = os.system(cmd)
if ret:
	raise Exception(ret)


cmd = "cntraining eng.counter.exp.tr"
ret = os.system(cmd)
if ret:
	raise Exception(ret)

cmd = "cntraining eng.counter.exp.tr"
ret = os.system(cmd)
if ret:
	raise Exception(ret)



"""
"mftraining -F font_properties -U unicharset -O eng.unicharset " eng.counter.exp0.tr
::mftraining -F font_properties -U unicharset end.counter.exp0.tr

cntraining eng.counter.exp0.tr


combine_tessdata eng.

tesseract x.png output -l eng
"""

ret = os.system("tesseract test.png output -l eng")
if ret:
	raise Exception
