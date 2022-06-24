#include <iostream>
#include <string>

using namespace std;

string checker(string chess[]){
    string res;

    for (int x = 0; x < 8; x++){
        for (int y = 0; y < 8; y++){
            //cout<<chess[x][y];
            if (chess[x][y] == '#'){
                if (chess[x-1][y-1] == '#' && chess[x+1][y+1] == '#' && chess[x-1][y+1] == '#' && chess[x+1][y-1] == '#'){
                    res = to_string(x+1);
                    res += " ";
                    res += to_string(y+1);
                    return res;
                }
            }
        }
        //cout<<endl;
    }
}

int main(){
    int t = 0;
    string chess[8];

    do{
        cin>>t;
    } while (t < 1 || t > 36);

    string tests[t];

    for (int x = 0; x < t; x++){
        for(int x = 0; x < 8; x++){
            cin>>chess[x];
        }
        tests[x] = checker(chess);
    }

    for (int x = 0; x < t; x++){
        if (x + 1 == t){
            cout<<tests[x];
        } else {
            cout<<tests[x]<<endl;
        }   
    }
}