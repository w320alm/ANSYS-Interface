def heartsim_am(x, params):
    omega = params['omega']
    t = params['cur_time']

    import os;
    os.system();
    from subprocess import call
    import datetime



    def runAPDL152E(ansyscall,workingdir,scriptFilename):
        """
        runs the APDL script: scriptFilename.inp
        located in the folder: workingdir
        using APDL executable invoked by: ansyscall
        using the number of processors in: numprocessors
        returns the number of Ansys errors encountered in the run
        """
        inputFile = os.path.join(workingdir,
                                 scriptFilename+".inp")
        # make the output file be the input file plus timestamp
        outputFile = os.path.join(workingdir,
                                  scriptFilename+
                                  '{:%Y%m%d%H%M%S}'.format(datetime.datetime.now())+
                                  ".out")
        # keep the standard ansys jobname
        jobname = "file"
        callString =("\"{}\" -p aa_r -dir \"{}\" -j \"{}\" -s read -l en-us -b -i \"{}\" -o \"{}\"").format(
                          ansyscall,
                          workingdir,
                          jobname,
                          inputFile,
                          outputFile)
        print("invoking ansys with: ",callString)
        call(callString,shell=False)


        # check output file for errors
        print("checking for errors")
        numerrors = "undetermined"
        try:
            searchfile = open('output_ansys.out', "r")
        except:
            print("could not open",'output_ansys.out')
        else:
            for line in searchfile:
                if "NUMBER OF ERROR" in line:
                    print(line)
                    numerrors = int(line.split()[-1])
            searchfile.close()
        return(numerrors)


    def main():
        ansyscall = "C:\\Program Files\\ANSYS Inc\\v121\\ANSYS\\bin\\winx64\\ansys121.exe"
       #numprocessors = 8
        workingdir = "C:\\Users\\ecslogon\\Desktop\\trail"
        scriptFilename = "input_ansys"
        nErr = runAPDL(ansyscall,
                       workingdir,
                       scriptFilename)
        print ("number of Ansys errors: ",nErr)


    if __name__ == '__main__':
         main()



    #import pyansys
    #from pyansys import C:\Users\Miranda\Desktop\Testing_Runs,input_IA2+'{:%Y%m%d%H%M%S}'.format(datetime.datetime.now())+".out"

    #outfile=C:\Users\Miranda\Desktop\Testing_Runs,input_IA2+'{:%Y%m%d%H%M%S}'.format(datetime.datetime.now()).out
    #result=pyansys.ResultReader(outfile)
    #freqs= result.GetTimeValues()
    #print(result)     #might not do this part
    #print(freqs)      #would only do this because at time only attempting one timestep

    deriv= (result-input)/deltat


return deriv

#problem currently: getting an ouput file after running IA2 but no results are showing up(possibly
#the input file could not be correct, only took the mechanical and not fluid flow part may need
# to use the combining tool on the workbench to extract an input file) from this point then the import pyansys
#can be tested to read in the results and lastly rework the variable deriv to give mousai a derivative answer
