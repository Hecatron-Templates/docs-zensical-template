#! python3
import os, sys, subprocess, shutil

# Zensical Build Script
class ZensicalBuild(object):

    # Class Init
    def __init__(self):
        self.WORKDIR = "./"
        self.BUILDDIR = "site"

    # Run a command
    def run_cmd(self, cmdarray, workingdir):
        proc = subprocess.Popen(cmdarray, cwd=workingdir, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        proc_out, proc_err = proc.communicate()
        print(proc_out)
        print(proc_err)
        if proc.returncode != 0:
            raise RuntimeError("Failure to run command")
        return

    # Empty a directory
    def emptydir(self, top):
        if(top == '/' or top == "\\"): return
        else:
            for root, dirs, files in os.walk(top, topdown=False):
                for name in files:
                    os.remove(os.path.join(root, name))
                for name in dirs:
                    os.rmdir(os.path.join(root, name))

    # Print Usage
    def usage(self):
        print ("Please use build.py <target> where <target> is one of")
        print ("  build       to build the standalone HTML files into the " + self.BUILDDIR + " directory")
        print ("  clean       to clean the output directory:" + self.BUILDDIR)
        print ("  serve       Serve the site out on a port for previewing")

    # Do the main build of doxygen html
    def build(self):
        self.clean()        
        print("Building Zensical Files")
        cmdopts = ["zensical", "build"]
        self.run_cmd(cmdopts, self.WORKDIR)
        print ("Build finished. The HTML pages are in " + self.BUILDDIR)

    # Clean the Build directory
    def clean(self):
        self.emptydir("site")
        print ("Clean finished")

    # Serve files for development
    def serve(self):
        print("Starting Zensical Server http://127.0.0.1:8000")
        cmdopts = ["zensical", "serve", "--open"]
        self.run_cmd(cmdopts, self.WORKDIR)
        print ("Server Closed.")

    def main(self):
        if len(sys.argv) != 2:
            self.usage()
            return
        if sys.argv[1] == "build":
            self.build()
        if sys.argv[1] == "clean":
            self.clean()
        if sys.argv[1] == "serve":
            self.serve()

if __name__ == "__main__":
    ZensicalBuild().main()
