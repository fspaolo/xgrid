# Xgrid.py 

Generate and submit batch files for Apple's Xgrid computing. 

These scripts are wrappers around the `xgrid` command line tool. It 
facilitates the construction and submission of batch files for 
*multiple* input files. 

- `xg-batch.py` - Generate and submit batch files to the Xgrid controller.
- `xg-result.py` - Get results from the Xgrid controller.

## Examples

To see the available options::

    python xg-batch.py -h

To generate and submit a batch file with jobs that run a program
`prog` with command line argument `arg` on several files:

    python xg-batch.py -s -j jobname -c "/path/to/prog -a arg" /path/to/files/*.ext 

To retrieve the results by passing the ID files generated by `xg-batch.py`:

    python xg-result.py file1.id file2.id file3.id ... 

Or by passing the directory containing those ID files:

    python xg-result.py /path/to/directory

## Grid computing with Apple's Xgrid

How to set up a grid of computers using the Mac OSX desktop version:  
[https://gist.github.com/fspaolo/5942163](https://gist.github.com/fspaolo/5942163)

## See Also

[Xgrid](http://www.apple.com/science/hardware/gridcomputing.html)  
[Tutorials](http://macresearch.org/the_xgrid_tutorials)  
[Wiki/Docs/FAQ](http://tengrid.com)
