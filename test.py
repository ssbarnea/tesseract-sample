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
		raise Exception



cmd = "unicharset_extractor " 
cmd2 = "mftraining -F font_properties -U unicharset -O eng.unicharset "
for i in range(0,samples):
	cmd += "eng.counter.exp%s.box " % i
	cmd2 += "eng.counter.exp%s.tr " % i
ret = os.system(cmd)
if ret:
	raise Exception
print cmd2
ret = os.system(cmd2)
if ret:
	raise Exception



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
