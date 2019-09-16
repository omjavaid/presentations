#include <iostream>
#include <fstream>
#include "string.h"
#include <iomanip>

using namespace std;

struct module
{
   string name;
   int status;
   int ID;
};
const char filename[]="modules.txt";
void read_file(const char * filename,module m[],int size, int * index)
{

   ifstream readFile;
   readFile.open(filename);
   
   if (readFile.is_open()) {
       while (!readFile.eof() && *index < size)
       {
           readFile >> m[*index].name;
           readFile >> m[*index].ID;
           readFile >> m[*index].status;
           (*index)++;
           
       }
       readFile.close();
   }
   
}

int main()
{
   int index = 0;
   const int size = 200;
   module m[size];

   read_file(filename, m,size, &index);

   return 0;
}

