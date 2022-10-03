#include "bits/stdc++.h"

using namespace std;

// #include <ext/pb_ds/assoc_container.hpp> 
// #include <ext/pb_ds/tree_policy.hpp> 
// using namespace __gnu_pbds; 

#define ll long long
#define ff first
#define ss second   
#define pb push_back
#define mp  make_pair
typedef vector<ll> vi;
typedef pair<ll, ll> ii; 
typedef vector<ii> vii;
#define TR(c, it) for (auto it = (c).begin(); it != (c).end(); it++)
#define REP(i,a,b) for(int i=int(a);i<=int(b);i++)

// Templates
template <class T> ostream& operator << (ostream &os, const vector<T> &v) { for (T i : v) os << i << ' '; return os; }
template <class T> ostream& operator << (ostream &os, const set<T> &v) { for (T i : v) os << i << ' '; return os; }
template <class T, class S> ostream& operator << (ostream &os, const pair<T, S> &v) { os << v.first << ' ' << v.second; return os; }
template <class T, class S> ostream& operator << (ostream &os, const unordered_map<T, S> &v) { for (auto i : v) os << '(' << i.first << "=>" << i.second << ')' << ' '; return os; }

#define TRACE
#ifndef ONLINE_JUDGE
#define tr(...) __f(#__VA_ARGS__, __VA_ARGS__)
template <typename Arg1>
void __f(const char* name, Arg1&& arg1){
    cerr << name << " : " << arg1 << endl;
}
template <typename Arg1, typename... Args>
void __f(const char* names, Arg1&& arg1, Args&&... args){
    const char* comma = strchr(names + 1, ',');cerr.write(names, comma - names) << " : " << arg1<<" | ";__f(comma+1, args...);
}
#else
#define tr(...)
#endif


// template <typename T>
// using indexed_set = tree<T, null_type,less<T>, rb_tree_tag, tree_order_statistics_node_update>;
 
template <typename T>
using max_heap = priority_queue<T>;
 
template <typename T>
using min_heap = priority_queue<T, vector<T>, greater<T>>;



int main()
{
    // ifstream fin ('input.txt');
    // ofstream fout ('output.txt');
    #ifndef ONLINE_JUDGE
        freopen("input.txt","r",stdin);
        freopen("output.txt","w",stdout);
        freopen("error.txt", "w", stderr);
    #endif

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int t;
    cin>>t;
    while(t--) {
        int n;
        cin>>n;
        vi a(n);
        vector<vi> m(150001,vi());
        REP(i,0,n-1) {
            cin>>a[i];
            m[a[i]].pb(i);
        }
        if(n == 2 and a[0] == a[1])
            cout<<1<<"\n";
        else {
            int ans = -1;
            REP(i,1,150000) {
                REP(j,1,m[i].size()-1) {
                    int left = m[i][j-1];
                    int right = n-1-m[i][j];
                    ans = max(ans,left + right+1);
                }
            }

            cout<<ans<<"\n";
        }

    }
    return 0;
}
