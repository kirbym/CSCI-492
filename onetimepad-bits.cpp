//Michael Kirby
//10/25/17
//One time pad encryption and decryption scheme implemented in C++
//Able to encrypt files of any type (encrypt .jpeg with another .jpeg)

#include <iostream>
#include <fstream>    //file processing
using namespace std;

//take command line arguments, argc: number of arguments including exe file, argv[]: array of given arguments
int main(int argc, char* argv[]){
    fstream file1;  //file objects
    fstream file2;
    fstream file3;
    file1.open(argv[1], fstream::in | fstream::binary);  //open 2 files to read from in binary mode
    file2.open(argv[2], fstream::in | fstream::binary);
    file3.open(argv[3], fstream::out | fstream::trunc | fstream::binary);   //open file to write to in binary mode

    if(argc != 4){  //check number of command line arguments
        cout << "usage: " << argv[0] << " <input file> <key file> <output file>\n";
    } else {
        if(!file1.is_open() || !file2.is_open() || !file3.is_open()){   //check if problems opening files
            cout << "Could not open one or more of the files\n";
        } else {
            file1.seekg(0, file1.end);    //move file pointer to end of file to find length of file (with tellg())
            int length1 = file1.tellg();
            file1.seekg(0, file1.beg);      //move file pointer to beginning
            char* buffer1 = new char [length1];     //character array for all bytes of file
            file1.read(buffer1, length1);       //read whole file

            file2.seekg(0, file2.end);      //same process as file1
            int length2 = file2.tellg();
            file2.seekg(0, file2.beg);
            char* buffer2 = new char [length2];
            file2.read(buffer2, length2);

            char a, b, c;
            for(int i = 0; i < length1; i++){
                a = buffer1[i];     //get each element of input file
                b = buffer2[i % length2];  //get elements of key file (repeat if necessary)
                c = (a ^ b);        //XOR bytes to encrypt input file with key file
                //same process works in reverse to decrypt a file (XOR output with key to return to input)
                file3 << c;   //write to output file
            }

            delete[] buffer1;   //delete arrays to deallocate memory
            delete[] buffer2;
        }
    }

    file1.close();    //close all files
    file2.close();
    file3.close();
    return 0;
}
