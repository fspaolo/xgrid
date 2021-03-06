#!/usr/bin/env python
"""
Get results from Xgrid controller given the job IDs.

This script is a wrapper around the xgrid command line tool. It 
facilitates getting the results from the controller for *multiple* 
job IDs. The following can be passed trough the command line:

1) the ID files generated by the `xg-batch.py` script, or
2) a directory containing those ID files.

Examples
--------
Retrieving results by passing ID files (generated by `xg-batch.py`)::

$ python xg-result.py file1.id file2.id file3.id ... 

Or by passing a dir containing those files::

$ python xg-result.py /path/to/dir

See Also
--------
Xgrid: http://www.apple.com/science/hardware/gridcomputing.html
Tutorials: http://macresearch.org/the_xgrid_tutorials
Wiki/Docs/FAQ/etc: http://tengrid.com

"""
# Fernando <fpaolo@ucsd.edu>
# April 21, 2011

import argparse as ap
from glob import glob
import re
import os
import sys

# parse command line arguments
parser = ap.ArgumentParser()
parser.add_argument('files', nargs='+', help='job ID file[s] '
    '(it can be files or a directory) [ex: file1.id file2.id ... or '
    'dir_with_id_files]')

args = parser.parse_args()


def get_jobs_and_ids(args):
    """Get job names and IDs. 

    Get a list of job names (file names) and their ID numbers by
    scanning the content of ID files (passed trough the command
    line or in a *given* directory).
    """
    jobs = []
    ids = []
    if os.path.isdir(args.files[0]):             # directory passed
        files = glob('%s/*.id' % args.files[0])  # search for *.id files
    elif os.path.isfile(args.files[0]):          # files passed
        files = args.files
    else:                                        # string passed
        print 'no ID files or directory!'
        sys.exit()

    for fname in files:
        jobname, _ = os.path.splitext(fname) 
        idNo = re.findall('\d+', open(fname).read())
        jobs.append(jobname)
        ids.append(idNo[0])
    return jobs, ids


def get_results(jobs, ids):
    """Get results from the controller. 

    Check first if the environmental variables for controller 'name' 
    and 'password' are defined, otherwise raise an error.
    """
    controller = os.environ.get('XGRID_CONTROLLER_HOSTNAME')
    password = os.environ.get('XGRID_CONTROLLER_PASSWORD')
    if (not controller) or (not password):
        print 'error: no controller name/password specified!'
        print 'please set the following environmental variables:'
        print 'XGRID_CONTROLLER_HOSTNAME=hostname'
        print 'XGRID_CONTROLLER_PASSWORD=password'
        sys.exit()
    for j, i in zip(jobs, ids):
        os.system('xgrid -job results -id %s -so %s.out -se %s.err' % (i, j, j))
        print 'xgrid -job results -id %s -so %s.out -se %s.err' % (i, j, j)
        print 'std output -> %s.out' % j
        print 'std error  -> %s.err' % j


def main():
    jobs, ids = get_jobs_and_ids(args)    
    get_results(jobs, ids)
    print 'done.'


if __name__ == '__main__':
    main()
