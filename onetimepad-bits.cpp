#include <iostream>
#include <fstream>
using namespace std;

int main(int argc, char* argv[]){
    fstream file1;
    fstream file2;
    fstream file3;
    file1.open(argv[1], fstream::in | fstream::binary);
    file2.open(argv[2], fstream::in | fstream::binary);
    file3.open(argv[3], fstream::out | fstream::trunc | fstream::binary);

    if(argc != 4){
        cout << "usage: " << argv[0] << " <input file> <key file> <output file>\n";
    } else {
        if(!file1.is_open() || !file2.is_open() || !file3.is_open()){
            cout << "Could not open one or more of the files\n";
        } else {
            file1.seekg(0, file1.end);
            int length1 = file1.tellg();
            file1.seekg(0, file1.beg);
            char* buffer1 = new char [length1];
            file1.read(buffer1, length1);

            file2.seekg(0, file2.end);
            int length2 = file2.tellg();
            file2.seekg(0, file2.beg);
            char* buffer2 = new char [length2];
            file2.read(buffer2, length2);

            char a, b, c;
            for(int i = 0; i < length1; i++){
                a = buffer1[i];
                b = buffer2[i % length2];
                c = (a ^ b);

                file3 << c;
            }

            delete[] buffer1;
            delete[] buffer2;
        }
    }

    file1.close();
    file2.close();
    file3.close();
    return 0;
}
