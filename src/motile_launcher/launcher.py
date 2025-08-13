import argparse
import logging
import multiprocessing
import os
import sys

from motile_tracker.__main__ import main


def _configure_logging(logfile=None, verbose=False):
    loglevel = logging.DEBUG if verbose else logging.INFO
    logformat = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

    if logfile:
        logdir = os.path.dirname(logfile)
        if logdir and not os.path.exists(logdir):
            os.makedirs(logdir, exist_ok=True)  # Create parent dirs if needed

        handler = logging.FileHandler(logfile)
    else:
        handler = logging.StreamHandler(stream=sys.stdout)

    logging.basicConfig(level=loglevel,
                        format=logformat,
                        datefmt='%Y-%m-%d %H:%M:%S',
                        handlers=[
                            handler
                        ])
    return logging.getLogger()



def _define_args():
    args_parser = argparse.ArgumentParser(description='Motile Tracker launcher')

    args_parser.add_argument('--verbose', action='store_true', help='Enable verbose logging')
    args_parser.add_argument('--version', action='store_true', help='Display version')
    args_parser.add_argument('--arch', action='store_true', help='Display machine architecture')
    args_parser.add_argument('-l', '--logfile', dest='logfile', help='Log file path')

    args = args_parser.parse_args()

    return args


def _print_version():
    from motile_tracker import __version__ as motile_tracker_version

    print(motile_tracker_version)


def _print_arch():
    import platform

    arch = (platform.machine() or "generic").lower().replace("amd64", "x86_64")

    print(arch)


def motile_launcher():
    # freeze_support is required to prevent
    # creating a viewer every time a napari action is invoked
    multiprocessing.freeze_support()

    args = _define_args()
    
    global logger
    logger = _configure_logging(args.logfile, args.verbose)

    if args.version:
        _print_version()
    elif args.arch:
        _print_arch()
    else:
        main()
    
    sys.exit()


if __name__ == '__main__':
    motile_launcher()
