#include <iostream>
#include <string>

using namespace std;

int mystrStr(string& s1, string& s2 )
{
    size_t sz1 = s1.size();
    size_t sz2 = s2.size();
    if(sz2 == 0)
        return 0;

    int ret = -1;
    int pos = 0;
    while( sz1-pos >= sz2 ){
        char ch = s1[pos];
        if(ch == s2[0]){
            bool isfound = true;
            for(int i= 1; i < sz2; i++){
                if(s1[pos+i] != s2[i]){
                    isfound = false;
                    break;
                }
            }
            if(isfound){
                ret = pos;
                break;
            }
        }
        pos++;
    }
    return ret;
}


int main(int argc, char** argv)
{
    string s1 = argv[1];
    string s2 = argv[2];

    cout << mystrStr(s1, s2) << endl;

}
