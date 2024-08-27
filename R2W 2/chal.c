#include <stdio.h>
#include <string.h>
// gcc -no-pie -fno-stack-protector -g -o chal chal.c

void win() {
    puts("flag{win}");
   # system("/bin/sh");
}

void vuln() {
    char buffer1[16];

    gets(buffer1);
}

int main() {
    vuln();
}
