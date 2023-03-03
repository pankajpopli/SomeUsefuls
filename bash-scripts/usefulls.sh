#copy only specific files
find . -name '*.pdf' | cpio -pdm  ~/Pictures/
