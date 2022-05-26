int main() {
    string line = Stdio.stdin->gets();
    sscanf(line, "%d", int a);
    int res = 860798509*a;
    res += 198609463;
    res %= 1000000007;
    write(res + "\n");
    return 0;
}