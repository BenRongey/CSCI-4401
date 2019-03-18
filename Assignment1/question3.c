// cc [FILENAME] to complie
// then ./[a.out] to run the program

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

int main() {

    int i;
    int loopCount;
    int levelCount = 0;
    
    printf("Enter the number of forks to run:\n");
    scanf("%d", &loopCount);
    FILE *fptr;
    fptr= fopen("forkOutput.csv", "w");
    fprintf(fptr, "PID, PPID, Level, Fork Of\n");
    fprintf(fptr, "%d, %d, %d, N/A\n", getpid(), getppid(), levelCount);
    fclose(fptr);

    for(i = 0; i < loopCount; i++) { 
        
        if(fork() == 0) {
            
            levelCount = levelCount + 1;
            fptr = fopen("forkOutput.csv", "a");
            fprintf(fptr, "%d, %d, %d, %d\n", getpid(), getppid(), levelCount, getppid()); 
            fclose(fptr);

            // Without this exit command, the for loop will call recursively.  Else, all forks will have the same PPID
            // exit(0); 
            
            fclose(fptr);
        }
        else {
            waitpid(-1, 0, 0);
            break;
        }
         
    }

    for(i = 0; i < loopCount; i++) {
     
        wait(NULL);
    }

    return 0;

}