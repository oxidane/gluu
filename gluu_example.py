#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

The MIT License (MIT)

Copyright 2014, Oxidane

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

"""

""" GLUU HEADER gap=1 break=3 width=120 """ # --------------------------------------------------------------------------



##----------------------------------------------------------------------------------------------------------------------
##
## General Link-Unlink Utility (GLUU) :: Example Program
##
## GLUU is an inline Python 3.x program that when integrated with your program, gives it the ability of self-interchange
## between "multiple-files" and "single-file" representations.  Properly implemented programs run identically in either
## representation, and the source will be identical when fully cycled.  See "cyclic proof" for details.
##
## GLUU is intended for projects where a single source file is desirable for distribution purposes, but multiple files
## are preferred for development.  Note: If you develop in single-file, you should regularly test multiple-files.
##
## GLUU is only compatible with certain program structures.  If your program includes files that cross-reference, files
## that conflict when they are merged, or other similar patterns, then your program may not be compatible with GLUU.
## It's up to you to determine whether GLUU is right for your project.
##
## This example program is a fully working demonstration of a GLUU-enabled application.  It also serves as an example of
## how to use global variables in a way that is compatible with GLUU.  Running this example in either of the two forms
## (single-file or multiple-files) produces identical results.  The same should hold true for your code to the extent
## that it's deterministic, compatible with GLUU, and properly integrated.
##
## The concept of GLUU had been a "to do" for some time.  It was eventually written in a few hours on March 24th, 2014.
## Since then, several size optimizations have been made.  I've made some reasonable attempts to keep it as legible as
## possible through these optimizations, but may still be somewhat difficult to follow.
##
##----------------------------------------------------------------------------------------------------------------------
##
## Revision history:
##
##	2014-08-27	1.0.2	Various edits and clean up, source uses spaces instead of tabs for github readability
##	2014-05-29	1.0.1	Minor changes to the help menu and documentation
##	2014-05-28	1.0.0	Initial release
##
##----------------------------------------------------------------------------------------------------------------------
##
## Possible additions:
##
##		Checksum validation table for verifying files at runtime and easily tracking changes (separate project?).
##
##		Try a single preceding file import, instead of all preceding files (FILELINKER).  If it works when chained
##		together like this, then it would save some space in larger programs.
##
##		Preserve file ownership (chown).
##
##----------------------------------------------------------------------------------------------------------------------
##
## The following are the tags used by GLUU.  GLUU tags begin with block comment (triple double-quotes), followed by a
## single space, followed by a "GLUU".  The settings for the HEADER tag: gap = blank lines after file before divider,
## break = blank lines between files, width = vertical divider length.
##
##		Tag			Arguments	Description
##		-----------	-----------	---------------------------------------------------------------------------------
##		HEADER		Settings	At top of every file, typically includes the execution language and file encoding
##		TITLE		-			The source's main identification, only placed at the top of the entry program
##		PROGRAM		-			GLUU program, located on top of the entry program, has execution priority
##		IMPORTS		-			Imports centralized here, these are added to every file in files mode
##		FILELINKER	-			FILES MODE ONLY: Imports the previous files into the current file
##		ENDFILE		Filename	FILE MODE ONLY: After each individual file in the application
##		FOOTER		-			This is the application main area including program entry
##		-----------	-----------	---------------------------------------------------------------------------------
##
##----------------------------------------------------------------------------------------------------------------------
##
## Cyclic proof:
##
## This demonstrates total source integrity when fully cycled (merge -> split -> merge).  Note that you should not
## modify the GLUU-generated lines of code, as those changes may not be preserved.
##
##		1) Copy this example program to the temporary directory
##
##			$ cp -a gluu_example.py /tmp/program.py
##
##		2) Split single file into a directory of multiple files
##
##			$ /tmp/program.py gluu split /tmp/multiple
##
##		3) Merge the multiple files into a single file
##
##			$ /tmp/multiple/program.py gluu merge /tmp/program2.py
##
##		4) Compare the sources for cyclic proof
##
##			$ diff -s /tmp/program.py /tmp/program2.py
##			Files /tmp/program.py and /tmp/program2.py are identical
##
## Developer's version:
##
##		rm -rf /tmp/x /tmp/y /tmp/z
##		cp -a gluu_example.py /tmp/x ; /tmp/x gluu files /tmp/y ; /tmp/y/x gluu file /tmp/z ; diff -s /tmp/x /tmp/z
##
##----------------------------------------------------------------------------------------------------------------------
##
## Code golf:
##
## This program is designed to be as small as possible.  Developers are welcome to further reduce the line count, but
## modifications must: 1) retain drop-in compatibility with existing GLUU-enabled programs, 2) not exceed 120 character
## line width, 3) make reasonable attempts to preserve legibility.  Note: The original source was about 94 lines of
## already compact code, reduced to 72 lines prior to release.
##
## 		Oxidane (72 lines)
##
##----------------------------------------------------------------------------------------------------------------------

""" GLUU TITLE """ # ---------------------------------------------------------------------------------------------------



##----------------------------------------------------------------------------------------------------------------------
##
## Program : General Link-Unlink Utility (GLUU)
## Credits : Copyright 2014, Oxidane
## License : MIT (http://opensource.org/licenses/MIT)
## Storage : https://github.com/oxidane/gluu
##
##----------------------------------------------------------------------------------------------------------------------

while __name__ == "__main__": # GLUU 1.0.2 (2014-08-27)
	gluu_name = "GLUU" ; gluu_ver = "1.0.2" ; gluu_mark = "\"\"\" " + gluu_name ; import sys, os, collections, operator
	gluu_this = "file" ; gluu_hdr = "    " + " ".join([gluu_name, gluu_ver]) ; gluu_tag = "a" ; gluu_len = 2 # 2 digits
	gluu_type = "\tgluu_this = \"file" ; gluu_cores = "HEADER TITLE PROGRAM FILELINKER IMPORTS ENDFILE FOOTER".split()
	if not sys.argv or len(sys.argv) < 2 or sys.argv[1].upper() != gluu_name: break # Skip if not a GLUU command
	ExtractSourceOf = lambda batch, specifiedcore: [code for (core, args, code) in batch if core == specifiedcore][0]
	Write_Divider = lambda f2, hd, bt, sc, ar: (f2.write(GenerateLabel(hd, bt, sc, ar)), Write_Blanks(f2, hd, 'break'))
	Swap = lambda src, b, a: "\n".join([(a.join(l.split(b, 1)) if l[:18] == gluu_type else l) for l in src.split("\n")])
	self, cli = sys.argv[0], " ".join(sys.argv[2:]) ; print(gluu_hdr + " (as \"" + gluu_this + "\")")
	cli = cli.split() if cli else [""] ; Write_Blanks = lambda f2, hdict, which: f2.write("\n" * (1+int(hdict[which])))
	def SourceSplit(fn, self=None):
		f = open(((os.path.dirname(self)+"/") if self else "") + fn, "rU") ; line = code = "" ; batch = [] ; skip = True
		while line or skip:
			line = f.readline() ; skip = False ; tags = line.split("\"\"\"") ; tags = tags if len(tags) >= 2 else None
			if tags: tags = [tag.strip() for tag in tags if tag and tag.strip() and tag.strip()[0] != "#"]
			if not tags or line[:len(gluu_mark)] != gluu_mark or len(tags) != 1: code += line ; continue
			gluu, core, args = tags[0].split()[:2] + [" ".join(tags[0].split()[2:])]
			batch, code = ( (batch + [(core, args, code)], "") if gluu == gluu_name else (batch, code + line) )
		return [(core, args, code.strip()) for core, args, code in batch if core in gluu_cores]
	def ExtractHeaderDict(batch):
		args = [args for (core, args, code) in batch if core == "HEADER"][0] ; hdict = {}
		htemp = [ {left: right} for left, right in [ [pair.split("=")][0] for pair in args.split() ] ]
		for d in htemp: hdict.update(d)
		return collections.OrderedDict( sorted(hdict.items(), key=operator.itemgetter(0), reverse=False) )
	def GenerateLabel(hdict, batch, specifiedcore, args=None):
		args = ([args for (core, args, code) in batch if core == specifiedcore] + ["", ])[0] if args is None else args
		line = gluu_mark + " " + specifiedcore + (" " if args else "") + args + " \"\"\" # " ; wd = int(hdict['width'])
		return line if (wd - len(line)) <= 1 else ( line + ( "-" * (wd - len(line)) ) )
	def Write_Source(f2, hdict, batch, specifiedcore):
		if specifiedcore != "PROGRAM": code = ExtractSourceOf(batch, specifiedcore)
		elif gluu_this == "file": code = Swap( ExtractSourceOf(batch, specifiedcore), "file", "files")
		elif gluu_this == "files": code = Swap( ExtractSourceOf(batch, specifiedcore), "files", "file")
		f2.write(code) ; Write_Blanks(f2, hdict, 'gap') ; Write_Divider(f2, hdict, batch, specifiedcore, None)
	def FileFabricate(fd, hdict, batch, *args):
		for key in args:
			if type(key) is str: Write_Source( fd, hdict, batch, key )
			elif type(key) is tuple: Write_Divider( fd, hdict, batch, key[0], key[1] if len(key) > 1 else None )
			elif type(key) is list and len(key) <= 1: fd.write( ExtractSourceOf( batch, key[0] ) )
			elif type(key) is list and key[1] <= 1: Write_Blanks( fd, hdict, key[0] )
			elif type(key) is list and key[1] <= 2: fd.write( key[0] if key[0] else "" )
	if cli[0] == "file" or cli[0] == "merge": # gluu file [filename]
		if gluu_this == "file": print("    Already packaged into a single file") ; exit(1)
		if len(cli) < 2: print("    Please specify a filename") ; exit(1)
		if os.path.exists(cli[1]): print("    Already exists, aborting") ; exit(1)
		for fn in [fn for fn in os.listdir(os.path.dirname(self)) if fn != "__pycache__"]:
			rank = 0 if len(fn) < 1 + gluu_len or not fn.startswith(gluu_tag) else int(fn[1:(1+gluu_len)])
			fl = [fl, fl.append((rank, fn))][0] if 'fl' in locals() else [(rank, fn)]
		fl = sorted(fl, key=operator.itemgetter(0,1)) if 'fl' in locals() else [] ; f2 = open(cli[1], "w")
		os.chmod( cli[1], os.stat(self).st_mode&0o777 ) ; print("    Merging into filename: " + cli[1])
		for rank, fn in fl:
			batch = SourceSplit(fn, self) ; hdict = ExtractHeaderDict(batch)
			if rank != 0: FileFabricate(f2, hdict, batch, ["FOOTER",], ['gap',1], ("ENDFILE",fn[(1+gluu_len+1):]))
			else: FileFabricate(f2, hdict, batch, "HEADER", "TITLE", "PROGRAM", "IMPORTS") ; sb, sh = batch, hdict
		unused = Write_Source(f2, sh, sb, "FOOTER") if (sh and sb) else None ; print("    Success") ; exit(0)
	if cli[0] == "files" or cli[0] == "split": # gluu files [directory]
		if gluu_this == "files": print("    Already split into multiple files") ; exit(1)
		if len(cli) < 2: print("    Please specify a directory") ; exit(1)
		if os.path.exists(cli[1]): print("    Already exists, aborting") ; exit(1)
		print("    Splitting into directory: " + cli[1]) ; os.mkdir(cli[1]) ; imp = "" ; batch = SourceSplit(self)
		num = 1 ; files = 0 ; hdict = ExtractHeaderDict(batch) ; width = int(hdict['width']) ; loop = 1
		while loop:
			loop = 0
			for ix, core, args, code in [((ix,)+tup) for ix, tup in enumerate(batch) if tup[0] == "ENDFILE"]:
				fn = gluu_tag + str(num).zfill(gluu_len) + "_" + args ; of = cli[1]+"/"+fn ; num += 1 ; f2 = open( \
				of, "w") ; ti = "from " + fn.split(".")[0]+" import *" ; FileFabricate(f2, hdict, batch, "HEADER", \
				[imp,2], ['gap',1], ("FILELINKER",), "IMPORTS", [code,2], ['break',1], ("FOOTER",) ) ; imp = ti if \
				not imp else ( (imp+"\n"+ti) if len(imp.split("\n")[-1]) + 3 + len(ti) > width else (imp+" ; "+ti) )
				batch = batch[:ix]+batch[ix+1:] ; os.chmod( of, os.stat(self).st_mode&0o777 ) ; loop = 1 ; break
		of = cli[1] + "/" + self.split("/")[-1] ; f2 = open(of, "w") ; FileFabricate(f2, hdict, batch, "HEADER", \
		"TITLE", "PROGRAM", [imp,2], ['gap',1], ("FILELINKER",), "IMPORTS", "FOOTER", ['break',1])
		os.chmod( of, os.stat(self).st_mode&0o777 ) ; print("    Success") ; exit(0)
	x="    Usages: " ; print(x+("\n"+(" "*len(x))).join(["gluu split [directory]", "gluu merge [filename]"])) ; exit(1)

""" GLUU PROGRAM """ # -------------------------------------------------------------------------------------------------



##
## Imports
##

import sys

""" GLUU IMPORTS """ # -------------------------------------------------------------------------------------------------



##
## Globals
##

class glob():
	string = "1"
	@staticmethod
	def init():
		glob.string = glob.string + "3"

""" GLUU ENDFILE globals.py """ # --------------------------------------------------------------------------------------



##
## Class 1
##

class class1():
	@staticmethod
	def run():
		glob.string = glob.string + "4"

""" GLUU ENDFILE class1.py """ # ---------------------------------------------------------------------------------------



##
## Class 2
##

class class2():
	@staticmethod
	def run():
		glob.string = glob.string + "5"

""" GLUU ENDFILE class2.py """ # ---------------------------------------------------------------------------------------



##
## Main
##

if __name__ == "__main__":
	print("")
	if len(sys.argv) > 1:
		print("There are no arguments in this demonstration, unless you want to interact with GLUU")
		print("To use GLUU, run again as the following: " + sys.argv[0] + " gluu help")
	else:
		expecting = "112123123412345"
		produced = ""
		print("This is an example GLUU-enabled program that performs a simple globals test")
		produced += glob.string
		glob.string = glob.string + "2"
		produced += glob.string
		glob.init()
		produced += glob.string
		class1.run()
		produced += glob.string
		class2.run()
		produced += glob.string
		if produced == expecting:
			print("SUCCESS, the program is working")
		else:
			print("FAILED ... Compare the results:")
			print("    Expecting : " + expecting)
			print("    Produced  : " + produced)
	print("")

""" GLUU FOOTER """ # --------------------------------------------------------------------------------------------------



