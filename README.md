

# General Link-Unlink Utility (GLUU)

GLUU gives your program the innate ability to split and merge itself.  This makes it possible for a project to be developed as multiple files, while distributed as a single file, or vice-versa.  You might call this a dual-form executable, since application-level functionality is identical in either form.

See the example source for more details and some exceptions.



## Requirements

* [Python 3](http://www.python.org/getit/)



## Usage

To use GLUU from a GLUU-enabled application, run with `gluu` as the first argument.

For a menu, or to report the application's current representation:

	$ ./gluu_example.py gluu help

Split the included single-file example into a multiple-files representation:

	$ ./gluu_example.py gluu split /tmp/multiple-files

Unite the multiple-files back into a single-file:

	$ /tmp/multiple-files/gluu_example.py gluu merge /tmp/single-file.py

Compare results for a cyclic proof:

	$ diff -s ./gluu_example.py /tmp/single-file.py
	Files ./gluu_example.py and /tmp/single-file.py are identical



## Notes

To create a new GLUU-enabled application, you should adapt an existing one, like the included example.

To add a new file to a GLUU project, it may be easier in multiple-files mode, where you may copy and adapt an existing file.  The new file should be renumbered to the position of insertion, and cycling it through single-file mode may be necessary to correctly renumber the files.  Note that the file prefix "a[0-9]" should always be preserved when modifying filenames in either mode.

Latest version is found here: [https://github.com/oxidane/gluu](https://github.com/oxidane/gluu).



## Copyright and License

Copyright 2014, Oxidane.  All rights reserved.

Distributed under the [MIT License](http://opensource.org/licenses/MIT).  The copyright and license must be included with any use, modification, or redistribution of the source.  See the license for details.

